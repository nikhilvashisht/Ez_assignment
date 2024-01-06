from fileserver.models import File
from fileserver.serializers import FileSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from fileserver.forms import FileForm
from django.http import HttpResponse
# Create your views here.


@api_view(['GET'])
def get_file(request):
    """
        Returns the list of uploaded files
    """
    files = File.objects.all()
    serialized_files = FileSerializer(files, many=True)
    return Response(serialized_files.data)


@api_view(['GET'])
def download_file(request, file_id):
    """
        Returns the url of requested file
        TODO: implement unique url for download
    """
    uploaded_file = File.objects.get(file_name=file_id)
    response = HttpResponse(
        uploaded_file.file, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{uploaded_file.file_name}"'
    return response


@api_view(['POST'])
def upload_file(request):
    """
        Uploads a file \n
        Only ops users have access to this method
    """
    username = request.POST['username']
    user = User.objects.get(username=username)
    if (user.has_perm('fileserver.add_file')):
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            response = Response()
            response.data = "File uploaded successfully"
            response.status_code = 200
            return response
        else:
            response = Response()
            response.data = "File upload unsuccessful"
            response.status_code = 400
            return response
    else:
        return Response("Not permitted.")


@api_view(['POST'])
def register(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    # check if user already exists or not
    count = User.objects.filter(username=username, email=email).count()
    if count != 0:
        response = Response()
        response.data = "User already exists. Please log in."
        response.status_code = 400
        return response
    # if not existing already, register user
    else:
        user = User.objects.create_user(
            username=username, email=email, password=password)
        user.save()
        response = Response()
        response.data = "Successfully registered user."
        response.status_code = 200
        return response


@api_view(['POST'])
def login(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    user = authenticate(username=username, email=email, password=password)
    if user is not None:
        response = Response()
        response.data = "Successfully logged in."
        response.status_code = 200
        return response
    else:
        response = Response()
        response.data = "Invalid credentials."
        response.status_code = 400
        return response

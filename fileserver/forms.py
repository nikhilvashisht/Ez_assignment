from django import forms
from fileserver.models import File


class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('username', 'file_name', 'file')

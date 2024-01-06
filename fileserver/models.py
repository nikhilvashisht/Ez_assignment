from django.db import models

# Create your models here.


class File(models.Model):
    username = models.CharField(max_length=225, null=False, default='')
    file_name = models.CharField(max_length=225)
    file = models.FileField(upload_to='')

    class Meta:
        permissions = []

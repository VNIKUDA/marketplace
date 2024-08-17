from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

import os
from hashlib import sha3_224
from datetime import datetime

def custom_upload_directory(instance, filename):
    # Main directory of the upload (is the name of the parent model class)
    directory = instance.parent_type.model

    # Subdirectory of the upload (is hashed version of the parent's id)
    subderictory_hash = sha3_224()
    subderictory_hash.update(f"{instance.parent_id}".encode())
    subderictory = subderictory_hash.hexdigest()

    # Hashed version of the upload file
    filename, filetype = os.path.splitext(filename)
    filename_hash = sha3_224()
    filename_hash.update(f"{filename}{datetime.now()}".encode()) # add current time to the name of 
    filename = filename_hash.hexdigest()                         # the file and then hash it

    return f"{directory}/{subderictory}/{filename}{filetype}"

# Create your models here.
class UploadFile(models.Model):
    file = models.FileField(upload_to=custom_upload_directory)

    parent_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    parent_id = models.PositiveIntegerField()
    parent = GenericForeignKey("parent_type", "parent_id")

    def __str__(self):
        return self.file.name
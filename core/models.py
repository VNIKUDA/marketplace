from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

import os
from hashlib import sha3_224
from datetime import datetime

def custom_upload_directory(instance, filename):
    directory = instance.parent_type.model

    filename, filetype = os.path.splitext(filename)

    filename_hash = sha3_224()
    filename_hash.update(f"{filename}{datetime.now()}".encode())
    filename = filename_hash.hexdigest()

    return f"{directory}/{filename}{filetype}"

# Create your models here.
class UploadFile(models.Model):
    file = models.FileField(upload_to=custom_upload_directory)

    parent_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    parent_id = models.PositiveIntegerField()
    parent = GenericForeignKey("parent_type", "parent_id")

    def __str__(self):
        return self.file.name
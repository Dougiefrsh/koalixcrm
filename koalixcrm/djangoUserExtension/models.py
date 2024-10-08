# -*- coding: utf-8 -*-

from koalixcrm.djangoUserExtension.user_extension.document_template import *
from koalixcrm.djangoUserExtension.user_extension.template_set import *
from koalixcrm.djangoUserExtension.user_extension.user_extension import *
from koalixcrm.djangoUserExtension.user_extension.text_paragraph import *
from django.db import models

# Define the XSLFile model with explicit primary key type
class XSLFile(models.Model):
    id = models.BigAutoField(primary_key=True)  # Explicit primary key type
    title = models.CharField(max_length=100)
    xslfile = models.FileField(upload_to='xsl_files/')
    
    def __str__(self):
        return self.title

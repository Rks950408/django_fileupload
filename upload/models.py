from django.db import models

class FileUpload(models.Model):
    file = models.FileField(upload_to='files/')
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"File: {self.file.name}, Description: {self.description}"

from django.db import models

# Create your models here.

class ArchivoCsv(models.Model):
    nombre  = models.CharField(max_length=50)
    csv     = models.FileField(upload_to='csvs')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='archivocsv'
        verbose_name_plural="archivoscsv"
    
    def __str__(self):
        return self.nombre

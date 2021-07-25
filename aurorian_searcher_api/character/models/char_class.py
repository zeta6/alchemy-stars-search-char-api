from django.db import models

def upload_path(instance, filename):
    return 'class_icons/{0}/{1}'.format(instance.name, filename)

class CharClass(models.Model):
     
    name = models.CharField(max_length=15)  
    icon = models.ImageField(upload_to=upload_path, height_field=None, width_field=None, max_length=None)  

    class Meta:
        verbose_name = "Class"
        verbose_name_plural = "Classes"

    def __str__(self):
        return self.name
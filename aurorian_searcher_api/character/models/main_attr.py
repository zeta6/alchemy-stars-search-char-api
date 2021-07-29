from django.db import models

def upload_path(instance, filename):
    return 'main_attr_icons/{0}/{1}'.format(instance.name, filename)

class MainAttribute(models.Model):
     
    name = models.CharField(max_length=10, blank=True)  
    icon = models.ImageField(upload_to=upload_path, height_field=None, width_field=None, max_length=None, blank=True)  

    class Meta:
        verbose_name = "Mattr"
        verbose_name_plural = "Mattrs"

    def __str__(self):
        return self.name
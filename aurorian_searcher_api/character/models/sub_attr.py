from django.db import models

def upload_path(instance, filename):
    return 'sub_attr_icons/{0}/{1}'.format(instance.name, filename)

class SubAttribute(models.Model):
     
    name = models.CharField(max_length=10, blank=True, null=True)  
    icon = models.ImageField(upload_to=upload_path, height_field=None, width_field=None, max_length=None, blank=True, null=True)  

    class Meta:
        verbose_name = "Sattr"
        verbose_name_plural = "Sattrs"

    def __str__(self):
        return self.name
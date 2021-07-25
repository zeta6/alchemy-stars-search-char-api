from django.db import models

def upload_path(instance, filename):
    return '{0}/{1}'.format(instance.image_id, filename)

class Image(models.Model):
     
    image_id = models.OneToOneField("Character", verbose_name="image", on_delete=models.CASCADE, db_column="image")
    ascension_0 = models.ImageField(upload_to=upload_path, height_field=None, width_field=None, max_length=None)  
    ascension_3 = models.ImageField(upload_to=upload_path, height_field=None, width_field=None, max_length=None)  

    class Meta:
        verbose_name = "image"
        verbose_name_plural = "images"

    
    # def __str__(self):
    #     return self.image_id

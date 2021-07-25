from django.db import models

class CharFile(models.Model):
     
    file_id = models.OneToOneField("Character", verbose_name="char file", on_delete=models.CASCADE, db_column="char_file")
    name = models.CharField(max_length=50)
    nickname = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    height = models.CharField(max_length=10)
    birthday= models.CharField(max_length=20)
    birthplace = models.CharField(max_length=50)
    element = models.CharField(max_length=20)
    affilition = models.CharField(max_length=100)
    fighting_style = models.CharField(max_length=200)

    class Meta:
        verbose_name = "char file"
        verbose_name_plural = "char files"
    
    def __str__(self):
        return self.nickname
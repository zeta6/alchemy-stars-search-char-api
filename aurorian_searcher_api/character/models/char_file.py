from django.db import models

class CharFile(models.Model):
     
    file_id = models.OneToOneField("Character", related_name="char_file", on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True, null=True)
    nickname = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    height = models.CharField(max_length=10, blank=True, null=True)
    birthday= models.CharField(max_length=20, blank=True, null=True)
    birthplace = models.CharField(max_length=50, blank=True, null=True)
    element = models.CharField(max_length=20, blank=True, null=True)
    affilition = models.CharField(max_length=100, blank=True, null=True)
    fighting_style = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = "file autoinput: name, gender(여),elemnet, affil,ftile(equip)"
        verbose_name_plural = "char files"

    def save(self, *args, **kwargs):
        if self.name == None:
            self.name = self.file_id.name
        if self.gender == None:
            self.gender = "여"
        if self.element == None:
            self.element = self.file_id.main_attribute.name
        if self.affilition == None:
            self.affilition = self.file_id.faction.name
        if self.fighting_style == None:
            self.fighting_style = self.file_id.equipment.name
            
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
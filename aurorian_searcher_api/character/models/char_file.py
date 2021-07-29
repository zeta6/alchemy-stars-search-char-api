from django.db import models

class CharFile(models.Model):
     
    file_id = models.OneToOneField("Character", related_name="char_file", on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True)
    nickname = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=10, blank=True)
    height = models.CharField(max_length=10, blank=True)
    birthday= models.CharField(max_length=20, blank=True)
    birthplace = models.CharField(max_length=50, blank=True)
    element = models.CharField(max_length=20, blank=True)
    affilition = models.CharField(max_length=100, blank=True)
    fighting_style = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name = "file autoinput: name, gender(여),elemnet, affil,ftile(equip)"
        verbose_name_plural = "char files"

    def save(self, *args, **kwargs):
        if self.name == "":
            self.name = self.file_id.name
        if self.gender == "":
            self.gender = "여"
        if self.element == "":
            if self.file_id.main_attribute != None:
                self.element = self.file_id.main_attribute.name
        if self.affilition == "":
            if self.file_id.faction != None:
                self.affilition = self.file_id.faction.name
        if self.fighting_style == "":
            if self.file_id.equipment != None:
                self.fighting_style = self.file_id.equipment.name
            
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
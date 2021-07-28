from django.db import models

class Breakthrough(models.Model):
     
    brth_id = models.OneToOneField("Character", related_name="breakthrough", on_delete=models.CASCADE)
    count_1 = models.TextField(null=True,blank=True)
    count_2 = models.TextField(null=True,blank=True)
    count_3 = models.TextField(null=True,blank=True)
    count_4 = models.TextField(null=True,blank=True)
    count_5 = models.TextField(null=True,blank=True)
    count_6 = models.TextField(null=True,blank=True)

    class Meta:
        verbose_name = "breakthrough autoinput = 6성 기본 텍스트"
        verbose_name_plural = "breakthroughs"

    def save(self, *args, **kwargs):
        if self.count_1 == "":
            self.count_1 = "생명력 +300"
        if self.count_2 == "":
            self.count_2 = "방어력 +40" 
        if self.count_3 == "":
            self.count_3 = "액티브 기술 강화 : 스킬 쿨 다운이 1턴 감소한다"
        if self.count_4 == "":
            self.count_4 = "기초 최대 생명력을 300 + 5 % 상승"
        if self.count_5 == "":
            self.count_5 = "기초 방어력을 40 + 5 % 상승"    
        if self.count_6 == "":
            self.count_6 = "액티브 기술 강화 : 액티브 스킬이 선제 공격으로 변경된다. 전투 시작 시, 즉시 사용할 수 있다."                 
        super().save(*args, **kwargs)
    
    # def __str__(self):
    #     return self.name
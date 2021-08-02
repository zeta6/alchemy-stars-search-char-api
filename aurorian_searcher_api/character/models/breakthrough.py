from django.db import models

class Breakthrough(models.Model):
     
    brth_id = models.OneToOneField("Character", related_name="breakthrough", on_delete=models.CASCADE)
    count_1 = models.TextField(blank=True)
    count_2 = models.TextField(blank=True)
    count_3 = models.TextField(blank=True)
    count_4 = models.TextField(blank=True)
    count_5 = models.TextField(blank=True)
    count_6 = models.TextField(blank=True)

    class Meta:
        verbose_name = "breakthrough autoinput = 6성 기본 텍스트"
        verbose_name_plural = "breakthroughs"

    def save(self, *args, **kwargs):
        if self.brth_id.rarity == 6:
            if self.count_1 == "":
                self.count_1 = "생명력이 300 상승합니다."
            if self.count_2 == "":
                self.count_2 = "방어력이 40 상승합니다." 
            if self.count_3 == "":
                self.count_3 = "[액티브 스킬 강화] : 스킬 쿨 다운이 1턴 감소한다"
            if self.count_4 == "":
                self.count_4 = "300+5%기본 최대 HP가 상승합니다."
            if self.count_5 == "":
                self.count_5 = "40+5%기본 방어력이 상승합니다."    
            if self.count_6 == "":
                self.count_6 = "[액티브 스킬 강화]: 선제공격."     
        elif self.brth_id.rarity == 5:
            if self.count_1 == "":
                self.count_1 = "생명력이 250 상승합니다."
            if self.count_2 == "":
                self.count_2 = "[액티브 스킬 강화]: 스킬 쿨 다운이 1턴 감소한다."
            if self.count_3 == "":
                self.count_3 = "250+5%기본 최대 HP가 상승합니다."
            if self.count_4 == "":
                self.count_4 = "30+5%기본 방어력이 상승합니다."  
            if self.count_5 == "":
                self.count_5 = "[액티브 스킬 강화]: 선제공격."
        elif self.brth_id.rarity == 4:
            if self.count_1 == "":
                self.count_1 = "생명력이 200 상승합니다."
            if self.count_2 == "":
                self.count_2 = "25+5%기본 방어력이 상승합니다."
            if self.count_3 == "":
                self.count_3 = "200+5%기본 최대 HP가 상승합니다."
            if self.count_4 == "":
                self.count_4 = "[액티브 스킬 강화]: 선제공격." 
        elif self.brth_id.rarity == 3:
            if self.count_1 == "":
                self.count_1 = "생명력이 200 상승합니다."
            if self.count_2 == "":
                self.count_2 = "방어력이 25 상승합니다."
            if self.count_3 == "":
                self.count_3 = "[액티브 스킬 강화]: 선제공격." 
                
        super().save(*args, **kwargs)
    
    # def __str__(self):
    #     return self.name
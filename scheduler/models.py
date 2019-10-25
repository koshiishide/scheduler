from django.db import models


class Org(models.Model):
    team_id      = models.CharField(max_length=256, primary_key=True)
    team_pre     = models.CharField(max_length=256,null=True)
    team_aft     = models.CharField(max_length=256,null=True)
    #name =  models.CharField(max_length=30)
    """
    def get_absolute_url(self):
        return reverse('team-detail', args=[str(self.id_team)])
    
    def __str__(self):
        return self.team_id
    """

class User(models.Model):
    student_id   = models.CharField(max_length=256, primary_key=True)    
    #name= models.CharField(max_length=256,null=True)
    team   = models.ForeignKey("Org", to_field="team_id", on_delete=models.SET_NULL, null=True)
    qtr_pre      = models.IntegerField(default=0) # 前期講義日程(合計） 
    qtr_aft      = models.IntegerField(default=0) # 後期講義日程(合計)
    
    """
    def get_absolute_url(self):
        return reverse('member-detail', args=[str(self.student_id)])
    
    def __str__(self):
        return self.org
    """




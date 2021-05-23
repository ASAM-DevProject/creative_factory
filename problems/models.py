from django.db import models
from users.models import CustomizeUserModel
# Create your models here.



class TagLevelOneModeModel(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

class TegLevelTwoModel(models.Model):
    name = models.CharField(max_length=255)
    tag_level_one = models.ForeignKey(to=TagLevelOneModeModel, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.name

class TagLevelThreeModel(models.Model):
    name = models.CharField(max_length=255)
    tag_level_two = models.ForeignKey(to=TegLevelTwoModel, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class FactoryProblemModel(models.Model):
    PUBLISH_STATUS = (
        ('published', 'published'),
        ('fail','fail'),
    )
    SOLVE_STATUS = (
        ('solved','solved'),
        ('not solved','not solved'),
        ('solving','solving'),

    )
    title = models.CharField(max_length=255)
    text = models.TextField(max_length=600)
    publish_status = models.CharField(max_length=20, choices=PUBLISH_STATUS, default='published')
    solve_status = models.CharField(max_length=20, choices=SOLVE_STATUS, default='not solved')
    offer_price = models.CharField(max_length=16)
    senders = models.ForeignKey(to=CustomizeUserModel, on_delete=models.PROTECT)
    tag_level_one = models.ForeignKey(to=TagLevelOneModeModel, on_delete=models.CASCADE)
    tag_level_two = models.ForeignKey(to=TegLevelTwoModel, on_delete=models.CASCADE)
    tag_level_three = models.ForeignKey(to=TagLevelThreeModel,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
    


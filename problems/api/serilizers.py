from django.db.models import fields
from rest_framework import serializers
from problems.models import (TagLevelOneModeModel, TagLevelThreeModel, TegLevelTwoModel, FactoryProblemModel)

class TagLevelOneSerilizers(serializers.ModelSerializer):
    class Meta:
        model = TagLevelOneModeModel
        fields = "__all__"

class TagLevelTwoSerializers(serializers.ModelSerializer):
    class Meta:
        model = TegLevelTwoModel
        fields = "__all__"

class TagLevelThreeSerializers(serializers.ModelSerializer):
    class Meta:
        model = TagLevelThreeModel
        fields = "__all__"
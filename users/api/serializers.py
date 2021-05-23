from rest_framework import serializers
from users.models import (CustomizeUserModel, UserProfileModel, FactoryProfileModel, OfficeProfileModel)



class CutomizeUserserializer(serializers.ModelSerializer):
    class Meta:
        model = CustomizeUserModel
        fields= "__all__"

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfileModel
        fields = "__all__"

class OfficeProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfficeProfileModel
        fields = "__all__"
    
class FactoryProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactoryProfileModel
        fields = "__all__"

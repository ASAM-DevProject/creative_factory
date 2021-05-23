from django.shortcuts import render
from rest_framework import generics
from problems.models import (TagLevelOneModeModel, TegLevelTwoModel, TagLevelThreeModel, FactoryProblemModel)
from problems.api.serilizers import (TagLevelOneSerilizers,TagLevelTwoSerializers,TagLevelThreeSerializers)
# Create your views here.


class TagLevelOneView(generics.ListCreateAPIView):
    queryset = TagLevelOneModeModel.objects.all()
    serializer_class = TagLevelOneSerilizers


class TagLevelTwoView(generics.ListCreateAPIView):
    queryset = TegLevelTwoModel.objects.all()
    serializer_class = TagLevelTwoSerializers
class TagLevelThreeView(generics.ListCreateAPIView):
    queryset = TagLevelThreeModel.objects.all()
    serializer_class = TagLevelThreeSerializers

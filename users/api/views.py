from rest_framework import generics
from users.models import (CustomizeUserModel, UserProfileModel, FactoryProfileModel,OfficeProfileModel)
from users.api.serializers import (CutomizeUserserializer, UserProfileSerializer,OfficeProfileSerializer,FactoryProfileSerializer)


class UsersList(generics.ListCreateAPIView):
    queryset = CustomizeUserModel.objects.all()
    serializer_class = CutomizeUserserializer


class UsersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomizeUserModel.objects.all()
    serializer_class = CutomizeUserserializer

class UserProfileViewsLis(generics.ListCreateAPIView):
    queryset = UserProfileModel.objects.all()
    serializer_class = UserProfileSerializer
class UsersProfileDetailViewsLis(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfileModel.objects.all()
    serializer_class = UserProfileSerializer


class FactoryProfileView(generics.ListCreateAPIView):
    queryset = FactoryProfileModel.objects.all()
    serializer_class = FactoryProfileSerializer

class FactoryProfileDetailViews(generics.RetrieveUpdateDestroyAPIView):
    queryset = FactoryProfileModel.objects.all()
    serializer_class = FactoryProfileSerializer

class OfficeProfileView(generics.ListCreateAPIView):
    queryset = OfficeProfileModel.objects.all()
    serializer_class = OfficeProfileSerializer

class OfficeProfileDetailViews(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = OfficeProfileModel.objects.all()
    serializer_class = OfficeProfileSerializer


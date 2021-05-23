from django.urls import path
from users.api.views import (UsersList, UserProfileViewsLis, FactoryProfileView,
OfficeProfileView,UsersDetail,UserProfileViewsLis, UsersProfileDetailViewsLis,FactoryProfileView,OfficeProfileDetailViews)


urlpatterns = [
    path('userslist/',UsersList.as_view(),name="userslist" ),
    path('userslist/<int:pk>/',UsersDetail.as_view(),name="userslistDetail"),
    path('usersprofilelist/', UserProfileViewsLis.as_view(), name='usersprofilelist'),
    path('usersprofilelist/<int:pk>/', UsersProfileDetailViewsLis.as_view(), name="usersprofilelistdetail"),
    path('factoryprofilelist/', FactoryProfileView.as_view(), name='factoryprofilelist'),
    path('factoryprofilelist/<int:pk>/', FactoryProfileView.as_view(), name='factoryprofilelistdetail'),
    path('officefactorylist/', OfficeProfileView.as_view(), name='officefactorylist'),
    path('officefactorylist/<int:pk>/', OfficeProfileDetailViews.as_view(), name='officefactorylistdetail'),
    


]
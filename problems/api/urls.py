from django.urls import path
from problems.api.views import TagLevelOneView,TagLevelTwoView, TagLevelTwoView,TagLevelThreeView

urlpatterns = [
    path('tagone/', TagLevelOneView.as_view(), name="taglevelone"),
    path('tagtwo/', TagLevelTwoView.as_view(), name="tagtwo"),
    path('tagthree/', TagLevelThreeView.as_view(), name='tagthree'),


]
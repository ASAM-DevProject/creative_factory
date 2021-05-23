from django.contrib import admin
from users.models import (CustomizeUserModel, UserProfileModel, OfficeProfileModel, FactoryProfileModel)

# Register your models here.


admin.site.register(CustomizeUserModel)
admin.site.register(UserProfileModel)
admin.site.register(OfficeProfileModel)
admin.site.register(FactoryProfileModel)

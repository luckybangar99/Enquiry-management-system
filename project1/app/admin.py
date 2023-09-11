from django.contrib import admin
from .models import UserDataBase,AdminDataBase,QueryDataBase


admin.site.register(UserDataBase)
admin.site.register(AdminDataBase)
admin.site.register(QueryDataBase)

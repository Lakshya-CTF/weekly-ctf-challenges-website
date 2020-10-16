from django.contrib import admin

from .models import CustomUser,Question


admin.site.site_header = 'Lakshya Weekly Challenges Admin Portal'
admin.site.index_title = 'Adminsitration'

# Register your models here.


admin.site.register(CustomUser)
admin.site.register(Question)

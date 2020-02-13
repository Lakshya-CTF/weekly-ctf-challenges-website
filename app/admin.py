from django.contrib import admin

from .models import CustomUser,Question
from import_export.admin import ImportExportActionModelAdmin


admin.site.site_header = 'Lakshya Weekly Challenges Admin Portal'
admin.site.index_title = 'Adminsitration'

# Register your models here.


class CustomUserAdmin(ImportExportActionModelAdmin):
    pass

class QuestionAdmin(ImportExportActionModelAdmin):
	pass

admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(Question,QuestionAdmin)
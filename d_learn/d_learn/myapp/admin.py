from django.contrib import admin
from myapp.models import student

# Register your models here.
#admin.site.register(student)
class studentAdmin(admin.ModelAdmin):
    list_display=('id','cName','cSex','cBirthday','cEmail','cPhone',)
    list_filter=('cSex',)
    search_fields=('cName','cEmail','cPhone',)
    ordering=('id','cName',)

admin.site.register(student, studentAdmin)
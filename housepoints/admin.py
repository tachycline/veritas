from django.contrib import admin

# Register your models here.
from .models import House, Student, Category, FacStaffType, FacStaff, Award

admin.site.register(House)
admin.site.register(Student)
admin.site.register(Category)
admin.site.register(FacStaffType)
admin.site.register(FacStaff)
admin.site.register(Award)

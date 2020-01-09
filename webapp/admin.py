from django.contrib import admin
from .models import CourseData

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id','course_no','course_name','trainer_name','start_date','start_time','trainer_exp']
admin.site.register(CourseData,CourseAdmin)

from django.contrib import admin
from .models import Faculty,ProDetails,EduDetails,NewsItem,EventItem, Student,Course

admin.site.register(Faculty)
admin.site.register(ProDetails)
admin.site.register(EduDetails)
admin.site.register(NewsItem)
admin.site.register(EventItem)
admin.site.register(Student)
admin.site.register(Course)
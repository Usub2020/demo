from django.contrib import admin
from polls.models import *

# Register your models here.

@admin.register(contact)
class Contactadmin(admin.ModelAdmin):
    list_display = ('subject','date',)
    search_fields = ('name','email','date',)
    list_filter = ('email','date',)

class grup (admin.StackedInline):
    model = text_multi

@admin.register(Courses)
class Coursesadmin(admin.ModelAdmin):
    inlines = [grup]
    list_display = ('name','category','create_date','update_date','available',)
    search_fields = ('name','category',)
    list_filter = ('available','create_date',)

@admin.register(Blog)
class Blogadmin(admin.ModelAdmin):
    list_displey = ('date','head')
    list_filter = ('head','date',)

@admin.register(Student_comment)
class Student_comment_admin(admin.ModelAdmin):
    list_displey = ('student',)

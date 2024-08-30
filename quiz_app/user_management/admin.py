from django.contrib import admin
from .models import Teacher, Student

# Register your models here.

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('get_user_id', 'get_user_username')

    def get_user_id(self, obj):
        return obj.user.id
    get_user_id.short_description = 'User ID'

    def get_user_username(self, obj):
        return obj.user.username
    get_user_username.short_description = 'Username'

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('get_user_id', 'get_user_username')

    def get_user_id(self, obj):
        return obj.user.id
    get_user_id.short_description = 'User ID'

    def get_user_username(self, obj):
        return obj.user.username

    get_user_username.short_description = 'Username'

    get_user_username.short_description = 'Username'


from django.contrib import admin
from .models import AnswerSubmission
from question_management.models import Option

@admin.register(AnswerSubmission)
class AnswerSubmissionAdmin(admin.ModelAdmin):
    list_display = ('student', 'option', 'status', 'is_correct')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'option':
            if request._obj_ is not None:
                kwargs['queryset'] = Option.objects.filter(question=request._obj_.question)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_form(self, request, obj=None, **kwargs):
        # Save the object reference for use in formfield_for_foreignkey
        request._obj_ = obj
        return super().get_form(request, obj, **kwargs)

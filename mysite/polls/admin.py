from django.contrib import admin

from .models import Question, Choice

class QuestionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Question._meta.fields]

class ChoiceAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Choice._meta.fields]


admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice,ChoiceAdmin)
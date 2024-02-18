from django.contrib import admin

from .models import Challenge, Task, Completion

#@admin.register(Challenge)
class ChallengeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Challenge._meta.fields]

#@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Task._meta.fields]

#@admin.register(Completion)
class CompletionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Completion._meta.fields]


admin.site.register(Completion, CompletionAdmin)
admin.site.register(Task,TaskAdmin)
admin.site.register(Challenge,ChallengeAdmin)
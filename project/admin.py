from django.contrib import admin
from project.models import Project

# Register your models here.
class ProjectAdim(admin.ModelAdmin):
    pass


admin.site.register(Project, ProjectAdim)
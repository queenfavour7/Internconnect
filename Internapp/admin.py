from django.contrib import admin
from .models import department, Intern
# Register your models here.

@admin.register(department)
class departmentAdmin (admin.ModelAdmin):
    list_display =['course','description']
    search_fields = ['course','description','slug']

@admin.register(Intern)
class InternAdmin(admin.ModelAdmin):
    list_display = ['name','phone_number','is_active','created_on','ends_on']
    search_fields = ['department','name','created_at']
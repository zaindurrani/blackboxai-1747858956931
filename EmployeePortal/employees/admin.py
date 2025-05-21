from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'position', 'department', 'date_joined', 'promoted')
    search_fields = ('full_name', 'email', 'department')
    list_filter = ('position', 'department', 'promoted')
    ordering = ('full_name',)
    list_per_page = 10
    actions = ['mark_as_promoted']

    @admin.action(description='Mark selected employees as promoted')
    def mark_as_promoted(self, request, queryset):
        queryset.update(promoted=True)

# Customizing admin interface
admin.site.site_header = "Employee Portal Administration"
admin.site.site_title = "Employee Portal Admin"
admin.site.index_title = "Welcome to Employee Portal"

admin.site.register(Employee, EmployeeAdmin)

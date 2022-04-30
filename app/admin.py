from django.contrib import admin
from app.models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
      list_display =["name","address","salary","designation" ]
      list_filter = ["name","salary"]

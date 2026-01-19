from django.contrib import admin
from .models import userreg

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = ("name", "email")
    prepopulated_fields = {"slug":("name",)}

admin.site.register(userreg, MemberAdmin)

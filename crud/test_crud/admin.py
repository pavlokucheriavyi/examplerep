from django.contrib import admin
from .models import Crud


class CrudAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'is_completed')


admin.site.register(Crud, CrudAdmin)

# Register your models here.

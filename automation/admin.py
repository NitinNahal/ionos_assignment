from django.contrib import admin
from .models import *

# Register your models here.

class CuboidDataAdmin(admin.ModelAdmin):
    list_display = ('edge_a', 'edge_b', 'edge_c', 'addedDate',)

admin.site.register(CuboidData, CuboidDataAdmin)


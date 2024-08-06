from django.contrib import admin

from .models import Flat


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('owner', 'owners_phonenumber', 'description', 'town', 'town_district', 'address', 'floor')


admin.site.register(Flat, FlatAdmin)

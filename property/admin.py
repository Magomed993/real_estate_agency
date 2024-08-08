from django.contrib import admin

from .models import Flat
from .models import Complaint



class FlatAdmin(admin.ModelAdmin):
    search_fields = ('owner', 'owners_phonenumber', 'description', 'town', 'town_district', 'address', 'floor')
    readonly_fields = ['created_at']
    list_display = ('address', 'price', 'new_building', 'construction_year',
                    'town', 'owners_phonenumber', 'owner_pure_phone')
    list_editable = ['new_building']
    list_filter = ('new_building', 'rooms_number', 'has_balcony')
    raw_id_fields = ('liked_by',)


class ComlaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('who_complained', 'apartment_complained')


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComlaintAdmin)

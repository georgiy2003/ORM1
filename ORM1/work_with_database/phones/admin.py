from django.contrib import admin
from phones.models import Phone
# Register your models here.

@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'release_date', 'lte_exists', 'slug')
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ('name',)
    list_filter = ('lte_exists', 'release_date')
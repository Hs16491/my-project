from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price','category', 'active') #('stock', 'available', 'created', 'updated')
    list_filter = ('category', 'available')
    list_editable = ('category',)
    list_display_links = ('name',)
    search_fields = ('name', 'price', 'category')
    fields = ('name', 'content', 'price', 'image', 'active', 'category', 'available')
    #prepopulated_fields = {'slug': ('name',)}
    #ordering = ('-created',)


admin.site.register(Product, ProductAdmin)
admin.site.site_header = "Habiba's Admin"
admin.site.site_title = "Habiba's Admin Portal"
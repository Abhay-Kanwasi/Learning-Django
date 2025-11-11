from django.contrib import admin
from .models import Product, CustomUser

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity', 'category', 'is_available']
    list_filter = ['price']
    search_fields = ['name']
    list_editable = ['quantity']

    # fieldsets = [
    #     ('Basic Info', {'fields': ['name']}),
    #     ('Pricing', {'fields': ['price']})
    # ]

    actions = ['make_available', 'make_unavailable']

    def make_available(self, request, queryset):
        queryset.update(is_available='Yes')

        self.message_user(request, 'Products made available')

admin.site.register(Product, ProductAdmin)
admin.site.register(CustomUser)
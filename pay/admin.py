from django.contrib import admin

from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    '''Admin View for Payment'''

    list_display = ('email', 'amount', 'date_created', 'verified')
    list_filter = ('date_created', 'verified')
    search_fields = ('email', 'date_created')
    ordering = ('-date_created',)

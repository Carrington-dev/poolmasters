from django.contrib import admin
from applications.book.models import Contact, Subscribe


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    '''Admin View for Contact'''

    list_display = ('full_name', 'email_address', 'subject', 'date_recieved')
    list_filter = ('date_recieved',)
    search_fields = ('full_name', 'email_address', 'subject',)
    date_hierarchy = 'date_recieved'
    ordering = ('-pk',)
    readonly_fields = [ 'message']
    list_per_page: int = 30

@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_subscribed', 'date_recieved', 'date_last_viewed')
    list_filter = ('is_subscribed',)
    search_fields = ('email', )
    date_hierarchy = 'date_recieved'
    ordering = ('-pk',)
    list_per_page: int = 30

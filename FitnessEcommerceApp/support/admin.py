from django.contrib import admin

from fitnessEcommerceApp.support.models import SupportTicket


@admin.register(SupportTicket)
class SupportTicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_resolved')
    search_fields = ('title', 'message')
    list_filter = ('is_resolved', 'created_at')

    ordering = ('-created_at',)

    fieldsets = (
        (None, {
            'fields': ('title', 'message', 'created_at', 'is_resolved')
        }),
    )

    readonly_fields = ('created_at',)

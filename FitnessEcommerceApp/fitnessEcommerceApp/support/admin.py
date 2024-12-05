from django.contrib import admin

from fitnessEcommerceApp.support.models import SupportTicket, Response


class ResponseInline(admin.StackedInline):
    model = Response
    extra = 1
    readonly_fields = ('created_at',)


@admin.register(SupportTicket)
class SupportTicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_resolved')
    search_fields = ('title', 'message')
    list_filter = ('is_resolved', 'created_at')

    ordering = ('-created_at',)

    inlines = [ResponseInline]

    fieldsets = (
        (None, {
            'fields': ('title', 'message', 'created_at', 'is_resolved')
        }),
    )

    readonly_fields = ('created_at',)


@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'message', 'created_at')
    search_fields = ('ticket__title', 'message')
    ordering = ('-created_at',)


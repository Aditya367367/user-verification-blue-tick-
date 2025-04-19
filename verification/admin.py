from django.contrib import admin
from .models import Verification

@admin.register(Verification)
class VerificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'type', 'doc_type', 'doc_number', 'status')
    list_filter = ('status',)
    search_fields = ('email', 'personal_details__name', 'doc_number')
    actions = ['mark_as_verified', 'mark_as_rejected']

    def mark_as_verified(self, request, queryset):
        queryset.update(status=1)  # 1 = Verified
        self.message_user(request, "Selected submissions have been marked as Verified.")

    def mark_as_rejected(self, request, queryset):
        queryset.update(status=0)  # 0 = Rejected
        self.message_user(request, "Selected submissions have been marked as Rejected.")

    mark_as_verified.short_description = "Mark selected as Verified"
    mark_as_rejected.short_description = "Mark selected as Rejected"
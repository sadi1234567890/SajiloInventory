from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('staff', 'address', 'phone', 'department', 'joined_date', 'total_leaves', 'attendance')
    search_fields = ('staff__username', 'address', 'phone', 'department')
    list_filter = ('department', 'joined_date')
    ordering = ('-joined_date',)


admin.site.register(Profile, ProfileAdmin)

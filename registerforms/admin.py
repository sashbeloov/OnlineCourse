from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from django.contrib.auth.models import User
from django.contrib import admin
from .models import UserProfile

# Custom admin view to manage UserProfile
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'address', 'profile_picture')
    search_fields = ('user__username', 'user__email', 'phone_number')
    list_filter = ('user__is_active',)

# Register UserProfile model in admin
admin.site.register(UserProfile, UserProfileAdmin)

# Extend the default UserAdmin to include user profile info
class UserAdmin(DefaultUserAdmin):
    list_display = DefaultUserAdmin.list_display + ('get_phone_number', 'get_address')

    # Method to display phone number in user admin
    def get_phone_number(self, obj):
        return obj.userprofile.phone_number

    # Method to display address in user admin
    def get_address(self, obj):
        return obj.userprofile.address

    # Method to make the profile fields editable in the User admin page
    fieldsets = DefaultUserAdmin.fieldsets + (
        (None, {'fields': ('userprofile',)}),
    )

    # Add methods to allow inline editing of user profile info
    get_phone_number.short_description = 'Phone Number'
    get_address.short_description = 'Address'

# Unregister the default User admin and register it with the customized UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

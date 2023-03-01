from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
	("Profile", {
			"fields": ("username","grade","phone","email","age","birthday","gender",),
			"classes": ("wide",),
		},
	),
	# ("Permissions",{
	# 		"fields": (
	# 			"is_active",
	# 			"is_staff",
	# 			"is_superuser",
	# 			"user_permissions",
	# 		),
	# 	},
	# ),
	("Important Dates", {
			"fields": ("uid","last_login", "date_joined"),
			"classes": ("collapse",),   #접었다폈다
		},
	),
)
    list_display = ("username","uid", "grade","is_staff", "is_active")
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    search_fields = ("username", )
    ordering = ("username",)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )
	
    readonly_fields = ("uid","username", "date_joined", "last_login")
   
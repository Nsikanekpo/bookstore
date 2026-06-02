from django.contrib import admin
from django.urls import path, include
from pages.views import LogoutConfirmView, custom_logout

urlpatterns = [
    path('admin/', admin.site.urls),

    # STEP 1: show confirmation page
    path(
        'accounts/logout/',
        LogoutConfirmView.as_view(),
        name='account_logout'
    ),

    # STEP 2: actual logout
    path(
        'accounts/logout/confirm/',
        custom_logout,
        name='logout_confirm'
    ),

    # allauth routes
    path('accounts/', include('allauth.urls')),

    # local apps
    path('', include('pages.urls')),
]

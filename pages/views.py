from django.views.generic import TemplateView
from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import redirect


class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


# STEP 1: Show logout confirmation page
class LogoutConfirmView(TemplateView):
    template_name = 'account/logout.html'


# STEP 2: Perform actual logout
def custom_logout(request):
    logout(request)
    messages.success(
        request,
        'You have been logged out successfully.'
    )
    return redirect('home')

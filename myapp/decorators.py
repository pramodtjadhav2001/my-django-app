# decorators.py

from django.http import HttpResponseForbidden

def login_required(view_func):
    def wrapped_view(request, *args, **kwargs):
        # Check if user is authenticated and is an admin
        if request.user.is_authenticated and request.user.is_staff:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("You are not authorized to access this page.")
    return wrapped_view

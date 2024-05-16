# SMS/decorators.py
from django.http import HttpResponseForbidden
from functools import wraps

def admin_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.admin:
            return HttpResponseForbidden("No tienes permiso para acceder a esta página.")
        return view_func(request, *args, **kwargs)
    return _wrapped_view

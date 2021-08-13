from django.shortcuts import redirect

class SuperUserRequireMixin(object):
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_staff:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect('index')
    
from main.forms import RegistrationForm
from django.views.generic import FormView
from main.models import User

class RegistrationFormView(FormView):
    form_class = RegistrationForm

    def get(self, request):
        if (request.GET.get("unregister") == "1") and request.session.get("registered"):
            request.session.pop("registered")

        return super().get(request)

    def form_valid(self, form):
        if form.can_register_user and not self.request.session.get("registered"):
            self.request.session["registered"] = form.get_username()
        
        return super().form_valid(form)

class RegistrationAndMainView(RegistrationFormView):
    template_name = "index.html"
    success_url = "/"

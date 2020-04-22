from main.forms import RegistrationForm
from django.views.generic import FormView, base
from main.models import User
from news.models import Article

class RegistrationFormView(FormView):
    form_class = RegistrationForm

    def get(self, request, *args, **kwargs):
        if (request.GET.get("unregister") == "1") and request.session.get("registered"):
            request.session.pop("registered")

        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        if form.can_register_user and not self.request.session.get("registered"):
            self.request.session["registered"] = form.get_username()
        
        return super().form_valid(form)

class RegistrationAndMainView(RegistrationFormView):
    template_name = "index.html"
    success_url = "/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["articles"] = Article.objects.all().order_by("-id")[:10]
        registered = self.request.session.get("registered")

        if registered:
            user = User.objects.get(username=registered)
            context["registered"] = user
        else:
            context["registered"] = None

        return context

class StopSpamView(base.TemplateView):
    template_name = "stop_spam.html"

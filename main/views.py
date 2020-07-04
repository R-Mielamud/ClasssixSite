from main.forms import RegistrationForm
from django.views.generic import FormView
from main.models import User
from news.models import Article
from django.core.cache import cache
from django.core.cache.utils import make_template_fragment_key

class RegistrationFormView(FormView):
    form_class = RegistrationForm

    def get(self, request, *args, **kwargs):
        if (request.GET.get("unregister") == "1") and request.session.get("registered"):
            request.session.pop("registered")
            students_sidebar = make_template_fragment_key("editratings_students_sidebar")
            table = make_template_fragment_key("editratings_table_body")
            cache.delete(students_sidebar)
            cache.delete(table)

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

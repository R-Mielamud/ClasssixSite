from main.views import RegistrationFormView
from django.shortcuts import redirect

class SelectThemeView(RegistrationFormView):
    template_name = "select_theme.html"
    success_url = "/select_theme/"

    def post(self, request, *args, **kwargs):
        request.session["theme"] = request.POST.get("theme") or "Light"
        return redirect("/")

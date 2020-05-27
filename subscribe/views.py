from main.views import RegistrationFormView
from django.views.generic import View
from django.shortcuts import redirect
from main.models import User

class UnsubscribeView(View):
    def get(self, request, *args, **kwargs):
        username = request.session.get("registered")

        if not username:
            return redirect("/")
        else:
            user = User.objects.get(username=username)

            if not user.email:
                return redirect("/")

            user.email = None
            user.is_subscriber = False
            user.save()

        return redirect("/")

class SubscribeView(RegistrationFormView):
    success_url = "/subscribe/"
    template_name = "subscribe.html"

    def _is_email_valid(self, email):
        splited = email.split("@")

        if len(splited) != 2 or splited[0] == "":
            return False

        service = splited[1]
        splited_service = service.split(".")

        if len(splited_service) != 2 or splited_service[0] == "" or splited_service[1] == "":
            return False
        
        return True

    def post(self, request, *args, **kwargs):
        email = request.POST.get("email")

        if not self._is_email_valid(email):
            request.session["is_invalid_email"] = True
            return super().post(request, *args, **kwargs)
        else:
            request.session["is_invalid_email"] = None
            username = request.session.get("registered")

            if not username:
                return redirect("/")

            user = User.objects.get(username=username)
            user.email = email
            user.is_subscriber = True
            user.save()

        return redirect("/")

    def get(self, request, *args, **kwargs):
        username = self.request.session.get("registered")

        if not username:
            return redirect("/")
            
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["can_show_warning"] = self.request.session.get("is_invalid_email")
        return context

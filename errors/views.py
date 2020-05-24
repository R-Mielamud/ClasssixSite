from django.views.generic.base import TemplateView

class ErrorView(TemplateView):
    template_name = "error.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["status"] = self.kwargs["status"][:3]
        context["message"] = self.kwargs["phrase"][:len(self.kwargs["phrase"]) - 1]
        return context

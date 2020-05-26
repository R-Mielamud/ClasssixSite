from django.views.generic.base import TemplateView
from diary import constants

class WikipediaView(TemplateView):
    template_name = "wikipedia.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["status_to_color"] = constants.STATUS_TYPE_TO_COLOR
        return context

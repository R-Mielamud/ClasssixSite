from django.views import View
from django.shortcuts import redirect
from main.models import User
from diary_pdf.utils import render_to_pdf
from django.http import HttpResponse

class DiaryPdfView(View):
    def get(self, request, *args, **kwargs):
        user = User.objects.filter(username=request.session.get("registered")).first()

        if not user or user.is_teacher:
            return redirect("/")

        pdf = render_to_pdf("diary_pdf.html", {

        })

        return HttpResponse(pdf, content_type="application/pdf")

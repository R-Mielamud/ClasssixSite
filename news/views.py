from main.views import RegistrationFormView
from django.views.generic import View
from news.models import Article
from main.models import User
from django.shortcuts import redirect
from ClasssixSite.celery import send_emails

class DeleteArticleView(View):
    def get(self, request, *args, **kwargs):
        if not request.session.get("registered"):
            return redirect("/")

        if request.GET.get("pk") and request.GET.get("pk").isdigit():
            pk = request.GET.get("pk")
            article = Article.objects.filter(pk=pk).first()

            if article:
                article.delete()

        return redirect("/")

class EditArticleView(RegistrationFormView):
    success_url = "/add_article/"
    template_name = "edit_article.html"

    def get(self, request, *args, **kwargs):
        pk = request.GET.get("pk")

        if not pk or not pk.isdigit() or not Article.objects.filter(pk=int(pk)).first():
            return redirect("/add_article/")

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = Article.objects.get(pk=int(self.request.GET.get("pk")))
        context["header"] = article.header
        context["text"] = article.text

        if not self.request.session.get("registered"):
            context["canRedirect"] = "y"

        return context

    def post(self, request, *args, **kwargs):
        if not request.session.get("registered"):
            return redirect("/")

        article = Article.objects.get(pk=int(self.request.GET.get("pk")))
        article.header = request.POST.get("header")
        article.text = request.POST.get("text")

        if request.POST.get("image_changed") == "y":
            article.image = request.FILES.get("image")

        if request.POST.get("video_changed") == "y":
            article.video = request.FILES.get("video")

        article.save()
        return redirect("/")

class AddArticleView(RegistrationFormView):
    success_url = "/add_article/"
    template_name = "add_article.html"

    def _send_emails(self, data):
        send_emails(data)

    def post(self, request, *args, **kwargs):
        if not request.session.get("registered"):
            return redirect("/")

        if request.POST.get("save_article"):
            registered = request.session.get("registered")
            author = User.objects.get(username=registered)
            header = request.POST.get("header")
            text = request.POST.get("text")
            image = request.FILES.get("image")
            video = request.FILES.get("video")

            Article.objects.create(
                author=author,
                header=header,
                text=text,
                image=image,
                video=video
            )

            email_data = {
                "subject": "Новина!",
                "message": "Хтось написав новину! Переходь сюди: http://rl-classfive.com.ua",
                "from": "admin@rl-classfive.com.ua"
            }

            self._send_emails(email_data)

        return redirect("/")

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        if not self.request.session.get("registered"):
            context["canRedirect"] = "y"
        
        return context 

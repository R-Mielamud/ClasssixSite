from django.conf.urls import url
from news.views import AddArticleView, EditArticleView, DeleteArticleView

urlpatterns = [
    url(r"^add_article/$", AddArticleView.as_view()),
    url(r"^edit_article/$", EditArticleView.as_view()),
    url(r"^delete_article/$", DeleteArticleView.as_view())
]

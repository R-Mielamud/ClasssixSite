from main.models import User

def buttons(request):
    registered = request.session.get("registered")

    context = {
        "canShowToDiaryButton": "n",
        "canShowEditRatingsButton": "n",
        "canShowUnsubscribeButton": "n",
        "user_obj": User.objects.filter(username=registered).first(),
        "theme": request.session.get("theme") or "Light"
    }
    
    if registered:
        user = User.objects.filter(username=registered).first()

        if user and (not user.is_teacher):
            context["canShowToDiaryButton"] = "y"
        else:
            context["canShowEditRatingsButton"] = "y"

        if user and user.email:
            context["canShowUnsubscribeButton"] = "y"

    return context

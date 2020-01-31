from main.models import User

def buttons(request):
    registered = request.session.get("registered")

    context = {
        "canShowToDiaryButton": "n",
        "canShowEditRatingsButton": "n"
    }
    
    if registered:
        user = User.objects.get(username=registered)

        if not user.is_teacher:
            context["canShowToDiaryButton"] = "y"
        else:
            context["canShowEditRatingsButton"] = "y"

    return context

from main.views import RegistrationFormView
from editratings.forms import EditRatingsForm
from main.models import User
from diary import constants
from diary.models import Rating, RatingSet, Subject

class EditRatingsView(RegistrationFormView):
    template_name = "editratings.html"
    success_url = "/editratings/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["students"] = User.objects.filter(is_teacher=False)
        context["subjects"] = Subject.objects.all()
        context["possible_statuses"] = [status[0] for status in constants.RATING_TYPES]
        registered = self.request.session.get("registered")

        if registered:
            user = User.objects.get(username=registered)

            if not user.is_teacher:
                context["canRedirect"] = "y"
            else:
                context["canRedirect"] = "n"
        else:
            context["canRedirect"] = "y"

        return context

    def post(self, request, *args, **kwargs):
        if request.POST.get("submit"):
            students = User.objects.filter(is_teacher=False)
            post = request.POST
            subject = post.get("subject-input")

            for student in students:
                ratings = []

                for i in range(1, 5, 1):
                    value = post.get("rating-input-" + str(i) + "-for-" + student.username)
                    status = post.get("status-input-" + str(i) + "-for-" + student.username)

                    if value != "":
                        value = int(value)

                        ratings.append(Rating(
                            value=value,
                            status=status
                        ))

                date = post.get("date-input-for-" + student.username)
                date_splited = date.split("-")
                year, month, day = date_splited
                del year
                month_formatted = int(month) - 8 if int(month) > 8 else int(month) + 4

                for r in ratings:
                    r.save()

                if len(ratings) > 0:
                    rating1 = ratings[0] if len(ratings) >= 1 else None
                    rating2 = ratings[1] if len(ratings) >= 2 else None
                    rating3 = ratings[2] if len(ratings) >= 3 else None
                    rating4 = ratings[3] if len(ratings) >= 4 else None

                    rating_set = RatingSet(
                        rating1=rating1,
                        rating2=rating2,
                        rating3=rating3,
                        rating4=rating4,
                        subject=Subject.objects.get(name=subject),
                        month=month_formatted,
                        day=day
                    )

                    rating_set.save()
                    student.ratings.add(rating_set)

        return super().post(request, *args, **kwargs)

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
        context["possible_statuses"] = [status[0] for status in constants.RATING_TYPES]
        return context

    def post(self, request, *args, **kwargs):
        if request.POST.get("submit"):
            students = User.objects.filter(is_teacher=False)
            post = request.POST

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
                    subject=Subject.objects.get(name="Укр. мова"),
                    month=1,
                    day=1
                )

                rating_set.save()
                student.ratings.add(rating_set)

        return super().post(request, *args, **kwargs)







































# if request.POST["submit"]:
        #     post = request.POST
        #     ratings = []
        #     rating_sets = []

        #     for student in User.objects.filter(is_teacher=False):
        #         for i in range(1, 5, 1):
        #             rating = post["rating-input-" + str(i) + "-for-" + student.username]

        #             ratings.append(Rating(
        #                 value=int(rating) if rating != "" else None,
        #                 status=post["status-input-" + str(i) + "-for-" + student.username]
        #             ))

        #         for r in ratings:
        #             if r.value is not None:
        #                 r.save()
        #             else:
        #                 r.save()
        #                 r.delete()

        #         if len(ratings) >= 2:
        #             print("2")

        #         rating_sets.append(RatingSet(
        #             rating1=ratings[0] if len(ratings) >= 1 else None,
        #             rating2=ratings[1] if len(ratings) >= 2 else None,
        #             rating3=ratings[2] if len(ratings) >= 3 else None,
        #             rating4=ratings[3] if len(ratings) >= 4 else None,
        #             subject=Subject.objects.get(name="Укр. мова"),
        #             month=1,
        #             day=1
        #         ))

        #         ratings = []

        #     for rs in rating_sets:
        #         rs.save()

        #     user = User.objects.get(username=request.session.get("registered"))
        #     user.ratings.add(*rating_sets)



























# def post(self, request, *args, **kwargs):
    #     Post = request.POST or None
    #     edit_ratings_form = self.edit_ratings_form_class(Post, prefix="rating_set")
    #     context = self.get_context_data(edit_ratings_form=edit_ratings_form)

    #     if edit_ratings_form.is_valid():
    #         self.edit_ratings_form_valid(edit_ratings_form)

    #     super().post(request, *args, **kwargs)
    #     return self.render_to_response(context)

    # def edit_ratings_form_valid(self, form):
    #     print("All works!!!")
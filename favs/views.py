from django.shortcuts import redirect, reverse, render
from django.contrib.auth.decorators import login_required


from favs.models import FavList
from books.models import Book
from movies.models import Movie


@login_required()
def fav_list(request):
    try:
        favlist = FavList.objects.get(created_by=request.user)
    except FavList.DoesNotExist:
        return redirect(reverse("core:home"))

    return render(
        request,
        "pages/favs/fav_list.html",
        {
            "favlist": favlist,
        },
    )


@login_required()
def toggleList(request, pk):
    type = request.GET.get("type", "movie")
    print(pk)
    user = request.user
    fav_list, _ = FavList.objects.get_or_create(created_by=user)
    print(fav_list)
    if type == "movie":
        movie = Movie.objects.get(pk=pk)
        if movie in fav_list.movies.all():
            fav_list.movies.remove(movie)
        else:
            fav_list.movies.add(movie)
        fav_list.save()
        return redirect(reverse("core:home"))
    else:
        book = Book.objects.get(pk=pk)
        print(book)
        if book in fav_list.books.all():
            fav_list.books.remove(book)
        else:
            fav_list.books.add(book)
        fav_list.save()
        return redirect(reverse("core:home"))


# def toggleList(request, pk):
#     user = request.user
#     if str(user) == "AnonymousUser":
#         return redirect(reverse("users:login"))
#     action = request.GET.get("action")
#     room = room_models.Room.objects.get(pk=pk)
#     if room is not None and action is not None:
#         the_list, b = list_models.List.objects.get_or_create(
#             user=request.user, name="My Favorite Houses"
#         )
#         if action == "add":
#             the_list.rooms.add(room)
#         elif action == "remove":
#             the_list.rooms.remove(room)
#     return redirect(reverse("core:home"))

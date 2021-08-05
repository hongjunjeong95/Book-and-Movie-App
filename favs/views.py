from django.shortcuts import redirect, reverse, render
from django.contrib.auth.decorators import login_required


from favs.models import FavList


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

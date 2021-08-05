from django import template
from favs.models import FavList

register = template.Library()


@register.simple_tag(takes_context=True)
def is_book_on_favs(context, book):
    user = context.request.user
    if str(user) == "AnonymousUser":
        return False
    try:
        the_list = FavList.objects.get(created_by=user)
        return book in the_list.books.all()
    except FavList.DoesNotExist:
        return False


@register.simple_tag(takes_context=True)
def is_movie_on_favs(context, movie):
    user = context.request.user
    if str(user) == "AnonymousUser":
        return False
    try:
        the_list = FavList.objects.get(created_by=user)
        return movie in the_list.movies.all()
    except FavList.DoesNotExist:
        return False

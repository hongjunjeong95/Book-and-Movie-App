from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", include("core.urls", namespace="core")),
    path("books/", include("books.urls", namespace="books")),
    path("movies/", include("movies.urls", namespace="movies")),
    path("category/", include("categories.urls", namespace="category")),
    path("people/", include("people.urls", namespace="people")),
    path("users/", include("users.urls", namespace="users")),
    path("favs/", include("favs.urls", namespace="favs")),
    path("reviews/", include("reviews.urls", namespace="reviews")),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

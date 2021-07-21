from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", include("core.urls", namespace="core")),
    path("books/", include("books.urls", namespace="books")),
    # path("movies/", include("movies.urls", namespace="movies")),
    # path("genres/", include("genres.urls", namespace="genres")),
    # path("people/", include("people.urls", namespace="people")),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

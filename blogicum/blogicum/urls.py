from django.contrib import admin
from django.urls import include, path

urlpatterns: list[path] = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('pages/', include('pages.urls')),
]

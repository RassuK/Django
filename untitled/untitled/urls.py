from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path("projects/", include("portfolio_app.urls")),

    path("blog/", include("blog.urls")),
]

from django.urls import path

from . import views
urlpatterns = [
    path('', views.index),
    path('blog', views.blog),
    path('blog/new', views.new),
    path('blog/create', views.create),
    path('show/<int:num>', views.show),
    path('<num>/edit', views.edit),
    path('<int:num>/delete', views.destroy),
    path('blog/json', views.bonus),
]
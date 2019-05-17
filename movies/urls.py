from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('<int:movie_pk>/update_comment/<int:comment_pk>/', views.update_comment, name='update_comment'),
    path('<int:movie_pk>/delete_comment/<int:comment_pk>/', views.delete_comment, name='delete_comment'),
    path('<int:movie_pk>/create_comment/', views.create_comment, name='create_comment'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    path('listings/<int:genre_pk>', views.genre_listings, name="genre_listings"),
    path('listings/', views.listings, name="listings"),
    path('', views.list, name="list"),
]
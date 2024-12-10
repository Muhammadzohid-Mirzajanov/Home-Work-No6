from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<int:category_id>/', views.category_books, name='category_books'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
]

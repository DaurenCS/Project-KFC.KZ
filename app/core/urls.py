from django.urls import path

from . import views

urlpatterns = [
    path("categories/", views.ListFoodTypes.as_view()),
    path("foodlist/", views.ListAllFood.as_view()),
    path("bevlist/", views.ListAllBev.as_view()),
    path("food/<int:food_id>/", views.GetItemById.as_view()),
    path("food_cat/<int:food_cat_id>/", views.GetItemsByType.as_view()),
    path("adverts/", views.AdvertisementsAPIView.as_view())
]

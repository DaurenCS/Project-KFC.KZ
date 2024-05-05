from django.urls import path

from . import views

urlpatterns = [
    path("create-or-get/", views.CreateOrderView.as_view()),
    path("<int:order_id>/", views.GetOrderById.as_view()),
    path("<int:order_id>/pay/", views.PayOrderView.as_view()),
    path("<int:order_id>/accept/", views.AcceptDeliveryView.as_view()),
    path("<int:order_id>/status/", views.GetOrderStatus.as_view()),
    path("<int:order_id>/add_item/", views.AddItemToOrder.as_view()),
    path("<int:order_id>/add_items/", views.AddItemsToOrder.as_view()),
    path("<int:order_id>/remove_item/", views.RemoveItemFromOrder.as_view()),
    path("<int:order_id>/delete/", views.DeleteOrder.as_view()),
    path("user/all/", views.GetAllOrders.as_view()),
]
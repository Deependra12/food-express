from os import name
from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path("create/", views.order_create_cash_payment, name="order_create"),
    path("create/pay-by-khalti/<str:token>/", views.order_create_khalti_payment, name="order_create_khalti_payment"),
    path("ajax/verify-payment/", views.verify_payment, name='verify_payment'),
    path("order_detail/<int:order_id>/", views.order_detail, name='order_detail'),
    path("order_detail/verify/<int:order_id>", views.verify_order, name="verify_order"),
    path("order_detail/unverify/<int:order_id>/", views.unverify_order, name="unverify_order"),

    # buy now
    path("create/buynow/<int:food_id>/<int:quantity>/", views.order_create_buy_now, name="order_create_buy_now"),
    path("create/buynow/<int:food_id>/<int:quantity>/<str:coupon>/", views.order_create_buy_now, name="order_create_buy_now_coupon"),
    path("create/buynow/pay-by-khalti/<int:food_id>/<int:quantity>/<str:token>/", views.order_create_buy_now_khalti_payment,name="order_create_buy_now_khalti_payment"),
    path("create/buynow/pay-by-khalti/<int:food_id>/<int:quantity>/<str:token>/<str:coupon>", views.order_create_buy_now_khalti_payment,name="order_create_buy_now_khalti_payment_coupon"),

    path('admin/order/<int:order_id>/invoice/', views.admin_order_pdf, name='admin_order_pdf'),

    # reorder
    path('reorder/<int:order_id>/', views.reorder, name='reorder'),
    path('reorder/create/<int:order_id>/', views.create_order_reorder, name="create_order_reorder"),
    path('reorder/create/<int:order_id>/<str:coupon>/', views.create_order_reorder, name="create_order_reorder_coupon"),
    path('reorder/create/pay-by-khalti/<int:order_id>/<str:token>/', views.create_order_reorder_khalti, name="create_order_reorder_khalti"),
    path('reorder/create/pay-by-khalti/<int:order_id>/<str:token>/<str:coupon>/', views.create_order_reorder_khalti, name="create_order_reorder_khalti_coupon"),

]

from django.contrib import admin
from django.urls import path
from payments.views import payments_list, create_payment

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pays/', payments_list),
    path('create/', create_payment)
]

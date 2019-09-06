from django.contrib import admin
from django.urls import path
from payments.views import payments_list, create_payment
from circulars.views import circular, create_circular

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pays/', payments_list),
    path('create/', create_payment),
    path('circulars/',circular),
    path('create_circular/',create_circular)
]

from django.contrib import admin
from django.urls import path, include
from requests import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('requests.urls'))
]

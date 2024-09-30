# main_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('userAuth.urls')),
    path('admin/', admin.site.urls),
    path('matumizi/', include('matumizi.urls')),
    path('income/', include('incomes.urls'))

]

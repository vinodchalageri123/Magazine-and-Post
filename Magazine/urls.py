from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('magazines', views.all_magazine, name='list-magazines'),
    path('add_magazine', views.add_magazine, name="add-magazine"),

    # path('update_magazine', views.update_magazine, name="update-magazine"),
    path('magazine_pdf', views.magazine_pdf, name="magazine-pdf"),

]

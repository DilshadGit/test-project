from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from . import views
from .views import home_view, list_items, create_item, detail_item, update_item, delete_item

urlpatterns = [
    url(r'^$', views.home_view, name='home'),
    url(r'^list/$', views.list_items, name='item_list'),
    url(r'^create/$', views.create_item, name='item_create'),
    url(r'^detail/(?P<slug>[\w-]+)/$', views.detail_item, name='item_detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', views.update_item, name='item_update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', views.delete_item, name='item_delete'),
]

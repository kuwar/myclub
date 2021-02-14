from django.urls import path, re_path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'events', views.EventViewSet)

urlpatterns = [

    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # path('', views.index, name='index'),
    # path('<int:year>/<str:month>/', views.index, name='index'),
    re_path(r'^(?P<year>[0-9]{4})/(?P<month>0?[1-9]|1[0-2])/', views.index, name='index'),

    # events
    # path('events/', views.all_events, name='show-events'),
]

from  rest_framework.routers import DefaultRouter
from . import views
from django.urls import path
from .views import *

# router=DefaultRouter()
# router.register('api/todo',views.ToDoViewSet,basename='todo')
# router.register('api/to-do',views.ToDoApiView,basename='to-do')
# router.register('api/todo<int:id>',views.ToDoApiIdView,basename='to-do-id')


# urlpatterns =router.urls
# urlpatterns =router.urls
# urlpatterns =router.urls

urlpatterns=[
    path('api/to-do/',ToDoApiView.as_view()),
    path('api/to=do/<int:id>',ToDoApiIdView.as_view())
]

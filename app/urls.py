from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('topic/<id>',views.topic ,name='topic'),
    path('subtopic/<id>',views.subtopic ,name='subtopic'),
]

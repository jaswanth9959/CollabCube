from django.urls import path
from .views import activityPage, createRoom, deleteMessage, deleteRoom, rooms,room,joinRoom, topicsPage, updateRoom

urlpatterns = [
    path('',rooms,name='rooms'),
    path('room/<str:pk>',room,name="room"),
    path('create-room/',createRoom,name= "create-room"),
    path('update-room/<str:pk>',updateRoom,name= "update-room"),
    path('delete-room/<str:pk>',deleteRoom,name= "delete-room"),
    path('delete-message/<str:pk>',deleteMessage,name= "delete-message"),
    path('join-room/<str:pk>', joinRoom, name = "join-room"),    
    path('topics/', topicsPage, name="topics"),
    path('activity/', activityPage, name="activity"),
]
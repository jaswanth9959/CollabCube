from django.urls import path
from .views import announcement, announcements, createAnnouncement, createMessage, createSkill, inbox, mynotes, notes,updateSkill,deleteSkill, editAccount, loginUser, logoutUser, profiles, uploadnotes, userAccount,myAnnouncements,userProfile,registerUser, viewMessage, updateAnnouncement, deleteAnnouncement,editnotes, deletenotes
urlpatterns=[
    path('',profiles, name="profiles"),
    path('profile/<str:pk>/',userProfile,name="user-profile"),
    path('login/',loginUser,name="login"),
    path('logout/',logoutUser,name="logout"),
    path('register/',registerUser,name="register"),
    path('account/',userAccount,name= "account"),
    path('edit-account/', editAccount,name="edit-account"),
    path('create-skill/',createSkill,name="create-skill"),
    path('update-skill/<str:pk>/',updateSkill,name="update-skill"),
    path('delete-skill/<str:pk>/',deleteSkill,name="delete-skill"),
    path('inbox/',inbox,name="inbox"),
    path('message/<str:pk>/',viewMessage,name="message"),
    path('create-message/<str:pk>/', createMessage,name="create-message"),
    path('announcements/',announcements,name="announcements"),
    path('create-announcement/',createAnnouncement,name="create-announcement"),
    path('update-announcement/<str:pk>',updateAnnouncement,name="update-announcement"),
    path('delete-announcement/<str:pk>',deleteAnnouncement,name="delete-announcement"),
    path('announcement/<str:pk>',announcement,name="announcement"),
    path('myannouncements/',myAnnouncements,name="myAnnouncements"),
    path('notes/',notes,name="notes"),
    path('mynotes/',mynotes,name="my-notes"),
    path('uploadnotes/',uploadnotes,name="upload-notes"),
    path('editnotes/<str:pk>',editnotes,name="edit-notes"),
    path('deletenotes/<str:pk>',deletenotes,name="delete-notes"),

]
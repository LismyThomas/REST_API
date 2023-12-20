from django.urls import path,include
from . views import PersonListCreateView,PersonDetailView


urlpatterns = [
   
    path('',PersonListCreateView,name='person-list-create'),
    path('person/<pk>/',PersonDetailView,name='person_details'),
 
]
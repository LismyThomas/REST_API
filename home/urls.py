
from django.urls import path,include
from . views import PersonListCreateView,PersonDetailView


urlpatterns = [
   
    path('',PersonListCreateView.as_view(),name='person-list-create'),
    path('person/<pk>/',PersonDetailView.as_view(),name='person_details'),
 
]
from django.urls import path
from .views import home, tour, about, view, contact, read, create,  update, delete, parvoz, yunalish, overall


urlpatterns = [
   path('home', home, name="home"),
   path('tour/<int:id>/', tour, name="tour"),
   path('about', about, name="about"),
   path('view/<int:service_id>/', view, name="view"),
   path('contact/', contact, name="contact"),
   
  
  
   path('read/<int:id>/', read, name="read"),
   path('create', create, name="create"),
   path('update/<int:id>/', update , name="update"),
   path('delete/<int:id>/', delete , name="delete"),
   
   
   path('parvoz/<int:id>/', parvoz , name="parvoz"),
   path('yunalish', yunalish, name="yunalish"),
   path('overall/<int:id>/', overall, name="overall"),
   
   
   
   
   
   
   
   
   

    
]

from department_heads import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
   
    url('dhead/',views.departmentheads),
    
]
from django.urls import path
from .views import home
app_name = "slideshow"
urlpatterns = [
	path('',home,name="home")

]
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.urls import path
from .views import  about_view, contact
from .views import login_view, register_user ,profile_view 
from django.contrib.auth.views import LogoutView

app_name = 'djangoapp'
urlpatterns = [
    # route is a string contains a URL pattern
    # view refers to the view function
    # name the URL

    # path for about view

    # urls.py
    path(route='', view=views.get_dealerships, name='index'),


    
    path('about/', about_view, name='about'),
    # Add more paths as needed



    # path for contact us view
    path('contact/', contact, name='contact'),
   


    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path('logout/', LogoutView.as_view(next_page='djangoapp:index'), name='logout'),
    path('profile/', profile_view, name='profile'),
    

    

    # path for dealer reviews view

    # path for add a review view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path
from .import views
from .views import logout_user
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.index,name='index'),
    path('services/',views.services,name='services'),
    path('register/',views.register,name='register'),
    path('post-service/',views.postServices,name='post-service'),
    path('profile/',views.profile,name='profile'),
    path('get-post', views.get_post, name='get_post'),
    path('update_service_post/', views.update_service_post, name='update_service_post'),
    path('add-post/', views.addPost, name='add_post'),
    path('login/',views.loginUser,name='login'),
    path('logout/', logout_user, name='logout'),
    path('delete_post/', views.delete_post, name='delete_post'),
    path('pageNotFound/',views.errorPage,name='pageNotFound'),        
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

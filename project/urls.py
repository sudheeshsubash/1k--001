
from django.contrib import admin
from django.urls import path
from application import views as application_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', application_views.index, name='index'),
    path('projects', application_views.listprojects, name='listprojects'),
    path('project/<int:id>', application_views.projects, name='project'),
    path('members', application_views.listmembers, name='listmembers'),
    path('member/<int:id>', application_views.members, name='member'),
    
]


from django.urls import path
from . import views
app_name='dramaapp'
urlpatterns = [

    path('',views.index,name='index'),
    path('drama/<int:drama_id>/',views.detail,name='detail'),
    path('add/',views.add_drama,name='add_drama'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')


]
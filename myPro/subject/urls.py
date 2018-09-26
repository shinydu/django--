from django.urls import path,re_path

from .views import SubjectList ,AddView,DetailView,DeleteView,EditView
app_name='subject'
urlpatterns = [
    path('',SubjectList.as_view(),name='home') ,
    path('add/',AddView.as_view(),name='add'),
    path('detail/',DetailView.as_view(),name='detail'),
    path('delete/',DeleteView.as_view(),name='delete'),
    path('edit/',EditView.as_view(),name='edit11')
]
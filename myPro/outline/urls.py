from django.urls import path,re_path
from .views import OutlineListView,DetailView,DeleteView,AddView,EditView
app_name='outline'
urlpatterns=[
    path('list/',OutlineListView.as_view(),name='list'),
    path('detail/',DetailView.as_view(),name='detail'),
    path('delete/',DeleteView.as_view(),name='delete'),
    path('add/',AddView.as_view(),name='add'),
    path('edit/',EditView.as_view(),name='edit')
]
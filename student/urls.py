from django.urls import path
from.import views
urlpatterns = [
    path('register/',views.register),
    path('display/',views.display),
    path('up/(?P<pk>\w+)/',views.update_new, name='update'),
    path('delete/(?P<pk>\d+)/',views.delete, name='delete'),
    path('std_api/',views.student_view.as_view())

]
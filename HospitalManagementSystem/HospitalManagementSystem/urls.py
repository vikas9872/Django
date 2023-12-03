from django.contrib import admin
from django.urls import path,include
# import views from the app 
from hmsapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Update the url patterns
    path('',views.home),
    path('toappointment',views.gotoappointment),
    path('viewdetails/',views.displayOperation),
    path('viewdetails/deletedetails/<int:id>',views.deleteOperation),
    path('viewdetails/updatedetails/<int:id>',views.editPage),
    path('update/<int:id>',views.updateOperation),
    path('makeappointment',views.makeappointment)
]

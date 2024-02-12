from django.contrib import admin
from django.urls import path,include
from.import views



app_name="fileapp"
# from authentication.views import upload_file

admin.site.site_header = "Admin  pashya"
admin.site.site_title = "pashya Admin Portal"
admin.site.index_title = "Welcome to pashya Researcher Portal"



urlpatterns = [
    path('degree',views.degree,name='degreeselection'),
    path('home',views.home, name="home"),
    path('signup',views.signup, name="signup"),
    path('signin',views.signin , name="signin"),
    path('adminpashya',views.adminpashya, name="signinhome"),
    path('signout',views.signout, name="signuout"),
    # path('homes',views.ASSIGNMENT,name="home2"),
    path('view',views.show_file,name="views"),
    path('view2',views.show_file2,name="view20"),
    # path('list/',upload_file,name='list'),
    # path('assign/',views.show_upload,name='assign/'),
    path('subject/',views.subject,name='subject1/'),
    path('uploadj',views.index3,name='uploads'),
    # path('upload',views.send_files,name='uploads'),
    path('seej',views.show_j,name='seej1'),
    path('upload',views.ASSIGNMENT,name='uploadsa'),
    path('uploadfees',views.fees,name='uploadsf'),
    path('seefees',views.show_fees,name='seefee'),
    path('',views.class_note,name='uploadclass_notebook'),
    path('seeclassnote',views.show_classnote,name='seenclass_notebook'),
   

    path('upassignments',views.assignments,name='upassignment'),
    path('seeassignments',views.show_assignments,name='seeassignments'),
   ]
from django.contrib import admin
from django.urls import path
from chemicals import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home_page,name='home'),
    path('start/', views.startpage,name = 'start'),
    path('', views.startpage),
    path('detail/<int:id>', views.detailpage2),
    path('enterchemical/', views.detail),
    path('addtosql/', views.addtosql),
    path('modifysql/', views.modifysql),
    path('delete/<int:id>', views.deleteItem, name = 'deleteItem'),
    path('downloadcsv/', views.export_csv),
    path('login/', views.loginpage, name='login'),
    path('signup/', views.signup),
    path('searched/', views.searchedResults, name = 'searchedresult'),
    path('logout/', views.logoutUser,name = 'logout'),
    path('printpage/<int:id>', views.print,name = 'printpage')
]

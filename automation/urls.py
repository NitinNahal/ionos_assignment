from django.urls import path, include
from . import views

app_name = 'automation'
urlpatterns = [
    path('', views.index, name='index'),
    #path('getData/<str:datatype>/', views.getData, name='getData'),
    path('upData/<str:datatype>/', views.upData, name='upData'),    
    
    # path('login', views.login, name='login'),
    # path('logout', views.logout, name='logout'),
    # path('inputFile/<str:defaultActivity>', views.inputFile, name='inputFile'),
    # path('data/<str:datatype>/', views.data, name='data'),

    # # celery view
    # path('getData/<str:datatype>/', views.getData, name='getData'),
    # path('upData/<str:datatype>/', views.upData, name='upData'),

    # path('updatedata/<str:datatype>/', views.updatedata, name='updatedata'),
    # path('clearAllData', views.clearAllData, name='clearAllData'),
    # path('newDayData', views.newDayData, name='newDayData'),
    # path('appendErrorList', views.insertErrorList, name='insertErrorList'),
    # path('appendUserList', views.insertUserList, name='insertUserList'),
    # path('cleanData', cron.thread_delete_data, name='cleanData'),
    # path('resetpassword/<str:datatype>/', views.resetpassword, name='resetpassword'),
    # path('getJSONFormFillData/<str:datatype>/', views.getJSONFormFillData, name='getJSONFormFillData'),
    # path('dataPost/<str:datatype>/', views.runDesign, name='dataPost'),

    # # To check multidb
    # path('multidb', views.multidb, name='multidb'),

    # # To check Activity Seperately
    # #path('test', views.test, name='test'),

    # # To check data encryption
    # path("checkPE", views.checkPE, name='checkPE'),
    
]

from django.urls import path
from . import views
urlpatterns = [
    path('dashboard', views.dashboardView ,name="YieldDASHBoard" ),
    path('calender', views.calenderView ,name="YieldCalender" ),
    path('marketplace', views.marketPlaceView ,name="YieldMarketPlace" ),
    path('yieldhistory', views.yieldHistoryView ,name="YieldRateHistory" ),
    path('forcasts', views.forcastView ,name="YieldForcasts" ),
    path('room_type', views.roomTypeView ,name="YieldRoomType" ),
    path('Dow_yoy', views.dowYoyView ,name="YieldDOWYOY" ),
    path('main', views.mainYieldView ,name="YieldMain" ),
    path('monthly', views.monthlyView ,name="YieldMonthly" ),
    path('top10', views.TopView ,name="YieldTop10" ),
    path('settings', views.settingView ,name="YieldSettings" ),
    path('setting-delete/<status> <id>', views.settingDelete, name="SettingDeleteForm")
]
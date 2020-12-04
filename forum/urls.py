from django.urls import path
from . import views

app_name='forum'

urlpatterns = [
   path('main/',views.main,name='main'),
   path('searchForum/',views.searchForum,name='searchForum'),
   path('addForumQues/',views.addForumQues,name='addForumQues'),
   path('addForumAns/<int:forum_id>',views.addForumAns,name='addForumAns'),
   path('ques_details/<int:forum_id>',views.ques_details,name='ques_details'),
   path('post_comment/<int:video_id>',views.post_comment,name='post_comment'),
   path('post_reply/<int:parent_id>',views.post_reply,name='post_reply'),
   path('show_reply/<int:parent_id>',views.show_reply,name='show_reply'),
    
]
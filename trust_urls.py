from django.urls import path

from aquene_app.trust_views import Trust_view, Add_tru_child, View_Trust_children, Recieved_amnt, Receive_msg, sponsor_view,\
                                    view_profile, edit_profile

urlpatterns = [
    path('',Trust_view.as_view()),
    # path('v_ch',View_children.as_view())
    path('trust_child',Add_tru_child.as_view()),
    path('vi_trust',View_Trust_children.as_view()),
    path('trust_don_amnt',Recieved_amnt.as_view()),
    path('rcv_msg',Receive_msg.as_view()),
    path('view_sponsor',sponsor_view.as_view()),
    path('view_profile',view_profile.as_view()),
    path('edit_profile',edit_profile.as_view())
]

def urls():
    return urlpatterns, 'trust', 'trust'
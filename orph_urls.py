from django.urls import path


from aquene_app.orph_views import Orph_view, Addchildren_orph, View_Orph_children, Recieved_donation, Rcv_msg,sponsor_view,\
                                  view_profile, edit_profile

urlpatterns = [
    path('',Orph_view.as_view()),
    path('orp_child',Addchildren_orph.as_view()),
    path('vi_orph',View_Orph_children.as_view()),
    path('r_dono',Recieved_donation.as_view()),
    path('rcv_m',Rcv_msg.as_view()),
    path('sponsor_view',sponsor_view.as_view()),
    path('view_profile',view_profile.as_view()),
    path('edit_profile',edit_profile.as_view()),
    # path('add',Add_child.as_view()),
    # path('vi_ch',Child_view.as_view()),
    # path('approve',ApproveView2.as_view()),
    # path('reject',RejectView2.as_view())
]

def urls():
    return urlpatterns, 'orphanage', 'orphanage'

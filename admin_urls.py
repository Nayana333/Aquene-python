
from django.urls import path

from aquene_app.admin_views import Adminview, Off_list, Officerview, ApproveView, RejectView, Don_view, Don_list, \
    Off_orp_view, Off_trust_view, Off_orp_list, Off_trust_list, Firm_view, Trust_donation, orphanage_donation, \
    Feedback_view

urlpatterns = [
    path('',Adminview.as_view()),
    path('of_vi',Officerview.as_view()),
    path('approve', ApproveView.as_view()),
    path('reject', RejectView.as_view()),
    path('of_li',Off_list.as_view()),
    path('do_vi',Don_view.as_view()),
    path('do_li',Don_list.as_view()),
    # path('or_vi',Orp_view.as_view()),
    # path('or_li',Orp_list.as_view()),
    # path('tr_vi',Trust_view.as_view()),
    # path('tr_li',Trust_list.as_view()),
    path('off_or_vi',Off_orp_view.as_view()),
    path('off_tr_vi',Off_trust_view.as_view()),
    path('off_or_li',Off_orp_list.as_view()),
    path('off_tr_li',Off_trust_list.as_view()),
    # path('ap_ch',Child_aprv.as_view()),
    path('fi_vi',Firm_view.as_view()),
    path('trust_donation',Trust_donation.as_view()),
    path('orpha_don',orphanage_donation.as_view()),
    path('Feedback',Feedback_view.as_view())
]


def urls():
    return urlpatterns, 'admin', 'admin'
from django.urls import path

from aquene_app.donors_views import Donors_view, Vi_reg_orp, Vi_reg_trust, Orp_donation, Tru_donation, Sponsor, \
    Sponsor_one, Sponsor_group, Sponsor_orph, Orph_msg, Trust_msg, view_child , Sponsor_trust

urlpatterns = [
    path('',Donors_view.as_view()),
    path('vi_regor',Vi_reg_orp.as_view()),
    path('vi_retr',Vi_reg_trust.as_view()),
    path('or_dono',Orp_donation.as_view()),
    path('tr_dono',Tru_donation.as_view()),
    # path('pay',Payment_trust.as_view()),
    path('spon',Sponsor.as_view()),
    path('spon_one',Sponsor_one.as_view()),
    path('spone_group',Sponsor_group.as_view()),
    path('Sponsor_orph',Sponsor_orph.as_view()),
    path('Sponsor_trust',Sponsor_trust.as_view()),
    path('omsg',Orph_msg.as_view()),
    path('tmsg',Trust_msg.as_view()),
    path('view_child',view_child.as_view()),

]
def urls():
    return urlpatterns, 'donors', 'donors'
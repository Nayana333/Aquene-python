from django.urls import path

from aquene_app.officers_views import OfficersIndexview, Off_orphview, ApproveView, RejectView, Off_trustview, \
    ApproveView1, RejectView1, Addfirm1, Addfirm2, Offiser_view, orphanage_view, view_profile, edit_profile

urlpatterns = [
    path('', OfficersIndexview.as_view()),
    path('oforview',Off_orphview.as_view()),
    path('approve', ApproveView.as_view()),
    path('reject', RejectView.as_view()),
    path('oftrview',Off_trustview.as_view()),
    path('approve1',ApproveView1.as_view()),
    path('reject1',RejectView1.as_view()),
    path('adf1',Addfirm1.as_view()),
    path('adf2',Addfirm2.as_view()),
    path('Offiser_view',Offiser_view.as_view()),
    path('orphanage_view',orphanage_view.as_view()),
    path('view_profile',view_profile.as_view()),
    path('edit_profile',edit_profile.as_view())


]

def urls():
    return urlpatterns, 'officer', 'officer'
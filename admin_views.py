from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.base import View

from aquene_app.models import officer_reg, don_reg, orph_reg, trust_reg, add_firm, trust_don, orph_don, Feedback


class Adminview(TemplateView):
    template_name='admin/admin_index.html'

class Officerview(TemplateView):
    template_name='admin/officers_view.html'

    def get_context_data(self, **kwargs):
        context = super(Officerview, self).get_context_data(**kwargs)

        ofview = officer_reg.objects.filter(user__last_name='0',user__is_staff='0',user__is_active='1')

        context['ofview'] = ofview
        return context


class ApproveView(View):
    def dispatch(self, request, *args, **kwargs):

        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name='1'
        user.save()
        return render(request,'admin/admin_index.html',{'message':" Account Approved"})

class RejectView(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.is_active='0'
        user.save()
        return render(request,'admin/admin_index.html',{'message':"Account Removed"})

class Off_list(TemplateView):
    template_name='admin/officers_list.html'

    def get_context_data(self, **kwargs):
        context = super(Off_list, self).get_context_data(**kwargs)

        oflist = officer_reg.objects.filter(user__last_name='1', user__is_staff='0', user__is_active='1')

        context['oflist'] = oflist
        return context

class Don_view(TemplateView):
    template_name = 'admin/donors_view.html'

    def get_context_data(self, **kwargs):
        context = super(Don_view, self).get_context_data(**kwargs)

        doview = don_reg.objects.filter(user__last_name='0',user__is_staff='0',user__is_active='1')

        context['doview'] = doview
        return context

class Don_list(TemplateView):
    template_name='admin/donors_list.html'

    def get_context_data(self, **kwargs):
        context = super(Don_list, self).get_context_data(**kwargs)

        dolist = don_reg.objects.filter(user__last_name='1', user__is_staff='0', user__is_active='1')

        context['dolist'] = dolist
        return context

class Off_orp_view(TemplateView):
    template_name = 'admin/off_orph_view.html'

    def get_context_data(self, **kwargs):
        context = super(Off_orp_view, self).get_context_data(**kwargs)

        oforview = orph_reg.objects.filter(user__last_name='0',user__is_staff='0',user__is_active='1',officer_status='verified')

        context['oforview'] = oforview
        return context

class Off_trust_view(TemplateView):
    template_name = 'admin/off_tru_view.html'

    def get_context_data(self, **kwargs):
        context = super(Off_trust_view, self).get_context_data(**kwargs)

        oftrview = trust_reg.objects.filter(user__last_name='0',user__is_staff='0',user__is_active='1',officer_status='verified')

        context['oftrview'] = oftrview
        return context

class Off_orp_list(TemplateView):
    template_name = 'admin/off_orph_list.html'

    def get_context_data(self, **kwargs):
        context = super(Off_orp_list, self).get_context_data(**kwargs)

        oforlist = orph_reg.objects.filter(user__last_name='1',user__is_staff='0',user__is_active='1')

        context['oforlist'] = oforlist
        return context

class Off_trust_list(TemplateView):
    template_name = 'admin/off_tru_list.html'

    def get_context_data(self, **kwargs):
        context = super(Off_trust_list, self).get_context_data(**kwargs)

        oftrlist = trust_reg.objects.filter(user__last_name='1',user__is_staff='0',user__is_active='1')

        context['oftrlist'] = oftrlist
        return context


class Trust_donation(TemplateView):
    template_name = 'admin/trust_donation.html'

    def get_context_data(self, **kwargs):
        # user = User.objects.get(id=self.request.user.id)
        context = super(Trust_donation, self).get_context_data(**kwargs)

        tr_ch = trust_don.objects.all()

        context['tr_ch'] = tr_ch
        return context


class orphanage_donation(TemplateView):
    template_name = 'admin/orphanage_don.html'

    def get_context_data(self, **kwargs):
        # user = User.objects.get(id=self.request.user.id)
        context = super(orphanage_donation, self).get_context_data(**kwargs)

        orp_ch1 = orph_don.objects.all()

        context['orp_ch1'] = orp_ch1
        return context

# class Child_aprv(TemplateView):
#     template_name = 'admin/app_orp_child.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(Child_aprv, self).get_context_data(**kwargs)
#
#         app_chld = add_child.objects.filter(status='approved')
#
#         context['app_chld'] = app_chld
#         return context

class Firm_view(TemplateView):
    template_name = 'admin/firm_view.html'

    def get_context_data(self, **kwargs):
        context = super(Firm_view, self).get_context_data(**kwargs)

        ad_firm = add_firm.objects.all()
        # lg=len(add_firm)
        # print(lg)


        context['ad_firm'] = ad_firm
        return context

class Feedback_view(TemplateView):
    template_name='admin/feedback_view.html'

    def get_context_data(self, **kwargs):
        context = super(Feedback_view, self).get_context_data(**kwargs)

        feed = Feedback.objects.all()

        context['feed'] = feed
        return context
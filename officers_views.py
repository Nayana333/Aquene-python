from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.base import View

from aquene_app.models import orph_reg, trust_reg, add_firm, officer_reg


class OfficersIndexview(TemplateView):
    template_name = 'officers/officers_index.html'

class Off_orphview(TemplateView):
    template_name = 'officers/off_orphview.html'

    def get_context_data(self, **kwargs):
        context = super(Off_orphview, self).get_context_data(**kwargs)

        ofor_view = orph_reg.objects.filter(user__last_name='0',user__is_staff='0',user__is_active='1',officer_status='0')

        context['ofor_view'] = ofor_view
        return context

class ApproveView(View):
    def dispatch(self, request, *args, **kwargs):

        id = request.GET['id']
        print(id)

        a=orph_reg.objects.get(id=id)
        print(a)
        a.officer_status='verified'
        a.save()
        return render(request,'officers/officers_index.html',{'message':" Account Approved"})

class RejectView(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        print(id)

        b = orph_reg.objects.get(id=id)
        print(b)
        b.officer_status = 'Notverified'
        b.save()
        return render(request,'officers/officers_index.html',{'message':"Account Removed"})

class Off_trustview(TemplateView):
    template_name = 'officers/off_trustview.html'

    def get_context_data(self, **kwargs):
        context = super(Off_trustview, self).get_context_data(**kwargs)

        oftr_view = trust_reg.objects.filter(user__last_name='0',user__is_staff='0',user__is_active='1',officer_status='0')

        context['oftr_view'] = oftr_view
        return context

class ApproveView1(View):
    def dispatch(self, request, *args, **kwargs):

        id = request.GET['id']
        print(id)

        a=trust_reg.objects.get(id=id)
        print(a)
        a.officer_status='verified'
        a.save()
        return render(request,'officers/officers_index.html',{'message':" Account Approved"})

class RejectView1(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        print(id)

        b = trust_reg.objects.get(id=id)
        print(b)
        b.officer_status = 'Notverified'
        b.save()
        return render(request,'officers/officers_index.html',{'message':"Account Removed"})

class Addfirm1(TemplateView):
    template_name = 'officers/ad_tr_firm.html'

    def post(self,request,*args,**kwargs):
        user = User.objects.get(id=self.request.user.id)

        Firm_id=request.POST['Firm_name']
        firm_address=request.POST['firm_address']
        children_name=request.POST['children_name']
        age = request.POST['age']
        clas = request.POST['clas']
        ad_firm1=add_firm()
        # usertype=UserType.objects.get()
        trust = trust_reg.objects.get(user_id=Firm_id)
        ad_firm1.user=user
        ad_firm1.Firm_name=trust.user.first_name
        ad_firm1.firm_address = firm_address
        ad_firm1.children_name = children_name
        ad_firm1.age = age
        ad_firm1.clas = clas
        ad_firm1.trust_id_id=trust.id
        ad_firm1.save()
        return render(request,'officers/officers_index.html')

    def get_context_data(self, **kwargs):
        context = super(Addfirm1, self).get_context_data(**kwargs)

        tru = trust_reg.objects.filter(user__last_name='1')

        context['tru'] = tru
        return context

class Addfirm2(TemplateView):
    template_name = 'officers/ad_orp_firm.html'

    def post(self,request,*args,**kwargs):
        user = User.objects.get(id=self.request.user.id)
        Firm_id=request.POST['Firm_name']
        firm_address=request.POST['firm_address']
        children_name=request.POST['children_name']
        age = request.POST['age']
        clas = request.POST['clas']

        ad_firm2=add_firm()
        orph = orph_reg.objects.get(user_id=Firm_id)

        ad_firm2.user=user
        ad_firm2.Firm_name=orph.user.first_name
        ad_firm2.firm_address = firm_address
        ad_firm2.children_name = children_name
        ad_firm2.age=age
        ad_firm2.clas=clas
        ad_firm2.orp_id_id=orph.id

        ad_firm2.save()
        return render(request,'officers/officers_index.html')

    def get_context_data(self, **kwargs):
        context = super(Addfirm2, self).get_context_data(**kwargs)

        orp = orph_reg.objects.filter(user__last_name='1')

        context['orp'] = orp
        return context

class Offiser_view(TemplateView):
    template_name = 'officers/trust_view.html'

    def get_context_data(self, **kwargs):
        context = super(Offiser_view, self).get_context_data(**kwargs)

        oftrlist = trust_reg.objects.filter(user__last_name='1',user__is_staff='0',user__is_active='1')

        context['oftrlist'] = oftrlist
        return context

class orphanage_view(TemplateView):
    template_name = 'officers/orphanage_view.html'

    def get_context_data(self, **kwargs):
        context = super(orphanage_view, self).get_context_data(**kwargs)

        oforlist = orph_reg.objects.filter(user__last_name='1',user__is_staff='0',user__is_active='1')

        context['oforlist'] = oforlist
        return context


class view_profile(TemplateView):
    template_name="officers/view_profile.html"

    def get_context_data(self, **kwargs):
        context = super(view_profile,self).get_context_data(**kwargs)

        orph = officer_reg.objects.filter(user_id=self.request.user.id)

        context['orph'] = orph
        return context
    
class edit_profile(TemplateView):
    template_name = 'officers/edit_profile.html'
    def get_context_data(self, **kwargs):
        context = super(edit_profile,self).get_context_data(**kwargs)
        id=self.request.user.id
        pro = officer_reg.objects.get(user_id=id)

        context['pro'] = pro
        return context
    
    def post(self,request,*args,**kwargs):
        id = request.POST['id'] 
        id2 = request.POST['id2']
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        phone = request.POST['phone']
        i = User.objects.get(pk=id)
        u = officer_reg.objects.get(pk=id2)
        i.first_name = name
        i.email = email
        i.save()
        u.address = address
        u.phone = phone
        u.save()
        
        return render(request,'officers/officers_index.html',{'message':"Profile Updated"})
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.base import View
from django.core.files.storage import FileSystemStorage

from aquene_app.models import orph_reg, add_firm, orph_don, message_tb, sponsor


class Orph_view(TemplateView):
    template_name = 'orphanages/orph_index.html'

# class Add_child(TemplateView):
#     template_name = 'orphanages/add_orph_child.html'
#
#     def post(self,request,*args,**kwargs):
#         user = User.objects.get(id=self.request.user.id)
#         name=request.POST['name']
#         age=request.POST['age']
#         clas=request.POST['clas']
#         ad_child=add_child()
#         ad_child.status='pending'
#         ad_child.user=user
#         ad_child.name=name
#         ad_child.age=age
#         ad_child.clas=clas
#         ad_child.save()
#         return render(request,'orphanages/orph_index.html')
#
# class Child_view(TemplateView):
#     template_name = 'orphanages/view_child.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(Child_view, self).get_context_data(**kwargs)
#
#         ch_vi = add_child.objects.filter(status='pending')
#
#         context['ch_vi'] = ch_vi
#         return context
#
# class ApproveView2(View):
#     def dispatch(self, request, *args, **kwargs):
#         id = request.GET['id']
#         app = add_child.objects.get(pk=id)
#         app.status = 'approved'
#         app.save()
#         return render(request, 'orphanages/orph_index.html', {'message': " Account Approved"})
#
#
# class RejectView2(View):
#     def dispatch(self, request, *args, **kwargs):
#         id = request.GET['id']
#         rej = add_child.objects.get(pk=id)
#         rej.status = 'rejected'
#         rej.save()
#         return render(request,'orphanages/orph_index.html',{'message':"Account Removed"})
#
#
class Addchildren_orph(TemplateView):
    template_name = 'orphanages/add_orp_children.html'

    def get_context_data(self, **kwargs):
        user = User.objects.get(id=self.request.user.id)
        context = super(Addchildren_orph, self).get_context_data(**kwargs)

        add_orp = orph_reg.objects.get(user_id=user.id)

        context['username'] = add_orp.user.username
        return context

    def post(self,request,*args,**kwargs):
        com= orph_reg.objects.get(user_id=self.request.user.id)
        Firm_name = request.POST['Firm_name']
        firm_address = request.POST['firm_address']
        children_name = request.POST['children_name']
        age = request.POST['age']
        clas = request.POST['clas']
        description = request.POST['description']
        image = request.FILES['image']
        fii=FileSystemStorage()
        filesss=fii.save(image.name,image)

        user=User.objects.get(id=self.request.user.id)
        ad_orp = add_firm()
        ad_orp.orp_id = com.id
        ad_orp.Firm_name = Firm_name
        ad_orp.firm_address = firm_address
        ad_orp.children_name = children_name
        ad_orp.description = description
        ad_orp.image = filesss
        ad_orp.age = age
        ad_orp.clas = clas
        ad_orp.user = user
        ad_orp.save()
        return render(request, 'orphanages/orph_index.html')

class View_Orph_children(TemplateView):
    template_name = 'orphanages/view_add_orph.html'

    def get_context_data(self, **kwargs):
        com = orph_reg.objects.get(user_id=self.request.user.id)
        context = super(View_Orph_children, self).get_context_data(**kwargs)

        orp_ch = add_firm.objects.filter(orp_id=com.id)

        context['orp_ch'] = orp_ch
        return context

class Recieved_donation(TemplateView):
    template_name = 'orphanages/recieve_don.html'

    def get_context_data(self, **kwargs):
        # user = User.objects.get(id=self.request.user.id)
        context = super(Recieved_donation, self).get_context_data(**kwargs)
        receive=orph_reg.objects.get(user_id=self.request.user.id)
        orp_ch1 = orph_don.objects.filter(orph_id=receive.id)

        context['orp_ch1'] = orp_ch1
        return context

class Rcv_msg(TemplateView):
    template_name = 'orphanages/rcv_msg.html'

    def get_context_data(self, **kwargs):
        user = User.objects.get(id=self.request.user.id)
        orphh = orph_reg.objects.get(user_id=user.id)
        context = super(Rcv_msg, self).get_context_data(**kwargs)

        rcv_1 = message_tb.objects.filter(orphange_id=orphh)
        context['rcv_1'] = rcv_1
        return context
    
class sponsor_view(TemplateView):
    template_name = 'orphanages/view_sponser.html'
    def get_context_data(self, **kwargs):
        
        context = super(sponsor_view, self).get_context_data(**kwargs)
        sh = sponsor.objects.filter(firm__user_id=self.request.user.id)
        context['sh'] = sh
        return context


class view_profile(TemplateView):
    template_name="orphanages/view_profile.html"

    def get_context_data(self, **kwargs):
        context = super(view_profile,self).get_context_data(**kwargs)

        orph = orph_reg.objects.filter(user_id=self.request.user.id)

        context['orph'] = orph
        return context
    
class edit_profile(TemplateView):
    template_name = 'orphanages/edit_profile.html'
    def get_context_data(self, **kwargs):
        context = super(edit_profile,self).get_context_data(**kwargs)
        id=self.request.user.id
        pro = orph_reg.objects.get(user_id=id)

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
        u = orph_reg.objects.get(pk=id2)
        i.first_name = name
        i.email = email
        i.save()
        u.address = address
        u.phone = phone
        u.save()
        
        return render(request,'orphanages/orph_index.html',{'message':"Profile Updated"})
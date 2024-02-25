from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage

from aquene_app.models import add_firm, trust_reg, trust_don, message_tb,sponsor


class Trust_view(TemplateView):
    template_name = 'trust/trust_index.html'

# class View_children(TemplateView):
#     template_name = 'trust/view_children.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(View_children,self).get_context_data(**kwargs)
#         usid=self.request.user.id
#         ad = add_firm.objects.filter(id=usid)
#
#         context['ad'] = ad
#         return context

class Add_tru_child(TemplateView):
    template_name = 'trust/add_tru_children.html'

    def get_context_data(self, **kwargs):
        user = User.objects.get(id=self.request.user.id)
        context = super(Add_tru_child, self).get_context_data(**kwargs)

        add_orp = trust_reg.objects.get(user_id=user.id)

        context['username'] = add_orp.user.username
        return context

    def post(self,request,*args,**kwargs):
        com= trust_reg.objects.get(user_id=self.request.user.id)

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
        ad_orp.trust_id = com.id
        ad_orp.Firm_name = Firm_name
        ad_orp.firm_address = firm_address
        ad_orp.children_name = children_name
        ad_orp.description = description
        ad_orp.image = filesss
        ad_orp.age = age
        ad_orp.clas = clas
        ad_orp.user = user
        ad_orp.save()
        return render(request, 'trust/trust_index.html')

class View_Trust_children(TemplateView):
    template_name = 'trust/view_add_tru.html'

    def get_context_data(self, **kwargs):
        com = trust_reg.objects.get(user_id=self.request.user.id)
        context = super(View_Trust_children, self).get_context_data(**kwargs)

        tr_ch = add_firm.objects.filter(trust_id=com.id)

        context['tr_ch'] = tr_ch
        return context

class Recieved_amnt(TemplateView):
    template_name = 'trust/recieve_donation.html'

    def get_context_data(self, **kwargs):
        # user = User.objects.get(id=self.request.user.id)
        context = super(Recieved_amnt, self).get_context_data(**kwargs)
        receive=trust_reg.objects.get(user_id=self.request.user.id)

        tr_ch = trust_don.objects.filter(trust_id_id=receive.id)

        context['tr_ch'] = tr_ch
        return context

class Receive_msg(TemplateView):
    template_name = 'trust/recieve_msg.html'

    def get_context_data(self, **kwargs):
        user = User.objects.get(id=self.request.user.id)
        trust = trust_reg.objects.get(user_id=user.id)
        context = super(Receive_msg, self).get_context_data(**kwargs)

        rcv = message_tb.objects.filter(trust_id=trust)
        context['rcv'] = rcv
        return context





class sponsor_view(TemplateView):
    template_name = 'trust/view_sponser.html'
    def get_context_data(self, **kwargs):
        
        context = super(sponsor_view, self).get_context_data(**kwargs)
        sh = sponsor.objects.filter(firm__user_id=self.request.user.id)
        context['sh'] = sh
        return context



class view_profile(TemplateView):
    template_name="trust/view_profile.html"

    def get_context_data(self, **kwargs):
        context = super(view_profile,self).get_context_data(**kwargs)

        trust = trust_reg.objects.filter(user_id=self.request.user.id)

        context['trust'] = trust
        return context
    
class edit_profile(TemplateView):
    template_name = 'trust/edit_profile.html'
    def get_context_data(self, **kwargs):
        context = super(edit_profile,self).get_context_data(**kwargs)
        id=self.request.user.id
        pro = trust_reg.objects.get(user_id=id)

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
        u = trust_reg.objects.get(pk=id2)
        i.first_name = name
        i.email = email
        i.save()
        u.address = address
        u.phone = phone
        u.save()
        
        return render(request,'trust/trust_index.html',{'message':"Profile Updated"})
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from aquene_app.models import orph_reg, trust_reg, orph_don, trust_don, add_firm, sponsor, message_tb, don_reg


class Donors_view(TemplateView):
    template_name = 'donors/donors_index.html'

class Vi_reg_orp(TemplateView):
    template_name = 'donors/vi_reg_orp.html'

    def get_context_data(self, **kwargs):
        context = super(Vi_reg_orp, self).get_context_data(**kwargs)

        or_reg = orph_reg.objects.filter(user__last_name='1',user__is_staff='0',user__is_active='1')

        context['or_reg'] = or_reg
        return context

class Vi_reg_trust(TemplateView):
    template_name = 'donors/vi_reg_trust.html'

    def get_context_data(self, **kwargs):
        context = super(Vi_reg_trust, self).get_context_data(**kwargs)

        tr_reg = trust_reg.objects.filter(user__last_name='1',user__is_staff='0',user__is_active='1')

        context['tr_reg'] = tr_reg
        return context

class Orp_donation(TemplateView):
    template_name = 'donors/orph_dono.html'
    def post(self,request,*args,**kwargs):
        user = User.objects.get(id=self.request.user.id)

        name=request.POST['name']
        address=request.POST['address']
        email=request.POST['email']
        phone=request.POST['phone']
        # payment_method=request.POST['payment_method']
        date=request.POST['date']
        dono =request.POST['dono']
        amount=request.POST['amount']
        id_orph=request.POST['select_orph']
        o_don=orph_don()
        o_don.user=user
        o_don.name=name
        o_don.email=email
        o_don.address=address
        o_don.phone=phone
        o_don.date=date
        if dono == 'study':
            o_don.study = dono
        else:
            o_don.others=dono
        # o_don.payment_method=payment_method
        o_don.amount=amount
        o_don.orph_id=id_orph

        o_don.save()
        return render(request,'donors/donors_index.html',{'donation': "donate successfully"})
    def get_context_data(self, **kwargs):
        context = super(Orp_donation, self).get_context_data(**kwargs)

        orp1 = orph_reg.objects.filter(user__last_name='1')
        context['orp1']=orp1
        return context

class Tru_donation(TemplateView):
    template_name = 'donors/trust_dono.html'

    def post(self,request,*args,**kwargs):
        user=User.objects.get(id=self.request.user.id)
        name=request.POST['name']
        address=request.POST['address']
        email=request.POST['email']
        phone=request.POST['phone']
        # payment_method=request.POST['payment_method']
        date=request.POST['date']
        amount=request.POST['amount']
        id_trust=request.POST['select_trust']
        t_don=trust_don()
        t_don.user=user
        t_don.name=name
        t_don.email=email
        t_don.address=address
        t_don.phone=phone
        # t_don.payment_method=payment_method
        t_don.date=date
        t_don.amount=amount
        t_don.trust_id_id=id_trust
        t_don.save()
        return render(request,'donors/donors_index.html',{'donation': "donate successfully"})


    def get_context_data(self, **kwargs):
        context = super(Tru_donation, self).get_context_data(**kwargs)

        tru1 = trust_reg.objects.filter(user__last_name='1')
        context['tru1'] = tru1
        return context


# class Payment_trust(TemplateView):
#     template_name = 'donors/payment_trust.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(Payment_trust, self).get_context_data(**kwargs)
#
#         am_pay = trust_don.objects.filter(user__last_name='1')
#         context['am_pay'] = am_pay
#         return context


class Sponsor(TemplateView):
    template_name = 'donors/sponsor.html'

    def post(self, request, *args, **kwargs):
        name = request.POST['sponsor']
        print(name)
        if name == 'one':
            One=add_firm.objects.all()
            return render(request,'donors/registered_child.html', {'result':One})
        elif name == 'group':
            Group=add_firm.objects.all()
            return  render(request,'donors/group_child.html', {'result1':Group})
        elif name == 'orph':
            Orph = orph_reg.objects.all()
            return render(request,'donors/orph_spons.html', {'result2':Orph})
        elif name == 'trust':
            Trust = trust_reg.objects.all()
            return render(request,'donors/trust_spons.html', {'result3':Trust})
        else:
            return redirect(request,'donors/sponsor.html')

class Sponsor_one(TemplateView):
    template_name = 'donors/registered_child.html'

    def post(self, request, *args, **kwargs):
        user = don_reg.objects.get(user_id=self.request.user.id)
        name = request.POST['select_child']
        spon = sponsor()
        spon.firm_id = name
        spon.user_id=user.id
        spon.status='sponsor one child'
        spon.save()
        return render(request,'donors/donors_index.html',{'message': "succesfully sponsored"})

class Sponsor_group(TemplateView):
    template_name = 'donors/group_child.html'

    def post(self, request, *args, **kwargs):
        user=don_reg.objects.get(user_id=self.request.user.id)
        name = request.POST.getlist('checks[]')

        spon = sponsor()
        spon.select_child = name
        spon.user_id=user.id
        spon.status='sponsor Group of children'
        spon.save()
        return render(request,'donors/donors_index.html',{'message': "succesfully sponsored"})

class Sponsor_orph(TemplateView):
    template_name = 'donors/orph_spons.html'

    def post(self, request, *args, **kwargs):
        user = don_reg.objects.get(user_id=self.request.user.id)
        name = request.POST['select_child']
        spon = sponsor()
        spon.select_child = name
        spon.user_id=user.id
        spon.status='sponsor orphanage'
        spon.save()
        return render(request,'donors/donors_index.html',{'message': "succesfully sponsored"})

class Sponsor_trust(TemplateView):
    template_name = 'donors/trust_spons.html'

    def post(self, request, *args, **kwargs):
        user = don_reg.objects.get(user_id=self.request.user.id)
        name = request.POST['select_child']
        spon = sponsor()
        spon.select_child = name
        spon.user_id=user.id
        spon.status='sponsor trust'
        spon.save()
        return render(request,'donors/donors_index.html',{'message': "succesfully sponsored"})

class Orph_msg(TemplateView):
    template_name = 'donors/orp_msg.html'

    def get_context_data(self, **kwargs):
        context = super(Orph_msg, self).get_context_data(**kwargs)

        orp2 = orph_reg.objects.filter(user__last_name='1')
        context['orp2']=orp2
        return context

    def post(self, request, *args, **kwargs):
        user = User.objects.get(id=self.request.user.id)
        id_orp = request.POST['orphange']
        message = request.POST['message']
        msg = message_tb()
        msg.user_id=user.id
        msg.orphange_id = id_orp
        msg.message=message
        msg.save()
        return render(request,'donors/donors_index.html')

class Trust_msg(TemplateView):
    template_name = 'donors/trust_msg.html'

    def get_context_data(self, **kwargs):
        context = super(Trust_msg, self).get_context_data(**kwargs)

        trust1 = trust_reg.objects.filter(user__last_name='1')
        context['trust1']=trust1
        return context

    def post(self, request, *args, **kwargs):
        user = User.objects.get(id=self.request.user.id)
        id_trust = request.POST['trust']
        message = request.POST['message']
        msg = message_tb()
        msg.user_id=user.id
        msg.trust_id = id_trust
        msg.message=message
        msg.save()
        return render(request,'donors/donors_index.html')


class view_child(TemplateView):
    template_name = 'donors/view_child.html'
    def get_context_data(self, **kwargs):
        context = super(view_child, self).get_context_data(**kwargs)
        vch = add_firm.objects.all()

        context['vch'] = vch
        return context


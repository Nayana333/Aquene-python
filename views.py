from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage

# Create your views here.
from django.views.generic import TemplateView

from aquene_app.models import UserType, don_reg, orph_reg, trust_reg, officer_reg, Feedback


class Indexview(TemplateView):
    template_name = 'index.html'

class Registration(TemplateView):
    template_name = 'registration.html'
    def post(self,request,*args,**kwargs):
        select_reg=request.POST['select_reg']
        name=request.POST['name']
        address=request.POST['address']
        email=request.POST['email']
        phone = request.POST['phone']
        district = request.POST['district']
        place = request.POST['place']
        image = request.FILES['image']
        fii=FileSystemStorage()
        filesss=fii.save(image.name,image)
        proof = request.FILES['proof']
        fii=FileSystemStorage()
        filesss1=fii.save(proof.name,proof)
        username = request.POST['username']
        password = request.POST['password']
        if select_reg == 'trust':
            user=User.objects._create_user(username=username,password=password,email=email,first_name=select_reg,is_staff='0',last_name='0')
            user.save()
            trust=trust_reg()
            trust.name=name
            trust.user=user
            trust.address=address
            trust.district=district
            trust.place=place
            trust.image=filesss
            trust.proof=filesss1
            trust.phone=phone
            trust.officer_status = "0"
            # trust.admin_status= "0"
            trust.save()
            usertype = UserType()
            usertype.user = user
            usertype.type = "trust"
            usertype.save()
            return render(request,"index.html")
        elif select_reg == 'donor':
            user = User.objects._create_user(username=username, password=password, email=email, first_name=select_reg,is_staff='0', last_name='0')
            user.save()
            donor = don_reg()
            donor.user = user
            donor.name=name
            donor.address = address
            donor.district=district
            donor.place=place
            donor.image=filesss
            donor.proof=filesss1
            donor.phone = phone
            donor.save()
            usertype = UserType()
            usertype.user = user
            usertype.type = "donors"
            usertype.save()
            return render(request, "index.html")
        elif select_reg == 'orphanage':
            user = User.objects._create_user(username=username, password=password, email=email, first_name=select_reg,is_staff='0', last_name='0')
            user.save()
            orph = orph_reg()
            orph.name=name
            orph.user = user
            orph.address = address
            orph.district = district
            orph.place = place
            orph.image = filesss
            orph.proof = filesss1
            orph.phone = phone
            orph.officer_status = "0"
            # orph.admin_status = "0"
            orph.save()
            usertype = UserType()
            usertype.user = user
            usertype.type = "orphanage"
            usertype.save()
            return render(request, "index.html")
        else:
            user = User.objects._create_user(username=username, password=password, email=email, first_name=select_reg,is_staff='0', last_name='0')
            user.save()
            regs = officer_reg()
            regs.name=name
            regs.user = user
            regs.address=address
            regs.district=district
            regs.place=place
            regs.image=filesss
            regs.proof=filesss1
            regs.phone = phone
            regs.save()
            usertype = UserType()
            usertype.user = user
            usertype.type = "officer"
            usertype.save()
            return render(request, "index.html")


class Login(TemplateView):
    template_name='login.html'

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        det = User.objects.get(id=1)
        det.last_name = 1
        det.save()

        if user is not None:

            login(request, user)
            if user.last_name == '1':

                if user.is_superuser:
                    return redirect('/admin')
                elif UserType.objects.get(user_id=user.id).type == "officer":
                    return redirect('/officer')
                elif UserType.objects.get(user_id=user.id).type == "donors":
                    return redirect('/donors')
                elif UserType.objects.get(user_id=user.id).type == "trust":
                    return redirect('/trust')
                elif UserType.objects.get(user_id=user.id).type == "orphanage":
                    return redirect('/orphanage')
                else:
                    return redirect('/guest')

            else:

                return render(request, 'login.html', {'message': " User Account Not Authenticated"})
        else:

            return render(request, 'login.html', {'message': "Invalid Username or Password"})
1
class feedback(TemplateView):
    template_name = 'feedback.html'

    def post(self, request, *args, **kwargs):
        name= request.POST['name']
        email=request.POST['email']
        feedback=request.POST['feedback']

        com = Feedback()
        com.name=name
        com.email=email
        com.feedback=feedback
        com.save()
        return render(request, 'index.html', {'message': "feedback added"})
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserType(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    type = models.CharField(max_length=50)

class officer_reg(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100, null=True)
    district = models.CharField(max_length=20, null=True)
    place = models.CharField(max_length=20, null=True)
    image = models.ImageField( null=True)
    address=models.CharField(max_length=100,null=True)
    phone = models.CharField(max_length=20, null=True)
    proof = models.ImageField( null=True)

class don_reg(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    phone=models.CharField(max_length=20,null=True)
    district = models.CharField(max_length=20, null=True)
    place = models.CharField(max_length=20, null=True)
    image = models.ImageField( null=True)
    proof = models.ImageField( null=True)


class orph_reg(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    district = models.CharField(max_length=20, null=True)
    place = models.CharField(max_length=20, null=True)
    image = models.ImageField( null=True)
    phone=models.CharField(max_length=20,null=True)
    officer_status = models.CharField(max_length=20, null=True)
    # status= models.CharField(max_length=20, null=True)
    proof = models.ImageField( null=True)


class trust_reg(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    phone=models.CharField(max_length=20,null=True)
    officer_status = models.CharField(max_length=20, null=True)
    district = models.CharField(max_length=20, null=True)
    place = models.CharField(max_length=20, null=True)
    image = models.ImageField( null=True)
    # admin_status=models.CharField(max_length=20,null=True)
    proof = models.ImageField( null=True)



class orph_don(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=20, null=True)
    date = models.DateField(null=True)
    study = models.CharField(max_length=20,null=True)
    others = models.CharField(max_length=20,null=True)
    payment_method = models.CharField(max_length=20,null=True)
    amount = models.CharField(max_length=20,null=True)
    select_orph = models.CharField(max_length=20,null=True)
    orph=models.ForeignKey(orph_reg, on_delete=models.CASCADE, null=True)

class trust_don(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name =models.CharField(max_length=20, null=True)
    email =models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=20, null=True)
    date = models.DateField(null=True)
    payment_method = models.CharField(max_length=20,null=True)
    amount = models.CharField(max_length=20,null=True)
    # select_trust = models.CharField(max_length=20,null=True)
    trust_id=models.ForeignKey(trust_reg, on_delete=models.CASCADE, null=True)


# class add_child(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
#     name = models.CharField(max_length=20, null=True)
#     age = models.CharField(max_length=100, null=True)
#     clas = models.CharField(max_length=100, null=True)
#     status= models.CharField(max_length=20,null=True)

class add_firm(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    Firm_name = models.CharField(max_length=20, null=True)
    firm_address = models.CharField(max_length=100, null=True)
    children_name = models.CharField(max_length=100, null=True)
    age = models.CharField(max_length=20, null=True)
    clas = models.CharField(max_length=100, null=True)
    age = models.CharField(max_length=20, null=True)
    description = models.CharField(max_length=200, null=True)
    trust = models.ForeignKey(trust_reg, on_delete=models.CASCADE, null=True)
    image = models.ImageField( null=True)
    orp = models.ForeignKey(orph_reg, on_delete=models.CASCADE, null=True)

class sponsor(models.Model):
    user = models.ForeignKey(don_reg, on_delete=models.CASCADE, null=True)
    select_child = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=50, null=True)
    firm=models.ForeignKey(add_firm, on_delete=models.CASCADE, null=True)


class message_tb(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    orphange = models.ForeignKey(orph_reg, on_delete=models.CASCADE, null=True)
    trust = models.ForeignKey(trust_reg, on_delete=models.CASCADE, null=True)
    message = models.CharField(max_length=50, null=True)

class Feedback(models.Model):
    name=models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=100, null=True)
    feedback=models.CharField(max_length=100,null=True)



















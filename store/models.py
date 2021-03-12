from django.db import models
from django.contrib.auth.models import User

# Pysical Product-------------------------------------------------------------------------------------------------------

class Customer(models.Model):
    user                          = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name                          = models.CharField(max_length=200, null=True)
    email                         = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name                          = models.CharField(max_length=150)
    price                         = models.FloatField(max_length=150)
    digital                       = models.BooleanField(default=False, null=True, blank=False)
    #image

    def __str__(self):
        return self.name


class Order(models.Model):
    customer                      = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.SET_NULL)
    date_ordered                  = models.DateTimeField(auto_now_add=True)
    complete                      = models.BooleanField(default=False)
    transaction_id                = models.CharField(max_length=150, null=True)

    def __str__(self):
        return str(self.customer) + ' | ' + str(self.transaction_id)


class OrderItem(models.Model):
    product                       = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    order                         = models.ForeignKey(Order, null=True, on_delete=models.SET_NULL)
    quantity                      = models.IntegerField(default=0, null=True, blank=True)
    date_added                    = models.DateTimeField(auto_now_add=True)


class ShippingAddress(models.Model):
    customer                      = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    order                         = models.ForeignKey(Order, null=True, on_delete=models.SET_NULL)
    address                       = models.CharField(max_length=150, null=False)
    city                          = models.CharField(max_length=150, null=False)
    zipcode                       = models.CharField(max_length=150, null=False)
    date_added                    = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.customer) + ' | ' + str(self.address)






#Order: customer can have multiple orders
#Curriculum consists of many tutorials


# one product goes into order item
# orderitmes will be the items in the cart
#(if physical product, can have multiple quantities but we are digital no quantity needed)

#why seperate? so that curriculum have multiple tutorials?, if I set product into cart, one cart can have only one item.

#orderitem: items in the cart


#OrderItem is connected to Order(curriculum) which is connected to customer.
#Order item model will be connected to the customer with a one to many relationship
from django.db import models

# Create your models here.
# Order (customer, items, is_delivered)
# OrderItem (order, product, quantity)
# Customer (name)
# Product (name, sku, price)

class Order(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    is_delivered = models.BooleanField(default=False)
    
    def __str__(self):
        return "Order[id=%s, customer=%s, is_delivered=%s]" % (self.id, self.customer, self.is_delivered)
    
    
class OrderItem(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    
    def __str__(self):
        return "OrderItem[id=%s, order=%s, product=%s, quantity=%s]" % (self.id, self.order, self.product, self.quantity)
    
    
class Customer(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return "Customer[id=%s, name=%s]" % (self.id, self.name)
    
class Product(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    sku = models.CharField(max_length=200, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    
    def __str__(self):
        return "Product[id=%s, name=%s, sku=%s, price=%s]" % (self.id, self.name, self.sku, self.price)

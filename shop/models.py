from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    objects = models.Manager()
    category = models.CharField(max_length=50, default="")
    sub_category = models.CharField(max_length=50, default="")
    price=models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to = 'shop/images', default="")

    def __str__(self):
        return self.product_name
        

class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    objects = models.Manager()
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    query =  models.CharField(max_length=500)

    def __str__(self):
        return self.name
    

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)    
    name = models.CharField(max_length=100)
    objects = models.Manager()
    items_json = models.CharField(max_length=5000)
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    city =  models.CharField(max_length=100)
    state =  models.CharField(max_length=100)
    zip_code =  models.CharField(max_length=50)

    def __str__(self):
        return self.name

class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    objects = models.Manager()
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Update for order id : " + str(self.order_id) + " ---> " + self.update_desc
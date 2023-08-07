from django.db import models
#from django.contrib.gis.db import models as gis_models

class AboutUs(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField(null=True)
    company = models.CharField(max_length=100, null=True)
    platforms = models.CharField(max_length=200, null=True)

class BillingInformation(models.Model):
    user = models.OneToOneField('UserTable', primary_key=True, on_delete=models.CASCADE)
    country = models.CharField(max_length=255, null=True)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    company_name = models.CharField(max_length=255, null=True)
    street_address = models.CharField(max_length=255, null=True)
    apartment = models.CharField(max_length=255, null=True)
    town = models.CharField(max_length=255, null=True)
    state = models.CharField(max_length=255, null=True)
    postcode = models.CharField(max_length=255, null=True)
    email_address = models.CharField(max_length=255, null=True)
    phone_number = models.CharField(max_length=255, null=True)

class CheckoutProducts(models.Model):
    user = models.ForeignKey('UserTable', null=True, on_delete=models.CASCADE)
    product_id = models.IntegerField(null=True)
    product_name = models.CharField(max_length=255, null=True)
    quantity = models.IntegerField(null=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    status = models.CharField(max_length=50, null=True)

class GoteraCheckoutProducts(models.Model):
    user = models.ForeignKey('UserTable', null=True, on_delete=models.CASCADE)
    product_id = models.IntegerField(null=True)
    product_name = models.CharField(max_length=255, null=True)
    quantity = models.IntegerField(null=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    status = models.CharField(max_length=50, null=True)

class GoteraProductTable(models.Model):
    product_id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=255, null=True)
    product_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    product_image_url = models.CharField(max_length=255, null=True)
    quantity = models.IntegerField(null=True)
    product_description = models.CharField(max_length=1000, null=True)
    data_sheet = models.CharField(max_length=1000, null=True)
    more_info = models.CharField(max_length=1000, null=True)
    category = models.CharField(max_length=50, null=True)

class GoteraSubscriberTable(models.Model):
    id = models.IntegerField(primary_key=True)
    fullname = models.CharField(max_length=30, null=True)
    phonenumber = models.CharField(max_length=15, null=True)
  #  location = gis_models.PointField(null=True)
    preferedpayment = models.CharField(max_length=40, null=True)
    username = models.CharField(max_length=20, null=True)
    password = models.CharField(max_length=30, null=True)
    profilepicture = models.BinaryField(null=True)

class GoteraUserBoughtProduct(models.Model):
    user = models.ForeignKey('UserTable', on_delete=models.CASCADE)
    bought_product = models.ForeignKey('ProductTable', on_delete=models.CASCADE)
    prod_quantity = models.IntegerField()

class GoteraUserCartedProduct(models.Model):
    user = models.ForeignKey('UserTable', on_delete=models.CASCADE)
    carted_product = models.ForeignKey('ProductTable', on_delete=models.CASCADE)

class UserBoughtProduct(models.Model):
    user = models.ForeignKey('UserTable', on_delete=models.CASCADE)
    bought_product = models.ForeignKey('ProductTable', on_delete=models.CASCADE)
    prod_quantity = models.IntegerField()

class UserCartedProduct(models.Model):
    user = models.ForeignKey('UserTable', on_delete=models.CASCADE)
    carted_product = models.ForeignKey('ProductTable', on_delete=models.CASCADE)

class UserTable(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, null=True)
    email = models.CharField(max_length=30, null=True)
    password = models.CharField(max_length=50, null=True)
    profile_picture = models.BinaryField(null=True)
    date_of_birth = models.DateField(null=True)
    country = models.CharField(max_length=50, null=True)
    username = models.CharField(max_length=50, null=True)

class ProductTable(models.Model):
    product_id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=100, null=True)
    product_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    product_image_url = models.ImageField(upload_to='products/', null=True)
    quantity = models.IntegerField(null=True)
    product_description = models.CharField(max_length=255)
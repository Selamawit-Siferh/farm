from rest_framework import serializers
from .models import *
class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'

class BillingInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillingInformation
        fields = '__all__'

class CheckoutProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckoutProducts
        fields = '__all__'

class GoteraCheckoutProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoteraCheckoutProducts
        fields = '__all__'

class GoteraProductTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoteraProductTable
        fields = '__all__'

class GoteraSubscriberTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoteraSubscriberTable
        fields = '__all__'

class GoteraUserBoughtProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoteraUserBoughtProduct
        fields = '__all__'

class GoteraUserCartedProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoteraUserCartedProduct
        fields = '__all__'

class UserBoughtProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBoughtProduct
        fields = '__all__'

class UserCartedProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCartedProduct
        fields = '__all__'

class UserTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTable
        fields = ['name','email','password',]

class ProductTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductTable
        fields = '__all__'
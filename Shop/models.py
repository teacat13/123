from django.db import models

class User(models.Model):
    SEX = [
        ('1', 'men'),
        ('0', 'women'),
        (None, "Unknown")
    ]
    email = models.EmailField(primary_key = True)
    first_name = models.CharField(max_length =50)
    last_name = models.CharField(max_length =50)
    phone_number = models.CharField(blank=True, max_length=50)
    city = models.CharField(editable=False, max_length =50)
    age = models.CharField(default=18, max_length=50)
    sex = models.CharField(choices=SEX, max_length=50, blank=True)

    def __str__(self):
        return f"{self.first_name.title()} {self.last_name.title()}"

class Product(models.Model):
    TYPE_PRODUCT = [
        ( '1', 'fruit'),
        ( '0', 'vegetables'),
        (None, "Unknown")
    ]
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length =70, unique = True)
    price = models.FloatField(blank=True)
    discount = models.BooleanField(default=False)
    price_discount = models.FloatField(blank=True)
    type = models.CharField(choices=TYPE_PRODUCT, max_length=50, blank=True)

    def __str__(self):
        return f"{self.name.title()}"

class Cart(models.Model):
    user = models.ForeignKey('User',on_delete=models.CASCADE )
    product = models.ForeignKey('Product',on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user} {self.product}"
    class Meta:
        unique_together = ('user', 'product')


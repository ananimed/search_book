from django.db.models import Model, CharField, DecimalField, ImageField


class Book(Model):
    name = CharField(unique=True, max_length=100)
    price = DecimalField(max_digits=10, decimal_places=2)
    image = ImageField(upload_to='books/')


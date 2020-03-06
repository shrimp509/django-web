from django.db import models
from django.utils import timezone
import os


def get_image_path(instance, filename):
    return os.path.join('uploads', filename)


class Product(models.Model):
    # basic info
    name = models.CharField(max_length=100, blank=False)
    price = models.DecimalField(blank=False, max_digits=65, decimal_places=0)
    img = models.ImageField(upload_to=get_image_path, default=get_image_path(instance=0, filename='product-1.jpg'))

    # discount
    on_sale = models.BooleanField(blank=True, null=True)
    tag = models.CharField(max_length=20, blank=True, null=True)
    percent_off = models.DecimalField(blank=True, null=True, max_digits=30, decimal_places=1)
    sale_price = models.DecimalField(blank=True, null=True, max_digits=30, decimal_places=0)

    # for analysis
    bought_counter = models.DecimalField(default=0, max_digits=30, decimal_places=0)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now
        self.save()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'product'

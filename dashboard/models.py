from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.

def validate_phone(value):
    if type(value) != int:
        raise ValidationError("شماره تلفن باید عددی باشد")


class Customer(models.Model):
    full_name = models.CharField(max_length=50, verbose_name="نام و نام خانوادگی", default="محمدرضا قاری")
    address = models.TextField(verbose_name="آدرس", max_length=255)

    phone_number = models.CharField(verbose_name="شماره تلفن", blank=True, default=9120001122
                                    , max_length=11)
    email = models.EmailField(default="reza.ghari@yahoo.com", null=True, blank=True, verbose_name="ایمیل")
    file = models.FileField(null=True, blank=True, verbose_name="آپلود مدارک",
                            upload_to='uploads/%Y/%m/%d/', help_text="میتوانید چیزی آپلود نکنید")
    website = "وبسایت"
    instagram = "اینستاگرام"
    people = "معرف"
    twitter = "توییتر"
    sms = "اسمس"
    off_add = "تبلیغات محیطی"
    on_add = "تبلیغات آنلاین"
    LEADS = [
        ("Website", website),
        ("Instagram", instagram),
        ("People", people),
        ("Twitter", twitter),
        ("SMS", sms),
        ("Off Add", off_add),
        ("On Add", on_add)
    ]
    lead = models.CharField(choices=LEADS, default="وبسایت", max_length=9,
                            verbose_name="نحوه آشنایی با شرکت")
    date = models.DateField(verbose_name="تاریخ اولین خرید", default="2020-02-02")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name= "مشتری"
        verbose_name_plural = "مشتریان"

class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name="نام محصول", default="دوربین مداربسته")
    code = models.CharField(max_length=5, verbose_name="کد محصول", default=10001)
    price = models.IntegerField(verbose_name="قیمت", max_length=10, help_text="به تومان", default=20000000)
    quantity = models.IntegerField(verbose_name="تعداد موجود", max_length=4, default=1)

    def __str__(self):
        return f"{self.code}-{self.name}"

    class Meta:
        verbose_name= "محصول"
        verbose_name_plural = "محصولات"

class Order2(models.Model):
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="نوع محصول",
                                     related_name="+")
    # unit_price = Product.objects.filter(name=product_name)[0].price
    order_quantity = models.IntegerField(max_length=4, verbose_name="تعداد", default=1)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name="نام مشتری")
    date = models.DateField(verbose_name="تاریخ ثبت", default="2020-02-02")
    # total_price = unit_price * order_quantity
    total_price = models.IntegerField(max_length=12, help_text="به تومان", verbose_name="قابل پرداخت")

    def __str__(self):
        return f"{self.customer}: {self.total_price}"

    class Meta:
        verbose_name= "سفارش"
        verbose_name_plural = "سفارشات"
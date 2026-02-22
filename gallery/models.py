from django.db import models

class Category(models.Model):
    name = models.CharField("Adı", max_length=100)
    slug = models.SlugField("Kısa ad (slug)", unique=True)

    class Meta:
        verbose_name = "Kategori"
        verbose_name_plural = "Kategoriler"

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name="Kategori", related_name='products', on_delete=models.CASCADE)
    title = models.CharField("Başlık", max_length=200)
    description = models.TextField("Açıklama", blank=True)
    price = models.DecimalField("Fiyat", max_digits=10, decimal_places=2)
    created_at = models.DateTimeField("Eklenme zamanı", auto_now_add=True)

    class Meta:
        verbose_name = "Ürün"
        verbose_name_plural = "Ürünler"

    def __str__(self):
        return self.title

class ProductImage(models.Model):
    product = models.ForeignKey(Product, verbose_name="Ürün", related_name='images', on_delete=models.CASCADE)
    image = models.ImageField("Görsel", upload_to='products/')

    class Meta:
        verbose_name = "Ürün görseli"
        verbose_name_plural = "Ürün görselleri"

    def __str__(self):
        return f"{self.product.title} görseli"

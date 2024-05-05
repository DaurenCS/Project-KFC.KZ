from django.core.validators import FileExtensionValidator
from django.db import models


def content_data_path(instance, filename):
    extension = filename.split(".")[-1]
    return f"content/{instance.pk}-{instance.__class__.__name__}-photo.{extension}"


class Advertisement(models.Model):
    url = models.URLField(verbose_name="ad url")
    banner = models.ImageField(
        verbose_name="banner for as",
        upload_to=content_data_path,
        validators=[FileExtensionValidator(
            allowed_extensions=["png", "jpg", "jpeg", "svg"]
        )],
    )


class FoodId(models.Model):
    food_id = models.CharField(max_length=50)
    name = models.CharField(max_length=100, null=True, blank=True)
    photo = models.ImageField(
        upload_to=content_data_path,
        validators=[FileExtensionValidator(allowed_extensions=["png", "jpg", "jpeg", "svg"])],
        null=True, blank=True
    )

    def __str__(self):
        return f"{self.id}) food id - {self.food_id}"


class PrimaryItem(models.Model):
    parent_id = models.PositiveIntegerField(editable=False, null=True)
    is_template = models.BooleanField(editable=False, default=True)
    name = models.CharField(max_length=300)
    price = models.PositiveIntegerField(default=0)
    amount = models.PositiveIntegerField(default=1, blank=True)
    description = models.TextField(blank=True, default="")
    photo = models.ImageField(
        upload_to=content_data_path,
        validators=[FileExtensionValidator(allowed_extensions=["png", "jpg", "jpeg", "svg"])],
    )
    special_food_id = models.ForeignKey(
        FoodId,
        on_delete=models.DO_NOTHING,
        related_name="foods"
    )

    def __str__(self):
        return f'{self.id}-{self.name} {self.price}₸'


class BevItem(PrimaryItem):
    color = models.CharField(max_length=20)
    bubbles = models.BooleanField()
    mlittres = models.PositiveIntegerField()

    def __str__(self):
        return super(BevItem, self).__str__() + f" for {self.mlittres}ml"


class FoodItem(PrimaryItem):
    weight = models.PositiveIntegerField()
    image_in = models.ImageField()


class CutleryItem(PrimaryItem):
    pass

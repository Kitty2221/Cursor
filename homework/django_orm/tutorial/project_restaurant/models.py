from django.db import models


class Restaurant(models.Model):
    STATUS_OPENED = 'opened'
    STATUS_CLOSED = 'closed'

    STATUS_CHOICES = (
        (STATUS_OPENED, "Opened"),
        (STATUS_CLOSED, "Closed"),
    )

    status = models.CharField(
        max_length=64,
        choices=STATUS_CHOICES,
        default=STATUS_OPENED,
        blank=True
    )

    name = models.CharField(
        max_length=64,
        blank=False
    )
    owner = models.CharField(
        max_length=64,
        blank=False
    )
    city = models.ForeignKey(
        'City',
        on_delete=models.CASCADE,
        related_name='cities'
    )
    country = models.ForeignKey(
        'Country',
        on_delete=models.CASCADE
    )
    staff = models.ManyToManyField(
        'Staff'
    )

    class Meta:
        verbose_name = 'Restaurant'
        verbose_name_plural = 'Restaurants'

    def __str__(self):
        return self.name


class Staff(models.Model):
    POST_ADMIN = 'administrator'
    POST_BARTENDER = 'bartender'
    POST_WAITER = 'waiter'
    POST_CHEF = 'chef'
    POST_CLEANER = 'cleaner'

    POSITION_CHOICES = (
        (POST_ADMIN, "Administrator"),
        (POST_BARTENDER, "Bartender"),
        (POST_WAITER, "Waiter"),
        (POST_CHEF, "Chef"),
        (POST_CLEANER, "Cleaner"),
    )
    first_name = models.CharField(
        max_length=64,
        blank=False
    )
    last_name = models.CharField(
        max_length=64,
        blank=False
    )

    post = models.CharField(
        max_length=50,
        choices=POSITION_CHOICES,
        blank=False,
    )
    phone = models.IntegerField(
        max_length=20,
        blank=True
    )

    class Meta:
        verbose_name = 'Staff'
        verbose_name_plural = 'Staff'

    def __str__(self):
        return f'{self.first_name} {self.last_name} is {self.position}'


class Country(models.Model):
    country = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.country


class City(models.Model):
    city = models.CharField(
        max_length=64
    )

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.city


class Dish(models.Model):
    dish = models.CharField(
        max_length=64
    )
    weight = models.IntegerField

    ingredients = models.TextField()

    price = models.FloatField

    class Meta:
        verbose_name = 'Dish'
        verbose_name_plural = 'Dishes'

    def __str__(self):
        return self.dish


class Menu(models.Model):
    SEASON_WINTER = 'winter'
    SEASON_SPRING = 'spring'
    SEASON_SUMMER = 'summer'
    SEASON_AUTUMN = 'autumn'

    SEASON_CHOICES = (
        (SEASON_WINTER, 'Winter'),
        (SEASON_SPRING, 'Spring'),
        (SEASON_SUMMER, 'Summer'),
        (SEASON_AUTUMN, 'Autumn'),
    )

    name = models.CharField(
        max_length=64
    )
    list_of_dishes = models.ManyToManyField(
        Dish
    )
    season_dish = models.CharField(
        max_length=64,
        choices=SEASON_CHOICES,
        default=SEASON_SUMMER,
        blank=True,
    )

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'

    def __str__(self):
        return self.name


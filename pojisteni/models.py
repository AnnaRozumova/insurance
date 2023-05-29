from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class Pojistence(models.Model):
    id_pojistence = models.BigAutoField(primary_key=True)
    jmeno = models.CharField(max_length=64)
    prijmeni = models.CharField(max_length=64)
    email = models.EmailField(max_length=254)
    telefon = models.IntegerField()
    adresa = models.CharField(max_length=64)
    pojisteni = []

    class Meta:
        verbose_name_plural = 'Pojistence'

    def __str__(self):
        return f'{self.jmeno} {self.prijmeni}'


class TypyPojisteni(models.Model):
    nazev = models.CharField(max_length=254)
    popis = models.TextField(blank=True)
    cena_za_mesic = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    class Meta:
        verbose_name_plural = 'Typy Pojisteni'

    def __str__(self):
        return f'{self.nazev}'


class Pojisteni(models.Model):
    id_pojisteni = models.BigAutoField(primary_key=True)
    id_pojistence = models.ForeignKey(Pojistence, on_delete=models.CASCADE)
    nazev = models.ForeignKey(TypyPojisteni, on_delete=models.PROTECT)
    predmet = models.CharField(max_length=64, blank=True)
    datum_smlouvy = models.DateField(auto_now_add=True)
    platnost_od = models.DateField()
    platnost_do = models.DateField()
    pojistna_osoba = models.CharField(max_length=254)

    class Meta:
        verbose_name_plural = 'Pojisteni'

    def __str__(self):
        return f'ID {self.id_pojisteni} {self.nazev}'
    
class UzivatelManager(BaseUserManager):
    # Vytvoří uživatele
    def create_user(self, email, password):
        print(self.model)
        if email and password:
            user = self.model(email=self.normalize_email(email))
            user.set_password(password)
            user.save()
        return user
    # Vytvoří admina
    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_admin = True
        user.save()
        return user

class Uzivatel(AbstractBaseUser):

    email = models.EmailField(max_length = 300, unique=True)
    is_admin = models.BooleanField(default=False)

    class Meta:
        verbose_name = "uživatel"
        verbose_name_plural = "uživatelé"

    objects = UzivatelManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return "email: {}".format(self.email)

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

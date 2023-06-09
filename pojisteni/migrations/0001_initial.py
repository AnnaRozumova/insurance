# Generated by Django 4.2.1 on 2023-05-18 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pojistence',
            fields=[
                ('id_pojistence', models.BigAutoField(primary_key=True, serialize=False)),
                ('jmeno', models.CharField(max_length=64)),
                ('prijmeni', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254)),
                ('telefon', models.IntegerField(max_length=64)),
                ('adresa', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='TypyPojisteni',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazev', models.CharField(max_length=254)),
                ('popis', models.TextField(blank=True)),
                ('cena_za_mesic', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='Pojisteni',
            fields=[
                ('id_pojisteni', models.BigAutoField(primary_key=True, serialize=False)),
                ('predmet', models.CharField(max_length=64)),
                ('datum_smlouvy', models.DateField(auto_now_add=True)),
                ('platnost_od', models.DateField()),
                ('platnost_do', models.DateField()),
                ('pojistna_osoba', models.CharField(max_length=254)),
                ('id_pojistence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pojisteni.pojistence')),
                ('nazev', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pojisteni.typypojisteni')),
            ],
        ),
    ]

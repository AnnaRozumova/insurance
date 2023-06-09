# Generated by Django 4.2.1 on 2023-05-29 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pojisteni', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Uzivatel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=300, unique=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'uživatel',
                'verbose_name_plural': 'uživatelé',
            },
        ),
        migrations.AlterModelOptions(
            name='pojistence',
            options={'verbose_name_plural': 'Pojistence'},
        ),
        migrations.AlterModelOptions(
            name='pojisteni',
            options={'verbose_name_plural': 'Pojisteni'},
        ),
        migrations.AlterModelOptions(
            name='typypojisteni',
            options={'verbose_name_plural': 'Typy Pojisteni'},
        ),
        migrations.AlterField(
            model_name='pojistence',
            name='telefon',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pojisteni',
            name='predmet',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]

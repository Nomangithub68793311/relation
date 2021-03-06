# Generated by Django 4.0.5 on 2022-06-10 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=1000)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Bio',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Signup.user')),
                ('gender', models.CharField(max_length=50)),
                ('pic', models.EmailField(max_length=50)),
                ('dOb', models.DateField()),
                ('country', models.CharField(max_length=100)),
            ],
        ),
    ]

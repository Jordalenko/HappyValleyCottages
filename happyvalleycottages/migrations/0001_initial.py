# Generated by Django 4.2.21 on 2025-05-28 10:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cottage',
            fields=[
                ('cottage_id', models.CharField(default='A', max_length=1, primary_key=True, serialize=False)),
                ('bedrooms', models.IntegerField()),
                ('bathrooms', models.IntegerField()),
                ('max_guests', models.IntegerField()),
                ('price_per_night', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('res_id', models.AutoField(primary_key=True, serialize=False)),
                ('check_in_date', models.DateField()),
                ('check_out_date', models.DateField()),
                ('discount', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('is_completed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('cottage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='happyvalleycottages.cottage')),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='happyvalleycottages.guest')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('review_id', models.AutoField(primary_key=True, serialize=False)),
                ('comment', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('cottage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='happyvalleycottages.cottage')),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='happyvalleycottages.guest')),
            ],
            options={
                'unique_together': {('guest', 'cottage')},
            },
        ),
    ]

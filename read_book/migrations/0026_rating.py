# Generated by Django 4.0.6 on 2022-08-03 08:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('read_book', '0025_like'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Very bad'), (2, 'Bad'), (3, 'OK'), (4, 'COOL'), (5, 'AMAZING')])),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='read_book.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

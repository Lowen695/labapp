# Generated by Django 3.2.7 on 2021-10-22 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chemicals', '0003_auto_20211018_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chemicals',
            name='arrive_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='chemicals',
            name='expire_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email address'),
        ),
    ]

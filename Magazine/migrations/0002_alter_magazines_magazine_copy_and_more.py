# Generated by Django 4.0.5 on 2022-08-25 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Magazine', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='magazines',
            name='magazine_copy',
            field=models.FileField(upload_to='upload/', verbose_name='Magazine_Copy'),
        ),
        migrations.AlterField(
            model_name='magazines',
            name='magazine_name',
            field=models.CharField(max_length=50, verbose_name='Magazine_Name'),
        ),
    ]

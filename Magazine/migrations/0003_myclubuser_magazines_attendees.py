# Generated by Django 4.0.5 on 2022-08-30 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Magazine', '0002_alter_magazines_magazine_copy_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyClubUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, verbose_name='User Email')),
            ],
        ),
        migrations.AddField(
            model_name='magazines',
            name='attendees',
            field=models.ManyToManyField(blank=True, to='Magazine.myclubuser'),
        ),
    ]
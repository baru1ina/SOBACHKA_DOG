# Generated by Django 4.2.7 on 2023-12-18 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0005_breed_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id_user', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('username', models.CharField(max_length=200)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('patronymic', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='breed',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='dogs',
            name='id_breeder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='breeder', to='main_page.user'),
        ),
        migrations.AlterField(
            model_name='dogs',
            name='id_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='main_page.user'),
        ),

    ]

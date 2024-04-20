# Generated by Django 5.0.3 on 2024-04-18 09:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delicious', '0010_remove_recipe_blog_ingredients'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('order', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('quantity', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('rating', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to='post_images/')),
            ],
        ),
        migrations.DeleteModel(
            name='recipe_blog',
        ),
        migrations.AddField(
            model_name='ingredient',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delicious.post'),
        ),
        migrations.AddField(
            model_name='contentsection',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delicious.post'),
        ),
    ]

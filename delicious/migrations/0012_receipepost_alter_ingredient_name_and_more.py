# Generated by Django 5.0.3 on 2024-04-18 14:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delicious', '0011_contentsection_ingredient_post_delete_recipe_blog_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReceipePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('rating', models.IntegerField(default=0)),
                ('preparation_time', models.PositiveIntegerField()),
                ('cook_time', models.PositiveIntegerField()),
                ('yield_items', models.PositiveIntegerField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.RenameModel(
            old_name='ContentSection',
            new_name='RecipeContentSection',
        ),
        migrations.CreateModel(
            name='ReceipeImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='receipe_img/')),
                ('receipe_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delicious.receipepost')),
            ],
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='delicious.receipepost'),
        ),
        migrations.AlterField(
            model_name='recipecontentsection',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delicious.receipepost'),
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]

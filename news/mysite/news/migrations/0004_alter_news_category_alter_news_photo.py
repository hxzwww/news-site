# Generated by Django 4.0.5 on 2022-07-06 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_category_alter_news_options_news_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='category',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.PROTECT, to='news.category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='news',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]

# Generated by Django 3.1.4 on 2022-01-03 06:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('jobRole', models.CharField(max_length=100)),
                ('comapanyName', models.CharField(max_length=100)),
                ('datePosted', models.DateTimeField(default=django.utils.timezone.now)),
                ('lastDateToApply', models.DateTimeField()),
                ('description', models.TextField()),
                ('companyWebsite', models.URLField()),
                ('applyingLink', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='CommentOnPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datePosted', models.DateTimeField(default=django.utils.timezone.now)),
                ('comment', models.CharField(max_length=800)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='placementPosts.post')),
            ],
        ),
    ]
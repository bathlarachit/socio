# Generated by Django 3.0.3 on 2021-03-15 06:02

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
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photos/')),
                ('profession', models.CharField(blank=True, max_length=256, null=True)),
                ('city', models.CharField(blank=True, max_length=256, null=True)),
                ('country', models.CharField(blank=True, max_length=256, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fri1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='User1', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('fri3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='User', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
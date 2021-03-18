# Generated by Django 3.0.3 on 2021-03-15 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='web',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personal_website', models.URLField(blank=True, null=True)),
                ('Insta_Username', models.CharField(blank=True, max_length=256, null=True)),
                ('Twitter', models.CharField(blank=True, max_length=256, null=True)),
                ('Facebook', models.CharField(blank=True, max_length=256, null=True)),
                ('Github', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='work_at',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
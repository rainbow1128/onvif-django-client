# Generated by Django 2.0.5 on 2018-06-02 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Camera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=200)),
                ('port', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
            ],
        ),
    ]

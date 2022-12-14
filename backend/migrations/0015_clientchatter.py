# Generated by Django 2.2.8 on 2021-04-19 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0014_client_mail_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientChatter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True)),
                ('flag', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now=True, null=True)),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.Client')),
                ('clientaddress', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.ClientAddress')),
            ],
        ),
    ]

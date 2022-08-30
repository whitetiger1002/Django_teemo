# Generated by Django 2.2.8 on 2021-05-03 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0019_auto_20210503_0947'),
    ]

    operations = [
        migrations.AddField(
            model_name='userrole',
            name='invent_add',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userrole',
            name='invent_del',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userrole',
            name='invent_up',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userrole',
            name='manufact_add',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userrole',
            name='manufact_del',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userrole',
            name='manufact_up',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userrole',
            name='offer_add',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userrole',
            name='offer_del',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userrole',
            name='offer_up',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userrole',
            name='outcome_add',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userrole',
            name='outcome_del',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userrole',
            name='outcome_up',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userrole',
            name='product_add',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userrole',
            name='product_del',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userrole',
            name='product_up',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userrole',
            name='purchase_add',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userrole',
            name='purchase_del',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userrole',
            name='purchase_up',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userrole',
            name='setting_add',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userrole',
            name='setting_del',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userrole',
            name='setting_up',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userrole',
            name='time_add',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userrole',
            name='time_del',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userrole',
            name='time_up',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userrole',
            name='transport_add',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userrole',
            name='transport_del',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userrole',
            name='transport_up',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userrole',
            name='trolley_add',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userrole',
            name='trolley_del',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userrole',
            name='trolley_up',
            field=models.BooleanField(default=False),
        ),
    ]
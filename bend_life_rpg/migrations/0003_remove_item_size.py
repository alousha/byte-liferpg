# Generated by Django 4.0.5 on 2022-07-04 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bend_life_rpg', '0002_rename_user_id_room_room_owner_item_size_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='size',
        ),
    ]

# Generated by Django 2.2.24 on 2024-08-07 13:08
import phonenumbers
from django.db import migrations


def move_phone(apps, schema_editors):
    Post = apps.get_model('property', 'Flat')
    for post in Post.objects.all():
        number_parse = phonenumbers.parse(post.owners_phonenumber, 'RU')
        final_number = phonenumbers.format_number(number_parse, phonenumbers.PhoneNumberFormat.E164)
        post.owner_pure_phone = final_number
        post.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_flat_owner_pure_phone'),
    ]

    operations = [
        migrations.RunPython(move_phone)
    ]

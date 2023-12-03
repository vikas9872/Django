# Generated by Django 4.2.5 on 2023-11-02 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=16)),
                ('lname', models.CharField(max_length=16)),
                ('age', models.IntegerField()),
                ('date', models.DateField(null=True)),
            ],
        ),
    ]
# Generated by Django 3.1.6 on 2021-02-14 10:53

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, unique=True)),
                ('email', models.CharField(blank=True, max_length=60, null=True)),
                ('contacted', models.BooleanField(default=False)),
                ('client', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=95)),
                ('sc', models.SmallIntegerField(default=0)),
                ('cb', models.SmallIntegerField(default=0)),
                ('interested', models.CharField(choices=[('LI', 'Low Interest'), ('MI', 'Medium Interest'), ('HI', 'High Interest')], default='MI', max_length=2)),
                ('comments', models.CharField(blank=True, max_length=500, null=True)),
                ('saved', models.BooleanField(default=False)),
                ('seen', models.BooleanField(default=False)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prospect.agent')),
            ],
        ),
    ]
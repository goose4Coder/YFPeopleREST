# Generated by Django 5.1.3 on 2024-12-05 11:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Member Email')),
                ('telegram', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField(verbose_name='Date of birth')),
            ],
        ),
        migrations.CreateModel(
            name='MemberTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('leader', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='members.member')),
                ('member', models.ManyToManyField(related_name='%(class)s_of_the_club', to='members.member')),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='tags',
            field=models.ManyToManyField(to='members.membertag'),
        ),
    ]
# Generated by Django 3.2.7 on 2021-09-14 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20)),
                ('hp', models.IntegerField(default=100)),
                ('mp', models.IntegerField(default=100)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('score', models.IntegerField(default=1)),
                ('character', models.ManyToManyField(to='game.Character')),
            ],
        ),
        migrations.CreateModel(
            name='Round',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='game date')),
                ('round_number', models.IntegerField(default=1)),
                ('p1', models.ManyToManyField(related_name='round_p1', to='game.Player')),
                ('p2', models.ManyToManyField(related_name='round_p2', to='game.Player')),
            ],
        ),
    ]

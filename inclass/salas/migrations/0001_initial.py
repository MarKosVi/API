# Generated by Django 2.2.7 on 2019-11-13 00:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('escolas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_sala', models.IntegerField()),
                ('campus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escolas.Escola')),
            ],
        ),
    ]

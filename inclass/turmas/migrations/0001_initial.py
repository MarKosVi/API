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
            name='Turma',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('qtd_alunos', models.IntegerField()),
                ('cod_turma', models.CharField(max_length=45)),
                ('curso', models.CharField(max_length=45)),
                ('turno', models.CharField(max_length=45)),
                ('id_escola', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escolas.Escola')),
            ],
        ),
    ]
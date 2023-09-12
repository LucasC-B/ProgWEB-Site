# Generated by Django 4.2.4 on 2023-09-12 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(help_text='Entre o nome', max_length=100)),
                ('idade', models.IntegerField(help_text='Entre a idade')),
                ('salario', models.DecimalField(decimal_places=2, help_text='Entre o salario', max_digits=8)),
                ('email', models.EmailField(help_text='Informe o email', max_length=254)),
                ('telefone', models.CharField(help_text='Telefone com DDD e DDI', max_length=20)),
                ('dtNasc', models.DateField(help_text='Nascimento no formato DD/MM/AAAA', verbose_name='Data de nascimento')),
            ],
        ),
    ]
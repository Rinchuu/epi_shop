# Generated by Django 5.1.1 on 2024-09-22 02:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epi_shops', '0002_usuarios_delete_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cargo', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.RenameField(
            model_name='usuarios',
            old_name='nome_de_usuario',
            new_name='usuario',
        ),
        migrations.RemoveField(
            model_name='usuarios',
            name='tipo_de_usuario',
        ),
        migrations.AddField(
            model_name='usuarios',
            name='tipo_usuario',
            field=models.CharField(choices=[('Cliente', 'Cliente'), ('Funcionario', 'Funcionario'), ('Gerente', 'Gerente')], default='Cliente', max_length=12),
        ),
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razao_social', models.CharField(max_length=100)),
                ('cnpj', models.CharField(max_length=14)),
                ('usuarios', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clientes_usuarios', to='epi_shops.usuarios')),
            ],
        ),
        migrations.CreateModel(
            name='Emprestimos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emprestimo', models.DateField()),
                ('devolucao_prevista', models.DateField()),
                ('devolucao_efetiva', models.DateField()),
                ('clientes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emprestimos_clientes', to='epi_shops.clientes')),
            ],
        ),
        migrations.CreateModel(
            name='Epis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cliente', models.CharField(max_length=100)),
                ('quantidade', models.IntegerField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=7)),
                ('fornecedor', models.CharField(max_length=50)),
                ('disponibilidade', models.CharField(max_length=100)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='epis_categorias', to='epi_shops.categorias')),
            ],
        ),
        migrations.CreateModel(
            name='Carrinhos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('tipo', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('clientes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carrinhos_clientes', to='epi_shops.clientes')),
                ('epis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carrinhos_epis', to='epi_shops.epis')),
            ],
        ),
        migrations.CreateModel(
            name='Funcionarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admissao', models.DateField()),
                ('cargos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='funcionarios_cargos', to='epi_shops.cargos')),
                ('usuarios', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='funcionarios_usuarios', to='epi_shops.usuarios')),
            ],
        ),
        migrations.CreateModel(
            name='Manutencoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio', models.DateField()),
                ('data_fim', models.DateField()),
                ('descricao', models.TextField()),
                ('epis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='manutencoes_epis', to='epi_shops.epis')),
            ],
        ),
        migrations.CreateModel(
            name='Pagamentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=7)),
                ('data_compra', models.DateField()),
                ('clientes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pagamentos_clientes', to='epi_shops.clientes')),
            ],
        ),
        migrations.CreateModel(
            name='Historico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('clientes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='historico_clientes', to='epi_shops.clientes')),
                ('epis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='historico_epis', to='epi_shops.epis')),
                ('pagamentos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='historico_pagamentos', to='epi_shops.pagamentos')),
            ],
        ),
    ]

# Generated by Django 2.1.4 on 2018-12-12 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(help_text='exemplo@email.com', max_length=254)),
                ('telefone_comercial', models.CharField(blank=True, help_text='(DDD)9999-9999', max_length=50, null=True, verbose_name='Telefone Comercial')),
                ('telefone_celular', models.CharField(blank=True, help_text='(DDD)9-99999-9999', max_length=50, null=True, verbose_name='Telefone Celular')),
                ('logradouro', models.CharField(blank=True, help_text='Rua/Av/Vila etc...', max_length=50, null=True, verbose_name='Logradouro')),
                ('numero', models.PositiveIntegerField(blank=True, null=True)),
                ('nome', models.CharField(max_length=50)),
                ('bairro', models.CharField(blank=True, max_length=50, null=True)),
                ('cidade', models.CharField(blank=True, max_length=50, null=True)),
                ('estado', models.CharField(blank=True, choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tacantins')], max_length=50, null=True, verbose_name='Estado')),
                ('pais', models.CharField(blank=True, default='Brasil', max_length=20, null=True, verbose_name='País')),
                ('observacoes', models.TextField(blank=True, help_text='500 caracteres no máximo', max_length=500, null=True, verbose_name='Observações')),
            ],
        ),
        migrations.CreateModel(
            name='Fisica',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='clientes.Pessoa')),
                ('rg', models.BigIntegerField(blank=True, help_text='Somente Números', null=True, verbose_name='RG')),
                ('cpf', models.BigIntegerField(help_text='Somente Números', null=True, verbose_name='CPF')),
                ('estado_civil', models.CharField(blank=True, choices=[('sol', 'solteiro(a)'), ('cas', 'casado(a)'), ('div', 'divorciado(a)'), ('sep', 'separado(a)'), ('dis', 'disquitado(a)'), ('ou', 'Outros')], max_length=50, null=True, verbose_name='Estado Civil')),
            ],
            options={
                'verbose_name': 'Pessoa Física',
                'verbose_name_plural': 'Pessoas Físicas',
            },
            bases=('clientes.pessoa',),
        ),
        migrations.CreateModel(
            name='Juridica',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='clientes.Pessoa')),
                ('razao_social', models.CharField(blank=True, max_length=30, null=True, verbose_name='Razão Social')),
                ('cnpj', models.CharField(max_length=30, verbose_name='CNPJ')),
                ('rg', models.CharField(blank=True, help_text='RG do responsável. Somente Números', max_length=50, null=True, verbose_name='RG')),
                ('cpf', models.CharField(blank=True, help_text='CPF do responsável. Somente Números', max_length=50, null=True, verbose_name='CPF')),
                ('estado_civil', models.CharField(blank=True, choices=[('sol', 'solteiro'), ('cas', 'casado'), ('div', 'divorciado'), ('sep', 'separado'), ('dis', 'disquitado'), ('ou', 'Outros')], help_text='Estado Civil do Responsável', max_length=50, null=True)),
                ('ie', models.CharField(blank=True, max_length=30, null=True, verbose_name='Inscrição Estadual')),
            ],
            options={
                'verbose_name': 'Pessoa Jurídica',
                'verbose_name_plural': 'Pessoas Jurídicas',
            },
            bases=('clientes.pessoa',),
        ),
    ]

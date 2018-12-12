from django.db import models

# Create your models here.
class Pessoa(models.Model):
    UF_CHOICES = (
        ('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'),
        ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'),
        ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'),
        ('PE', 'Pernambuco'), ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'),
        ('RR', 'Roraima'), ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'), ('SE', 'Sergipe'),
        ('TO', 'Tacantins'),)
    email = models.EmailField(help_text='exemplo@email.com')
    telefone_comercial = models.CharField(max_length=50, null=True,
                                          blank=True, verbose_name="Telefone Comercial"
                                          , help_text="(DDD)9999-9999")
    telefone_celular = models.CharField(max_length=50, null=True,
                                        blank=True, verbose_name="Telefone Celular"
                                        , help_text="(DDD)9-99999-9999")
    logradouro = models.CharField(max_length=50, verbose_name='Logradouro'
                                  , null=True, blank=True, help_text="Rua/Av/Vila etc...")
    numero = models.PositiveIntegerField(null=True, blank=True)
    nome = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50, null=True, blank=True)
    cidade = models.CharField(max_length=50, null=True, blank=True)
    estado = models.CharField(max_length=50, verbose_name='Estado',
                              choices=UF_CHOICES, null=True, blank=True)
    pais = models.CharField(default='Brasil', max_length=20, null=True,
                            blank=True, verbose_name="País")
    observacoes = models.TextField(max_length=500, blank=True, null=True
                                   , verbose_name="Observações", help_text='500 caracteres no máximo')

    def __str__(self):
        return self.nome


class Fisica(Pessoa):
    ESTADO_CIVIL_CHOICES = (('sol', 'solteiro(a)'), ('cas', 'casado(a)'),
                            ('div', 'divorciado(a)'), ('sep', 'separado(a)'), ('dis', 'disquitado(a)'),
                            ('ou', 'Outros'))
    rg = models.BigIntegerField(verbose_name='RG', null=True,
                                blank=True, help_text="Somente Números")
    cpf = models.BigIntegerField(verbose_name='CPF', null=True
                                 , help_text="Somente Números")
    estado_civil = models.CharField(max_length=50,
                                    choices=ESTADO_CIVIL_CHOICES, blank=True, null=True
                                    , verbose_name="Estado Civil")

    class Meta:
        verbose_name = "Pessoa Física"
        verbose_name_plural = "Pessoas Físicas"


class Juridica(Pessoa):
    ESTADO_CIVIL_CHOICES = (('sol', 'solteiro'), ('cas', 'casado'),
                            ('div', 'divorciado'), ('sep', 'separado'), ('dis', 'disquitado'),
                            ('ou', 'Outros'))
    razao_social = models.CharField(max_length=30,
                                    verbose_name='Razão Social', blank=True, null=True)
    cnpj = models.CharField(max_length=30, verbose_name='CNPJ')
    rg = models.CharField(max_length=50, verbose_name='RG'
                          , blank=True, null=True
                          , help_text="RG do responsável. Somente Números")
    cpf = models.CharField(max_length=50, verbose_name='CPF'
                           , blank=True, null=True
                           , help_text="CPF do responsável. Somente Números")
    estado_civil = models.CharField(max_length=50,
                                    choices=ESTADO_CIVIL_CHOICES, blank=True, null=True,
                                    help_text='Estado Civil do Responsável')

    ie = models.CharField(max_length=30, verbose_name='Inscrição Estadual',
                          null=True, blank=True)

    class Meta:
        verbose_name = "Pessoa Jurídica"
        verbose_name_plural = "Pessoas Jurídicas"

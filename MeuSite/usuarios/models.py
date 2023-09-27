from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class AdminMinhaConta(BaseUserManager):

    def cria_usuario(self, email, nome, senha = None):
        if not email:
            raise ValueError("Usuario precisa ter um endereço de email")
        if not nome:
            raise ValueError("Usuario precisa ter um nome")

        user = self.model(
                email = self.normalize_email(email),
                username = nome,

        )

        user.set_password(senha)
        user.save(using=self._db)

        return user
    
    def cria_superusuario(self,email,nome, senha):

        user = self.create_user(
                email = self.normalize_email(email),
                password = senha,
                username = nome,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

class Usuario(AbstractBaseUser):

    id = models.AutoField(primary_key=True, null=False, blank=False)

    nome = models.CharField(help_text='Entre o nome', 
                            max_length=100, null=False, blank=False)
    
    idade = models.IntegerField(help_text='Entre a idade', null=False, blank=False)

    
    email = models.EmailField(help_text='Informe o email',
                              max_length=254, null=False, blank=False, unique=True)
    

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['nome',]
    
    def __str__(self):
        return self.nome


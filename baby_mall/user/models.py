from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self, userid, password, username, **kwargs):
        user = self.model(
            userid = userid,
            username = username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, userid, password, username, **kwargs):
        superuser = self.create_user(
            userid = userid,
            username = username,
            password = password,
            is_admin = True,
        )
        superuser.save(using=self._db)
        return superuser

class Profile(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()
    userid = models.CharField(max_length=30, unique=True)
    password = models.TextField()
    username = models.CharField(max_length=20)
    user_image = models.ImageField(blank=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'userid'
    REQUIRED_FIELDS = ['username']

    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, user):
        return True

    @property
    def is_staff(self):
        return self.is_admin


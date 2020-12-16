from django.db import models


class Users(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(Users, related_name="books_set", on_delete=models.CASCADE)
    favorites = models.ManyToManyField(Users, related_name="favorites_set")


def insert_new_user(first_name, last_name, email, password):
    user = Users.objects.create(first_name=first_name, last_name=last_name, email=email, password=password)
    return user


def is_duplicate_email(email):
    users = Users.objects.filter(email=email).values()
    if len(users):
        return True
    return False


def get_user(email, passwd):
    users = Users.objects.filter(email=email, password=passwd)
    if not len(users):
        return None
    return users[0]
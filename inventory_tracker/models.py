from django.db.models import CharField, ForeignKey, IntegerField
from django.db.models import ManyToManyField, Model, TextField
from django.contrib.auth.models import User


class Category(Model):
    title = CharField(max_length=256)


class Item(Model):
    title = CharField(max_length=256)
    description = TextField(blank=True)
    owner = ForeignKey(User)
    category = ForeignKey(Category)


class Inventory(Model):
    title = CharField(max_length=256)
    owner = ForeignKey(User)
    entries = ManyToManyField(Item, through='Entry')


class Entry(Model):
    count = IntegerField()
    item = ForeignKey(Item)
    inventory = ForeignKey(Inventory)

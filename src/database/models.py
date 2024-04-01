from peewee import *

# from config import settings


pg_db = PostgresqlDatabase('goTest', user='postgres', password='postgres',
                           host='localhost', port=5432)


class BaseModel(Model):
    class Meta:
        database = pg_db


class Rack(BaseModel):
    name = CharField(max_length=150)


class Product(BaseModel):
    name = CharField(max_length=150)
    main_rack = ForeignKeyField(Rack, backref='products')


class Order(BaseModel):
    number = IntegerField()
    product = ForeignKeyField(Product, backref='orders')
    quantity = IntegerField()

# class UserOrder(BaseModel):
#     number = IntegerField()

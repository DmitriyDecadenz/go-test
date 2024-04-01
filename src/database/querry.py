from models import *
pg_db.connect()
pg_db.create_tables([Product, Order, Rack])

Rack.insert(name='Стеллаж А').execute()
Rack.insert(name='Стеллаж Б').execute()
Rack.insert(name='Стеллаж Ж').execute()

Product.insert(name='Ноутбук',  main_rack=1).execute()
Product.insert(name='Телевизор',  main_rack=1).execute()
Product.insert(name='Телефон',  main_rack=2).execute()
Product.insert(name='Микрофон',  main_rack=3).execute()
Product.insert(name='Системный блок',  main_rack=3).execute()
Product.insert(name='Часы',  main_rack=3).execute()


Order.insert(product=1, quantity=2, number=10,).execute()
Order.insert(product=3,  quantity=1, number=10,).execute()
Order.insert(product=6,  quantity=1, number=10,).execute()
Order.insert(product=2,  quantity=3, number=11,).execute()
Order.insert(product=1,  quantity=3, number=14,).execute()
Order.insert(product=4,  quantity=4, number=14,).execute()
Order.insert(product=5,  quantity=1, number=15,).execute()

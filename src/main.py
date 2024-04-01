from database.models import *


class GetData:
    def __init__(self) -> None:
        self.order_number = self._ask_order_number()
        self.order_item = self.get_order_item()
        self.product = self.get_product()

    def _ask_order_number(self) -> list:
        number_list = []
        a = int(input('сколько заказов? \n'))
        for i in range(a):
            number = int(input('номер заказа:'))
            number_list.append(number)
        return number_list

    def get_order_item(self) -> list:
        order_item = []
        for i in range(len(self.order_number)):
            query_order_item = [x for x in Order.select().where(
                Order.number == self.order_number[i])]
            order_item.append(query_order_item)
        return order_item

    def get_product(self) -> list:
        product_id = []
        for i in self.order_item:
            for order_item in i:
                query_product = [x for x in Product.select().where(
                    Product.id == order_item.product)]

                product_id.append(query_product)
        return product_id


class Program:
    def __init__(self) -> None:
        self.data = GetData()
        self.consoleA = f''
        self.consoleB = f''
        self.consoleJ = f''

    def display(self) -> None:
        for i in self.data.get_product():
            for product in i:
                get_rack = Rack.select().where(Rack.id == product.main_rack)
                get_order = Order.select().where(Order.product == product.id)
                for rack in get_rack:
                    for order in get_order:
                        if rack.name == 'Стеллаж А':
                            self.consoleA += f'=={rack.name}\n{product.name} (id={product.id}) \nзаказ {order.number}, {order.quantity} шт \n '
                        elif rack.name == 'Стеллаж Б':
                            self.consoleB += f'=={rack.name}\n{product.name} (id={product.id}) \nзаказ {order.number}, {order.quantity} шт \n '
                        elif rack.name == 'Стеллаж Ж':
                            self.consoleJ += f'=={rack.name}\n{product.name} (id={product.id}) \nзаказ {order.number}, {order.quantity} шт \n '

        print(f'{self.consoleA}\n {self.consoleB}\n {self.consoleJ}')


if __name__ == '__main__':
    app = Program()
    app.display()

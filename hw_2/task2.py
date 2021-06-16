"""
2. Давайте представим, что мы занимаемся проектированием CRM для сервисного центра по обслуживанию и ремонту техники.
Реализуйте класс Заявка. Каждая заявка должна иметь следующие поля: уникальный идентификатор (присваивается в момент)
создания заявки автоматически, дата и время создания заявки (автоматически), имя пользователя, серийный номер
оборудования, статус (активная заявка или закрытая например, статусов может быть больше). Id заявки сделать приватным
полем.
У заявки должны быть следующие методы:
- метод, возвращающий, сколько заявка находится в активном статусе (если она в нём)
- метод, изменяющий статус заявки
- метод, возвращающий id заявки
"""
import uuid
from datetime import datetime


class Order:
    def __init__(self, user_name, serial_number, unique_id=uuid.uuid1(), date_time=datetime.now(), status=True):
        self.user_name = user_name
        self.__serial_number = serial_number
        self.unique_id = unique_id
        self.date_time = date_time
        self.status = status

    def set_status(self, status):
        self.status = status

    def get_id(self):
        return self.unique_id

    def get_active_time(self):
        if self.status:
            return datetime.now() - self.date_time

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)


order = Order('Vasya', 123)

print(order.get_active_time())

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


class Application:
    def __init__(self, user_name, device_number, status='active'):
        self.__application_id = uuid.uuid4()
        self.user_name = user_name
        self.device_number = device_number
        self.status = status
        self.date_created = datetime.now()

    def active_status_time(self):
        if self.status == 'active':
            return datetime.now() - self.date_created

        return None

    def set_status_inactive(self):
        self.status = 'inactive'

    def show_application_id(self):
        return self.__application_id


app1 = Application('Ben', '1')
app2 = Application('John', '2')
print(app1.show_application_id())
print(app2.show_application_id())

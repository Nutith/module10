import queue
import random
import threading
import time


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self, name=name)

    def run(self):
        time.sleep(random.randint(3, 10))


class Cafe:
    def __init__(self, *tables):
        self.tables = tables
        self.queue = queue.Queue()

    def get_free_table_list(self):
        return [table for table in self.tables if table.guest is None]

    def get_free_table(self):
        free_list = self.get_free_table_list()

        if not free_list:
            return None

        return random.choice(free_list)

    def __place_guest(self, table, guest):
        table.guest = guest
        table.guest.start()

    def guest_arrival(self, *guests):
        for guest in guests:
            table = self.get_free_table()
            if table:
                self.__place_guest(table, guest)
                print(f'{guest.name} сел(-а) за стол номер {table.number}')
            else:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self):
        while len(self.get_free_table_list()) < len(self.tables) or not self.queue.empty():
            for table in self.tables:
                if table.guest and not table.guest.is_alive():
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    table.guest = None
                    print(f'Стол номер {table.number} свободен')

            table = self.get_free_table()
            if not table:
                continue

            try:
                guest = self.queue.get(block=False)
            except queue.Empty:
                pass
            else:
                self.__place_guest(table, guest)
                print(f'{guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')


# Создание столов
tables = [Table(number) for number in range(1, 6)]

# Имена гостей
guests_names = ['Maria', 'Oleg', 'Vakhtang',
                'Sergey', 'Darya', 'Arman',
                'Vitoria', 'Nikita', 'Galina',
                'Pavel', 'Ilya', 'Alexandra']

# Создание гостей
guests = [Guest(name) for name in guests_names]

# Заполнение кафе столами
cafe = Cafe(*tables)

# Приём гостей
cafe.guest_arrival(*guests)

# Обслуживание гостей
cafe.discuss_guests()

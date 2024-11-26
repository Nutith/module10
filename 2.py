import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)

        self.power = power
        self.name = name

    def run(self):
        print(f'{self.name}, на нас напали!')

        enemies = 100
        days = 0

        while enemies != 0:
            enemies -= self.power
            days += 1

            if enemies < 0:
                enemies = 0

            time.sleep(1)
            print(f'{self.name}, сражается {days} день(дня)..., осталось {enemies} воинов.')

        print(f'{self.name} одержал победу спустя {days} дней(дня)')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

for thread in first_knight, second_knight:
    thread.start()

for thread in first_knight, second_knight:
    thread.join()

print('Все битвы закончились!')

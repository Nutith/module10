import threading
import random
import time


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

        self.lock.acquire()

    def deposit(self):
        for i in range(100):
            inc = random.randint(50, 500)
            self.balance += inc
            print(f'Пополнение: {inc}. Баланс: {self.balance}')

            if self.balance >= 500 and self.lock.locked():
                self.lock.release()

            time.sleep(0.001)

    def take(self):
        for i in range(100):
            dec = random.randint(50, 500)
            print(f'Запрос на {dec}')

            if dec > self.balance:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire(timeout=0.1)

            if dec <= self.balance:
                self.balance -= dec
                print(f'Снятие: {dec}. Баланс: {self.balance}')


bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')

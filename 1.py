import time
import threading


WORDS_COUNT = [10, 30, 200, 100]
FILE_NAME = 'example'


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf8') as f:
        for i in range(1, word_count+1):
            f.write(f'Какое-то слово № {i}\n')
            time.sleep(0.1)

    print(f'Завершилась запись в файл {file_name}')


start = time.time()

for i in range(4):
    write_words(WORDS_COUNT[i], f'{FILE_NAME}{i+1}.txt')

elapsed = time.time() - start
print(elapsed)

start = time.time()
threads = []

for i in range(4):
    thread = threading.Thread(target=write_words, args=(WORDS_COUNT[i], f'{FILE_NAME}{i+5}.txt'))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

elapsed = time.time() - start
print(elapsed)

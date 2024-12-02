import time
from multiprocessing import Pool


def read_info(name):
    all_data = []

    for line in open(name, encoding='utf-8'):
        all_data.append(line)


if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    start = time.time()

    # for filename in filenames:
    #     read_info(filename)

    with Pool(len(filenames)) as p:
        p.map(read_info, filenames)

    elapsed = time.time() - start

    print(elapsed)

# l = [0,1,2,3,4]
# try:
#     l.index(22)
# except ValueError as err:
#     l.append(22)
#     print(l.index(22))
# finally:
#     print('finish')
#
# print('hello')
################################################
# files
################################################
# try:
#     file = open('files/1.txt', mode='r')
# except FileNotFoundError:
#     file = open('files/1.txt', mode='w')
# file.close()
import os

# # print(os.listdir('.'))
# # os.mkdir('files2')
# path = os.path.join('files', '1.txt')
# with open(path, 'w') as file:
#     read = file.writelines(['hello\n', 'world'])

###############################################
# generators

# def gen(name):
#     for ch in name:
#         yield ch
#         print('hellp')
#
#
# g = gen('Vitaliy')
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# import uuid
# def gen_jpg_file():
#     pattern = '{}.jpg'
#     while True:
#         yield pattern.format(uuid.uuid1())
#
#
# gen = gen_jpg_file()
# print(next(gen))

# def gen():
#     yield 1
#     yield 2
#     yield 3
#     return 'Finish'
#
#
# # g = gen()
# # print(next(g))
# # print(next(g))
# # print(next(g))
# # try:
# #     print(next(g))
# # except StopIteration as err:
# #     print(err)
#
# def gen1(name):
#     for i in name:
#         yield i
#
#
# def gen2(n):
#     for i in range(n):
#         yield i
#
#
# tasks = [gen2(8), gen1('Max')]
#
# while tasks:
#     task = tasks.pop(0)
#     try:
#         i = next(task)
#         print(i)
#         tasks.append(task)
#     except StopIteration:
#         pass

# import asyncio
#
#
# @asyncio.coroutine
# def print_nums():
#     num = 1
#     while True:
#         print(num)
#         num += 1
#         yield from asyncio.sleep(1)
#
#
# @asyncio.coroutine
# def print_time():
#     time = 1
#     while True:
#         print('Time:', time)
#         time += 1
#         yield from asyncio.sleep(3)
#
#
# @asyncio.coroutine
# def main():
#     task1 = asyncio.ensure_future(print_nums())
#     task2 = asyncio.ensure_future(print_time())
#     yield from asyncio.gather(task1, task2)
#
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())
# loop.close()

###################################################################

# import asyncio
#
#
# async def print_nums():
#     num = 1
#     while True:
#         print(num)
#         num += 1
#         await asyncio.sleep(1)
#
#
# async def print_time():
#     time = 1
#     while True:
#         print('Time:', time)
#         time += 1
#         await asyncio.sleep(3)


# async def main():
#     task1 = asyncio.create_task(print_nums())
#     task2 = asyncio.create_task(print_time())
#     await asyncio.gather(task1, task2)
#
#
# asyncio.run(main())
#######################################################################################
# import requests
# import time
# import os
#
#
# def time_decor(func):
#     def wrap(*args, **kwargs):
#         start = time.time()
#         func(*args, **kwargs)
#         print('Time: ', round(time.time() - start))
#
#     return wrap
#
#
# def get_res(url):
#     return requests.get(url, allow_redirects=True)
#
#
# def write_file(res: requests.Response):
#     file_name = res.url.split('/')[-1]
#     with open(os.path.join('files', file_name), mode='wb') as file:
#         file.write(res.content)
#
#
# @time_decor
# def main():
#     url = 'https://loremflickr.com/320/240'
#     for i in range(20):
#         write_file(get_res(url))
#
# main()
####################################################################
import asyncio
import httpx
import time
import os
import uuid


def gen_jpg_file():
    pattern = '{}.jpg'
    while True:
        yield pattern.format(uuid.uuid1())


gen = gen_jpg_file()


def time_decor(func):
    def wrap(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        print('Time: ', round(time.time() - start))

    return wrap


def write_file(data):
    file_name = next(gen)
    with open(os.path.join('files', file_name), mode='wb') as file:
        file.write(data)


async def get_res(url, client):
    res = await client.get(url)
    write_file(res.read())


async def start():
    url = 'https://loremflickr.com/320/240'
    tasks = []
    async with httpx.AsyncClient() as client:
        for i in range(20):
            task = asyncio.create_task(get_res(url, client))
            tasks.append(task)
        await asyncio.gather(*tasks)


@time_decor
def main():
    asyncio.run(start())

main()

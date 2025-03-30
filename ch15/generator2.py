import time

def longtime_job():
    print('job start')
    time.sleep(1)       # 1초 지연(delay)
    return 'done'

# print(longtime_job())

list_job = (longtime_job() for i in range(5))
print(next(list_job))
print(next(list_job))
print(next(list_job))
print(next(list_job))
print(next(list_job))
# print(next(list_job))
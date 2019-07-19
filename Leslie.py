# encoding:utf-8
import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd

# 读取csv文件
def csv_read(path):
    csv_file = csv.reader(open(path, 'r'))
    dt = []
    dt1 = []
    for item in csv_file:
        dt.append(item)
    dt = np.array(dt)
    for i in dt:
        dt1.append(float(i))
    dt1 = np.array(dt1)
    dt1 = dt1.reshape((-1, dt1.shape[0])).T
    return dt1


# 写入csv文件
def csv_write(path, data):
    with open(path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        for list in data:
            print(list)
            csv_writer.writerow(list)




# 当年各个年龄女性人数 woman population
woman_population = csv_read('data/2013.csv') * 10000

# 当年各个年龄女性生育率 birth rate
birth_rate_1 = csv_read('data/1_birth_rate.csv') / 1000 / 2
birth_rate_2 = csv_read('data/2_birth_rate.csv') / 1000 / 2
birth_rate_3 = csv_read('data/3_birth_rate.csv') / 1000 / 2

# 当年各个年龄女性存活率 survival rate
survival_rate = csv_read('data/s_r.csv') / 100

# 迭代年数
year = 40

# 初始年份
begin_year = 2016

# 性别比
sex_ratio = 1.03

print('人口数量:', sum(woman_population))
print('\n')


def Leslie(woman_population, birth_rate, survival_rate, year, sex_ratio):
    survival_rate = survival_rate[0:-1]
    M = np.diag(survival_rate.flatten(), k=-1)
    M[0, :] = birth_rate.flatten()
    K = woman_population
    total_population = woman_population + woman_population * sex_ratio
    I = K
    for i in range(year):
        I1 = np.dot(M, I)
        total_population = np.c_[total_population, I1 + I1 * sex_ratio]
        I = I1

    return total_population


def age_rate(total_population):
    age_population = total_population[60:, :]
    return age_population.sum(axis=0)/total_population.sum(axis=0)


print('\n')


total_population_1 = Leslie(woman_population, birth_rate_1, survival_rate, year=year, sex_ratio=1.03)
total_population_2 = Leslie(woman_population, birth_rate_2, survival_rate, year=year, sex_ratio=1.03)
total_population_3 = Leslie(woman_population, birth_rate_3, survival_rate, year=year, sex_ratio=1.03)
t1 = total_population_1.sum(axis=0).reshape((year+1, 1))
t2 = total_population_2.sum(axis=0).reshape((year+1, 1))
t3 = total_population_3.sum(axis=0).reshape((year+1, 1))


# 输出历年人口人数
print('历年人口总数:', total_population_1.sum(axis=0))
print('历年人口总数:', total_population_2.sum(axis=0))
print('历年人口总数:', total_population_3.sum(axis=0))


# 老龄化比率
print('age1',age_rate(total_population_1))
print('age2',age_rate(total_population_2))
print('age3',age_rate(total_population_3))


def cal(total_p):
    print('-----------------------------------------')
    s = []
    for i in range(20):
        print(total_p[i:i+4, :].sum(axis=1))
        s.append(total_p[i:i+4, :].sum(axis=1))
    s = np.array(s)
    print(s.shape)
    print('-----------------------------------------')
    return s


print(cal(total_population_1))
csv_write('data/1.csv', cal(total_population_1))
csv_write('data/2.csv', cal(total_population_2))
csv_write('data/3.csv', cal(total_population_3))

csv_write('data/aging_rate_1.csv', age_rate(total_population_1).reshape((year+1, 1)))
csv_write('data/aging_rate_2.csv', age_rate(total_population_2).reshape((year+1, 1)))
csv_write('data/aging_rate_3.csv', age_rate(total_population_3).reshape((year+1, 1)))


plt.plot(total_population_1.sum(axis=0))
plt.plot(total_population_2.sum(axis=0))
plt.plot(total_population_3.sum(axis=0))
plt.legend(['计划生育', '单独二孩政策', '全面实行二孩政策'], loc='upper right')
plt.ylabel('人数（人）')
plt.xlabel('年份（年）')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.title('人口数量')
plt.show()




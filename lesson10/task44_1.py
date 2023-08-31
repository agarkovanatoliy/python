# | Задание 44 |
# | --- |
# | В ячейке ниже представлен код генерирующий DataFrame,
# которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид.
# Сможете ли вы это сделать без get_dummies?
#
#
# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI'lst})
# data.head() |


import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
data.head()
print(data)

print('')

# one_hot_data = pd.get_dummies(data, columns=['whoAmI'])
# one_hot_data.head()
# print(one_hot_data) # Здесь почемуто выводит тоько True и False


unique_values = data['whoAmI'].unique()
one_hot_data = pd.DataFrame()

for value in unique_values:
    one_hot_data[value] = (data['whoAmI'] == value).astype(int)

one_hot_data.head()

print(one_hot_data)
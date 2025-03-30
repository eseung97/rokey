# dic_num = {'a':10, 'b':20, 'c':30}
# def dic_sum():
#     total = dic_num['a'] + dic_num['b'] + dic_num['c']
#     return total
# print(dic_sum())


# def sum_dict_values(d):
#     return sum(d.values())
# data = {'a': 10, 'b': 20, 'c': 30}
# print("값의 합:", sum_dict_values(data))


def sum_values(input_dict): 
    sum = 0 
    for num in input_dict.values(): 
        sum += num 
    return sum 
input_dict = { 'a': 10, 'b': 20, 'c': 30 } 
output = sum_values(input_dict) 
print(output) # 60


# a = [1,10,2,13,17]
# max = a[0]
# for i in a:
#     if max < i:
#         max = i
# print(max)


# def selection_sort(arr):
#     for i in range(len(arr)):   
#         min_idx = i             
#         for j in range(i+1, len(arr)):  
#             if arr[j] < arr[min_idx]:
#                 min_idx = j     
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]
#     return arr

# data = [64, 25, 12, 22, 11]
# print(selection_sort(data))
# def calculate_average(numbers):
#     if not numbers:  
#         return "리스트가 비어 있습니다."
    
#     return sum(numbers) / len(numbers)  

# nums = [10, 20, 30, 40, 50]
# print("리스트의 평균:", int(calculate_average(nums)))

def sum_list(numList): 
    sum = 0 
    for num in numList: 
        sum += num 
    return sum 
    
sum1 = sum_list([1, 2, 3, 4, 5]) 
print("리스트 합:", sum1)
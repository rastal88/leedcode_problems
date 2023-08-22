'''Задан массив целых чисел и целое число(target).
Нужно вернуть индексы двух чисел сумма которых будет равна target.
Предполагается что в списке будет ежинственный правильный вариант, а не более.
Вы можете вернуть ответ в любом порядке.'''

'''Given an array of integers  and an integer , 
return indices of the two numbers such that they add up to target.numstarget
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
'''


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prevMap = {}  # val : index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return

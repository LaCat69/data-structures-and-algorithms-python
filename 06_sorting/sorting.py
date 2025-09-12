class Sorts:
    def bubble_sort(self, lst):
        for i in range(len(lst) - 1):
            for j in range(len(lst) - 1 - i):
                if lst[j] > lst[j+1]:
                    lst[j], lst[j+1] = lst[j+1], lst[j]

    
    def selection_sort(self, lst):
        for i in range(len(lst)):
            min_index = i
            for j in range(i, len(lst)):
                if lst[min_index] > lst[j]:
                    min_index = j
            lst[i], lst[min_index] = lst[min_index], lst[i]

    
    def insertion_sort(self, lst):
        for i in range(1, len(lst)):
            key = lst[i]
            j = i - 1
            while j >= 0 and key < lst[j]:
                lst[j + 1] = lst[j]
                j -= 1
            lst[j + 1] = key
    
    def merge_sort(self, lst):
        if len(lst) <= 1:
            return lst
        mid = len(lst) // 2
        left = self.merge_sort(lst[:mid])
        right = self.merge_sort(lst[mid:])
        return self.merge(left, right)
    
    def merge(self, left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
    def quick_sort(self, lst):
        if len(lst) <= 1:
            return lst
        pivot = lst[len(lst) // 2]
        left = [x for x in lst if x < pivot]
        middle = [x for x in lst if x == pivot]
        right = [x for x in lst if x > pivot]
        return self.quick_sort(left) + middle + self.quick_sort(right)
    
    def heapify(self, lst, n, i):
        largest = i
        left, right = i * 2 + 1, i * 2 + 2
        if left < n and lst[left] > lst[largest]:
            largest = left
        if right < n and lst[right] > lst[largest]:
            largest = right
        if largest != i:
            lst[i], lst[largest] = lst[largest], lst[i]
            self.heapify(lst, n, largest)
        
    def heap_sort(self, lst):
        n = len(lst)
        for i in range(n//2 -1, -1, -1):
            self.heapify(lst, n, i)
        for i in range(n - 1, 0, -1):
            lst[0], lst[i] = lst[i], lst[0]
            self.heapify(lst, i, 0)
            
lst1 = [5, 1, 2, 4, 3]
lst2 = [3, 2, 1]
lst3 = [6, 9, 7, 8, 10]
lst4 = [7, 10, 14, 5, 33, 1]
lst5 = [3, 5, 1, 2]
lst6 = [1, 3, -1, 0]
sort = Sorts()

sort.bubble_sort(lst1)
print(lst1)
sort.selection_sort(lst2)
print(lst2)
sort.insertion_sort(lst3)
print(lst3)
print(sort.merge_sort(lst4))
print(sort.quick_sort(lst5))
sort.heap_sort(lst6)
print(lst6)
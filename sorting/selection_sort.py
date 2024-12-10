class Solution:
    def selection_sort_algorithm_asc(self, arr):
        for i in range(len(arr)):
            min_val = min(arr[i:]) #find the minimum element in remaining unsorted array
            min_index = arr.index(min_val)
            arr[i], arr[min_index] = arr[min_index], arr[i] #swap
            
    def selection_sort_algorithm_desc(self, arr):
        for i in range(len(arr)):
            max_val = max(arr[i:])
            max_idx = arr.index(max_val)
            arr[i], arr[max_idx] = arr[max_idx], arr[i]
                
if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    print("Original array is:", arr)
    Solution().selection_sort_algorithm_asc(arr)
    print("Sorted array is:", arr)
    
    
    # Testing for descending order
    arr = [64, 25, 12, 22, 11]
    print("Original array is:", arr)
    Solution().selection_sort_algorithm_desc(arr)
    print("Sorted array is:", arr)
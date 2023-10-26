import sys
sys.path.append('../Algorithms-Tim-Sort/src')
from Algorithms_Tim_Sort import generate_list, timSort, mergeSort

def test_merge_sort():
    temp_list = generate_list(10000)
    temp_list_copy = temp_list.copy()
    temp_list = mergeSort(temp_list)
    temp_list_copy.sort()
    assert temp_list == temp_list_copy

def test_tim_sort():
    temp_list = generate_list(10000)
    temp_list_copy = temp_list.copy()
    timSort(temp_list)
    temp_list_copy.sort()
    assert temp_list == temp_list_copy

print("yes")
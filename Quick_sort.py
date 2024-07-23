def quick_sort(data_list):
    if len(data_list)<=1:
        return data_list
    else:
        pivot=data_list[0]
        lesser=[x for x in data_list[1:] if x<=pivot]
        greater=[x for x in data_list[1:] if x>pivot]
        return quick_sort(lesser)+[pivot]+quick_sort(greater)
l=[40,20,70,50,10,80,30]
l=quick_sort(l)
print(l)
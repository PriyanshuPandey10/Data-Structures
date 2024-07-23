def selection_sort(data_list):
    n=len(data_list)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if data_list[j]< data_list[min_index]:
                min_index=j 
        data_list[i],data_list[min_index]=data_list[min_index],data_list[i]
l=[40,20,70,50,10,80,30]
selection_sort(l)
print(l)
 
def long_cont_sum(arr):
    current_count = max_count = arr[0]
    for num in arr[1:]:
        current_count = max(current_count+num, num)

        max_count = max(current_count, max_count)


    print (max_count)

arr =[1,2,-2,3,4,10,11,24,-12,-5]
long_cont_sum(arr)

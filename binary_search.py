"""
二分查找有序数组
基础：先定义数组的最高
1、先将数组中间位置的值找到
2、将需要查找的值与中间值比对，如果中间值等于要查找的值，直接返回位置
3、如果中间值大于要查找的值 改变high，hign=mid-1（左移查找）
4、如果中间值小于要查找的值 改变low，low=mid+1 （右移查找）
5、直到中间值等于要查找的值直接返回位置
"""
def binary_search(list,item):

    low=0
    high=len(list)-1
    count = 0
    while low <=high:

        '''
        // 为整除法,因为py3中的除法是float除法，所以这里需要用整除法；
         如果是python2，两个int相除，整除法 ，结果为int；
         否则，float除法，结果为float；
        '''
        mid=(low+high)//2
        guess=list[mid]
        if guess == item:
            count=count+1
            return mid,count
        if guess>item:
            count = count + 1
            high=mid-1
        if guess<item:
            count = count + 1
            low=mid+1
    return None
a=[]
for i in range(128):
    a.append(i+4)
print (a)
print(binary_search(a,4))



def binary_search(arr,item):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low +high)//2
        guess=arr[mid]
        if guess==item:
            return mid
        if guess>item:
            high=mid-1
        if guess<item:
            low=mid+1
    return None
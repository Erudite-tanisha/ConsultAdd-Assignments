nums = [1,2,3,4,5,6,7]
k = 3
def rotate( nums, k):
        k = k%len(nums)
        rev(0,len(nums)-1, nums)        
        rev(0,k-1,nums)
        rev(k,len(nums)-1,nums)
        return nums

def rev(start, end, nums):
    i = 0
    while(start<end):
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1
    return nums    

print(rotate(nums,k))
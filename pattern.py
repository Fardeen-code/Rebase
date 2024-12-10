# # for i in range(20,0,-1):
# #     x='*'
# #     x=x*(2*i-1)
# #     print(f'{x:^40}')
# a,b=map(int,input('enter the value:').split())
# print(a,b)
# c=a^b
# print(c)
nums=list(map(int,input().split()))
l=list()
r=list()
for i in range(len(nums)-1):
    if nums[i]>nums[i+1]:
        l=nums[0:i+1]
        r=nums[i+1:len(nums)]
        break
print(l,r)
l=r+l
coun=0
print(l)
for i in range(len(l)-1):
    if l[i]>l[i+1]:
        print('false')
        coun=1
        break
if coun==0:
    print('true')
print('pattern'

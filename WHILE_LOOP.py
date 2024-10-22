# FIBONACCI SERIES
a,b = 0,1
while b<=85:
    print(b)
    a,b=b,a+b
print("done")

# UNION OF TWO LISTS
c=[]
a =[1,2,3,4,5,6,7]
b=[1,0,9,8,6,4,7,3]
c= list(set(a) |set(b))
print(c)

#tuple

tup=[1,2,33,45,6,66,3,1,3.8,"hii"]
print(tup)

#emplty
empty=()
print(empty)


#single
singleTuple=(5,)
print(singleTuple)

#heterogeneous
num=(1,"helloo",8.89,True)
print(num)

#accessing elements
print(tup[0])

print(tup[-1])

print(tup[1:4])

#unpacking

tuplee=(4,5,6)
a,b,c=tuplee
print(a,b,c)


#methods
number=(1,2,3,4,5,6,7,)
print(number.count(1))
print(number.index(3))


t1=(91,4,5)
t2=(5,7,8)
t=t1+t2
print(t)


repeat=t1*3
print(repeat)

#bult in functions

numbb=(6,5,4,3)

print('len',len(numbb))
print('max',max(numbb))
print('min',min(numbb))
print('sum',sum(numbb))

#sorted
name=("sh","aa","bye")
sort=sorted(name)
print(sort)
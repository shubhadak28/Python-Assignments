l=[1,2,3,4,5,6]
result=[i**3 for i in l]

print(result)

res=['even'if n%2==0 else 'odd' for n in range(11)]
print(res)

l1=[5,3,-2,-1]
r=[n if n >=0 else 0 for n in l1]
print(r)


#lambda map() filter()

n=[1,2,3,4,5]

sq=list(map(lambda x:x**2,n))
print(sq)

even=tuple(filter(lambda x:x%2==0,n))
print(even)

odd=tuple(filter(lambda x:x%2!=0,n))
print(odd)
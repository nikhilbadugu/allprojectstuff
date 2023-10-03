# employee_nam="nikhil"
# first= input("enter name ")
# second= input("enter name ")
# print("full name",first,second)
# gopi=(1,"a",True)
# print(gopi)
# print(gopi[2])
# print(len(gopi))
# l1=[1,"nikhil",3.14,True,2+5j]
# print(l1)
# print(type(l1))
# l1[0]=100
# print(l1.pop())
# l1.reverse()
# print(l1)

fruit={"apple":10,"orange":20,"mango":30,"banana":40,"grape":60}
print(type(fruit))  
fruit["apple"]=100
print(fruit)
l1={"apple":10,"orange":20}
l2={"banana":30,"mango":40}
l1.update(l2)
print(l1)

s1={1,"a","a",1}
s1.add("hello World")
s1.update(["abc","jack",3.14])
s1.remove(3.14)
print(s1)
s2={1,2,3,4}
s4={1,2,4,7,8}
s3={"a","b","c","d"}
print(s2.union(s3))
print(s2.intersection(s4))

a=10
b=20
if(a>b):
    print("a is greater ")
else :
    print("b i sgreater")

c=20
d=30
e=40
if(c>d & c>e ):
    print("a is the greatest ")
elif(d>c & d>e):
    print("b is the greatest ")
else:
    print("e is greatest")

tupe1=(1,2,3,4,)
if(6 in tupe1):
    print("6 is present in the tuple") 
else:
    print("6 is not present")
list1=[1,2,3,4,5,]
if(list1[4]==10):
    list1[1]=list1[1]+100
else:
    list1[4]=list1[4]+500
    print(list1)
i=1
while(i<=10):
    print(i)
    i=i+1

# a1=10
# a2=20
# print(a1+a2)
# print(a1==a2)
# a=True
# b=False
# print(b|b)
# Lisa="i am lisa"
# lisa="""this is a staring """
# print(Lisa)
# print(type(lisa))
# my="my name is nikhil"
# print(my[3:7])
# print(my[11:17])

#List 
my_list = ["India",1947,3.14,True,"Subinay",132,9.5,False]
print(my_list)
print(my_list[0])
print(my_list[-1])
print(my_list[-2])
print(dir(my_list))

my_list[1] = "Delhi"
print(my_list)

my_list.remove(True)
print(my_list)

for i in my_list:
    print(i)
    
my_list2 = ['a','c','b']
my_list2.sort()
print(my_list2)




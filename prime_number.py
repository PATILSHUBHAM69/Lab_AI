list1 = [10,11,12,13,14,15]
list_new= []

def prime(num):
  if num > 1:
    for i in range(2,num):
      if num%i==0:
        list_new.append(num)
        print(num,"is not prime number (",i,"times",num//i,"is",num,")")
        break
    else:
        print(num, "is prime number")

for item in list1:
  prime(item)
print("not prime number",list_new)

list1 = [10,11,12,13,14,15]
list_not_prime= []
list_prime= []

def prime(num):
  if num > 1:
    for i in range(2,num):
      if num%i==0:
        list_not_prime.append(num)
        print(num,"is not prime number (",i,"times",num//i,"is",num,")")
        break
    else:
        print(list_prime.append(num), "is prime number")

for item in list1:
  prime(item)
print("not prime number = ",list_not_prime)
print("prime number is = ",list_prime)

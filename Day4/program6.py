n1=int(input("Enter the size of dictionary"))
dict=[]
print("Enter the words of the dictionary")
for i in range(n1):
  dict.append(input("enter the word"+str(i+1) + ": "))

n2=int(input("Enter the size of character list"))
arr=[]
result=[]
for i in range(n2):
  arr.append(input())

for word in dict:
  if set(word).issubset(set(arr)):
     result.append(word)
 
print(", ".join(result)+".")
  

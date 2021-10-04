num_list=[]
n=int(input("Enter the Starting of the range:"))
k=int(input("Enter the Ending of the range:"))
for i in range(n,k):
  num_list.append(i)
print("Original Number List:", num_list)
even_list=[]
odd_list=[]
for i in range(len(num_list)):
  if(num_list[i]%2==0):
    even_list.append(num_list[i])
  else:
    odd_list.append(num_list[i])
print("Even Numbers List:", even_list)
print("Odd Numbers List:", odd_list)
n = len(odd_list)
  
get_sum = sum(odd_list)
mean = get_sum / n
  
print("Mean / Average is: " + str(mean))

n1 = len(odd_list)
odd_list.sort()
  
if n % 2 == 0:
    median1 = odd_list[n//2]
    median2 = odd_list[n//2 - 1]
    median = (median1 + median2)/2
else:
    median = odd_list[n//2]
print("Median is: " + str(median))



n3 = len(odd_list)
  
data = Counter(odd_list)
get_mode = dict(data)
mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]
  
if len(mode) == n:
    get_mode = "No mode found"
else:
    get_mode = "Mode is / are: " + ', '.join(map(str, mode))
      
print(get_mode)

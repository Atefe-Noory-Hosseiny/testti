numbers_list = []
total=0
count=0
largest_number=None
 
while True:
      user_input =input("Enter a number: ")
      if user_input == 'done':
         break
     
      try:
           number =float(user_input)
           numbers_list.append(number)
           total+=number
           count+=1
           average=total/count
           largest_number=max(numbers_list)
           if largest_number%2==0:
                is_even=True
           else:
                is_even=False
         
      except ValueError:
             print("Invalid input")

print(total,"\n",count,"\n",average,"\n", "largest number is even:" ,is_even)


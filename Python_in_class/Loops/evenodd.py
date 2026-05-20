# give a list of integers , count how many are even and odds using single for loop


num = [1,2,34,56,7,8,9]
even_count = 0
odd_count = 0

for n in num:
 if n%2 == 0:
    even_count += 1
 else:
   odd_count += 1

   print(f"even count is {even_count} and odd count is {odd_count}")
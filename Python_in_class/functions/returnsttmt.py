# reutrn statement - getting value back"

def square(n):
    return n ** 2
#return multiple values (tuple unpacking)

def min_max(nums):
    return min(nums), max(nums)


# Return ends the functions immedialtely 

def check_age(age):
    if age<0:
        return "invalid" #exit here
    if age < 18: 
        return "bacchha"
    return "Adult" # only if above two skipped


#using returns

print(sqaure(7))
lo, hi = min_max([1,2,3,4,5,6])
print(f"Min={lo}, Max={hi}")
print(check_age(25))
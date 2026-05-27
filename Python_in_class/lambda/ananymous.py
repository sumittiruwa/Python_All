#lambda with map()

nums = [1,2,3,4,5]
doubled = list(map(lambda x: x*2, nums))
evens = list(filter(lambda x: x%2==0, nums))
print(doubled)
print(evens)

#lambda in mL - custome loss weight

loss_weight = lambda epoch: 1.0 / (1 + 0.1* epoch)
print([round(loss_weight(e),3) for e in range(5)])
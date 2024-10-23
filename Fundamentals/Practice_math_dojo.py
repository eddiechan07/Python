class MathDojo:
    
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        self.result += num + sum(nums)
        return self
    def subtract(self, num, *nums):
        self.result -= num + sum(nums)
        return self

# create an instance:
md1 = MathDojo()
md2 = MathDojo()
md3 = MathDojo()
# to test:
x = md1.add(2).add(2,5,1).add(3,2).result
y = md2.subtract(1).subtract(4,5,2).subtract(7,2).result
z = md3.add(1).add(1,2,1).subtract(8,2).result

print(x)	# should print 15
print(y)	# should print -21
print(z)	# should print -5
# run each of the methods a few more times and check the result!



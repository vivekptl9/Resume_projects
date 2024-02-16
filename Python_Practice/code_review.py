my_init = [1, 2, 3]


class XXX:
    def __init__(self,y, x=my_init):
        self.x = x
        x.append(y)
    def __repr__(self):
        return f'({self.x})'

        
print(f"Original myint: {my_init}")
obj1=XXX(1)
print(f"Object 1 is: {obj1.x}")
print(f"myint after first call: {my_init}")

obj2=XXX([3,5,6])
print(f"Obecjt 2 is: {obj2.x}")
print(f"myint after second call: {my_init}")

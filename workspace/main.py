from executive import executive

print("Welcome to Pysweeper!")
print("Input Board Attributes :)")
print("Width = ")
w = input()
print("Height = ")
h = input()
print("Number of Bombs =")
b = input()

exe=executive(int(h),int(w),int(b))
exe.run()
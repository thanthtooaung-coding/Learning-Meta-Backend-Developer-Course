# class A:
#    a = 1

# class B(A):
#    a = 2

# class C(B):
#    pass

# c = C()
# print(c.a)

# print(issubclass(A,B))
# print(issubclass(B,A))

class A:
	pass
class B(A):
	pass

b = B()
print(isinstance(b,B))
print(isinstance(b,B))
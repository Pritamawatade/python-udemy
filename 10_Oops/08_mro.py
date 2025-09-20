class A:
    label = "A: Base class"
class B(A):
    label = "B: masala blend"
class C(A):
    label = "C: C class"
class D(B,C):
    pass

cup = D()

print(cup.label)
print(D.mro())
print()
print(D.__mro__)
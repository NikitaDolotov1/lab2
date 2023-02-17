class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def m1(self):
        print("Метод 1 из класса А")

    def m2(self):
        print("Метод 2 из класса А")

    def m3(self):
        print("Метод 3 из класса А")


class B(A):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c

    def m3(self):
        print("Метод 3 из класса Б")


class C(A):
    def __init__(self, a="default_a", b="default_b"):
        super().__init__(a, b)

    def m4(self):
        print("Метод 4 из класса С")

    def m5(self):
        print("Метод 5 из класса С")

a = A("a_value", "b_value")
b = B("a_value", "b_value", "c_value")
c = C()
a.m1()
a.m2()
a.m3()
print("==================")
b.m1()
b.m2()
b.m3()
print("==================")
c.m1()
c.m2()
c.m3()
c.m4()
c.m5()
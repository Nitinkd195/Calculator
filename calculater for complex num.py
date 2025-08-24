#calculare for complex num

print("                                         ""COMPLEX NUM CALCULATER")
class complex:
    a="real part offirst num"
    b=" ima.. part of second num"
    c="real part of 2nd num"
    d="ima.. part of second num"



    def com_num(self):
        print(f"The first complex num is C1={self.a}+{self.b}j")
        print()
        print(f"The first complex num is C2={self.c}+{self.d}j")

    def add_com(self):
        A=(self.a+self.c)
        B=(self.b+self.d)
        print(f"The addition of C1 and C2 is C={A}+{B}j ")

    def minus_com(self):
        A = (self.a - self.c)
        B = (self.b - self.d)
        print(f"The substraction of C1 and C2 is C={A}+{B}j ")

    def mul_com(self):
        A=(self.a*self.c)
        B=(self.b*self.d)
        print(f"The multiplication of C1 and C2 is C={A}+{B}j ")

    def devide_com(self):
        A=(self.a/self.c)
        B=(self.b/self.d)
        print(f"The division of C1 and C2 is C={A}+{B}j ")



C=complex()
while True:
    C.a = int(input("real part of first num="))
    C.b = int(input("ima.. part of second num="))
    C.c = int(input("real part of 2nd num="))
    C.d = int(input("ima.. part of second num="))
    print("--------------------------- ")
    C.com_num()
    print()
    user=int(input("for using complex num calculater press 1 "))
    if user==1:
        print()

        a=str(input("chosse your operater between [+,-,*,/] = "))
        print()
        if a=='+':
            C.add_com()
        elif a=='-':
            C.minus_com()
        elif a=='*':
            C.mul_com()
        elif a=='/':
            C.devide_com()
        else:
            print("Invalid operater chosse")

    break















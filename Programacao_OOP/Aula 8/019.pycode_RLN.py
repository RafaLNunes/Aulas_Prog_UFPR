class A:
    def Metodo(self):
        print("\nA.Metodo")
class B(A):
    def Metodo(self):
        print("\nB.Metodo")
        super().Metodo()
class C(A):
    def Metodo(self):
        print("\nC.Metodo")
        super().Metodo()
class D(B, C):
    def Metodo(self):
        print("\nD.Metodo")
        super().Metodo()

def main():
    Objs_A = A()
    Objs_B = B()
    Objs_C = C()
    Objs_D = D()
    
    Objs_A.Metodo()
    Objs_B.Metodo()
    Objs_C.Metodo()
    Objs_D.Metodo()
    
    
if __name__=="__main__":
    main()
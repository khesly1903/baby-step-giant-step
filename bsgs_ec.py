import math
import ec_overF_lib as ecf

def baby_steps(ec,q,P,Q):
    ord_P = ecf.order(ec,q,P)
    m = math.ceil(math.sqrt(ord_P))

    baby_arr = []
    for i in range(0,m):
        R = ecf.addition(ec,q,Q,ecf.double_and_add(ec,q,i,P))
        baby_arr.append(R)



    return baby_arr


def giant_steps(ec,q,P,Q):
    ord_P = ecf.order(ec,q,P)
    m = math.ceil(math.sqrt(ord_P))

    baby_arr = baby_steps(ec,q,P,Q)

    for i in range(1,m):
        R = ecf.double_and_add(ec,q,i*m,P)

        if R in baby_arr:
            j = baby_arr.index(R)
            print(f"i:{i}, j:{j}, m:{m} ")
            return (i * m - j )%q

def main():

    
    #print(giant_steps((33,48),47,(23,7),(27,41)))

    #print(giant_steps((81,384),9833,(16,76),(4079,879)))



    print("""
                           BSGS
                           
                           
     To construct an elliptic curve over a finite field, 
    please provide the parameters a and b for the equation 
                     y^2 = x^3 + ax + b 
              along with the prime number p.
                """)
    a = int(input("a: "))
    b = int(input("b: "))
    ec = (a,b)
    q = int(input("q: "))

    ecf.is_prime(q)
    
    print("""

                    Solve for Q = kP
                    
          """)
    
    x_0 , y_0 = input("P: ").split()
    x_1 , y_1 = input("Q: ").split()

    x_0 = int(x_0)
    y_0 = int(y_0)
    x_1 = int(x_1)
    y_1 = int(y_1)

    P = x_0 , y_0
    Q = x_1 , y_1

    ecf.is_on_curve(ec,q,P)
    ecf.is_on_curve(ec,q,Q)
    
    
    print("""

                       Baby Steps
                    
          """)
    print(baby_steps(ec,q,P,Q))
    
    print("""

                       Giant Steps
                    
          """)

    print(f"k = {giant_steps(ec,q,P,Q)}")


    #https://andrea.corbellini.name/ecc/interactive/modk-mul.html

if __name__ == "__main__":
    main()
    

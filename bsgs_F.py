import math

def is_prime(p):
    if p > 1:
        for i in range(2, (p//2)+1):    
            if (p % i) == 0:
                raise ValueError(f"{p} is not a prime number")
        else:
            True
    else:
        raise ValueError(f"{p} must be positive integer")


def baby_steps(g,h,p):
    m = math.ceil(math.sqrt(p-1))

    baby_step_arr = []

    for i in range(0,m):
        baby_step_arr.append((h * pow(g,i))%p)
    
    return baby_step_arr



def giant_steps(h,g,p):
    m = math.ceil(math.sqrt(p-1))

    baby_steps_arr = baby_steps(g,h,p)

    for i in range(1,m):
        y = pow(g,i*m,p)
        if y in baby_steps_arr:
            j = baby_steps_arr.index(y)
            print(f"i:{i}, j:{j}, m:{m} ")
            return (i * m - j )%p


def main():
    print()
    print("         Solve for h = g^x (mod p)")

    h = int(input("h:"))

    g = int(input("g:"))
    
    p = int(input("p:"))

    is_prime(p)
    
    print()

    print("Baby steps:")
    print(baby_steps(h,g,p))

    # h=12,g=14,p=53,x=12
    # h=124,g=140,p=137,x=93
    #https://asecuritysite.com/encryption/baby?val1=50&val2=11&val3=997

    print()
    print(f"x = {giant_steps(h,g,p)}")

    


if __name__ == "__main__":
    main()

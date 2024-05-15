import math


def baby_steps(g,h,p):
    m = math.ceil(math.sqrt(p-1))

    baby_step_arr = []

    for i in range(0,m):
        baby_step_arr.append((h * pow(g,i))%p)
    
    return baby_step_arr


def gs(h,g,p):
    m = math.ceil(math.sqrt(p-1))

    #baby_step_arr = baby_step(g,x,p)
    
    giant_steps_arr = []
    for i in range(1,m):
        y = (h * pow(g,i*m) * pow(h,-1,p))%p
        giant_steps_arr.append(y)

    return giant_steps_arr
        
def giant_steps(h,g,p):
    m = math.ceil(math.sqrt(p-1))

    baby_steps_arr = baby_steps(g,h,p)

    for i in range(1,m):
        y = (h * pow(g,i*m) * pow(h,-1,p))%p
        if y in baby_steps_arr:
            j = baby_steps_arr.index(y)
            print(f"i:{i}, j:{j}, m:{m} ")
            return (i * m - j )%p


def main():

    print("Solve for h = g^x (mod p)")

    h = int(input("h:"))

    g = int(input("g:"))
    
    p = int(input("p:"))

    print(baby_steps(h,g,p))

    print(f"x: {giant_steps(h,g,p)}")


if __name__ == "__main__":
    main()

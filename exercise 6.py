#snake water gun
m=10
you=0
cpu=0
l=("snake","water","gun")
while(True):
    if m>0:
        n = input("press s for snake, w for water and g for gun\n")
        m=m-1
        import random
        c = random.choice(l)
        if n == "s" and c == "water":
            print("you are winner")
            you = you + 1
            print("attempt remaining ",m,"out of 10\n")
        elif n == "s":
            print("you are defeated")
            cpu = cpu + 1
            print("attempt remaining ", m, "out of 10\n")
        elif n == "w" and c == "snake":
            print("you are defeated")
            cpu = cpu + 1
            print("attempt remaining ", m, "out of 10\n")
        elif n == "w":
            print("you are winner")
            you = you + 1
            print("attempt remaining ", m, "out of 10\n")
        elif n == "g" and c == "snake":
            print("you are winner")
            you = you + 1
            print("attempt remaining ", m, "out of 10\n")
        elif n=="g":
            print("you are defeated")
            cpu = cpu + 1
            print("attempt remaining ", m, "out of 10\n")
        else:
            print("check your input and try again\n")
            print("attempt remaining ", m, "out of 10\n")

    else:
        print("tournament over, here are the results\n")

        break
print("cpu won ",cpu,"times")
print("you won ",you,"times")
if cpu>you:
    print("So,you lost in this tournamment")
elif you>cpu:
    print("Congratulations :you won in this tournamment")
else:
    print("No winner")

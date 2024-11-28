import random
counter=0
while True:
    opt=input("Roll the die?(yes/no): ").lower()
    if opt=="yes":
        d1=random.randint(1,6)
        d2=random.randint(1,6)
        print(f'you rolled a {d1} and a {d2}')
        counter+=1
    elif opt=="no":
        print("Thanks for playing!")
        break
    else:
        print("invalid choice")
print(f"You have rolled the die {counter} times this session")
import random 
a = random.randint(0,100000)
print("Welcom to lucky draw")
print()
b=int(input("Please choose any number between 0 to 100 and if it matches lucky draw no. you win: "))
print()
print("Wining No. :",a)
print("Your No. :",b)
print()
if(a==b):
    print("You Win")
else:
    print("Better Luck Next Time")
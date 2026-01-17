No = 11 #Global (also called - Data Definition Statement)

def fun():
    global No
    print("value of no from fun is :", No)      #11
    No = No + 1     #12
    print("value of no from fun is :", No)      #12

print("valuue of No is :", No)      #11
fun()
print("valuue of No is :", No)      #12
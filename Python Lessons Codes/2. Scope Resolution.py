# LEGB = Local -> Enclosed -> Global -> Built-in

# any built in variable hold the Least Priority 
var = 5 # Global 
print(var)
def randomfnc1():
    var = 10 # Enclosed
    print(var)
    def randomfnc2():
        var = 15 #Local
        print(var)
    randomfnc2()
randomfnc1()
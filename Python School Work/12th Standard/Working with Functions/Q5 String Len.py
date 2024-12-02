def str_len(a,b):
    a_len, b_len = len(a), len(b)
    if a_len==b_len:
        return True
    else:
        return False
    
a = input("Input 1st String: ") 
b = input("Input 2nd String: ") 
print(str_len(a,b))
#exceptions
def main():
    x=get_int()
    print(f"x is {x}")
 
  
def get_int(prompt):
  
    while True:
        try:
            #return int(input("what's x? "))
            return int(input("prompt"))
          #"break" you can implement it here as well 
 
        except ValueError:
            pass
            #print("x is not an integer")
        #else:
            # return x
main()
#print(f"x is {x}")
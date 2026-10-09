import sys
#try:
#check for errors
if len(sys.argv)<2:
  sys.exit("Too few arguments")
elif len(sys.argv)>2:
  sys.exit("Too many arguments")
# else:
#print name tags
print("hello, name is", sys.argv[1])
#except IndexError:
    #print("Too few arguments")

for arg in sys.arg: 
  print("hello, my name is", arg) # this gives $ python name.py David Carter Rongxin
#hello, my name is name.py
#hello, my name is David
#hello, my name is Carter
#hello, my name is Rongxin

#slices this is going to remove the hello, my name is name.py
for arg in sys.arg[1:]:
  print("hello my name is",arg)

for arg in sys.arg[1:-1]:
  print("hello my name is",arg)
#output:hello, my name is Carter
#hello, my name is Rongxin


#4
import sys
if len(sys.argv)<2:
    sys.exit("less arguments")
#elif len(sys.argv)>2:
    #sys.exit("much arguments")

#print("how was your day",sys.argv[1] ,"?")

#5
for arg in sys.argv[1:]:
    print("how was your day",arg,"?")



#name=input("what's your name?")
    #open 
#with open("names.txt", "") as file:
 #   file.write(f"{name}\n")
    #read file
#with open("names.txt", "r") as file:
 #   lines = file.readlines()
  #  for line in lines:
   #     print(f"hey, {line. strip()}")

names=[]
with open("names.txt") as file:
    for line in file:
        names.append(line.strip())

for name in sorted(names):
    print(f"hey, {name}!")
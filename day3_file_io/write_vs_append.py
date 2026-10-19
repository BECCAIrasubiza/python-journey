

with open("demo.txt", "w") as f:
    f.write("first\n")
with open("demo.txt", "w") as f:      # "w" again -> "first" is ERASED
    f.write("second\n")
with open("demo.txt") as f:
    print("After two 'w' writes:", f.read().split())

with open("demo.txt", "a") as f:      # "a" -> "second" is KEPT
    f.write("third\n")
with open("demo.txt") as f:
    print("After one 'a' write: ", f.read().split())

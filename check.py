def chkpass():
 rp=input("set your password: ")
 atp=0
 matp=10
 while atp<matp:
  p=input("enter your password: ")
  atp+=1
  if p == rp:
   print("success")
   print(atp)
   return
  else:
   rm=matp-atp
   print("wrong password")
   if rm>0:
    print("you have ", rm, "attemps left")

 print("you have used all your attemps ")
 print("access denied")

chkpass()

# the hacker enters the type of pasword he wants to hack


print( " all paswords must be 12 digits ")
print( "1 : word and numbers :")
print( "2 : numbers  : ")
print( "3 : combined :")
print( " words only (uppercase and lowercase)")
u = int(input(" which type of password do u wonna crack"))

if u == 1:
     import datetim
     import random
     import sys
     d = input( " ENTER THE PASWORD :")
     print( "WELCOME TO  𝕽𝖀𝕱𝖀𝕾 𝕸𝕭𝖀𝕽𝖀 𝕻𝕬𝕾𝕾𝖂𝕺𝕽𝕯 𝕮𝕽𝕬𝕮𝕶𝕰𝕽 ")
     todays_date = datetime.datetime.now()
     print( " cracking started at ---" , todays_date , " ----------")
     print( "-" * 40)
     print( " -" * 30)
     print( " - " * 20)
     while True:
       
       
       
        
        
        
        
        
        
        
        c = " qwertyuiopasdfghjklzxcvbnm"
        f = " 1234567890"
        length = len(d)
        pas = c + f
        password = "".join(random.sample(pas,length))
        print(password)
        if password == d :
            print(" succesfully cracked  ---------")
            end = datetime.datetime.now()
            print( " craked at " , end)
            print(" your pasword is " , password)
            sys.exit()
elif u == 2 :
    import datetime 
    import random
    import sys
    print("ＲＵＦＵＳ░ＰΛＳＳＣ♢ＤΞ░ＣＲΛＣＫΞＲ　（映さッ） ")
    e = input(" Enter passcode : ")
    res = datetime.datetime.now()
    print(" started at " , res)
    print("-" * 50)
    print("_" * 40)
    y = "1234567890"
    t = "0987654321"
    k = len(e)
    r = y + t
    o = "".join(random.sample(k ,r))
    print(o)
    if e == 0:
        pizza = datetime.datetime.now()
        print(" cracked at  " ,pizza ) 
        print(" succefully cracked !!!!!!: ")
        print(" you passcode is " , o)
        sys.exit()
elif u == 3 :
    try:
        while True:
            import datetime
            import sys
            casp = input(" enter   combined pasword with special symbol : ")
            print(" 🆆🅴🅻🅲🅾🅼🅴 🆃🅾 🆁🆄🅵🆄🆂 🅼🅱🆄🆁🆄 🅿🅰🆂🆆🅾🆁🅳 🅲🆁🅰🅲🅺🅴🆁 ")
            dy =datetime.datetime.now()
            print(" started at " , dy )
            a = " qwertyuiopasdfghjklzxcvbnm"
            d = " QWERTYUIOPASDFGHJKLZXCVBNM"
            e = " 1234567890"
            z = " ~`!@#$%^&*()[]{}\|;:'<>/ +=_-"
            er = a + d + e + z 
            d = len(casp)
            passe = "".join( random.sample(er,d))
            print(passe)
            if passe == casp :
                end = datetime.datetime.now()
                print(" succesfully cracked at  ",end )
                print( " your pasword is  , " , passe)
    except KeyboardInterrupt:
        print("." * 50)
        print(" ." * 40)
        print(" fuck proces stoped byyyyyyyyeeeee !  ")
else :
    print(" fuction not available ")
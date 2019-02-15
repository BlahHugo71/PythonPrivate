print ("Hi")
print ("What's your name?")
name = input()
print ("Hello. It's a pleasure to meet you,", name)
print ("Hmm. I'm wondering how old you are. Would you care to tell me? (yes/no)")
old = input()
if old == "yes":
    print ("Well, how old are you?")
    age = input()
    print (."Interesting. So, next year you're going to be", str(int(age)+1), "years old, right?")
else:
    print ("Do you like bananas? (yes/no)")
    likeBananas = input()
    if likeBananas == "yes":
        print ("Then you're probably a Minion!")
    else:
        print ("Fine. I'll eat the banana.")
        
   

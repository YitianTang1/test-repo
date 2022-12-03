#Serena Tang
#04/23/2021
#M.W 3:30pm
#Assignment9


# function called valid_username
def valid_username(String):
    check=0
    a="False"
    #(1)check to see if 5 characters long
    if len(String)>=5:
        check+=1
    else:
        a="False"
    
    #(2)check if alphanumeric only
    s=0
    for i in String:
        if (ord(i)>=38 and ord(i)<=57) or (ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122):
            s+=1
        else:
            a="False"
        
    if s==len(String):
        check+=1

    #check to if the first character is a letter
    try:
        o=ord(String[0])
    except:
        a="False"
    else:
        if (o>=65 and o<=90) or (o>=97 and o<=122):
            check+=1
        else:
            a="False"

    #check to see if it's true
    if check==3:
        a="True"
    else:
        a="False"

    return a

"""
print( valid_username('abc123') )    # True
print( valid_username('abcde')  )    # True
print( valid_username('abc')    )    # False
print( valid_username('@#$%^')  )    # False
print( valid_username('1abcde') )    # False
print( valid_username('')       )    # False
"""


#valud pass_word
def valid_password(String):
    check=0
    a="False"
    #(1)check to see if 5 characters long
    if len(String)>=5:
        check+=1
    else:
        a="False"
    
    #(2)check if alphanumeric only
    s=0
    for i in String:
        if (ord(i)>=38 and ord(i)<=57) or (ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122):
            s+=1
        else:
            a="False"
        
    if s==len(String):
        check+=1

    #check to see if contain at least one uppercase
    u=0
    l=0
    n=0
    for i in String:
        #upper
        if ord(i)>=65 and ord(i)<=90:
            u+=1
        #lower
        if ord(i)>=97 and ord(i)<=122:
            l+=1
        #number
        if ord(i)>=48 and ord(i)<=57:
            n+=1
    if u>=1 and l>=1 and n>=1:
        check+=1

    if check==3:
        a="True"

    return a
        
"""         
print( valid_password('Abc123')     )   # True
print( valid_password('Abc123xyz')  )   # True
print( valid_password('Ab12')       )   # False
print( valid_password('abc123')     )   # False
print( valid_password('123456')     )   # False
print( valid_password('Abc123#')    )   # False
print( valid_password('')           )   # False
"""

#function username_exists
def username_exists(String):
    a="False"
    #OPEN THE FILE
    connection=open("user_info.txt","r")
    data=connection.read()
    connection.close()
    #split the text into a list
    List=data.split("\n")
    
    for i in List:
        I=i.split(",")
        if I[0]==String:
            a="True"
        if I[0]==String=="":
            a="False"
    return a

"""
print( username_exists('pikachu')           )   # True
print( username_exists('charmander')        )   # True
print( username_exists('squirtle')          )   # True
print( username_exists('Pidgey2020')        )   # True
print( username_exists('SquirtleSquad99')   )   # False
print( username_exists('eevee')             )   # False
print( username_exists('bobcat')            )   # False
print( username_exists('')                  )
"""

#function check_password
def check_password(name,password):
    #OPEN THE FILE
    connection=open("user_info.txt","r")
    data=connection.read()
    connection.close()
    List=data.split("\n")
    if username_exists(name)=="True":
        for i in List[0:-1]:
            I=i.split(",")
            if I[0]==name:
                if I[1]==password:
                    return "True"
                else:
                    return"False"
    else:
        return "False"
    
"""
print( check_password('pikachu', 'Abc123')              )    # True
print( check_password('squirtle', 'SquirtleSquad99')    )    # True
print( check_password('fearow', 'Pqr123')               )    # False
print( check_password('foobar', 'Hello123')             )    # False
print( check_password('', '')                           )    # False
"""
    
#function add_user
def add_user(name,password):
    if username_exists(name)=="False":
        if valid_username(name)=="True":
            if valid_password(password)=="True":
                #open the file for writing
                Set=name+","+password
                new=open("user_info.txt","a")
                new.write(Set)
                new.write("\n")
                new.close()
                return "True"
            else:
                return "False"
        else:
            return "False"
    else:
        return "False"


#function send_messages
def send_message(sender,recipient,message):
    
    file_name=recipient+".txt"
    import datetime
    d=datetime.datetime.now()
    month=d.month
    day=d.day
    year=d.year
    hour=d.hour
    minute=d.minute
    second=d.second
    file=open("messages/"+file_name,"a")
    d=sender+"|"+str(month)+"/"+str(day)+"/"+str(year)+" "+str(hour)+":"+str(minute)+":"+str(second)+"|"+message+"\n"
    file.write(d)
    file.close()
    


#function print_messages
def print_message(username):
    file="messages/"+username+".txt"
    connection=open(file,"r")
    data=connection.read()
    connection.close()
    Lines=data.split("\n")
    num=1
    for i in Lines[0:-1]:
        d=i.split("|")
        print("Message #"+str(num)+" received from "+d[0])
        print("Time:",d[1])
        print(d[2])
        print()
        num+=1

print_message("charmander")

#delete message
def delete_messages(username):
    file="messages/"+username+".txt"
    connection=open(file,"w")
    connection.write("")
    connection.close

    
#part3f
A="good"
while A=="good":
    user_input=str.lower(input("(l)ogin, (r)egister or (q)uit:"))
    print()
    if user_input=="r":
        print("Register for an account")
        Username=input("Username (case sensitive): ")
        Password=input("Password (case sensitive): ")
        check1=valid_username(Username)
        check2=valid_password(Password)
        check3=username_exists(Username)
        if check1=="True" and check2=="True" and check3=="False":
            add_user(Username,Password)
            admin="admin"
            message="Welcome to your account!"
            send_message(admin,Username,message)
            print("Registration successful!")
        elif check1=="False":
            print("Username is invalid,registration cancelled")
        elif check2=="False":
            print("Password is invalid, registration cancelled")
        elif check3=="True":
            print("Duplicate username, registration cancelled")
        print()
    
    elif user_input=="l":
        print("Log in")
        Username=input("Username (case sensitive): ")
        Password=input("Password (case sensitive): ")
        if check_password(Username,Password)=="True":
            while True:
                print("You have been logged in successfully as",Username)
                choice=str.lower(input("(r)ead messages, (s)end a message, (d)elete messages or (l)ogout:"))

                if choice=="r":
                    file="messages/"+Username+".txt"
                    connection=open(file,"r")
                    data=connection.read()
                    connection.close()
                    if len(data)==0:
                        print()
                        print("No messages in your inbox")
                        print()
                    else:
                        print()
                        print_message(Username)
                    
                elif choice=="s":
                    recipient=input("Username of recipient: ")
                    if username_exists(recipient)=="False":
                        print("Unknown recipient")
                        print()
                    else:
                        message=input("Type your message: ")
                        send_message(Username,recipient,message)
                        print("Message sent!")
                        print()
                        
                elif choice=="d":
                    delete_messages(Username)
                    print("Your messages have been deleted")
                    print()
                elif choice=="l":
                    print("Logging out as username",Username)
                    print()
                    break
        else:
            print("Your usernmae or password is invalid,try again")
            print()

    elif user_input=="q":
        print("Goodbye!")
        A="Bad"
    
                    

        
        
        
        
        
    
    
    


    
    





    

    
    

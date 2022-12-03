#Serena Tang
#2021.04.21
#M.W 3:30 Section
#Assignment9 part2

#get data from the quizzes.txt file
connection=open("quizzes.txt","r")
alldata=connection.read()
connection.close()
alldata_list=alldata.split("\n")






#use while loop
Valid="True"
while Valid=="True":
    #print the menu
    print("NYU Quizzing System - Main Menu")
    choice=str.lower(input("(q)uiz info, (s)core a file or (e)xit: "))
    #if the user choice is equal to q
    List=[]
    if choice=="q":
        num=0
        for i in alldata_list:
            num+=1
        print("There are",num,"quizzes available")
        for i in alldata_list:
            item=i.split(",")
            print('"'+item[0]+'"'+' has '+str(len(item[1]))+' questions')
        print()

    elif choice=="s":
        filename=str.lower(input("Enter a filename to score: "))
        #try to open
        try:
            quiz=open(filename,"r")
            
        except:
            print("File not found.")
            print()

        else:
            data=quiz.read()
            quiz.close()
            data_line=data.split("\n")
            #student_num
            num=0
            for i in data_line:
                for y in i:
                    if "N" in y:
                        num+=1  
            print("This file contains "+str(num)+" student entries for the test "+'"'+data_line[0]+'"')
            #get the answer key
            for i in alldata_list:
                a=i.split(",")
                if a[0]==data_line[0]:
                    answer=a[1]
            print("The answer key for this test is:",answer)
            #get the scoring
            List=[]
            for i in data_line:
                b=i.split(",")
                if len(b)==2:
                    ID=b[0]
                    Answer=b[1]
                    Total=len(Answer)
                    correct=0
                    for y in range(Total):
                        if Answer[y]==answer[y]:
                            correct+=1
                    List+=[correct]
                    #calculate the percentage correct
                    fraction=correct/Total
                    percentage="{:.2%}".format(fraction)
                    print(ID+" earned "+str(correct)+" out of "+str(Total)+" ("+percentage+")")
            #calculate the average score
            total=0
            for i in List:
                total+=int(i)
            average=total/num
            average=format(average,".2f")
            Highest=max(List)
            Lowest=min(List)
            Range=Highest-Lowest
            print()
            print("*** Class Report ***")
            print("Average score:",average)
            print("Highest score:",Highest)
            print("Lowest score:",Lowest)
            print("Range of scores:",Range)
            #calculate the mode
            Listnew=[]
            for i in List:
                new=List.count(i)
                Listnew+=[new]
            
            

            #get the maximum of the list
            Maximum=max(Listnew)
            Mode=[]
            for i in List:
                Index=List.index(i)
                if Listnew[Index]==Maximum:
                    if Mode.count(i)<1:
                        Mode+=[i]
                    
            print("Mode(s): ",end="")
            for i in Mode:
                print(str(i)+" ",end="")
            print()
            for i in [0,1,2,3,4,5,6,7,8,9,10]:
                try:
                    Index=List.index(i)
                    Repe=Listnew[Index]
                except:
                    print(format(str(i),">2s"))          
                else:
                    if Repe>0:
                        print(format(str(i),">2s"),"*"*Repe)
                    else:
                        print(format(str(i),">2s"))
            print()
                    
                
            
                
                                
                         

    elif choice=="e":
        print("Goodbye!")
        Valid="False"

    else:
        print("Unknown command,please try again")
        print()

    
        
        
        

#Serena Tang
#04.21.2021
#M.W 3:30 section
#Part 1


#print the heading
print("NYU Computer Science Registration System")

#open the class_data file for reading
class_open=open("class_data.txt","r")
#read in all data as one long string
class_data=class_open.read()
#close the file
class_open.close()
class_data_list=class_data.split("\n")

#open the enrollment_data for read
enrollment_open=open("enrollment_data.txt","r")
#read in all data as one long String
enrollment_data=enrollment_open.read()
#cloase the file
enrollment_open.close()
enrollment_data_list=enrollment_data.split("\n")


#ask the user for course id
course_id=str.upper(input("Enter a course ID (i.e. CS0002, CS0004): "))
#
check="False"

for i in class_data_list:
    ID=i.split(",")
    if course_id==ID[0]:
        print("The title of this class is",ID[1])
        check="True"
        num=0
        for z in enrollment_data_list:
            name=z.split(",")
            if course_id==name[0]:
                num+=1
        print("The course has",num,"students enrolled")

        for y in enrollment_data_list:
            name=y.split(",")
            if name[0]==course_id:
                print("* "+name[1]+","+name[2])
                 
            
   
if check=="False":
    print("Cannot find this course")
   
        
        
    
    
        
    
    

    
    

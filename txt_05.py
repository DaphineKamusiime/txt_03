print("1)Create a new file\n 2)Display the file\n3)Add a new item to the file\n")
selection=int(input(("Make a selection 1,2 or 3")))
if selection==1:
    subject=input("enter school subject\n")
    file=open("Subject.txt","w")
    file.write(subject+"\n")
    file.close()
elif selection==2:
    file=open("Subject.txt","r")
    print(file.read())
elif selection==3:
    file=open("Subject.txt","a")
    new_sub=input("enter new subject")
    file.write(new_sub +"\n")
    file.close()
    file=open("Subject.txt","r")
    print(file.read())
    
else:
    print("wrong input")

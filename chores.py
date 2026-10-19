#part1 total no of chores
total_chores=4
orignalcount=total_chores
print('no. of chores to do:',orignalcount)

#part2 counter for completed chores
completedcount=0
chorenum=1

#part3 repeat while
while chorenum<=total_chores:
    #part 4 workout the chore
    if chorenum==1:
        nextchore="make your bed"
    elif chorenum==2:
        nextchore="feed your pet"
    elif chorenum==3:
        nextchore="take out the trash"
    else: 
        nextchore="wash the dishes"

    ans=input(f"have u finished {nextchore} yes/no:")          
    #part5 move to next chore if done 
    if ans=="yes":
        completedcount+=1
        chorenum+=1
        print("chore completed.")
    else:
        print("finish chore and check again.")
    print("chore remaining=",total_chores-completedcount)       
print("All chores completed")      
print('Chores assigned=',orignalcount)
print("Chores completed=",completedcount)
print("chore remaining=",total_chores-completedcount)
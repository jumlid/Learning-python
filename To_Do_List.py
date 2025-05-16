import os
user_Data=[]
def start():
    print('Press the cammand given below to perform the task u want')
    print('1 view    2 delete')
    print('3 Add')
    user_input=int(input())
    if user_input==1:
      os.system('clear')
      print('View')
      i=0
      for u in user_Data:
          i+=1
          print(i,u)
      
    elif user_input==2:
      os.system('clear')
      print('Delete')
      i=0
      for u in user_Data:
          i+=1
          print(i,u)
      print('enter the number of the list you want to delete')
      r=int(input())
      user_Data.pop(r-1)    
      
      start()
    elif user_input==3:
      os.system('clear')
      print('Enter the stuff u want to add')
    user_Data.append(str(input()))
  
    start()
    
    

    
start()   

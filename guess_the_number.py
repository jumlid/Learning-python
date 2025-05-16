import random
n=0
user=0
def generate():
    global n
    n=random.randint(0,100)

def ask():
       
        generate()
        print(n)
    
        global user
        print('guess the number')
        user=int(input())
        if user > n:
            print('To high')
            ask()
        elif user <n:
            print('To low')
            ask()
        elif user ==n:
            print('yes!!!!!!!')        
            ask()
            
        
    
ask()
        


      
            
    

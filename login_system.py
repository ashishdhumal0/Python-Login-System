
#1. ask user do you have any account 
#2. accept email,username,password 
#3. check the password
#4. store all in text file 
#5. if you have account then check password from text file


class UserIp():

    def acc_ip(self):
        
        print("welcome...")

        ask = input("do you have account ? y or n : ")

        if ask == "n":
            
            while True:
                
                email = input('Enter Email Address: ')
        
                uname = input('Enter Username: ')
        
                passw1 = input('Enter Password: ')
        
                passw2 = input('Enter Password again:')

                if passw1 == passw2:
                    
                    print('login successful')
                    f = open(uname+".txt","w")
                    f.write(email+":"+uname+":"+passw1)
                    f.close()
                    break
                    
                else:
                    
                    print('login unsuccessful please login again')
    
        if ask == "y":

                while True:
                    try:     
                        us = input("Username : ")

                        p1 = input("Password : ")

                        f1 = open(us+".txt","r")
                        data=f1.readline()
                        
                        f1.close()

                        if data == us+":"+p1:
                            
                            print("login successful")
                            break
            
                    except FileNotFoundError:
                        print("Login Unsuccessful please login again")

u = UserIp()
u.acc_ip()









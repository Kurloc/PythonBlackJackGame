import time

class PlayerBank():
    username = ''
    password = ''
    def __init__(self):
        pass
    
    def register_andor_login(self):       
        creating_username = True
        playercash2 = []
        usernamelist = []
        passwordlist = []
        counter = 0
        while True:
            try:
                logging_in_variable = input('Enter 1 to Login, or 2 to create an account!')
                int(logging_in_variable) * int(logging_in_variable)
            except:
                pass
            else:
                break
            
        while creating_username == True:
            for zzz in range(100): print('\n')
            print('Please Input Your Username')
            username = input('Username: ')
            print('Please Input Your Password')
            password = input('Password: ')
            userstring = '\n' + username + '|' + password
            userlistfile = open('Userlist.text', 'r')
            dick = userlistfile.read()
            newdick = dick.split("\n")
            for z in newdick:
                if z == '':
                    pass
                else:
                    counted =+ 1
                    douche = z.split('|')[0]
                    oldcash = z.split('|')[2]
                    passwordlist.append(z.split('|')[1])
                    usernamelist.append(douche)

            if username in usernamelist:
                print()
                if int(logging_in_variable) == 1:
                    if password in passwordlist:
                        print("LOGGING IN!")
                        playercash = str(newdick[usernamelist.index(username)]).split('|')
                        time.sleep(1)
                        return playercash
                        break
                    else:
                        print('Login Failed!')
                        time.sleep(1)
                if int(logging_in_variable) == 2:
                    print('Username Taken')
                    time.sleep(1)
            else:
                    print('Account Created!')
                    userlistfile = open('Userlist.text','a')
                    userstring = userstring + '|500'
                    userlistfile.write(str(userstring))
                    userlistfile.close()
                    creating_username == False   
                    break 
                
        return username, password
    
    def get_current_player_cash(self, username, password):
        creating_username = True
        playercash2 = []
        usernamelist = []
        passwordlist = []
        counter = 0
            
        userstring = '\n' + username + '|' + password
        userlistfile = open('Userlist.text', 'r')
        dick = userlistfile.read()
        newdick = dick.split("\n")
        for z in newdick:
                if z == '':
                    pass
                else:
                    counted =+ 1
                    douche = z.split('|')[0]
                    oldcash = z.split('|')[2]
                    passwordlist.append(z.split('|')[1])
                    usernamelist.append(douche)

        if username in usernamelist:
                    playercash = str(newdick[usernamelist.index(username)]).split('|')
                    time.sleep(1)
                    return playercash
                
    def save_player_cash(self, username2, password, cash):
        creating_username = True
        playercash2 = []
        usernamelist = []
        passwordlist = []
        cashlist= []
        counter = 0
            
        userstring = '\n' + username2 + '|' + password
        userlistfile = open('Userlist.text', 'r')
        dick = userlistfile.read()
        newdick = dick.split("\n")
        for z in newdick:
            if z == '':
                pass
            else:
                counted =+ 1
                douche = z.split('|')[0]
                oldcash = z.split('|')[2]
                passwordlist.append(z.split('|')[1])
                usernamelist.append(douche)
                cashlist.append(oldcash)

        if username2 in usernamelist:
                    if username2 == '' or username2 == '\n':
                        pass
                    else:
                        derp2 = username2 +'|'+password+'|'+cashlist[usernamelist.index(username2)]
                        playercash = cashlist[usernamelist.index(username2)]
                        time.sleep(1)
                        newdick.append(playercash)
                        pad = ''
                        pad2 = ''
                        userlistfile = open('Userlist.text', 'r') 
                        derp3 = username2 +'|'+password+'|'+ str(cash)
                        contents = (userlistfile.readlines())
                        popme = (newdick.index(derp2))
                        contents.pop(popme)
                        contents.append(derp3)
                        userlistfile = open('Userlist.text', 'w')
                        for xxx in contents:
                            pad = xxx
                            pad2 = pad2 + pad
                            
                        userlistfile.write("\n".join(str(item) for item in contents if item != '\n'))
                        userlistfile.close()
                        return derp3      
        
          
                    
b = PlayerBank()

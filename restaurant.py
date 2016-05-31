from internetrestaurant import *

#global
loopFlag = 1 # 루프 제어 변수
###############

#Menu(console)

def PrintMenu():
    print('=====RestaurantMenu=====')
    print('1.PrintAll : a ')
    print('2.SearchKeyword : k ')
    print('3.SearchPosition : p ')
    print('4.SendEMail : e ')
    print('5.QuitProgram : q ')
    
def launcherFunction(menu):
    if menu == 'a':
        getRestaurantDataForList()    
    elif menu == 'k':
        Keyword = str(input ('input keyword to search :'))
        getRestaurantDataFromKeyword(Keyword)
    elif menu == 'p':
        inputX = str(input('input X :'))
        inputY = str(input('input Y :'))
        getRestaurantDataFromContent(inputX,inputY)
    elif menu == 'e':
        sendMain()
    elif menu == 'q':
        QuitRestaurantkMgr()
        
def QuitRestaurantkMgr():
    global loopFlag
    loopFlag = 0
    RestaurantFree()
        
##### run #####
while(loopFlag > 0):
    PrintMenu()
    menuKey = str(input ('select menu :'))
    launcherFunction(menuKey)
else:
    print ("Thank you! Good Bye")
     
     

import sys

from PyQt4 import QtCore, QtGui
from http.client import HTTPConnection

##global
conn = None
word = None
Positionret = []
ret = []
###################

# smtp 정보
host = "smtp.gmail.com" # Gmail SMTP 서버 주소.
port = "587"


regKey = "3n0ay%2Fk%2BocRtQBOiPEJNJ7hJNqBuoC1%2F2d%2BQY7GDxFynWHRxFJJM2Hm1MYFTyoe%2BVswgU6XVD%2BuDqwrOXOVUjA%3D%3D"
server = "api.visitkorea.or.kr"

# 키워드로 구하는 url #
def userURIBuilderKeyword(server,**user):
    str = "http://" + server+"/openapi/service/rest/KorService/searchKeyword?"
    for key in user.keys():
        str += key +"=" + user[key]+"&"
    return str
    
# 좌표로 구하는 url #
def userURIBuilderPosition(server,**user): # ** 사전 형식으로 받는다
    #str = "http://" + server + "/search" + "?"
    str = "http://" + server + "/openapi/service/rest/KorService/locationBasedList?"
    for key in user.keys():
        str += key + "=" + user[key] + "&"
    return str
    
def connectOpenAPIServer():
    global conn, server
    conn = HTTPConnection(server)

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(1450, 1000)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(575, 40, 300, 100))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("휴먼모음T"))
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.ClosepushButton = QtGui.QPushButton(Form)
        self.ClosepushButton.setGeometry(QtCore.QRect(1280, 920, 160, 70))
        
        
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("휴먼모음T"))
        font.setPointSize(10)
        self.ClosepushButton.setFont(font)
        self.ClosepushButton.setObjectName(_fromUtf8("ClosepushButton"))
        
        
        self.stackedWidget = QtGui.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(49, 139, 1381, 771))
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        
        
        self.Keyword_pushButton = QtGui.QPushButton(self.page)
        self.Keyword_pushButton.setGeometry(QtCore.QRect(560, 100, 230, 100))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("휴먼모음T"))
        font.setPointSize(11)
        self.Keyword_pushButton.setFont(font)
        self.Keyword_pushButton.setObjectName(_fromUtf8("Keyword_pushButton"))
        
        
        
        
        self.Position_pushButton = QtGui.QPushButton(self.page)
        self.Position_pushButton.setGeometry(QtCore.QRect(560, 270, 230, 100))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("휴먼모음T"))
        font.setPointSize(11)
        self.Position_pushButton.setFont(font)
        self.Position_pushButton.setObjectName(_fromUtf8("Position_pushButton"))
        
        
        
        self.Email_pushButton = QtGui.QPushButton(self.page)
        self.Email_pushButton.setGeometry(QtCore.QRect(560, 450, 230, 100))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("휴먼모음T"))
        font.setPointSize(11)
        self.Email_pushButton.setFont(font)
        self.Email_pushButton.setObjectName(_fromUtf8("Email_pushButton"))
        
        
        ##keyword menu
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.label_5 = QtGui.QLabel(self.page_2)
        self.label_5.setGeometry(QtCore.QRect(520, 40, 350, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("휴먼모음T"))
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        
        
        self.keyword_Edit = QtGui.QLineEdit(self.page_2)
        self.keyword_Edit.setGeometry(QtCore.QRect(535, 110, 300, 100))
        self.keyword_Edit.setObjectName(_fromUtf8("keyword_Edit"))
        
        self.keyword_Edit.returnPressed.connect(self.getRestaurantDataFromKeyword)
        
        
        self.tableWidget = QtGui.QTableWidget(self.page_2)
        self.tableWidget.setGeometry(QtCore.QRect(55, 240, 1250, 500))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(30)
        
        self.tableWidget.setColumnWidth(0,380)
        self.tableWidget.setColumnWidth(1,380)
        self.tableWidget.setColumnWidth(2,380)

        for i in range(30):
            self.tableWidget.setRowHeight(i,50) 
            
        columns = ['가게명','주소','전화번호']
        self.tableWidget.setHorizontalHeaderLabels(columns)
        
        
        self.HomepushButton_key = QtGui.QPushButton(self.page_2)
        self.HomepushButton_key.setGeometry(QtCore.QRect(1110, 20, 187, 60))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("휴먼모음T"))
        self.HomepushButton_key.setFont(font)
        self.HomepushButton_key.setObjectName(_fromUtf8("HomepushButton_key"))
        
        
        self.stackedWidget.addWidget(self.page_2)
        
        self.page_5 = QtGui.QWidget()
        self.page_5.setObjectName(_fromUtf8("page_5"))
        self.label_7 = QtGui.QLabel(self.page_5)
        self.label_7.setGeometry(QtCore.QRect(520, 40, 320, 90))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("휴먼모음T"))
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        
        
        
        self.position_lineEdit = QtGui.QLineEdit(self.page_5)
        self.position_lineEdit.setGeometry(QtCore.QRect(540, 120, 270, 100))
        self.position_lineEdit.setObjectName(_fromUtf8("position_lineEdit"))
        self.position_lineEdit.returnPressed.connect(self.getRestaurantDataFromContent) 
        
        
        
        self.tableWidget_2 = QtGui.QTableWidget(self.page_5)
        self.tableWidget_2.setGeometry(QtCore.QRect(70, 250, 1250, 500))
        self.tableWidget_2.setObjectName(_fromUtf8("tableWidget_2"))
        self.tableWidget_2.setColumnCount(4)
        self.tableWidget_2.setRowCount(70)
        
        self.tableWidget_2.setColumnWidth(0,300)
        self.tableWidget_2.setColumnWidth(1,600)
        self.tableWidget_2.setColumnWidth(2,270)
        self.tableWidget_2.setColumnWidth(3,125)

        for i in range(70):
            self.tableWidget_2.setRowHeight(i,50) 
        
        columns2 = ['가게명','주소','전화번호','거리']
        self.tableWidget_2.setHorizontalHeaderLabels(columns2)
        
        
        
        self.checkBox = QtGui.QCheckBox(self.page_5)
        self.checkBox.setGeometry(QtCore.QRect(1120, 200, 192, 34))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("휴먼모음T"))
        font.setPointSize(10)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        
        self.checkBox.stateChanged.connect(self.checkBoxState)
        
        
        self.HomepushButton_po = QtGui.QPushButton(self.page_5)
        self.HomepushButton_po.setGeometry(QtCore.QRect(1120, 40, 187, 60))
        
        
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("휴먼모음T"))
        self.HomepushButton_po.setFont(font)
        self.HomepushButton_po.setObjectName(_fromUtf8("HomepushButton_po"))
        
        
        
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QtGui.QWidget()
        self.page_6.setObjectName(_fromUtf8("page_6"))
        self.label_8 = QtGui.QLabel(self.page_6)
        self.label_8.setGeometry(QtCore.QRect(30, 30, 133, 30))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.page_6)
        self.label_9.setGeometry(QtCore.QRect(20, 100, 170, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("휴먼모음T"))
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.page_6)
        self.label_10.setGeometry(QtCore.QRect(320, 50, 100, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("휴먼모음T"))
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(self.page_6)
        self.label_11.setGeometry(QtCore.QRect(300, 170, 130, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("휴먼모음T"))
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(self.page_6)
        self.label_12.setGeometry(QtCore.QRect(310, 290, 130, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("휴먼모음T"))
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(self.page_6)
        self.label_13.setGeometry(QtCore.QRect(330, 410, 61, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("휴먼모음T"))
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_14 = QtGui.QLabel(self.page_6)
        self.label_14.setGeometry(QtCore.QRect(310, 530, 130, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("휴먼모음T"))
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_15 = QtGui.QLabel(self.page_6)
        self.label_15.setGeometry(QtCore.QRect(300, 640, 130, 40))
        
        
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("휴먼모음T"))
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.lineEditSender = QtGui.QLineEdit(self.page_6)
        self.lineEditSender.setGeometry(QtCore.QRect(450, 20, 470, 81))
        self.lineEditSender.setObjectName(_fromUtf8("lineEditSender"))
        
        
        self.lineEditRecipient = QtGui.QLineEdit(self.page_6)
        self.lineEditRecipient.setGeometry(QtCore.QRect(450, 140, 470, 81))
        self.lineEditRecipient.setObjectName(_fromUtf8("lineEditRecipient"))
        
        
        self.lineEditPW = QtGui.QLineEdit(self.page_6)
        self.lineEditPW.setGeometry(QtCore.QRect(450, 270, 470, 81))
        self.lineEditPW.setObjectName(_fromUtf8("lineEditPW"))
        
        
        self.lineEditTitle = QtGui.QLineEdit(self.page_6)
        self.lineEditTitle.setGeometry(QtCore.QRect(450, 390, 470, 81))
        self.lineEditTitle.setObjectName(_fromUtf8("lineEditTitle"))
        
        
        self.lineEditKeyword = QtGui.QLineEdit(self.page_6)
        self.lineEditKeyword.setGeometry(QtCore.QRect(450, 510, 470, 81))
        self.lineEditKeyword.setObjectName(_fromUtf8("lineEditKeyword"))
        
        
        self.lineEditMsg_2 = QtGui.QLineEdit(self.page_6)
        self.lineEditMsg_2.setGeometry(QtCore.QRect(450, 610, 470, 150))
        self.lineEditMsg_2.setObjectName(_fromUtf8("lineEditMsg_2"))
        
        
        self.send_pushButton = QtGui.QPushButton(self.page_6)
        self.send_pushButton.setGeometry(QtCore.QRect(950, 690, 180, 57))
        
        
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("휴먼모음T"))
        font.setPointSize(10)
        self.send_pushButton.setFont(font)
        self.send_pushButton.setObjectName(_fromUtf8("send_pushButton"))
        
        
        self.pushButtonHome = QtGui.QPushButton(self.page_6)
        self.pushButtonHome.setGeometry(QtCore.QRect(10, 690, 180, 57))
        
        
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("휴먼모음T"))
        font.setPointSize(10)
        self.pushButtonHome.setFont(font)
        self.pushButtonHome.setObjectName(_fromUtf8("pushButtonHome"))
        self.stackedWidget.addWidget(self.page_6)
        

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.pushButtonHome, QtCore.SIGNAL(_fromUtf8("clicked()")),self.page1)
        QtCore.QObject.connect(self.HomepushButton_po,QtCore.SIGNAL(_fromUtf8("clicked()")),self.page1)
        QtCore.QObject.connect(self.HomepushButton_key,QtCore.SIGNAL(_fromUtf8("clicked()")),self.page1)
        QtCore.QObject.connect(self.Keyword_pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")),self.page2)
        QtCore.QObject.connect(self.Position_pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")),self.page5)
        QtCore.QObject.connect(self.Email_pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")),self.page6)
        QtCore.QObject.connect(self.send_pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")),self.sendMain)
        QtCore.QObject.connect(self.ClosepushButton,QtCore.SIGNAL(_fromUtf8("clicked()")),Form.close)      
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "~음식점 찾기~", None))
        self.ClosepushButton.setText(_translate("Form", "종료", None))
        self.Keyword_pushButton.setText(_translate("Form", "키워드 검색", None))
        self.Position_pushButton.setText(_translate("Form", "위치 검색", None))
        self.Email_pushButton.setText(_translate("Form", "이메일 전송", None))
        self.label_5.setText(_translate("Form", "원하는 키워드 입력", None))
        self.HomepushButton_key.setText(_translate("Form", "홈", None))
        self.label_7.setText(_translate("Form", "원하는 키워드 입력", None))
        self.checkBox.setText(_translate("Form", "거리 정렬", None))
        self.HomepushButton_po.setText(_translate("Form", "홈", None))
        self.label_8.setText(_translate("Form", "Email", None))
        self.label_9.setText(_translate("Form", "이메일 전송", None))
        self.label_10.setText(_translate("Form", "Sender", None))
        self.label_11.setText(_translate("Form", "Recipient", None))
        self.label_12.setText(_translate("Form", "Passwd", None))
        self.label_13.setText(_translate("Form", "Title", None))
        self.label_14.setText(_translate("Form", "Keyword", None))
        self.label_15.setText(_translate("Form", "msgtext", None))
        self.send_pushButton.setText(_translate("Form", "확인", None))
        self.pushButtonHome.setText(_translate("Form", "홈", None))
        
    
    def page1(self):
        self.stackedWidget.setCurrentWidget(self.page)
    def page2(self):
        self.stackedWidget.setCurrentWidget(self.page_2)
    def page5(self):
        self.stackedWidget.setCurrentWidget(self.page_5)
    def page6(self):
        self.stackedWidget.setCurrentWidget(self.page_6)
        
    ### 키워드 함수 ###
    def getRestaurantDataFromKeyword(self):
            self.tableWidget.clearContents()
            global server,regkey,conn
            if conn == None :
                connectOpenAPIServer()
               
            word = self.keyword_Edit.text()       
            import urllib
            
            #newkeyword =  URLEncoder.encode(word,"UTF-8");
            newkeyword = urllib.parse.quote(word)
            uri = userURIBuilderKeyword(server,ServiceKey=regKey,keyword=newkeyword,contentTypeId='39',arrange='A',listYN='Y',pageNo='1',numOfRows='30',MobileOS='ETC',MobileApp='AppTesting')
            conn.request("GET", uri)
                
            req = conn.getresponse()
            if int(req.status) == 200 :
                 print("Restaurant data downloading complete!")
                 return self.extractRestaurantData(req.read())
            else:
                 print ("OpenAPI request has been failed!! please retry")
                 return None
        
    def extractRestaurantData(self,strXml):
             from xml.etree import ElementTree
             tree = ElementTree.fromstring(strXml)
             
             ret = []
             # restaurant 엘리먼트를 가져옵니다.
             itemElements = tree.getiterator("item")

             for item in itemElements:
                 strTitle = item.find("title")
                 strAddr1 = item.find("addr1")
                 strTel = item.find("tel")
                 strDist = item.find("dist")
                 
                 if strDist != None:
                     l = [strTitle.text,strAddr1.text,strTel.text,strDist.text]
                 elif strTel != None:
                     l =  [strTitle.text,strAddr1.text,strTel.text,' ']
                 elif strTel == None or strDist == None:
                     l = [strTitle.text,strAddr1.text,' ',' ']
                 else : l = None

                 ret.append(l)
             n=-1
             for i in ret:
                 n=n+1
                 title = QtGui.QTableWidgetItem(i[0])
                 addr = QtGui.QTableWidgetItem(i[1])
                 tel = QtGui.QTableWidgetItem(i[2])
                 
                 self.tableWidget.setItem(n,0,title)
                 self.tableWidget.setItem(n,1,addr)
                 self.tableWidget.setItem(n,2,tel)
                 
             return ret
                 
    def getRestaurantDataFromContent(self):
        self.tableWidget_2.clearContents()
        global server, regKey, conn
        if conn == None :
            connectOpenAPIServer()
            
        ########입력한 position으로 구글 맵에서 위도 경도 구해오기 #######
        import urllib
        import urllib.request
        import json        
        
        Position = self.position_lineEdit.text()        
        
        newP = urllib.parse.quote(Position)    
        
        data = urllib.request.urlopen("http://maps.googleapis.com/maps/api/geocode/json?sensor=false&language=ko&address=" + newP)
        json = json.loads(data.read().decode("utf-8"))
    
    
        latitude = json["results"][0]["geometry"]["location"]["lat"]
        longitude = json["results"][0]["geometry"]["location"]["lng"]
    
        print(latitude," ",longitude)
    
        uri = userURIBuilderPosition(server, ServiceKey=regKey, contentTypeId='39', mapX=str(longitude),mapY=str(latitude),radius='500',pageNo='1',numOfRows='74',listYN='Y',arrange='A',MobileOS='ETC',MobileApp='AppTestin') 
        conn.request("GET", uri)
        
        req = conn.getresponse()
        if int(req.status) == 200 :
            print("Restaurant data downloading complete!")
            return self.extractRestaurantDataP(req.read())
        else:
            print ("OpenAPI request has been failed!! please retry")
            return None
            
    def extractRestaurantDataP(self,strXml):
             from xml.etree import ElementTree
             tree = ElementTree.fromstring(strXml)
             
             # restaurant 엘리먼트를 가져옵니다.
             itemElements = tree.getiterator("item")
             
             global Positionret
             Positionret.clear()
             for item in itemElements:
                 strTitle = item.find("title")
                 strAddr1 = item.find("addr1")
                 strTel = item.find("tel")
                 strDist = item.find("dist")
                 
                 if strDist != None:
                     l = [strTitle.text,strAddr1.text,strTel.text,strDist.text]
                 elif strTel != None:
                     l =  [strTitle.text,strAddr1.text,strTel.text]
                 elif strTel == None and strDist == None:
                     l = [strTitle.text,strAddr1.text]
                 else : l = None

                 Positionret.append(l)
             
             n=-1
             
             for i in Positionret:
                 n=n+1
                 title = QtGui.QTableWidgetItem(i[0])
                 addr = QtGui.QTableWidgetItem(i[1])
                 tel = QtGui.QTableWidgetItem(i[2])
                 dist = QtGui.QTableWidgetItem(i[3])
                 
                 self.tableWidget_2.setItem(n,0,title)
                 self.tableWidget_2.setItem(n,1,addr)
                 self.tableWidget_2.setItem(n,2,tel)
                 self.tableWidget_2.setItem(n,3,dist)
                
             return Positionret
             
    def checkBoxState(self):
        if self.checkBox.isChecked() == True:
            print('check')

            Positionret.sort(key=lambda x:(x[3],x[0]))
                 
            n=-1
            for i in Positionret:
                n=n+1
                title = QtGui.QTableWidgetItem(i[0])
                addr = QtGui.QTableWidgetItem(i[1])
                tel = QtGui.QTableWidgetItem(i[2])
                dist = QtGui.QTableWidgetItem(i[3])
                     
                self.tableWidget_2.setItem(n,0,title)
                self.tableWidget_2.setItem(n,1,addr)
                self.tableWidget_2.setItem(n,2,tel)
                self.tableWidget_2.setItem(n,3,dist)
        elif self.checkBox.isChecked() != True:
            print('Uncheck')
            
            Positionret.sort(key=lambda x:(x[0],x[3]))
                 
            n=-1
            for i in Positionret:
                n=n+1
                title = QtGui.QTableWidgetItem(i[0])
                addr = QtGui.QTableWidgetItem(i[1])
                tel = QtGui.QTableWidgetItem(i[2])
                dist = QtGui.QTableWidgetItem(i[3])
                     
                self.tableWidget_2.setItem(n,0,title)
                self.tableWidget_2.setItem(n,1,addr)
                self.tableWidget_2.setItem(n,2,tel)
                self.tableWidget_2.setItem(n,3,dist)
                
    def getRestaurantDataFromKeywordEmail(self,keyword):
            
            global server,regkey,conn
            if conn == None :
               connectOpenAPIServer()
                   
            import urllib
            
            #newkeyword =  URLEncoder.encode(word,"UTF-8");
            newkeyword = urllib.parse.quote(keyword)
            uri = userURIBuilderKeyword(server,ServiceKey=regKey,keyword=newkeyword,contentTypeId='39',arrange='A',listYN='Y',pageNo='1',numOfRows='30',MobileOS='ETC',MobileApp='AppTesting')
            conn.request("GET", uri)
                
            req = conn.getresponse()
            if int(req.status) == 200 :
                 print("Restaurant data downloading complete!")
                 return self.extractRestaurantData(req.read())
            else:
                 print ("OpenAPI request has been failed!! please retry")
                 return None
    def extractRestaurantDataEmail(self,strXml):
             from xml.etree import ElementTree
             tree = ElementTree.fromstring(strXml)
             
             ret = []
             # restaurant 엘리먼트를 가져옵니다.
             itemElements = tree.getiterator("item")

             for item in itemElements:
                 strTitle = item.find("title")
                 strAddr1 = item.find("addr1")
                 strTel = item.find("tel")
                 strDist = item.find("dist")
                 
                 if strDist != None:
                     l = [strTitle.text,strAddr1.text,strTel.text,strDist.text]
                 elif strTel != None:
                     l =  [strTitle.text,strAddr1.text,strTel.text]
                 elif strTel == None and strDist == None:
                     l = [strTitle.text,strAddr1.text]
                 else : l = None

                 ret.append(l)
            
             for item in ret:
                 print(item)
             print()
                 
             return ret
        
                
    def sendMain(self):
        global host, port
        html = ""
        title = self.lineEditTitle.text()
        senderAddr = self.lineEditSender.text()
        recipientAddr = self.lineEditRecipient.text()
        msgtext = self.lineEditMsg_2.text()
        passwd = self.lineEditPW.text()
        
      
        word = self.lineEditKeyword.text()
        html = self.MakeHtmlDoc(self.getRestaurantDataFromKeywordEmail(word))
        
        import smtplib
        # MIMEMultipart의 MIME을 생성합니다.
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        
        #Message container를 생성합니다.
        msg = MIMEMultipart('alternative')
    
        #set message
        msg['Subject'] = title
        msg['From'] = senderAddr
        msg['To'] = recipientAddr
        
        msgPart = MIMEText(msgtext, 'plain')
        bookPart = MIMEText(html, 'html', _charset = 'UTF-8')
        
        # 메세지에 생성한 MIME 문서를 첨부합니다.
        msg.attach(msgPart)
        msg.attach(bookPart)
        
        print ("connect smtp server ... ")
        s = smtplib.SMTP(host,port)
        #s.set_debuglevel(1)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(senderAddr, passwd)    # 로긴을 합니다. 
        s.sendmail(senderAddr , [recipientAddr], msg.as_string())
        s.close()
        
        print ("Mail sending complete!!!")
        #QtGui.QMessageBox.about(self,"message", "Mail sending complete!!!")
        
    
    def MakeHtmlDoc(self,List):
        from xml.dom.minidom import getDOMImplementation
        #get Dom Implementation
        impl = getDOMImplementation()
        
        
        newdoc = impl.createDocument(None, "html", None)  #DOM 객체 생성
        top_element = newdoc.documentElement
        header = newdoc.createElement('header')
        top_element.appendChild(header)
    
        # Body 엘리먼트 생성.
        body = newdoc.createElement('body')
    
        for item in List:
            #create bold element
            b = newdoc.createElement('b')
            #create text node
            titleText = newdoc.createTextNode("가게명 : " + item[0])
            b.appendChild(titleText)
    
            body.appendChild(b)
            
            ##
            br = newdoc.createElement('br')
            body.appendChild(br)
        
                #create addr Element
            p = newdoc.createElement('p')
                #create text node
            addrText= newdoc.createTextNode("주소 : "+item[1])
            p.appendChild(addrText)
            body.appendChild(p)
            body.appendChild(br)  #line end
            
            ##
            brr = newdoc.createElement('brr')
            body.appendChild(brr)
        
                #create addr Element
            pr = newdoc.createElement('pr')
                #create text node
            telText= newdoc.createTextNode("전화 번호 : "+item[2])
            p.appendChild(telText)
            body.appendChild(pr)
            body.appendChild(brr)  #line end
            
            
    
        #append Body
        top_element.appendChild(body)
        
        return newdoc.toxml()
            


class MyForm(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        self.show()
   
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    app.exec_()
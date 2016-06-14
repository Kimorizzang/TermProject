from xmlrestaurant import *
from http.client import HTTPConnection
from http.server import BaseHTTPRequestHandler, HTTPServer
                           
##global
conn = None
ret = []
###################
regKey = "3n0ay%2Fk%2BocRtQBOiPEJNJ7hJNqBuoC1%2F2d%2BQY7GDxFynWHRxFJJM2Hm1MYFTyoe%2BVswgU6XVD%2BuDqwrOXOVUjA%3D%3D"
server = "api.visitkorea.or.kr"


# smtp 정보
host = "smtp.gmail.com" # Gmail SMTP 서버 주소.
port = "587"

# 리스트 url #
def userURIBuilder(server,**user):
     str = "http://" + server + "/openapi/service/rest/KorService/areaBasedList?"
     for key in user.keys():
         str += key + "=" + user[key] + "&"
     return str  
     
# 좌표로 구하는 url #
def userURIBuilderPosition(server,**user): # ** 사전 형식으로 받는다
    #str = "http://" + server + "/search" + "?"
    str = "http://" + server + "/openapi/service/rest/KorService/locationBasedList?"
    for key in user.keys():
        str += key + "=" + user[key] + "&"
    return str

# 키워드로 구하는 url #
def userURIBuilderKeyword(server,**user):
    str = "http://" + server+"/openapi/service/rest/KorService/searchKeyword?"
    for key in user.keys():
        str += key +"=" + user[key]+"&"
    return str
    
def connectOpenAPIServer():
    global conn, server
    conn = HTTPConnection(server)

def getRestaurantDataForList():
    global server, regKey, conn
    if conn == None :
        connectOpenAPIServer()

    uri = userURIBuilder(server,ServiceKey=regKey,contentTypeId='39',areaCode='',sigunguCode='',cat1='A05',cat2='A0502',cat3='',listYN='Y',MobileOS='ETC',MobileApp='TourAPI3.0_Guide',arrange='A',numOfRows='6103',pageNo='1')
    conn.request("GET", uri)


    
    req = conn.getresponse()
 
    if int(req.status) == 200 :
        print("Restaurant data downloading complete!")
        extractRestaurantData(req.read())    
 
    else:
        print ("OpenAPI request has been failed!! please retry")
        return None
            
        
# 좌표 기반 #
def getRestaurantDataFromContent(Position):
    global server, regKey, conn
    if conn == None :
        connectOpenAPIServer()
        
    ########입력한 position으로 구글 맵에서 위도 경도 구해오기 #######
    import urllib
    import json        
    
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
        return extractRestaurantData(req.read())
    else:
        print ("OpenAPI request has been failed!! please retry")
        return None

# 키워드 기반 #
def getRestaurantDataFromKeyword(word):
    global server,regkey,conn
    if conn == None :
        connectOpenAPIServer()
        
    import urllib
    #newkeyword =  URLEncoder.encode(word,"UTF-8");
    newkeyword = urllib.parse.quote(word)
    uri = userURIBuilderKeyword(server,ServiceKey=regKey,keyword=newkeyword,contentTypeId='39',arrange='A',listYN='Y',pageNo='1',numOfRows='80',MobileOS='ETC',MobileApp='AppTesting')
    conn.request("GET", uri)
    
    req = conn.getresponse()
    print (req.status)
    if int(req.status) == 200 :
        print("Restaurant data downloading complete!")
        return extractRestaurantData(req.read())
    else:
        print ("OpenAPI request has been failed!! please retry")
        return None


def extractRestaurantData(strXml):
    from xml.etree import ElementTree
    tree = ElementTree.fromstring(strXml)
    
    l = []
    ret = []

    # restaurant 엘리먼트를 가져옵니다.
    itemElements = tree.getiterator("item")

    for item in itemElements:
        strTitle = item.find("title")
        strAddr1 = item.find("addr1")
        strTel = item.find("tel")
        strDist = item.find("dist")
        
        if strDist != None and strTel != None:
            l = [strTitle.text,strAddr1.text,strTel.text,strDist.text]
        elif strTel != None and strDist == None:
            l =  [strTitle.text,strAddr1.text,strTel.text]
        elif strTel ==None and strDist != None:
            l =  [strTitle.text,strAddr1.text,strDist.text]
        elif strTel == None and strDist == None:
            l = [strTitle.text,strAddr1.text]
        else : l = None
       
        for x in l:
            print(x)   
        print()
               
        ret.append(l)
        
    print('============')
    for x in ret:
        print(x)
    print()
    
    if strDist != None:
        select = str(input('Dist Sort (y/n) - only SearchPosition : '))
        if select == 'y':
           ret.sort(key=lambda x:(x[3],x[0]))
                                       
           print('=========')
           for item in ret:
                print(item)
           print()  
           return ret 
        elif select == 'n':
            return ret
        else: return ret
    return ret
    
def distSort(ret):
    for x in ret:
        return x[3]
        
def sendMain():
    global host, port
    html = ""
    title = str(input ('Title :'))
    senderAddr = str(input ('sender email address :'))
    recipientAddr = str(input ('recipient email address :'))
    msgtext = str(input ('write message :'))
    passwd = str(input (' input your password of gmail account :'))
    msgtext = str(input ('Do you want to include restaurant data (y/n):'))
    
    if msgtext == 'y' :
        word = str(input ('input keyword to search:'))
        html = MakeHtmlDoc(getRestaurantDataFromKeyword(word))
    
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

def MakeHtmlDoc(List):
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
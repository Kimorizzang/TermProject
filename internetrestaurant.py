from xmlrestaurant import *
from http.client import HTTPConnection
from http.server import BaseHTTPRequestHandler, HTTPServer

##global
conn = None
###################
regKey = "3n0ay%2Fk%2BocRtQBOiPEJNJ7hJNqBuoC1%2F2d%2BQY7GDxFynWHRxFJJM2Hm1MYFTyoe%2BVswgU6XVD%2BuDqwrOXOVUjA%3D%3D"
server = "api.visitkorea.or.kr"

def userURIBuilder(server,**user): # ** 사전 형식으로 받는다
    #str = "http://" + server + "/search" + "?"
    str = "http://" + server + "/openapi/service/rest/KorService/locationBasedList?"
    for key in user.keys():
        str += key + "=" + user[key] + "&"
    return str
    
def connectOpenAPIServer():
    global conn, server
    conn = HTTPConnection(server)
        
def getRestaurantDataFromContent(inputX,inputY):
    global server, regKey, conn
    if conn == None :
        connectOpenAPIServer()
   # uri = userURIBuilder(server, key=regKey, query='%20', display="1", start="1", target="book_adv", d_isbn=isbn)

    uri = userURIBuilder(server, ServiceKey=regKey, contentTypeId='39', mapX=inputX,mapY=inputY,radius='500',pageNo='1',numOfRows='10',listYN='Y',arrange='A',MobileOS='ETC',MobileApp='AppTestin') 
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
    #print (strXml)
    # restaurant 엘리먼트를 가져옵니다.
    itemElements = tree.getiterator("item")  # return list type
    #print(itemElements)
    for item in itemElements:
        inputX = item.find("MapX")
        inputY = item.find("MapY")
        strTitle = item.find("title")
        strAddr1 = item.find("addr1")
        #print (strTitle)
        if len(strTitle.text) > 0 :
           return print(strTitle.text," : ",strAddr1.text)#{"contentid":contentid.text,"title":strTitle.text}
           
from xml.dom.minidom import parse, parseString
from xml.etree import ElementTree
import xml.dom.minidom

import http.client


##### global
xmlFD = -1
ResDoc = None
##############
    
def Load():
    global xmlFD, ResDoc
    
    conn = http.client.HTTPConnection("api.visitkorea.or.kr")
    conn.request("GET", "/openapi/service/rest/KorService/locationBasedList?ServiceKey=3n0ay%2Fk%2BocRtQBOiPEJNJ7hJNqBuoC1%2F2d%2BQY7GDxFynWHRxFJJM2Hm1MYFTyoe%2BVswgU6XVD%2BuDqwrOXOVUjA%3D%3D&contentTypeId=39&mapX=126.981611&mapY=37.568477&radius=500&pageNo=1&numOfRows=10&listYN=Y&arrange=A&MobileOS=ETC&MobileApp=AppTestin")
    req = conn.getresponse() 
    print(req.status,req.reason)
    
  #  print(req.read(int(cLen).decode('utf-8') )
    cLen = req.getheader("Content-Length") #가져온 데이터 길이
    data = req.read().decode('utf-8')   
   # try:
    #    xmlFD = open(xmlFile,'w')
    #except IOError:
     #   print ("invalid file name or path")
    #else:
    try:
            #dom = parse(xmlFD)
        dom = xml.dom.minidom.parseString(data)
        
    except Exception:
        print ("loading fail!!!")
    else:
        print ("XML Document loading complete")
        ResDoc = dom
        return dom
    return None

def PrintRList(tags): 
    Load()
    global ResDoc  
    
    if not checkDocument():
       return None
         
    body = ResDoc.childNodes
    item = body[0].childNodes
    
    for x in item:
        if x.nodeName == "item":
            subitems = x.childNodes
            for atom in subitems:
               if atom.nodeName in tags:
                   print("title=",atom.lastChild.nodeValue)
  
         
def SearchAddr(keyword):
    global ResDoc

    Load()    
    
    retlist = []
    if not checkDocument():
        return None
        
    try:
        tree = ElementTree.fromstring(str(ResDoc.toxml()))
    except Exception:
        print ("Element Tree parsing Error : maybe the xml document is not corrected.")
        return None
    
    #get Book Element
    resElements = tree.getiterator("item")  # return list type
    for item in resElements:
        strTitle = item.find("addr1")
        if (strTitle.text.find(keyword) >=0 ):
            retlist.append((item.attrib["addr1"], strTitle.text))
    
    return retlist
    
def RestaurantFree():
    if checkDocument():
        ResDoc.unlink()

def checkDocument():
    global ResDoc
    if ResDoc == None:
        print("Error : Document is empty")
        return False
    return True
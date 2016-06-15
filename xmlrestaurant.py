from xml.dom.minidom import parse, parseString
from xml.etree import ElementTree
import xml.dom.minidom


##### global
xmlFD = -1
ResDoc = None
##############
    

    
def RestaurantFree():
    if checkDocument():
        ResDoc.unlink()
        
def checkDocument():
    global ResDoc
    if ResDoc == None:
        #print("Error : Document is empty")
        return False
    return True
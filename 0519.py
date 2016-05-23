import http.client

conn = http.client.HTTPConnection("api.visitkorea.or.kr")

conn.request("GET", "/openapi/service/rest/KorService/locationBasedList?ServiceKey=3n0ay%2Fk%2BocRtQBOiPEJNJ7hJNqBuoC1%2F2d%2BQY7GDxFynWHRxFJJM2Hm1MYFTyoe%2BVswgU6XVD%2BuDqwrOXOVUjA%3D%3D&contentTypeId=39&mapX=126.981611&mapY=37.568477&radius=500&pageNo=1&numOfRows=10&listYN=Y&arrange=A&MobileOS=ETC&MobileApp=AppTestin") 
req = conn.getresponse() 
print(req.status,req.reason)

cLen = req.getheader("Content-Length") #가져온 데이터 길이
req.read(int(cLen)).decode('utf-8')
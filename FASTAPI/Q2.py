#Return the titels of articles where:
#title is NOT null
#and num_comments == 0
#https://jsonmock.hackerrank.com/api/articles?page=<page>

import requests

def countArticlesWithTitle():
    
    url = "https://jsonmock.hackerrank.com/api/articles"
    
    page = 1
    total_pages = 1
    result = []
    
    while page<=total_pages:
        
        response= requests.get(url,params={"page":page})
        data = response.json()
        
        total_pages = data["total_pages"]
        
        for item in data["data"]:
            
            title = item.get("title")
            comments = item.get("num_comments") or 0
            
            if title and comments == 0:
                result.append(title)
        page+=1
    return result
                
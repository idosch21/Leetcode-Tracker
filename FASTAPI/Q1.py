#Return the number of articles where:
#title is NOT null
#Ignore story_title (don’t use fallback)
#https://jsonmock.hackerrank.com/api/articles?page=<page>

import requests

def countArticlesWithTitle():
    url = "https://jsonmock.hackerrank.com/api/articles"
    
    page = 1
    total_pages = 1
    counter = 0
    
    while page<= total_pages:
        
        response = requests.get(url,params={"page":page})
        data = response.json()
        
        total_pages = data["total_pages"]
        
        for item in data["data"]:
            
            title = item.get("title")
            
            if title:
                counter+=1
                
        page+=1
    return counter
#https://jsonmock.hackerrank.com/api/articles?page=<page>
#Return a list of titles of the top limit articles, sorted by:
#Highest num_comments first
#If tie → lexicographically smaller title

import requests

def topArticles(limit):
    url = "https://jsonmock.hackerrank.com/api/articles"
    
    page = 1
    total_pages = 1
    result = []
    
    while page <= total_pages:
        
        response = requests.get(url, params={"page":page})
        data = response.json()
        
        if page == 1:
            total_pages = data["total_pages"]
        
        for item in data["data"]:
            
            title = item.get("title") or item.get("story_title")
            num_comments = item.get("num_comments") or 0
            
            if title:
                result.append((num_comments,title))
                
        page+=1
        
    result.sort(key=lambda x: (-x[0], x[1]))
    
    return [title for _, title in result[:limit]]
#Return the sum of all transactions for a given userId of articles where:
#https://jsonmock.hackerrank.com/api/transactions/search?userId=<userId>&page=<page>

import requests

def sumTransactions(userId):
    
    url = "https://jsonmock.hackerrank.com/api/transactions/search"
    
    page = 1
    total_pages = 1
    sum_txn = 0
    
    while page <= total_pages:
        
        response = requests.get(url,params={"page":page,"userId":userId})
        data = response.json()
        
        total_pages = data["total_pages"]
        
        for item in data["data"]:
            
            amount = item.get("amount") or "$0"

            clean_amount = amount.replace("$","").replace(",","")
            f_amount = float(clean_amount)
            
            sum_txn += f_amount
        page += 1
        
    return sum_txn
#return the ID of the tansaction with the highest amount
#https://jsonmock.hackerrank.com/api/transactions/search?userId=<userId>&page=<page>

import requests

def getMaxTransactionId(userId):
    
    url = "https://jsonmock.hackerrank.com/api/transactions/search"
    
    page = 1
    total_pages = 1
    resultId = None
    max_txn = float('-inf')
    
    while page <= total_pages:
        response = requests.get(url, params={"page":page, "userId":userId})
        data = response.json()
        
        total_pages = data["total_pages"]
        
        for item in data["data"]:
            
            txn_Id = item.get("id")
            amount = item.get("amount") or "$0"
            
            clean_amount = amount.replace("$","").replace(",","")
            f_amount = float(clean_amount)
            
            if f_amount > max_txn:
                max_txn = f_amount    
                resultId = txn_Id
            elif f_amount == max_txn:
                resultId = min(resultId,txn_Id)
        page+=1
        
    return resultId
            
            
            
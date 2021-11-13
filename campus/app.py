import requests


class Wrapper:
    def __init__(self) -> None:
        self.BASE_API = "https://api-campus.softwarica.edu.np/"
        self.headers = {
            'Connection': 'keep-alive',
            'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
            'Accept': 'application/json, text/plain, */*',
            'CSRF-Token': 'undefined',
            'Content-Type': 'application/json;charset=UTF-8',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
            'sec-ch-ua-platform': '"Windows"',
            'Origin': 'https://campus.softwarica.edu.np',
            'Sec-Fetch-Site': 'same-site',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://campus.softwarica.edu.np/',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        pass

    def login(self,username,password):
        data = {"username":username,"password":password}
        response = requests.post('https://api-campus.softwarica.edu.np/verification/login', headers=self.headers, json=data)
        self.cookies = response.cookies
        return response.json()
    

    def routine(self,batch):
        r=requests.get(self.BASE_API+"routines/"+batch,cookies=self.cookies,headers=self.headers)
        return r.json()

    def notices(self):
        return requests.get(self.BASE_API+"notices/all-notices/1",cookies=self.cookies,headers=self.headers).json()
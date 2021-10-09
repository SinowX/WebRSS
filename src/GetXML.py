import requests

class GetXML:
    url = ""
    xml = ""
    def __init__(self,URL:str):
        self.url=URL
        pass

    def GetResult(self):
        # 获取xml内容
        print("Getting Response")
        res = requests.get(self.url)
        self.xml = res.content
        return self.xml

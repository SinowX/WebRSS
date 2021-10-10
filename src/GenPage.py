# from _typeshed import Self
from DBConn import DBConn
import xml.dom.minidom as minidom
import os

title_prefix_length = 16
title_suffix_length = 11

descr_prefix_length = 22
descr_suffix_length = 17

TplPath = '../dist/static/rss_template.html'
PageStorage = '../dist/pages'
if ~os.path.exists(PageStorage):
    os.makedirs(PageStorage)


class GenPages:
    xml = ""
    Items = None
    Title_Str = ""
    Content_Str = ""
    db_handler = DBConn
    def __init__(self,XML:str):
        self.xml = XML
        self.db_handler = DBConn()
        self.db_handler.Connect("remoter","asd123456")
        pass

    def ParseXML(self):
        print("Parsing XML")
        DOMTree = minidom.parseString(self.xml)
        collection = DOMTree.documentElement
        self.Items = collection.getElementsByTagName("item")
        pass

    def Traverse(self):
        for i in range(self.Items.length):
            
            titleNode = self.Items[i].getElementsByTagName('title')
            assert titleNode.length == 1
            Title_Str:str = titleNode[0].toxml()[title_prefix_length:-title_suffix_length]
            Title_Str = Title_Str.replace('/','-').replace(' ','_')
            print("Parsing No.",str(i),Title_Str)
            descrNode = self.Items[i].getElementsByTagName('description')
            assert descrNode.length == 1
            Content_Str = descrNode[0].toxml()[descr_prefix_length:-descr_suffix_length]
            if(~self.CheckIfExists(Title_Str)):
                
                self.WritePage(Title_Str,Content_Str)
                self.UpdateDB(Title_Str)
                pass

        pass

    def CheckIfExists(self,title:str):
        return False

    def UpdateDB(self, title:str):

        pass

    def WritePage(self, title:str, content: str):
        print("Writing Page ",title)
        index = open(TplPath,'r').read().format(TITLE=title, CONTENT=content)
        filePath = PageStorage+'/'+title+'.html'
        if ~os.path.exists(filePath):
            f = open(filePath, 'w')
            f.write(index)
            f.close()
            print("Write Success")
            pass
        pass

    

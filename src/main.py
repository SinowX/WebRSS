import GenPage

import GetXML

url = "http://localhost:1200/zhihu/collection/718626041"

xml = GetXML.GetXML(url).GetResult()

processor = GenPage.GenPages(xml)

processor.ParseXML()

processor.Traverse()


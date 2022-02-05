import xml.etree.ElementTree as Xet
import pandas as pd
  
cols = ["title", "description", "keywords", "url", "url_hash"]
rows = []
  
# Parsing the XML file
xmlparse = Xet.parse('enwiki-latest-abstract.xml')
root = xmlparse.getroot()
for i in root:
    title = i.find("anchor").text
    description =''
    keywords = ''
    url = i.find("link").text
    url_hash = ''
  
    rows.append({"title": title,
                 "description": description,
                 "keywords": keywords,
                 "url": url,
                 "url_hash": url_hash})
    print(title)
df = pd.DataFrame(rows, columns=cols)
  
# Writing dataframe to csv
df.to_csv('output.csv')
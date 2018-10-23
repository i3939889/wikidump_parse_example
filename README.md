# wikidump_parse_example
本範例示範如何parse wiki dump檔案,並過濾含有linux template的page

### 使用方式
下載專案後 在專案下建立名稱為wiki的目錄,並將用bzip2解壓縮的dump檔案放置在目錄內,  
修改程式內的FILENAME_WIKI檔案名稱即可

### 主要使用套件
#### lxml: 
<https://github.com/lxml/lxml>  
用iterate方式讀取大型xml的函式庫

#### mwparserfromhell: 
<https://github.com/earwig/mwparserfromhell>  
解析wikitext函式庫

### 參考:
<https://www.heatonresearch.com/2017/03/03/python-basic-wikipedia-parsing.html>  
Reading Wikipedia XML Dumps with Python

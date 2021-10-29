from lxml import html
import requests
import string
import re

CHINA_GDP = None;
CHINA_GNI = None;
CHINA_HDI = None;

US_GDP = 0;
US_GNI = 0;
US_HDI = 0;

UK_GDP = None;
UK_GNI = None;
UK_HDI = None;

IND_GDP = None;
IND_GNI = None;
IND_HDI = None;


def get_GDP_GNI():
    url = 'http://wdi.worldbank.org/table/4.10'
    
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/604.5.6 (KHTML, like Gecko) Version/11.0.3 Safari/604.5.6'}
    page = requests.get(url, headers=headers)
    tree = html.fromstring(page.content)
    print("GNI & GDP")
    global CHINA_GDP
    global CHINA_GNI
    CHINA_GDP = [tree.xpath('///*[@id="scrollTable"]/tbody/tr[41]/td[2]/div/text()')]
    CHINA_GDP = str(CHINA_GDP[0][0])
    CHINA_GDP = float(CHINA_GDP.replace(',',''))
    CHINA_GNI = [tree.xpath('//*[@id="scrollTable"]/tbody/tr[41]/td[4]/div/text()')]
    CHINA_GNI = str(CHINA_GNI[0][0])
    CHINA_GNI = float(CHINA_GNI.replace(',',''))
    
    global US_GDP
    global US_GNI
    US_GDP = [tree.xpath('//*[@id="scrollTable"]/tbody/tr[204]/td[2]/div/text()')]
    US_GDP = str(US_GDP[0][0])
    US_GDP = float(US_GDP.replace(',',''))
    US_GNI = [tree.xpath('//*[@id="scrollTable"]/tbody/tr[204]/td[4]/div/text()')]
    US_GNI = str(US_GNI[0][0])
    US_GNI = float(US_GNI.replace(',',''))

    global UK_GDP
    global UK_GNI
    UK_GDP = [tree.xpath('//*[@id="scrollTable"]/tbody/tr[203]/td[2]/div/text()')]
    UK_GDP = str(UK_GDP[0][0])
    UK_GDP = float(UK_GDP.replace(',',''))
    UK_GNI = [tree.xpath('//*[@id="scrollTable"]/tbody/tr[203]/td[4]/div/text()')]
    UK_GNI = str(UK_GNI[0][0])
    UK_GNI = float(UK_GNI.replace(',',''))

    global IND_GDP
    global IND_GNI
    IND_GDP = [tree.xpath('//*[@id="scrollTable"]/tbody/tr[88]/td[2]/div/text()')]
    IND_GDP = str(IND_GDP[0][0])
    IND_GDP = float(IND_GDP.replace(',',''))
    IND_GNI = [tree.xpath('//*[@id="scrollTable"]/tbody/tr[88]/td[4]/div/text()')]
    IND_GNI = str(IND_GNI[0][0])
    IND_GNI = float(IND_GNI.replace(',',''))

    print("CHINA: ",CHINA_GDP, CHINA_GNI)
    print("US: ",US_GDP, US_GNI)
    print("UK: ",UK_GDP, UK_GNI)
    print("INDIA: ",IND_GDP, IND_GNI)
def get_HDI():
    url = 'http://hdr.undp.org/en/composite/HDI'
    
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/604.5.6 (KHTML, like Gecko) Version/11.0.3 Safari/604.5.6'}
    page = requests.get(url, headers=headers)
    tree = html.fromstring(page.content)
    print("Human Development Index")

    global US_HDI
    US_HDI = [tree.xpath('/html/body/div[2]/div/section/div/div/div/div/div/table/tbody/tr[14]/td[3]/text()')]
    US_HDI = str(US_HDI[0][0])
    US_HDI = float(US_HDI)

    global UK_HDI
    UK_HDI = [tree.xpath('/html/body/div[2]/div/section/div/div/div/div/div/table/tbody/tr[15]/td[3]/text()')]
    UK_HDI = str(UK_HDI[0][0])
    UK_HDI = float(UK_HDI)

    global IND_HDI
    IND_HDI = [tree.xpath('/html/body/div[2]/div/section/div/div/div/div/div/table/tbody/tr[133]/td[3]/text()')]
    IND_HDI = str(IND_HDI[0][0])
    IND_HDI = float(IND_HDI)

    global CHINA_HDI
    CHINA_HDI = [tree.xpath('/html/body/div[2]/div/section/div/div/div/div/div/table/tbody/tr[88]/td[3]/text()')]
    CHINA_HDI = str(CHINA_HDI[0][0])
    CHINA_HDI = float(CHINA_HDI)

    print("US: ", US_HDI)
    print("UK: ", UK_HDI)
    print("INDIA: ", IND_HDI)
    print("CHINA: ", CHINA_HDI)

get_GDP_GNI()
get_HDI()
print('\n\n')
print("US: ",US_HDI+US_GNI+US_GDP)
print("UK: ",UK_HDI+UK_GNI+UK_GDP)
print("INDIA: ",IND_HDI+IND_GNI+IND_GDP)
print("CHINA: ",CHINA_HDI+CHINA_GNI+CHINA_GDP)
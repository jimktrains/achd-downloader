#!/usr/bin/env python3



# curl 'http://webapps.achd.net/Restaurant/RestaurantSearch.aspx' -H 'Host: webapps.achd.net' -H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:43.0) Gecko/20100101 Firefox/43.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'Referer: http://webapps.achd.net/Restaurant/' -H 'Connection: keep-alive' -H 'Cache-Control: max-age=0' --data 'ctl00%24ContentPlaceHolder1%24txtFDBA=&ctl00%24ContentPlaceHolder1%24ddlPCode=*&ctl00%24ContentPlaceHolder1%24txtNum=&ctl00%24ContentPlaceHolder1%24txtStreet=&ctl00%24ContentPlaceHolder1%24txtCity=&ctl00%24ContentPlaceHolder1%24txtZip=&ctl00%24ContentPlaceHolder1%24ddlMuni=901&ctl00%24ContentPlaceHolder1%24ddlPlacard=*&ctl00%24ContentPlaceHolder1%24btnFind=Find'
#        <option value="">Please Select</option>
#        <option value="901">Aleppo</option>
#        <option value="0">All Municipalities</option>
#        <option value="801">Aspinwall</option>
#        <option value="802">Avalon</option>
#        <option value="877">Baldwin Boro</option>
#        <option value="902">Baldwin Twp</option>
#        <option value="883">Bell Acres</option>
#        <option value="803">Bellevue</option>
#        <option value="804">Ben Avon</option>
#        <option value="805">Ben Avon Hgts</option>
#        <option value="876">Bethel Park</option>
#        <option value="806">Blawnox</option>
#        <option value="807">Brackenridge</option>
#        <option value="808">Braddock</option>
#        <option value="872">Braddock Hills</option>
#        <option value="809">Bradford Woods</option>
#        <option value="810">Brentwood</option>
#        <option value="811">Bridgeville</option>
#        <option value="812">Carnegie</option>
#        <option value="813">Castle Shannon</option>
#        <option value="814">Chalfant</option>
#        <option value="815">Cheswick</option>
#        <option value="816">Churchill</option>
#        <option value="201">Clairton</option>
#        <option value="905">Collier</option>
#        <option value="817">Coraopolis</option>
#        <option value="818">Crafton</option>
#        <option value="906">Crescent</option>
#        <option value="819">Dormont</option>
#        <option value="820">Dravosburg</option>
#        <option value="301">Duquesne</option>
#        <option value="907">East Deer</option>
#        <option value="821">East McKeesport</option>
#        <option value="822">East Pittsburgh</option>
#        <option value="823">Edgewood</option>
#        <option value="824">Edgeworth</option>
#        <option value="825">Elizabeth Borough</option>
#        <option value="908">Elizabeth Township</option>
#        <option value="826">Emsworth</option>
#        <option value="827">Etna</option>
#        <option value="909">Fawn</option>
#        <option value="910">Findlay</option>
#        <option value="828">Forest Hills</option>
#        <option value="911">Forward</option>
#        <option value="868">Fox Chapel</option>
#        <option value="884">Franklin Park</option>
#        <option value="913">Frazer</option>
#        <option value="829">Glassport</option>
#        <option value="830">Glenfield</option>
#        <option value="831">Greentree</option>
#        <option value="914">Hampton</option>
#        <option value="915">Harmar</option>
#        <option value="916">Harrison</option>
#        <option value="832">Haysville</option>
#        <option value="833">Heidelberg</option>
#        <option value="834">Homestead</option>
#        <option value="917">Indiana</option>
#        <option value="835">Ingram</option>
#        <option value="878">Jefferson</option>
#        <option value="919">Kennedy</option>
#        <option value="920">Kilbuck</option>
#        <option value="921">Leet</option>
#        <option value="836">Leetsdale</option>
#        <option value="837">Liberty Boro</option>
#        <option value="881">Lincoln</option>
#        <option value="923">Marshall</option>
#        <option value="927">McCandless</option>
#        <option value="841">McDonald</option>
#        <option value="842">McKees Rocks</option>
#        <option value="401">McKeesport</option>
#        <option value="838">Millvale</option>
#        <option value="879">Monroeville</option>
#        <option value="925">Moon</option>
#        <option value="926">Mt Lebanon</option>
#        <option value="839">Mt Oliver</option>
#        <option value="840">Munhall</option>
#        <option value="928">Neville</option>
#        <option value="843">North Braddock</option>
#        <option value="929">North Fayette</option>
#        <option value="930">North Versailles</option>
#        <option value="931">O'Hara</option>
#        <option value="844">Oakdale</option>
#        <option value="845">Oakmont</option>
#        <option value="932">Ohio</option>
#        <option value="846">Osborne</option>
#        <option value="999">Out Of County</option>
#        <option value="934">Penn Hills</option>
#        <option value="871">Pennsbury Village</option>
#        <option value="935">Pine</option>
#        <option value="847">Pitcairn</option>
#        <option value="998">Pittsburgh (All)</option>
#        <option value="101">Pittsburgh-101</option>
#        <option value="102">Pittsburgh-102</option>
#        <option value="103">Pittsburgh-103</option>
#        <option value="104">Pittsburgh-104</option>
#        <option value="105">Pittsburgh-105</option>
#        <option value="106">Pittsburgh-106</option>
#        <option value="107">Pittsburgh-107</option>
#        <option value="108">Pittsburgh-108</option>
#        <option value="109">Pittsburgh-109</option>
#        <option value="110">Pittsburgh-110</option>
#        <option value="111">Pittsburgh-111</option>
#        <option value="112">Pittsburgh-112</option>
#        <option value="113">Pittsburgh-113</option>
#        <option value="114">Pittsburgh-114</option>
#        <option value="115">Pittsburgh-115</option>
#        <option value="116">Pittsburgh-116</option>
#        <option value="117">Pittsburgh-117</option>
#        <option value="118">Pittsburgh-118</option>
#        <option value="119">Pittsburgh-119</option>
#        <option value="120">Pittsburgh-120</option>
#        <option value="121">Pittsburgh-121</option>
#        <option value="122">Pittsburgh-122</option>
#        <option value="123">Pittsburgh-123</option>
#        <option value="124">Pittsburgh-124</option>
#        <option value="125">Pittsburgh-125</option>
#        <option value="126">Pittsburgh-126</option>
#        <option value="127">Pittsburgh-127</option>
#        <option value="128">Pittsburgh-128</option>
#        <option value="129">Pittsburgh-129</option>
#        <option value="130">Pittsburgh-130</option>
#        <option value="131">Pittsburgh-131</option>
#        <option value="132">Pittsburgh-132</option>
#        <option value="873">Pleasant Hills</option>
#        <option value="880">Plum</option>
#        <option value="848">Portvue</option>
#        <option value="849">Rankin</option>
#        <option value="937">Reserve</option>
#        <option value="938">Richland</option>
#        <option value="939">Robinson</option>
#        <option value="940">Ross</option>
#        <option value="850">Rosslyn Farms</option>
#        <option value="941">Scott</option>
#        <option value="851">Sewickley</option>
#        <option value="869">Sewickley Heights</option>
#        <option value="882">Sewickley Hills</option>
#        <option value="944">Shaler</option>
#        <option value="852">Sharpsburg</option>
#        <option value="946">South Fayette</option>
#        <option value="945">South Park</option>
#        <option value="947">South Versailles</option>
#        <option value="853">Springdale Borough</option>
#        <option value="948">Springdale Township</option>
#        <option value="949">Stowe</option>
#        <option value="854">Swissvale</option>
#        <option value="855">Tarentum</option>
#        <option value="856">Thornburg</option>
#        <option value="857">Trafford</option>
#        <option value="858">Turtle Creek</option>
#        <option value="997">Unspecified</option>
#        <option value="950">Upper St Clair</option>
#        <option value="859">Verona</option>
#        <option value="860">Versailles</option>
#        <option value="861">Wall</option>
#        <option value="952">West Deer</option>
#        <option value="862">West Elizabeth</option>
#        <option value="863">West Homestead</option>
#        <option value="870">West Mifflin</option>
#        <option value="864">West View</option>
#        <option value="865">Whitaker</option>
#        <option value="875">White Oak</option>
#        <option value="874">Whitehall</option>
#        <option value="953">Wilkins</option>
#        <option value="866">Wilkinsburg</option>
#        <option value="867">Wilmerding</option>

# <table rules="all" id="ctl00_ContentPlaceHolder1_gvFSO" style="color:#333333;background-color:#FCFCFC;text-decoration:none;width:800px;border-collapse:collapse;" cellspacing="0" align="Center" border="1">
#         <tbody><tr style="color:White;background-color:#0E4997;">
#                 <th scope="col"><a href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$gvFSO','Sort$CLIENT_NAME')" style="color:White;">Client Name</a></th><th scope="col"><a href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$gvFSO','Sort$NUM')" style="color:White;">Street #</a></th><th scope="col"><a href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$gvFSO','Sort$STREET')" style="color:White;">Street</a></th><th scope="col"><a href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$gvFSO','Sort$CITY')" style="color:White;">City</a></th><th scope="col"><a href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$gvFSO','Sort$ZIP')" style="color:White;">Zip</a></th><th scope="col">Phone</th><th scope="col"><a href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$gvFSO','Sort$INSP_DATE_WEB')" style="color:White;">Inspection Date</a></th><th scope="col">Priority Code</th><th scope="col">Placard Status</th>
#         </tr><tr>
#                 <td align="left">
#         <a id="ctl00_ContentPlaceHolder1_gvFSO_ctl02_hypJavascript"></a>
#             <a href="javascript:void(window.open('RestaurantDetail.aspx?ID=200809050012','Details','width=800,height=500 menubar=no,resizable=no,directories=no,location=no'));">Masonic Village at Sewickley Child Care Center</a>
#     </td><td>1000</td><td align="left"><a href="http://maps.google.com/maps?f=q&amp;source=s_q&amp;hl=en&amp;geocode=&amp;q=1000+Masonic Dr+Sewickley+15143" target="_blank">Masonic Dr</a></td><td align="left">Sewickley</td><td align="center">15143</td><td style="white-space:nowrap;" align="center">412-7411400</td><td align="center"><a href="http://appsrv.achd.net/reports/rwservlet?food_rep_insp&amp;P_ENCOUNTER=201509250007" target="_blank">09/24/2015</a></td><td align="center"><a href="PCodes.htm" target="_blank">1</a></td><td style="color:White;background-color:Green;" align="center">Green</td>
#         </tr><tr>
#                 <td align="left">
#         <a id="ctl00_ContentPlaceHolder1_gvFSO_ctl03_hypJavascript"></a>
#             <a href="javascript:void(window.open('RestaurantDetail.aspx?ID=200302240004','Details','width=800,height=500 menubar=no,resizable=no,directories=no,location=no'));">Masonic Village Clubhouse</a>
#     </td><td>1000</td><td align="left"><a href="http://maps.google.com/maps?f=q&amp;source=s_q&amp;hl=en&amp;geocode=&amp;q=1000+Masonic Dr+Sewickley+15143" target="_blank">Masonic Dr</a></td><td align="left">Sewickley</td><td align="center">15143</td><td style="white-space:nowrap;" align="center">412-7411400</td><td align="center"><a href="http://appsrv.achd.net/reports/rwservlet?food_rep_insp&amp;P_ENCOUNTER=201510290027" target="_blank">10/29/2015</a></td><td align="center"><a href="PCodes.htm" target="_blank">1</a></td><td style="color:White;background-color:Green;" align="center">Green</td>
#         </tr><tr>
#                 <td align="left">
#         <a id="ctl00_ContentPlaceHolder1_gvFSO_ctl04_hypJavascript"></a>
#             <a href="javascript:void(window.open('RestaurantDetail.aspx?ID=201310220003','Details','width=800,height=500 menubar=no,resizable=no,directories=no,location=no'));">Masonic Village Country Kitchen</a>
#     </td><td>1000</td><td align="left"><a href="http://maps.google.com/maps?f=q&amp;source=s_q&amp;hl=en&amp;geocode=&amp;q=1000+Masonic+Sewickley+15143" target="_blank">Masonic Drive</a></td><td align="left">Sewickley</td><td align="center">15143</td><td style="white-space:nowrap;" align="center">412-7496862</td><td align="center"><a href="http://appsrv.achd.net/reports/rwservlet?food_rep_insp&amp;P_ENCOUNTER=201310240002" target="_blank">10/08/2013</a></td><td align="center"><a href="PCodes.htm" target="_blank">1</a></td><td style="color:White;background-color:Green;" align="center">Green</td>
#         </tr>
# </tbody></table>


import csv
import copy
from bs4 import BeautifulSoup
import httplib2
from urllib.parse import urlencode
import sys

def extract_record(row):
    #<tr>
    #<td align="left">
    #  <font color="#333333">
    #     <a id="ctl00_ContentPlaceHolder1_gvFSO_ctl51_hypJavascript"></a>
    #     <a href="javascript:void(window.open('RestaurantDetail.aspx?ID=201404090002','Details','width=800,height=500 menubar=no,resizable=no,directories=no,location=no'));">
    #        Eddie Merlots
    #     </a>
    # #  </font>
    # </td>
    # <td>
    #    <font color="#333333">
    #        444
    #    </font>
    # </td>
    # <td align="left">
    #    <font color="#333333">
    #        <a href="http://maps.google.com/maps?f=q&amp;source=s_q&amp;hl=en&amp;geocode=&amp;q=444+Liberty+Pittsburgh+15222" target="_blank">
    #            Liberty Avenue
    #        </a>
    #    </font>
    # </td>
    # <td align="left">
    #    <font color="#333333">
    #        Pittsburgh
    #    </font>
    # </td>
    # <td align="center">
    #    <font color="#333333">
    #        15222
    #    </font>
    #</td>
    #<td align="center" nowrap="nowrap">
    #    <font color="#333333">412-2357676</font>
    #</td>
    #<td align="center">
    #    <font color="#333333">
    #        <a href="http://appsrv.achd.net/reports/rwservlet?food_rep_insp&amp;P_ENCOUNTER=201508310031" target="_blank">
    #            08/31/2015
    #        </a>
    #    </font>
    #</td>
    #<td align="center">
    #    <font color="#333333">
    #        <a href="PCodes.htm" target="_blank">H</a>
    #    </font>
    #</td>
    #<td align="center" bgcolor="Green"><font color="White">Green</font></td>
    #</tr>
    cells = row.find_all('td')
    if len(cells) < 1: return

    name = cells[0].find_all('a')
    if len(name) != 2: return
    name = name[1]
    name = name.get_text()

    street_number = cells[1].get_text()
    street_name = cells[2].get_text()
    city = cells[3].get_text()
    zipcode = cells[4].get_text()

    return {
        'name': name,
        'street_number': street_number,
        'street_name': street_name,
        'city': city,
        'zipcode': zipcode
    }


headers = {
    'HTTP_USER_AGENT': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.13) Gecko/2009073022 Firefox/3.0.13',
    'HTTP_ACCEPT': 'text/html,application/xhtml+xml,application/xml; q=0.9,*/*; q=0.8',
    'Content-Type': 'application/x-www-form-urlencoded'
}

class ASPState:
    def __init__(self, start_url):
        self.h = httplib2.Http()
        self.asp_hidden_inputs = {}
        self.get(start_url)

    def get_hidden(self, soup):
        for hidden in soup.find_all('input', type='hidden'):
            if '_' == hidden['name'][0]:
                self.asp_hidden_inputs[hidden['name']] = hidden['value']
    def bs(self, content):
        str_content = content.decode('utf-8')
        soup = BeautifulSoup(str_content, 'html.parser')
        self.get_hidden(soup)
        return soup
    def get(self, url):
        resp, content = self.h.request(url, "GET")
        soup = self.bs(content);
        return soup
    def post(self, url, data):
        data.update(self.asp_hidden_inputs.copy())
        resp, content = self.h.request(url, "POST", urlencode(data), headers)
        soup = self.bs(content)
        return soup

url = 'http://webapps.achd.net/Restaurant/RestaurantSearch.aspx'
a = ASPState(url)

form_fields_orig = {
    'ctl00$ContentPlaceHolder1$txtFDBA':'',
    'ctl00$ContentPlaceHolder1$ddlPCode':'*',
    'ctl00$ContentPlaceHolder1$txtNum':'',
    'ctl00$ContentPlaceHolder1$txtStreet':'',
    'ctl00$ContentPlaceHolder1$txtCity':'',
    'ctl00$ContentPlaceHolder1$txtZip':'',
    'ctl00$ContentPlaceHolder1$ddlMuni':'901',
    'ctl00$ContentPlaceHolder1$ddlPlacard':'*',
    'ctl00$ContentPlaceHolder1$btnFind':'Find',
    '__LASTFOCUS':'',
    '__EVENTTARGET':'',
    '__EVENTARGUMENT':''
}


munis=["101","102","103","104","105","106","107","108","109",
"110","111","112","113","114","115","116","117","118","119",
"120","121","122","123","124","125","126","127","128","129",
"130","131","132","201","301","401","801","802","803","804",
"805","806","807","808","809","810","811","812","813","814",
"815","816","817","818","819","820","821","822","823","824",
"825","826","827","828","829","830","831","832","833","834",
"835","836","837","838","839","840","841","842","843","844",
"845","846","847","848","849","850","851","852","853","854",
"855","856","857","858","859","860","861","862","863","864",
"865","866","867","868","869","870","871","872","873","874",
"875","876","877","878","879","880","881","882","883","884",
"901","902","905","906","907","908","909","910","911","913",
"914","915","916","917","919","920","921","923","925","926",
"927","928","929","930","931","932","934","935","937","938",
"939","940","941","944","945","946","947","948","949",
"950","952","953","997","999"]

def parse_page(soup):
    records = []
    # because nested tables
    for table in soup.find_all('table', id='ctl00_ContentPlaceHolder1_gvFSO'):
        # Only the table with the data seems to have an id?
        # Yes, why this and that? -- historical, one works sometimes and
        #      the other doesn't :-\
        if 'id' in table.attrs:
            for row in table.find_all('tr'):
                record = extract_record(row)
                if record is not None:
                    records.append(record)
        # The page links are in the same table...because why not?
        pages = find_pages(table)
        return (pages, records)

def find_pages(table):
    pages = []
    # Because ASP.NET is much too good for plebian links
    for link in table.select('a[href^="javascript:__doPostBack(\'ctl00$ContentPlaceHolder1$gvFSO\'"]'):
        page = link['href'][59:-2]
        # Because, you know, let's use the same variables for everything!
        # Sorting is done with the same ctl00$ContentPlaceHolder1$gvFSO
        # callback and is in the same table
        if 'Page' in page:
            pages.append(page)
    return pages
with open('places.csv', 'w') as csvfile:
    fieldnames = ['name', 'street_number', 'street_name', 'city', 'zipcode']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for muni in munis:
        form_fields = copy.deepcopy(form_fields_orig)
        form_fields['ctl00$ContentPlaceHolder1$ddlMuni'] = muni
        print("Getting muni " + muni);
        soup = a.post(url, form_fields)
        pages, records = parse_page(soup)
        for record in records:
            writer.writerow(record)
        for page in pages:
            form_fields['ctl00$ContentPlaceHolder1$ScriptManager1'] = "ctl00$ContentPlaceHolder1$UpdatePanel1|ctl00$ContentPlaceHolder1$gvFSO"
            form_fields['__EVENTTARGET'] = "ctl00$ContentPlaceHolder1$gvFSO"
            form_fields['__EVENTARGUMENT'] = page
            print(page)
            #form_fields['__ASYNCPOST'] = "true"
            soup = a.post(url, form_fields)
            pages, records = parse_page(soup)
            if records is None:
                print("No records returned")
                continue
            for record in records:
                writer.writerow(record)
        print(len(records))
        sys.exit(0)

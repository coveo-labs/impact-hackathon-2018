import string
import re
 

def getUrlPart(field, nr, fieldtoset, trim):
    #Clean up
    result=''
    content=field
    parts=content.split('/')
    if (len(parts)>nr):
        result = parts[nr]
        partsclean = result.split(trim)
        #Clean it
        newresult = partsclean[0].replace("-"," ").title()
        #Set the field
        document.add_meta_data({fieldtoset:newresult})
        #Log it
        document.log(fieldtoset+' set to: '+newresult)
    return result

#URL="http://retail.coveodemo.com/shop/Computers-and-Tablets_computers%20and%20tablets/Fusion-10%2C-d-%2C1%E2%80%9D-2-in-1%E2%80%942GB-Memory%2C-16GB-Flash-Memory_6042186
URL=document.get_meta_data_value('clickableuri')[0]
#Ugly fix for URL
URL=URL.replace('%C2','-')
#For Logging
document.log(URL)

getUrlPart(URL,4,'mycategory','_')

#Fix broken titles
title=document.get_meta_data_value('title')[0]
if title=='- Habitat Retail':
    title=URL.split('/')[5]
    document.add_meta_data({'title':title})

#Fix title, remove ' - Habitat Retail'
title=title.replace(' - Habitat Retail','')
document.add_meta_data({'title':title})

#Check brand... if brand is in metadata use that, else use title
metabrand = document.get_meta_data_value('productbrandname','converter')[0]
if metabrand:
    document.add_meta_data({'mybrand':metabrand})
else:
    mybrand = document.get_meta_data_value('title')[0].split(' ')[0].title()

    document.log('Retrieved title for brand: '+mybrand)
    document.add_meta_data({'mybrand':mybrand})

#Check price... if price is in metadata set we can use that
metaprice = document.get_meta_data_value('productlistprice','converter')[0]
if metaprice:
    document.add_meta_data({'myprice':metaprice})
else:
    #Fix price 2,4999.00 --> 2499.00
    price = document.get_meta_data_value('myprice','crawler')[0]
    document.add_meta_data({'myprice':price.replace(',','')})

#Set proper url for image
try:
    image = ''+document.get_meta_data_value('myimage')[0]
    if 'https://retail-static.coveodemo.com' not in image:
        image= 'https://retail-static.coveodemo.com/'+image
    document.add_meta_data({'ytthumbnailurl':image})
except Exception as e:
    log(str(e))


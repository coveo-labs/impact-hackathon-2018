import string
import re

#URL should contain Shop
#URL should have a minimum length of 5

#URL="http://retail.coveodemo.com/shop/Computers-and-Tablets_computers%20and%20tablets/Fusion-10%2C-d-%2C1%E2%80%9D-2-in-1%E2%80%942GB-Memory%2C-16GB-Flash-Memory_6042186
URL=document.get_meta_data_value('clickableuri')[0]
#For Logging
document.log(URL)

#Reject if it is not the shop
if '/shop/' not in URL:
    document.log('No Shop item')
    document.reject()
#Reject if length<=5
if len(URL.split('/'))<=5:
    document.log('Invalid URL length')
    document.reject()
'''
import re
original_plain_text = "00 mum +61 7 310 310 46 my i on (03) 9790 2803. phone number is 02 6051-7373 (02) 6051-7373 and emai is ryan@sibmail.com ewar2 2222222222222"
emails = set()
telephone_numbers = set()

re_email = r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+"
re1 = r'(0[0-9]{1,1}.[0-9]{3,5}.[0-9]{3,5})'
re2 = r'(\([0-9]{2,2}\).[0-9]{3,5}.[0-9]{3,5})'
re3 = r'\+61.[0-9]{1,1}.[0-9]{2,5}.[0-9]{2,5}.[0-9]{2,5}'

emails.update(set(re.findall(re_email, original_plain_text, re.I)))
telephone_numbers.update(set(re.findall(re1, original_plain_text, re.I)))
telephone_numbers.update(set(re.findall(re2, original_plain_text, re.I)))
telephone_numbers.update(set(re.findall(re3, original_plain_text, re.I)))

print telephone_numbers
print emails
'''
import re
s1= "$28 an hour"
s2 = "$60,001 - $80,000 a year"

if re.search(r' a year', s2):
    s2 = s1.split(' a year')
    
.group()
 
print s2

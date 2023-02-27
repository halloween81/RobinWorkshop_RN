# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 18:47:52 2023

@author: tuyen
"""



#%%  Extracted from WEEK 5's BRINGING IT ALL TOGETHER

import feedparser
from urllib.parse import urlencode
# from pprint import pprint

def get_fuel(product_id, suburb, day):
    params = {
        'Product': product_id,
        'Suburb': suburb,
        'Day': day
    }
    
    data_source = 'http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?' + urlencode(params)
    print('...Reading data from: ', data_source)
    data = feedparser.parse(data_source)
    print('\n', 'Number of stations: ', len(data['entries']), '\n')
    
    return [
        {
            'brand': i['brand'],
            'price': float(i['price']),
            'date': i['date'],
            'location': i['location'],
            'address': i['address'],
            'title': i['title'],
            'custom': 'Tuyen',
        }
        for i in data['entries']    
    ]
        
# fuel_list = get_fuel(1, 'Cloverdale', 'Today')



# --------------------------------------------------------
# This is the long way to write code:
    
# tr_list = [
#     '<tr><td>{location}</td><td>{price}</td></tr>'.format(**d)  # List destructuring
#     for d in  fuel_list
# ]
   
# my_html = '<table>'+ ''.join(tr_list) + '</table>'

# my_html = '<table>'+ ''.join(
#     '<tr><td>{location}</td><td>{price}</td></tr>'.format(**d)
#     for d in  fuel_list
# ) + '</table>'


# --------------------------------------------------------
# This is the shorter way:

# M = get_fuel(1, 'Cloverdale', 'Today')  # This is for debugging mode, to see what's inside M
    
my_html = '<table>{}</table>'.format(''.join(
    '<tr><td>{brand}</td><td>{price}</td><td>{location}</td><td>{address}</td><td>{date}</td><td>{custom}</td><td>{title}</td></tr>'.format(**j)
    for j in get_fuel(1, 'Cloverdale', 'Today')))

# ... for j in M))   # this should complement the assignment of M above. 

print(my_html) # Try 2 git

# Robin's code: writing file to the current folder (where anaconda python is first executed in this session)
# with open('table.html', 'w') as f:
#     f.write(html)

# Changing to the desired folder: 

folder = 'C:/PYTHON/2_Robin Workshop'
file_name = 'table.html'
with open(folder + '/' + file_name, 'w') as file:
    file.write(my_html)
print('\n', '...Writing data to: ', folder + '/' + file_name)
    
        




#%% Debugging 1 --------------------------------------------------
import feedparser
from urllib.parse import urlencode
import pprint

params = {
    'Product': 1,
    'Suburb': 'Cloverdale',
    'Day': 'Today'
}

data_source = 'http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?' + urlencode(params)
print('...Reading data from: ', data_source)

data = feedparser.parse(data_source)
read_data = pprint.pformat(data, indent = 4)

folder = 'C:/PYTHON/2_Robin Workshop'
file_name = 'read_data.txt'
with open(folder + '/' + file_name, 'w') as file:
    file.write(read_data)
print('...Writing data to: ', folder + '/' + file_name)

fuel_list = [
    {
        'brand': i['brand'],
        'price': float(i['price']),
        'date': i['date'],
        'location': i['location'],
        'address': i['address'],
        'title': i['title'],
        'custom': 'blah2',
    }
    for i in data['entries']    
]

print('Number of items: ', len(data['entries']))



#%% 

# --------------------------------------------------------
# This is the long way to write code:
    
tr_list = [
    '<tr><td>{location}</td><td>{price}</td></tr>'.format(**j)  # List destructuring
    for j in  fuel_list
]
   
my_html = '<table>'+ ''.join(tr_list) + '</table>'

my_html = '<table>'+ ''.join(
    '<tr><td>{location}</td><td>{price}</td></tr>'.format(**j)
    for j in  fuel_list
) + '</table>'


#%% 




#%% 




#%% 




#%% 




#%% 




 


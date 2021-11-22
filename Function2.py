def extract_info(info):
    return [info.get('pincode'),info.get('city')+':City',info.get('state'),info.get('country')]
pincode,city,state,country = extract_info({'pincode':'752031','city':'Banpur','state':'Odisha',
              'country':'INDIA'})

print(pincode)
print(city)
print(state)
print(country)
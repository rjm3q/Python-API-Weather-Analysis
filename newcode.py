lng= []
lat= []
cname= []
county= []
date= []
cloud= []
hum= []
temp= []

incr= 1
print("Gathering Weather Data")
print("=-=-=-=--=-=-=-=-=-=-=-=-=-")

for city in cities:
    try:
        resp= requests.get(site+city).json()
        lng.append(resp['coord']['lon'])
        lat.append(resp['coord']['lat'])
        cname.append(resp['name'])
        country.append(resp['sys']['country'])
        date.append(resp['dt'])
        cloud.append(resp['clouds']['all'])
        hum.append(resp['main']['humidity'])
        temp.append(resp['main']['temp_max'])
        count= resp['name']
        print()
        print(site+city)
        incr= incr + 1
        time.sleep(1.05)
        
    except:
        print(f"Gathering city {incr} || ... City not located... trying a better city...")
        #incr= incr + 1
    continue
print("=-=-=-=--=-=-=-=-=-=-=-=-=-")
print("Data Gathering Completed")

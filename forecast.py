
print()
print()
print("-----Welcome to My Little Forecast!-----")
print(">> Here you can get infromation about the weather in your region")

while True:
    print(">> Do you want to get a short report, or a detailed one? (s/d)")
    answ = input(">> ")
    if (answ=="s"):
        # provide a short report
        break
    elif (answ=="d"):
        flag = 1
        # provide a detailed report
        break
    else:
        print("Your answer is a bit confusing, try typing s or d depending on whether you'd like the short or longer form of weather report")


# # Using socket module to get user's IP adress
# import socket
# hostname = socket.gethostname()
# ip_address = socket.gethostbyname(hostname)
# print(f"Hostname: {hostname}")
# print(f"IP Address: {ip_address}")

from requests import get
ip = '208.67.222.221'

# using ipapi service to get the latitude and longitude of the user's IP
# from documetation of the resource:


# curl https://ipapi.co/8.8.8.8/json/
# {
# "ip" : "8.8.8.8"
# "city" : "Mountain View"
# "region" : "California"
# "region_code" : "CA"
# "country_code" : "US"
# "country_code_iso3" : "USA"
# "country_name" : "United States"
# "country_capital" : "Washington"
# "country_tld" : ".us"
# "continent_code" : "NA"
# "in_eu" : false
# "postal" : "94035"
# "latitude" : 37.386
# "longitude" : -122.0838
# "timezone" : "America/Los_Angeles"
# "utc_offset" : "-0800"
# "country_calling_code" : "+1"
# "currency" : "USD"
# "currency_name" : "Dollar"
# "languages" : "en-US,es-US,haw"
# "asn" : "AS15169"
# "org" : "Google LLC"
# }


# curl https://ipapi.co/8.8.8.8/country/
# US
# curl https://ipapi.co/8.8.8.8/city/
# Mountain View
# curl https://ipapi.co/8.8.8.8/latitude/
# 37.3845
# curl https://ipapi.co/8.8.8.8/latlong/   <--- can define location quite percisely
# 37.384500,-122.088100
# curl https://ipapi.co/8.8.8.8/org/
# Google Inc.

# latlong = get('https://ipapi.co/{}/latlong/'.format(ip)).text.split(',')
# if ("True" in latlong[0]):
#     print("I'm sorry, something went wrong while retrieving the data ;(")
#     print("Check your internet connection and try again")

latlong = ["37.77","122.39"]
weather = get('https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid={API key}').json()
print()



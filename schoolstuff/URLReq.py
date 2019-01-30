def main():
    import re
    import urllib.request
    print("Current observations are available for:")
    cities = {
        "New London": "https://w1.weather.gov/xml/current_obs/KGON.xml",
        "New York": "https://w1.weather.gov/xml/current_obs/KJRB.xml",
        "Houston": "https://w1.weather.gov/xml/current_obs/KIAH.xml",
        "Los Angeles": "https://w1.weather.gov/xml/current_obs/KIAH.xml"
    }
    for k in cities.keys():
        print('-', k)
    print()
    city_entry = input("Enter a city you would like a weather report for: ").title()
    while city_entry not in cities.keys():
        print("No data available.")
        city_entry = input("Enter a city you would like a weather report for: ").title()
    print("Accessing weather data . . . ")
    city_weath = urllib.request.urlopen(cities[city_entry])
    print("The current weather data has been accessed for", city_entry, '\n')
    city_weather = city_weath.read()
    city_str = str(city_weather)
    weath_info = {
        'location': re.search('(<location>)(.*)(</location>)', city_str).group(2),
        'weather': re.search('(<weather>)(.*)(</weather>)', city_str).group(2),
        'temperature': re.search('(<temp_f>)(.*)(</temp_f>)', city_str).group(2) + " in degrees F",
        'humidity': re.search('(<relative_humidity>)(.*)(</relative_humidity>)', city_str).group(2) + "%",
        'wind': re.search('(<wind_string>)(.*)(</wind_string>)', city_str).group(2),
        'observation': re.search('(<observation_time>)(.*)(</observation_time>)', city_str).group(2)
    }
    print("Information available:")
    for k in weath_info.keys():
        print('-', k)
    print()
    infosearch = input("What weather information would you like? ").lower()
    while infosearch != 'done':
        try:
            print("The", infosearch, 'in', city_entry, 'is', weath_info[infosearch], '\n')
        except KeyError:
            print("That data is not available.\n")
            infosearch = input("What weather information would you like? Or, to end, enter \"done\". ").lower()
        else:
            infosearch = input("What weather information would you like? Or, to end, enter \"done\". ").lower()
    export = input("Would you like to export a weather report? (yes/no)")
    if export == 'yes':
        print("A full weather report has been exported.")
        file = open(city_entry+" Weather Report.txt", 'w')
        file.write("Weather for "+city_entry+'\n\n')
        for k in weath_info.items():
            file.write(str(k[0].title()+':'+" "+k[1]+'\n'))
        file.close()


def alt_main():
    import re
    import html.parser
    import xml.etree.ElementTree
    import urllib.request
    alltags = []
    alldata = []
    class HTMLParser(html.parser.HTMLParser):

        def handle_starttag(self, tag, attrs):
            alltags.append(tag)

        def handle_endtag(self, tag):
            alltags.append(tag)

        def handle_data(self, data):
            alldata.append(data)



    stations = urllib.request.urlopen("https://w1.weather.gov/xml/current_obs/index.xml")
    states_source = urllib.request.urlopen("https://abbreviations.yourdictionary.com/articles/state-abbrev.html")
    states_raw = states_source.read()
    states_str = str(states_raw)
    htmlparse = HTMLParser()
    states_html = htmlparse.feed(states_str)
    alldata_str = "".join(alldata)
    def countrysearch(x):
        return re.search(r"(State Postal Abbreviations List)(.*)(Additional)", x).group(2)
    countries = countrysearch(alldata_str)
    countriesformat = re.sub(r'(-)', '', countries).strip().split("  ")
    countriesformat.remove(" US Commonwealth and Territories")
    states = {}
    for i in range(0, len(countriesformat), 2):
        states[countriesformat[i]] = countriesformat[i+1]
    alldata.clear()
    alltags.clear()
    # for k in states.items():
    #     print(k)


    # station_xml = xml.etree.ElementTree.parse(stations)
    # stationroot = station_xml.getroot()
    # station_ids = {}
    # for c in stationroot.findall("station"):
    #     stationid = c.find("station_id").text
    #     name = c.find("station_name").text
    #     state = c.find("state").text
    #     station_ids[stationid] = [name, state]
    # for k in station_ids.items():
    #     print(k)

    # print("Current observations are available for:")
    # cities = {
    #     "New London": "https://w1.weather.gov/xml/current_obs/KGON.xml",
    #     "New York": "https://w1.weather.gov/xml/current_obs/KJRB.xml",
    #     "Houston": "https://w1.weather.gov/xml/current_obs/KIAH.xml",
    #     "Los Angeles": "https://w1.weather.gov/xml/current_obs/KIAH.xml"
    # }
    # for k in cities.keys():
    #     print('-', k)
    # print()
    # city_entry = input("Enter a city you would like a weather report for: ").title()
    # while city_entry not in cities.keys():
    #     print("No data available.")
    #     city_entry = input("Enter a city you would like a weather report for: ").title()
    # print("Accessing weather data . . . ")
    # city_weath = urllib.request.urlopen(cities[city_entry])
    # print("The current weather data has been accessed for", city_entry, '\n')
    # print("Information available:")
    # city_xml = xml.etree.ElementTree.parse(city_weath)
    # root = city_xml.getroot()
    # weath_attr = {}
    # for c in root:
    #     weath_attr[c.tag.replace('_', " ")] = c.text
    # for k in weath_attr.keys():
    #     print(k)
    # infosearch = input("What weather information would you like? ").lower()
    # while infosearch != 'done':
    #     try:
    #         print("The", infosearch, 'in', city_entry, 'is', weath_attr[infosearch], '\n')
    #     except KeyError:
    #         print("That data is not available.\n")
    #         infosearch = input("What weather information would you like? Or, to end, enter \"done\". ").lower()
    #     else:
    #         infosearch = input("What weather information would you like? Or, to end, enter \"done\". ").lower()
    #     export = input("Would you like to export a weather report? (yes/no)")
    #     if export == 'yes':
    #         print("A full weather report has been exported.")
    #         file = open(city_entry+" Weather Report.txt", 'w')
    #         file.write("Weather for "+city_entry+'\n\n')
    #         for k in weath_attr.items():
    #             file.write(str(k[0].title()+':'+" "+k[1]+'\n'))
    #         file.close()


alt_main()

import datetime
import time
import pytz
from time import strftime
import sys
utc_dt = datetime.datetime.now(datetime.timezone.utc)
time_format_p1 = strftime("%a, %d %b %Y")
time_format_p2= strftime("%H:%M:%S")

__dictionary__ = {
    "GMT" : pytz.timezone('Universal'),
    "GMT-1" : pytz.timezone('Etc/GMT+1'),
    "GMT-2" : pytz.timezone('Etc/GMT+2'),
    "GMT-3" : pytz.timezone('Etc/GMT+3'),
    "GMT-4" : pytz.timezone('Etc/GMT+4'),
    "GMT-5" : pytz.timezone('Etc/GMT+5'),
    "GMT-6" : pytz.timezone('Etc/GMT+6'),
    "GMT-7" : pytz.timezone('Etc/GMT+7'),
    "GMT-8" : pytz.timezone('Etc/GMT+8'),
    "GMT-9" : pytz.timezone('Etc/GMT+9'),
    "GMT-10" : pytz.timezone('Etc/GMT+10'),
    "GMT-11" : pytz.timezone('Etc/GMT+11'),
    "GMT-12" : pytz.timezone('Etc/GMT+12'),
    "GMT+1" : pytz.timezone('Etc/GMT-1'),
    "GMT+2" : pytz.timezone('Etc/GMT-2'),
    "GMT+3" : pytz.timezone('Etc/GMT-3'),
    "GMT+4" : pytz.timezone('Etc/GMT-4'),
    "GMT+5" : pytz.timezone('Etc/GMT-5'),
    "GMT+6" : pytz.timezone('Etc/GMT-6'),
    "GMT+7" : pytz.timezone('Etc/GMT-7'),
    "GMT+8" : pytz.timezone('Etc/GMT-8'),
    "GMT+9" : pytz.timezone('Etc/GMT-9'),
    "GMT+10" : pytz.timezone('Etc/GMT-10'),
    "GMT+11" : pytz.timezone('Etc/GMT-11'),
    "GMT+12" : pytz.timezone('Etc/GMT-12'),
    "MART" : pytz.timezone('Pacific/Marquesas'),#all timezones with less than 1 hour difference - GMT-9:30
    "NDT" : pytz.timezone('Canada/Newfoundland'),#GMT-2:30
    "IRDT" : pytz.timezone('Iran'), #GMT+4:30
    "IST" :  pytz.timezone('Asia/Colombo'), #GMT+5:30
    "NPT" : pytz.timezone('Asia/Katmandu'),#GMT+5:45
    "CCT" : pytz.timezone('Indian/Cocos'), #GMT+6:30
    "CWST" : pytz.timezone('Australia/Eucla'),#GMT+8:45
    "ACST" : pytz.timezone('Australia/Yancowinna'),#GMT+9:30
    "LHST" : pytz.timezone('Australia/Lord_Howe'),#GMT+10:30
    "CHAST" : pytz.timezone('NZ-CHAT'),#GMT+12:45

}
# complete 34 timezones. 34 complete.
"""
    elif __timezone__ == "" or __timezone__ == "" or __timezone__ == "" or __timezone__ == "" or __timezone__ == "" or __timezone__ == "" or __timezone__ == "" or __timezone__ == "" or __timezone__ == "" or __timezone__ == "" or __timezone__ == "" or __timezone__ == "":
        print("format: year, month, isoformat or datetime day, datetime hour, minute, second, milisecond")
        bool = True
        while bool == True:
            for timezone in __dictionary__:
                time.sleep(1)
                print(f"time in {__timezone__}",  end=' ')
                print("in isoformat: {}".format(datetime.datetime.now(__dictionary__[""]).isoformat('T')))
                print(f"time in {__timezone__}:              {(datetime.datetime.now(__dictionary__['']))}")
# copy paste
"""
print("All timezones must be uppercase")
print('All location names should be capital city or a famous city or province or state')
__timezone__ = input("input short form of time zone or generalized location name: ")

def all_timezones():
    if __timezone__ == "cvst" or __timezone__ == "Etc/GMT+1" or __timezone__ == "CVST" or __timezone__ == "AZOT" or __timezone__ == "EGT"  or __timezone__ == "Cape Verde":
        print("format: year, month, isoformat or datetime day, datetime hour, minute, second, milisecond")
        bool = True
        while bool == True:
            for timezone in __dictionary__:
                time.sleep(1)
                print(f"time in {__timezone__}",  end=' ')
                print("in isoformat: {}".format(datetime.datetime.now(__dictionary__["GMT-1"]).isoformat('T')))
                print(f"time in {__timezone__}:              {(datetime.datetime.now(__dictionary__['GMT-1']))}")
    elif __timezone__ == "GMT-2" or __timezone__ == "Etc/GMT+2" or __timezone__ == "BRST" or __timezone__ == "FNT" or __timezone__ == "GST" or __timezone__ == "PMDT" or __timezone__ == "UYST" or __timezone__ == "WGST"  or __timezone__ == "Noronha" or __timezone__ == "South Georgia" or __timezone__ == "Nuuk" or __timezone__ == "Miquelon":
        print("format: year, month, isoformat or datetime day, datetime hour, minute, second, milisecond")
        bool = True
        while bool == True:
            for timezone in __dictionary__:
                time.sleep(1)
                print(f"time in {__timezone__}",  end=' ')
                print("in isoformat: {}".format(datetime.datetime.now(__dictionary__["GMT-2"]).isoformat('T')))
                print(f"time in {__timezone__}:              {(datetime.datetime.now(__dictionary__['GMT-2']))}")
    elif __timezone__ == "GMT-3" or __timezone__ == "Etc/GMT+3" or __timezone__ == "ADT" or __timezone__ == "AMST" or __timezone__ == "ART" or __timezone__ == "BRT" or __timezone__ == "CLST" or __timezone__ == "FKST"or __timezone__ == "GFT" or __timezone__ == "PMST" or __timezone__ == "PYST" or __timezone__ == "ROTT" or __timezone__ == "SRT" or __timezone__ == "UYT" or __timezone__ == "WGST" or __timezone__ == "Palmer" or __timezone__ == "Cayenne" or __timezone__ == "Bermuda" or __timezone__ == "San Luis" or __timezone__ == "Argentina" or __timezone__ == "Halifax" or __timezone__ == "Buenos Aires" or __timezone__ == "Cordoba" or __timezone__ == "Belem" or __timezone__ == "Goose Bay" or __timezone__ == "Thule" or __timezone__ == "Bahia" or __timezone__ == "Glace Bay" or __timezone__ == "Stanley" or __timezone__ == "Rio Gallegos" or __timezone__ == "Tucuman" or __timezone__ == "Araguina":
        print("format: year, month, isoformat or datetime day, datetime hour, minute, second, milisecond")
        bool = False
        while bool == False:
            for timezone in __dictionary__:
                time.sleep(1)
                print(f"time in {__timezone__}", end=' ')
                print("in isoformat: {}".format(datetime.datetime.now(__dictionary__["GMT-3"]).isoformat('T')))
                print(f"time in {__timezone__}:              {(datetime.datetime.now(__dictionary__['GMT-3']))}")
    elif __timezone__ == "EST" or __timezone__ == "Etc/GMT+4" or __timezone__ == "GMT-4" or __timezone__ == "AMT" or __timezone__ == "AST" or __timezone__ == "BOT" or __timezone__ == "CDT" or __timezone__ == "CLT" or __timezone__ == "COST" or __timezone__ == "FKT" or __timezone__ == "GYT" or __timezone__ == "VET" or __timezone__ == "Venezuela" or __timezone__ == "Grand Turk" or __timezone__ == "Puorta Rico" or __timezone__ == "EDT" or __timezone__ == "St Lucia" or __timezone__ == "St Thomas" or __timezone__ == "Toronto" or __timezone__ == "Waterloo" or __timezone__ == "Kitchener" or __timezone__ == "Iqaluit" or __timezone__ == "Ontario" or __timezone__ == "Monserrat" or __timezone__ == "Kentucky" or __timezone__ == "Detroit"or __timezone__ == "Blanc Soblon" or __timezone__ == "Santo Domingo" or __timezone__ == "Port of Spain" or __timezone__ == "Porto Velho" or __timezone__ == "Santiago" or __timezone__ == "Martinique" or __timezone__ == "Marigot" or __timezone__ == "St Vincent" or __timezone__ == "St Kitts" or __timezone__ == "Lower Princes" or __timezone__ == "Tortola" or __timezone__ == "Nipigon" or __timezone__ == "New York" or __timezone__ == "Thunder Bay" or __timezone__ == "Petersburg" or __timezone__ == "Indiana":
        bool = False
        print("format: year, month, isoformat or datetime hour, minute, second, milisecond")
        while bool == False:
            for timezone in __dictionary__:
                time.sleep(1)
                print(f"time in {__timezone__}",  end=' ')
                print("in isoformat: {}".format(datetime.datetime.now(__dictionary__["GMT-4"]).isoformat('T')))
                print(f"time in {__timezone__}:              {(datetime.datetime.now(__dictionary__['GMT-4']))}")
    elif __timezone__ == "GMT-5" or __timezone__ == "Etc/GMT+5" or __timezone__ == "ACT" or __timezone__ == "CDT" or __timezone__ == "COT" or __timezone__ == "CST" or __timezone__ == "EASST" or __timezone__ == "ECT" or __timezone__ == "PET" or __timezone__ == "Cayman" or __timezone__ == "Jamaica" or __timezone__ == "Winnipeg" or __timezone__ == "Mexico City"  or __timezone__ == "Chicago" or __timezone__ == "Coral Harbour" or __timezone__ == "Manitoba" or __timezone__ == "Lima" or __timezone__ == "Tell City" or __timezone__ == "Cancun" or __timezone__ == "Illinois" or __timezone__ == "Panama" or __timezone__ == "North Dakota" or __timezone__ == "Bismarck":
        print("format: year, month, isoformat or datetime day, datetime hour, minute, second, milisecond")
        bool = True
        while bool == True:
            for timezone in __dictionary__:
                time.sleep(1)
                print(f"time in {__timezone__}",  end=' ')
                print("in isoformat: {}".format(datetime.datetime.now(__dictionary__["GMT-5"]).isoformat('T')))
                print(f"time in {__timezone__}:              {(datetime.datetime.now(__dictionary__['GMT-5']))}")
    elif __timezone__ == "GALT" or __timezone__ == "Etc/GMT+6" or __timezone__ == "MDT" or __timezone__ == "MT" or __timezone__ == "MST" or __timezone__ == "El Salvador" or __timezone__ == "Regina" or __timezone__ == "Saskatchewan" or __timezone__ == "Yellowknife" or __timezone__ == "GMT-6" or __timezone__ == "Easter" or __timezone__ == "Edmonton" or __timezone__ == "Alberta" or __timezone__ == "Mazatlan" or __timezone__ == "Guatamala" or __timezone__ == "Galapagos" or __timezone__ == "Mazatlan" or __timezone__ == "Inuvik" or __timezone__ == "Chihhuahua" or __timezone__ == "Boise":
        print("format: year, month, isoformat or datetime day, datetime hour, minute, second, milisecond")
        bool = True
        while bool == True:
            for timezone in __dictionary__:
                time.sleep(1)
                print(f"time in {__timezone__}",  end=' ')
                print("in isoformat: {}".format(datetime.datetime.now(__dictionary__["GMT-6"]).isoformat('T')))
                print(f"time in {__timezone__}:              {(datetime.datetime.now(__dictionary__['GMT-6']))}")
    elif __timezone__ == "MST" or __timezone__ == "Etc/GMT+7" or __timezone__ == "PDT" or __timezone__ == "GMT-7" or __timezone__ == "Fort Nelson" or __timezone__ == "Vancouver" or __timezone__ == "Los Angeles" or __timezone__ == "White Horse" or __timezone__ == "Pheonix" or __timezone__ == "Hermosillo" or __timezone__ == "Creston" or __timezone__ == "Dawson" or __timezone__ == "Tijuana" or __timezone__ == "British Columbia" or __timezone__ == "Northwest Territories":
        print("format: year, month, isoformat or datetime day, datetime hour, minute, second, milisecond")
        bool = True
        while bool == True:
            for timezone in __dictionary__:
                time.sleep(1)
                print(f"time in {__timezone__}",  end=' ')
                print("in isoformat: {}".format(datetime.datetime.now(__dictionary__["GMT-7"]).isoformat('T')))
                print(f"time in {__timezone__}:              {(datetime.datetime.now(__dictionary__['GMT-7']))}")
    elif __timezone__ == "AKDT" or __timezone__ == "Etc/GMT+8" or __timezone__ == "CIST" or __timezone__ == "PST" or __timezone__ == "Yakutat" or __timezone__ == "Sitka" or __timezone__ == "Pitcairn" or __timezone__ == "Nome" or __timezone__ == "Juneau" or __timezone__ == "Metlakatla" or __timezone__ == "Anchorage" or __timezone__ == "Yukon" or __timezone__ == "Alaska":
        print("format: year, month, isoformat or datetime day, datetime hour, minute, second, milisecond")
        bool = True
        while bool == True:
            for timezone in __dictionary__:
                time.sleep(1)
                print(f"time in {__timezone__}",  end=' ')
                print("in isoformat: {}".format(datetime.datetime.now(__dictionary__["GMT-8"]).isoformat('T')))
                print(f"time in {__timezone__}:              {(datetime.datetime.now(__dictionary__['GMT-8']))}")
    elif __timezone__ == "AKST" or __timezone__ == "Etc/GMT+9" or __timezone__ == "GAMT" or __timezone__ == "GIT" or __timezone__ == "HADT" or __timezone__ == "Gambier" or __timezone__ == "Adak" or __timezone__ == "GMT-9":
        print("format: year, month, isoformat or datetime day, datetime hour, minute, second, milisecond")
        bool = True
        while bool == True:
            for timezone in __dictionary__:
                time.sleep(1)
                print(f"time in {__timezone__}",  end=' ')
                print("in isoformat: {}".format(datetime.datetime.now(__dictionary__["GMT-9"]).isoformat('T')))
                print(f"time in {__timezone__}:              {(datetime.datetime.now(__dictionary__['GMT-9']))}")
    elif __timezone__ == "GMT-10" or __timezone__ == "Etc/GMT+10" or __timezone__ == "CKT" or __timezone__ == "HAST" or __timezone__ == "Hawaii" or __timezone__ == "Taht" or __timezone__ == "Honululu" or __timezone__ == "Rarotonga" or __timezone__ == "Tahiti":
        print("format: year, month, isoformat or datetime day, datetime hour, minute, second, milisecond")
        bool = True
        while bool == True:
            for timezone in __dictionary__:
                time.sleep(1)
                print(f"time in {__timezone__}",  end=' ')
                print("in isoformat: {}".format(datetime.datetime.now(__dictionary__["GMT-10"]).isoformat('T')))
                print(f"time in {__timezone__}:              {(datetime.datetime.now(__dictionary__['GMT-10']))}")
    elif __timezone__ == "NUT" or __timezone__ == "GMT-11" or __timezone__ == "Etc/GMT+11" or __timezone__ == "SST" or __timezone__ == "Midway" or __timezone__ == "Niue" or __timezone__ == "Pago Pago" :
        print("format: year, month, isoformat or datetime day, datetime hour, minute, second, milisecond")
        bool = True
        while bool == True:
            for timezone in __dictionary__:
                time.sleep(1)
                print(f"time in {__timezone__}",  end=' ')
                print("in isoformat: {}".format(datetime.datetime.now(__dictionary__["GMT-11"]).isoformat('T')))
                print(f"time in {__timezone__}:              {(datetime.datetime.now(__dictionary__['GMT-11']))}")
    elif __timezone__ == "BIT" or __timezone__ == "Etc/GMT+12" or __timezone__ == "GMT-12" or __timezone__ == "Howland Island" or __timezone__ == "Baker Island":
        print("format: year, month, isoformat or datetime day, datetime hour, minute, second, milisecond")
        bool = True
        while bool == True:
            for timezone in __dictionary__:
                time.sleep(1)
                print(f"time in {__timezone__}",  end=' ')
                print("in isoformat: {}".format(datetime.datetime.now(__dictionary__["GMT-12"]).isoformat('T')))
                print(f"time in {__timezone__}:              {(datetime.datetime.now(__dictionary__['GMT-12']))}")
    elif __timezone__ == "GMT+1" or __timezone__ == "Etc/GMT-1" or __timezone__ == "BST" or __timezone__ == "CET" or __timezone__ == "CET" or __timezone__ == "Irland time" or __timezone__ == "Irland" or __timezone__ == "WAT" or __timezone__ == "WEST" or __timezone__ == "Algiers" or __timezone__ == "Brazzaville" or __timezone__ == "Douala" or __timezone__ == "Niamey" or __timezone__ == "Tunis" or __timezone__ == "Faroe" or __timezone__ == "Dublin" or __timezone__ == "Isle of Man" or __timezone__ == "Lisbon" or __timezone__ == "Bangui" or __timezone__ == "Casablanca" or __timezone__ == "El Aiun" or __timezone__ == "Lagos" or __timezone__ == "Luanda" or __timezone__ == "Ndjamena" or __timezone__ == "Porto Novo" or __timezone__ == "Canary" or __timezone__ == "Maderia" or __timezone__ == "Guernsey" or __timezone__ == "Jersey" or __timezone__ == "London"  or __timezone__ == "UK" or __timezone__ == "United Kingdom":
        print("format: year, month, isoformat or datetime day, datetime hour, minute, second, milisecond")
        bool = True
        while bool == True:
            for timezone in __dictionary__:
                time.sleep(1)
                print(f"time in {__timezone__}",  end=' ')
                print("in isoformat: {}".format(datetime.datetime.now(__dictionary__["GMT+1"]).isoformat('T')))
                print(f"time in {__timezone__}:              {(datetime.datetime.now(__dictionary__['GMT+1']))}")
    elif __timezone__ == "CAT" or __timezone__ == "Etc/GMT-2" or __timezone__ == "CEST" or __timezone__ == "GMT+2" or __timezone__ == "EET" or __timezone__ == "Israel" or __timezone__ == "Israel time" or __timezone__ == "SAST" or __timezone__ == "USZ1" or __timezone__ == "WAST" or __timezone__ == "Cairo" or __timezone__ == "Tripoli" or __timezone__ == "Blantyre" or __timezone__ == "Bujumbra" or __timezone__ == "Ceuta" or __timezone__ == "Longyearbyen" or __timezone__ == "Harare" or __timezone__ == "Juba" or __timezone__ == "Johannesburg" or __timezone__ == "Troll" or __timezone__ == "Amsterdam" or __timezone__ == "Belgrade" or __timezone__ == "Budapest" or __timezone__ == "Luxembourg" or __timezone__ == "Kaliningrad" or __timezone__ == "Oslo" or __timezone__ == "Malta" or __timezone__ == "Berlin" or __timezone__ == "Brussels" or __timezone__ == "Gibraltar" or __timezone__ == "Copenhagen" or __timezone__ == "Rome" or __timezone__ == "Vienna" or __timezone__ == "Stockholm" or __timezone__ == "Zurich" or __timezone__ == "Warsaw" or __timezone__ == "San Marino" or __timezone__ == "Madrid" or __timezone__ == "Paris" or __timezone__ == "Monaco" or __timezone__ == "Vaduz" or __timezone__ == "Vatican" or __timezone__ == "Sarajevo" or __timezone__ == "Windhoek" or __timezone__ == "Khartoum" or __timezone__ == "Kigali" or __timezone__ == "Podgorica" or __timezone__ == "Maseru" or __timezone__ == "Andorra":
        print("format: year, month, isoformat or datetime day, datetime hour, minute, second, milisecond")
        bool = True
        while bool == True:
            for timezone in __dictionary__:
                time.sleep(1)
                print(f"time in {__timezone__}",  end=' ')
                print("in isoformat: {}".format(datetime.datetime.now(__dictionary__["GMT+2"]).isoformat('T')))
                print(f"time in {__timezone__}:              {(datetime.datetime.now(__dictionary__['GMT+2']))}")
    elif __timezone__ == "AST" or __timezone__ == "Etc/GMT-3" or __timezone__ == "EAT" or __timezone__ == "EEST" or __timezone__ == "FET" or __timezone__ == "IDT" or __timezone__ == "MSK" or __timezone__ == "Moscow" or __timezone__ == "Showa" or __timezone__ == "MSK" or __timezone__ == "SYOT" or __timezone__ == "TRT" or __timezone__ == "Istanbul" or __timezone__ == "Ankara" or __timezone__ == "Izmir" or __timezone__ == "Bahrain" or __timezone__ == "Kuwait" or __timezone__ == "Qatar" or __timezone__ == "Athens" or __timezone__ == "Nicosia" or __timezone__ == "Helsinki" or __timezone__ == "Damascus" or __timezone__ == "Hebron" or __timezone__ == "Bucharest" or __timezone__ == "Minsk" or __timezone__ == "Kirov" or __timezone__ == "Baghdad" or __timezone__ == "Nairobi" or __timezone__ == "Aden" or __timezone__ == "Simferepol" or __timezone__ == "Vilnius" or __timezone__ == "Comoro" or __timezone__ == "Sofia" or __timezone__ == "Mayette" or __timezone__ == "Hebron" or __timezone__ == "Gaza" or __timezone__ == "Amman" or __timezone__ == "Jerusalem" or __timezone__ == "Dijbouti" or __timezone__ == "Volvograd" or __timezone__ == "Vilnius" or __timezone__ == "Nicosia" or __timezone__ == "GMT+3" or __timezone__ == "Famagusta" or __timezone__ == "Beirut":
        print("format: year, month, isoformat or datetime day, datetime hour, minute, second, milisecond")
        bool = True
        while bool == True:
            for timezone in __dictionary__:
                time.sleep(1)
                print(f"time in {__timezone__}",  end=' ')
                print("in isoformat: {}".format(datetime.datetime.now(__dictionary__["GMT+3"]).isoformat('T')))
                print(f"time in {__timezone__}:              {(datetime.datetime.now(__dictionary__['GMT+3']))}")
    elif __timezone__ == "GMT+4" or __timezone__ == "Etc/GMT-4" or __timezone__ == "AMT" or __timezone__ == "GET" or __timezone__ == "AZT" or __timezone__ == "GST" or __timezone__ == "RET" or __timezone__ == "MUT" or __timezone__ == "SCT" or __timezone__ == "SAMT" or __timezone__ == "VOLT" or __timezone__ == "Mauritius" or __timezone__ == "Dubai" or __timezone__ == "Seychelles" or __timezone__ == "Volgograd" or __timezone__ == "Saratov" or __timezone__ == "Samara" or __timezone__ == "Ulyanovsk" or __timezone__ == "Reunion" or __timezone__ == "Mahe" or __timezone__ == "Astrakhan" or __timezone__ == "Tbilisi" or __timezone__ == "Muscat" or __timezone__ == "Yerevan" or __timezone__ == "Baku" or __timezone__ == "Samara" or __timezone__ == "Azerbaijan" or __timezone__ == "Armenia":
        print("format: year, month, isoformat or datetime day, datetime hour, minute, second, milisecond")
        bool = True
        while bool == True:
            for timezone in __dictionary__:
                time.sleep(1)
                print(f"time in {__timezone__}",  end=' ')
                print("in isoformat: {}".format(datetime.datetime.now(__dictionary__["GMT+4"]).isoformat('T')))
                print(f"time in {__timezone__}:              {(datetime.datetime.now(__dictionary__['GMT+4']))}")
    elif __timezone__ == "GMT+5" or __timezone__ == "Etc/GMT-5" or __timezone__ == "HMT" or __timezone__ == "MAWT" or __timezone__ == "MVT" or __timezone__ == "ORAT" or __timezone__ == "PKT" or __timezone__ == "TFT" or __timezone__ == "TJT" or __timezone__ == "TMT" or __timezone__ == "UZT" or __timezone__ == "Yekt" or __timezone__ == "Mawson" or __timezone__ == "Aqtobe" or __timezone__ == "Atyrau" or __timezone__ == "Karachi" or __timezone__ == "Qyzylorda" or __timezone__ == "Tashkent" or __timezone__ == "Kerguelen" or __timezone__ == "Aqtau" or __timezone__ == "Ashgabat" or __timezone__ == "Dushanbe" or __timezone__ == "Oral" or __timezone__ == "Samarkand" or __timezone__ == "Yekaterinburg" or __timezone__ == "Maldives" :
        print("format: year, month, isoformat or datetime day, datetime hour, minute, second, milisecond")
        bool = True
        while bool == True:
            for timezone in __dictionary__:
                time.sleep(1)
                print(f"time in {__timezone__}",  end=' ')
                print("in isoformat: {}".format(datetime.datetime.now(__dictionary__["GMT+5"]).isoformat('T')))
                print(f"time in {__timezone__}:              {(datetime.datetime.now(__dictionary__['GMT+5']))}")
    elif __timezone__ == "GMT+6" or __timezone__ == "Etc/GMT-6" or __timezone__ == "BST" or __timezone__ == "BTT" or __timezone__ == "IOT" or __timezone__ == "KGT" or __timezone__ == "OMST" or __timezone__ == "VOST" or __timezone__ == "Vostok" or __timezone__ == "Bishek" or __timezone__ == "Omsk" or __timezone__ == "Thimphu" or __timezone__ == "Chagos" or __timezone__ == "Almaty" or __timezone__ == "Dhaka" or __timezone__ == "Qostanay" or __timezone__ == "Urumqi":
        print("format: year, month, isoformat or datetime day, datetime hour, minute, second, milisecond")
        bool = True
        while bool == True:
            for timezone in __dictionary__:
                time.sleep(1)
                print(f"time in {__timezone__}",  end=' ')
                print("in isoformat: {}".format(datetime.datetime.now(__dictionary__["GMT+6"]).isoformat('T')))
                print(f"time in {__timezone__}:              {(datetime.datetime.now(__dictionary__['GMT+6']))}")
    elif __timezone__ == "GMT+7" or __timezone__ == "Etc/GMT-7" or __timezone__ == "CXT" or __timezone__ == "DAVT" or __timezone__ == "HOVT" or __timezone__ == "ICT" or __timezone__ == "KRAT" or __timezone__ == "THA" or __timezone__ == "Thailand" or __timezone__ == "WIB" or __timezone__ == "Western Indonesia" or __timezone__ == "Davis" or __timezone__ == "Barnaul" or __timezone__ == "Hovd" or __timezone__ == "Krasnoyarsk" or __timezone__ == "Novosibirsk" or __timezone__ == "Pontianak" or __timezone__ == "Vientiane" or __timezone__ == "Bangkok" or __timezone__ == "Ho Chi Minh" or __timezone__ == "Tomsk" or __timezone__ == "Phnom Penh" or __timezone__ == "Novokuznetsk" or __timezone__ == "Jakarta" or __timezone__ == "Christmas":
        print("format: year, month, isoformat or datetime day, datetime hour, minute, second, milisecond")
        bool = True
        while bool == True:
            for timezone in __dictionary__:
                time.sleep(1)
                print(f"time in {__timezone__}",  end=' ')
                print("in isoformat: {}".format(datetime.datetime.now(__dictionary__["GMT+7"]).isoformat('T')))
                print(f"time in {__timezone__}:              {(datetime.datetime.now(__dictionary__['GMT+7']))}")
    elif __timezone__ == "GMT+8" or __timezone__ == "Etc/GMT-8" or __timezone__ == "AWST" or __timezone__ == "BDT" or __timezone__ == "BNT" or __timezone__ == "CHOT" or __timezone__ == "CIT" or __timezone__ == "CST" or __timezone__ == "HKT" or __timezone__ == "IRKT" or __timezone__ == "MST" or __timezone__ == "MYT" or __timezone__ == "PHT" or __timezone__ == "PST" or __timezone__ == "SGT" or __timezone__ == "ULAT" or __timezone__ == "WST" or __timezone__ == "Brunei" or __timezone__ == "Hong Kong" or __timezone__ == "Kuala Lumpur" or __timezone__ == "Macau" or __timezone__ == "Manila" or __timezone__ == "Singapore" or __timezone__ == "Ulaanbaatar" or __timezone__ == "Choibalsan" or __timezone__ == "Irkutsuk" or __timezone__ == "Makassar" or __timezone__ == "Kuching" or __timezone__ == "Shanghai" or __timezone__ == "Taipei" or __timezone__ == "Perth":
        print("format: year, month, isoformat or datetime day, datetime hour, minute, second, milisecond")
        bool = True
        while bool == True:
            for timezone in __dictionary__:
                time.sleep(1)
                print(f"time in {__timezone__}",  end=' ')
                print("in isoformat: {}".format(datetime.datetime.now(__dictionary__["GMT+8"]).isoformat('T')))
                print(f"time in {__timezone__}:              {(datetime.datetime.now(__dictionary__['GMT+8']))}")
    elif __timezone__ == "GMT+9" or __timezone__ == "Etc/GMT-9" or __timezone__ == "CHOST" or __timezone__ == "EIT" or __timezone__ == "JST" or __timezone__ == "KST" or __timezone__ == "PWT" or __timezone__ == "TLT" or __timezone__ == "ULAST" or __timezone__ == "WIT" or __timezone__ == "YAKT" or __timezone__ == "Chita" or __timezone__ == "Jayapura" or __timezone__ == "Pyongyang" or __timezone__ == "Tokyo" or __timezone__ == "Seoul" or __timezone__ == "South Korea" or __timezone__ == "Yakutsk" or __timezone__ == "Palau" or __timezone__ == "Khandyga" or __timezone__ == "Dili" or __timezone__ == "Timor Leste":
        print("format: year, month, isoformat or datetime day, datetime hour, minute, second, milisecond")
        bool = True
        while bool == True:
            for timezone in __dictionary__:
                time.sleep(1)
                print(f"time in {__timezone__}",  end=' ')
                print("in isoformat: {}".format(datetime.datetime.now(__dictionary__["GMT+9"]).isoformat('T')))
                print(f"time in {__timezone__}:              {(datetime.datetime.now(__dictionary__['GMT+9']))}")
    elif __timezone__ == "AEST" or __timezone__ == "GMT+10" or __timezone__ == "Etc/GMT-10" or __timezone__ == "CHST" or __timezone__ == "CHUT" or __timezone__ == "DDUT" or __timezone__ == "PGT" or __timezone__ == "VLAT" or __timezone__ == "DumontDUrville" or __timezone__ == "Ust Nera" or __timezone__ == "Ust-Nera" or __timezone__ == "Brisbane" or __timezone__ == "Sydney" or __timezone__ == "Lindeman" or __timezone__ == "Guam" or __timezone__ == "Saipan" or __timezone__ == "Macquarie" or __timezone__ == "Vladivostok" or __timezone__ == "Hobart" or __timezone__ == "Melbourne" or __timezone__ == "Chuuk" or __timezone__ == "Port Moresby":
        print("format: year, month, isoformat or datetime day, datetime hour, minute, second, milisecond")
        bool = True
        while bool == True:
            for timezone in __dictionary__:
                time.sleep(1)
                print(f"time in {__timezone__}",  end='')
                print(" in isoformat: {}".format(datetime.datetime.now(__dictionary__["GMT+10"]).isoformat('T')))
                print(f"time in {__timezone__}:              {(datetime.datetime.now(__dictionary__['GMT+10']))}")
    elif __timezone__ == "GMT+11" or __timezone__ == "Etc/GMT-11" or __timezone__ == "AEDT" or __timezone__ == "BST" or __timezone__ == "KOST" or __timezone__ == "LHDT" or __timezone__ == "MAGT" or __timezone__ == "MIST" or __timezone__ == "NCT" or __timezone__ == "NFT" or __timezone__ == "PONT" or __timezone__ == "SAKT" or __timezone__ == "SBT" or __timezone__ == "SRET" or __timezone__ == "VUT" or __timezone__ == "Vanuatu" or __timezone__ == "Solomon Islands" or __timezone__ == "Solomon Island" or __timezone__ == "Solomon" or __timezone__ == "New Caledonia" or __timezone__ == "Magadan" or __timezone__ == "Casey" or __timezone__ == "Sakhalin" or __timezone__ == "Bougainville" or __timezone__ == "Guadalcanal" or __timezone__ == "Norfolk" or __timezone__ == "Pohnpei" or __timezone__ == "Micronesia" or __timezone__ == "Magadan" or __timezone__ == "Srednekolymsk" or __timezone__ == "Efate" or __timezone__ == "Kosroa" or __timezone__ == "Noumea":
        print("format: year, month, isoformat or datetime day, datetime hour, minute, second, milisecond")
        bool = True
        while bool == True:
            for timezone in __dictionary__:
                time.sleep(1)
                print(f"time in {__timezone__}",  end=' ')
                print("in isoformat: {}".format(datetime.datetime.now(__dictionary__["GMT+11"]).isoformat('T')))
                print(f"time in {__timezone__}:              {(datetime.datetime.now(__dictionary__['GMT+11']))}")
    elif __timezone__ == "GMT+12" or __timezone__ == "Etc/GMT-12" or __timezone__ == "FJT" or __timezone__ == "GILT" or __timezone__ == "MHT" or __timezone__ == "NRT" or __timezone__ == "NZST" or __timezone__ == "PETT" or __timezone__ == "TVT" or __timezone__ == "WAKT" or __timezone__ == "WFT" or __timezone__ == "Gilbert Island" or __timezone__ == "Marshall" or __timezone__ == "Nauru" or __timezone__ == "Tuvalu" or __timezone__ == "Wake Island" or __timezone__ == "Wallis" or __timezone__ == "Futuna" or __timezone__ == "Wallis and Futuna" or __timezone__ == "McMurdo" or __timezone__ == "Kamchatka" or __timezone__ == "Fiji" or __timezone__ == "Kwajalein" or __timezone__ == "Nauru" or __timezone__ == "Wake" or __timezone__ == "Anadyr" or __timezone__ == "Auckland" or __timezone__ == "Funafuti" or __timezone__ == "Majuro" or __timezone__ == "Tarawa":
        print("format: year, month, isoformat or datetime day, datetime hour, minute, second, milisecond")
        bool = True
        while bool == True:
            for timezone in __dictionary__:
                time.sleep(1)
                print(f"time in {__timezone__}",  end=' ')
                print("in isoformat: {}".format(datetime.datetime.now(__dictionary__["GMT+12"]).isoformat('T')))
                print(f"time in {__timezone__}:              {(datetime.datetime.now(__dictionary__['GMT+12']))}")
    #all timezones with less than 1 hour difference
    elif __timezone__ == "GMT-9:30" or __timezone__ == "Etc/GMT+9:30" or __timezone__ == "Marquesas" or __timezone__ == "Marquesas Islands" or __timezone__ == "Marquesas Island" or __timezone__ == "Pacific/Marquesas	" or __timezone__ == "MART" or __timezone__ == "MIT":
        print("format: year, month, isoformat or datetime day, datetime hour, minute, second, milisecond")
        bool = True
        while bool == True:
            for timezone in __dictionary__:
                time.sleep(1)
                print(f"time in {__timezone__}",  end=' ')
                print("in isoformat: {}".format(datetime.datetime.now(__dictionary__["MART"]).isoformat('T')))#GMT-9:30
                print(f"time in {__timezone__}:              {(datetime.datetime.now(__dictionary__['MART']))}")
    elif __timezone__ == "GMT-2:30" or __timezone__ == "Etc/GMT+2:30" or __timezone__ == "NDT" or __timezone__ == "ndt" or __timezone__ == "America/St Johns" or __timezone__ == "St Johns" or __timezone__ == "St. Johns" or __timezone__ == "St.Johns" or __timezone__ == "Newfoundland daylight" or __timezone__ == "Newfoundland Daylight":
        print("format: year, month, isoformat or datetime day, datetime hour, minute, second, milisecond")
        bool = True
        while bool == True:
            for timezone in __dictionary__:
                time.sleep(1)
                print(f"time in {__timezone__}",  end=' ')
                print("in isoformat: {}".format(datetime.datetime.now(__dictionary__["NDT"]).isoformat('T')))#GMT-2:30
                print(f"time in {__timezone__}:              {(datetime.datetime.now(__dictionary__['NDT']))}")
    elif __timezone__ == "GMT+4:30" or __timezone__ == "Etc/GMT-4:30" or __timezone__ == "IRDT" or __timezone__ == "AFT" or __timezone__ == "Afghanistan" or __timezone__ == "Iran Daylight" or __timezone__ == "Iran daylight" or __timezone__ == "Kabul" or __timezone__ == "Tehran" or __timezone__ == "Asia/Kabul" or __timezone__ == "Asia/Tehran":
        print("format: year, month, isoformat or datetime day, datetime hour, minute, second, milisecond")
        bool = False
        while bool == False:
            for timezone in __dictionary__:
                time.sleep(1)
                print(f"time in {__timezone__}",  end=' ')
                print("in isoformat: {}".format(datetime.datetime.now(__dictionary__["IRDT"]).isoformat('T')))#GMT+4:30
                print(f"time in {__timezone__}:              {(datetime.datetime.now(__dictionary__['IRDT']))}")
    elif __timezone__ == "GMT+5:30" or __timezone__ == "Etc/GMT-5:30" or __timezone__ == "Indian standard time" or __timezone__ == "IST" or __timezone__ == "India" or __timezone__ == "SLST" or __timezone__ == "Colombo" or __timezone__ == "Kolkata" or __timezone__ == "Sri Lanka standard" or __timezone__ == "Sri Lanka standard time" or __timezone__ == "Delhi" or __timezone__ == "Mumbai" or __timezone__ == "Chennai" or __timezone__ == "Sri Lanka":
        print("format: year, month, isoformat or datetime day, datetime hour, minute, second, milisecond")
        bool = True
        while bool == True:
            for timezone in __dictionary__:
                time.sleep(1)
                print(f"time in {__timezone__}",  end=' ')
                print("in isoformat: {}".format(datetime.datetime.now(__dictionary__["IST"]).isoformat('T')))#GMT+5:30
                print(f"time in {__timezone__}:              {(datetime.datetime.now(__dictionary__['IST']))}")
    elif __timezone__ == "GMT+5:45" or __timezone__ == "Etc/GMT-5:45" or __timezone__ == "NPT" or __timezone__ == "Nepal" or __timezone__ == "Nepal time" or __timezone__ == "Kathmandu" or __timezone__ == "Nepal time" or __timezone__ == "Nepal Time":
        print("format: year, month, isoformat or datetime day, datetime hour, minute, second, milisecond")
        bool = True
        while bool == True:
            for timezone in __dictionary__:
                time.sleep(1)
                print(f"time in {__timezone__}",  end=' ')
                print("in isoformat: {}".format(datetime.datetime.now(__dictionary__["NPT"]).isoformat('T')))#GMT+5:45
                print(f"time in {__timezone__}:              {(datetime.datetime.now(__dictionary__['NPT']))}")
    elif __timezone__ == "GMT+6:30" or __timezone__ == "Etc/GMT-6:30" or __timezone__ == "CCT" or __timezone__ == "MMT" or __timezone__ == "Yangon" or __timezone__ == "Cocos" or __timezone__ == "Keeling" or __timezone__ == "Myanmar":
        print("format: year, month, isoformat or datetime day, datetime hour, minute, second, milisecond")
        bool = True
        while bool == True:
            for timezone in __dictionary__:
                time.sleep(1)
                print(f"time in {__timezone__}",  end=' ')
                print("in isoformat: {}".format(datetime.datetime.now(__dictionary__["CCT"]).isoformat('T')))#GMT+6:30
                print(f"time in {__timezone__}:              {(datetime.datetime.now(__dictionary__['CCT']))}")
    elif __timezone__ == "GMT+8:45" or __timezone__ == "Etc/GMT-8:45" or __timezone__ == "CWST" or __timezone__ == "ACWST" or __timezone__ == "Australian Central Western Standard Time" or __timezone__ == "Central Western Standard Time" or __timezone__ == "Eucla":
        print("format: year, month, isoformat or datetime day, datetime hour, minute, second, milisecond")
        bool = True
        while bool == True:
            for timezone in __dictionary__:
                time.sleep(1)
                print(f"time in {__timezone__}",  end=' ')
                print("in isoformat: {}".format(datetime.datetime.now(__dictionary__["CWST"]).isoformat('T')))#GMT+8:45
                print(f"time in {__timezone__}:              {(datetime.datetime.now(__dictionary__['CWST']))}")
    elif __timezone__ == "GMT+9:30" or __timezone__ == "Etc/GMT-9:30" or __timezone__ == "ACST" or __timezone__ == "Australian Central Standard Time" or __timezone__ == "Adelaile" or __timezone__ == "Darwin" or __timezone__ == "Broken Hill":
        print("format: year, month, isoformat or datetime day, datetime hour, minute, second, milisecond")
        bool = True
        while bool == True:
            for timezone in __dictionary__:
                time.sleep(1)
                print(f"time in {__timezone__}",  end=' ')
                print("in isoformat: {}".format(datetime.datetime.now(__dictionary__["ACST"]).isoformat('T')))#GMT+9:30
                print(f"time in {__timezone__}:              {(datetime.datetime.now(__dictionary__['ACST']))}")
    elif __timezone__ == "GMT+10" or __timezone__ == "Etc/GMT-10" or __timezone__ == "LHST" or __timezone__ == "ACDT" or __timezone__ == "Lord Howe" or __timezone__ == "Australian Central Daylight Savings Time" or __timezone__ == "Lord Howe Standard Time":
        print("format: year, month, isoformat or datetime day, datetime hour, minute, second, milisecond")
        bool = True
        while bool == True:
            for timezone in __dictionary__:
                time.sleep(1)
                print(f"time in {__timezone__}",  end=' ')
                print("in isoformat: {}".format(datetime.datetime.now(__dictionary__["LHST"]).isoformat('T')))#GMT+10:30
                print(f"time in {__timezone__}:              {(datetime.datetime.now(__dictionary__['LHST']))}")
    elif __timezone__ == "GMT+12:45" or __timezone__ == "Etc/GMT-12:45" or __timezone__ == "CHAST" or __timezone__ == "Chatham Standard Time" or __timezone__ == "Chatham" or __timezone__ == "CHAT" or __timezone__ == "" or __timezone__ == "" or __timezone__ == "" or __timezone__ == "" or __timezone__ == "" or __timezone__ == "":
        print("format: year, month, isoformat or datetime day, datetime hour, minute, second, milisecond")
        bool = True
        while bool == True:
            for timezone in __dictionary__:
                time.sleep(1)
                print(f"time in {__timezone__}",  end=' ')
                print("in isoformat: {}".format(datetime.datetime.now(__dictionary__["CHAST"]).isoformat('T')))
                print(f"time in {__timezone__}:              {(datetime.datetime.now(__dictionary__['CHAST']))}")
    elif __timezone__ == "all" or __timezone__ == "All" or __timezone__ == "all timezones":
        for k,v in __dictionary__.items():
            print(k, ":", datetime.datetime.now(v))
    elif __timezone__ == "now" or __timezone__ == "NOW":
        print(f"date in Greenwich = {time_format_p1}")
        print("time in Greenwich is", end=' ')
        print(f"{time_format_p2}")
        print("press CTRL R to rerun the code and input city/country/province name or a timezone")
    else:
        print(f"{__timezone__} = invalid input", end ="")
        raise pytz.UnknownTimeZoneError#GMT+8 complete today. from GMT+6 to GMT+8.
        sys.exit()
all_timezones()


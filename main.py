from urllib.request import urlopen

thisBrowser = {
    "youtube": {
        "Home": "https://youtube.com",
        "About": "fwffrwf"
    }
}

def open_Tab(title, url):
    thisBrowser.update({title: url})

open_Tab("ali", "www.ali.com")
open_Tab("christmas", "https://isitchristmas.com")
open_Tab("alfi", "https://youtube.com")

print(thisBrowser)

# def close_tab(index):
#     i = 0
#     for key in thisBrowser.keys():
#         if i == index:
#             key_to_delete = key
#         i = i + 1
#     if key_to_delete in thisBrowser:
#         del thisBrowser[key_to_delete]
#
# def close_tab():
#     thisBrowser.popitem()
#
#
# close_tab()
# print(thisBrowser)

# def switchTabs(index):
#     i = 0
#     for key, value in thisBrowser.items():
#         if i == index:
#             value_to_open = value
#         i = i + 1
#     page = urlopen(value_to_open)
#
#     html_bytes = page.read()
#     html = html_bytes.decode("utf-8")
#     print(html)
#
# def switchTabs():
#     i = 0
#     for key, value in thisBrowser.items():
#         value_to_open = value
#         i = i + 1
#     page = urlopen(value_to_open)
#
#     html_bytes = page.read()
#     html = html_bytes.decode("utf-8")
#     print(html)
#
# switchTabs()








# def mainmenu():
#     while True:
#         print(" 1. Open Tab \n 2. Close Tab \n 3. Switch Tab \n 4. Display All Tabs \n 5. Open Nested Tab \n 6. Sort All Tabs \n 7. Save Tabs \n 8. Import Tabs \n 9. Exit")
#         try:
#             choice = int(input("Enter your choice: "))
#         except:
#             print("Please enter a number between 1 and 9:")
#             continue
#
#         while choice < 0 or choice > 9:
#             try:
#                 choice = int(input("Please enter a number between 1 and 9: "))
#             except:
#                 print("Please enter a number between 1 and 6:")
#
# mainmenu()
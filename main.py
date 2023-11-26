from urllib.request import urlopen
import json

thisBrowser = {

}
def open_Tab(title, url):
    thisBrowser[title] = {"url": url, "children": {}}


# ---------------------------------------------------------------------------------------------------

# for this function I used this website as a help:
# https://stackoverflow.com/questions/55480586/remove-an-element-from-dictionary-python-based-on-index

def close_tab(index):
    i = 0
    key_to_delete = None
    for key in thisBrowser.keys():
        if i == index:
            key_to_delete = key
            break
        i += 1

    if key_to_delete is not None:
        del thisBrowser[key_to_delete]
#
#
# close_tab(1)
# print(thisBrowser)

# --------------------------------------------------------------------------

# for web scrapping I used this link:
# https://realpython.com/python-web-scraping-practical-introduction/

def switchTabs(index):
    i = 0
    for key, value in thisBrowser.items():
        if i == index:
            value_to_open = value["url"]
            break
        i = i + 1

    page = urlopen(value_to_open)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8", errors="ignore")
    print(html)



def switchTabs():
    i = 0
    for key, value in thisBrowser.items():
        value_to_open = value["url"]
        break
    i = i + 1

    page = urlopen(value_to_open)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8", errors="ignore")
    print(html)


# ------------------------------------------------------------------------------
def displayTabs(thisBrowser, lvl=0):
    for title, tab in thisBrowser.items():
        print("   " * lvl + title)
        displayTabs(tab["children"], lvl + 1)


# --------------------------------------------------------

# in this function I declared a main_tab to none that will be later the key of user's input index,
# then in my loop when i = to the index of user's input it will take the key at this index and assigned it to main_tab
# then in my last line I'm updating my dict at the specific key of main_tab

def openNestedTabs(index,title,url):
    i = 0
    main_tab = None
    for key, value in thisBrowser.items():
        if i == index:
            main_tab = key
            break
        i += 1

    thisBrowser[main_tab]["children"][title] = {"url": url, "children": {}}
#
# openNestedTabs(1,"sajdns","dsajdsdk")
# displayTabs(thisBrowser,0)

# --------------------------------------------------------------------------------------

# in order to sort my dict I used insertion method, so first I took all the keys in the dict and insert them
# to the key list then for this key list I used insertion method from assignment 5, and then I created a new sorted dict
# that contains the sorted keys from key list.

def insertionSort(dict):
    keys = list(dict.keys())
    for i in range(1, len(keys)):
        j = i
        while keys[j - 1].lower() > keys[j].lower() and j > 0:
            keys[j - 1], keys[j] = keys[j], keys[j - 1]
            j -= 1

    sorted_dict = {key: dict[key] for key in keys}
    return sorted_dict



# -----------------------------------------------------------------------------
# I used this website as my refrence https://www.javatpoint.com/save-json-file-in-python

def saveTabs(file):
    save_file = open(file, "w")
    json.dump(thisBrowser, save_file, indent=6)
    save_file.close()


#
# # -------------------------------------------------------------------------------
def importTabs(file):
    import_file = open(file, "r")
    b =json.load(import_file)
    import_file.close()
    return b

def mainmenu():
    while True:
        print(" 1. Open Tab \n 2. Close Tab \n 3. Switch Tab \n 4. Display All Tabs \n 5. Open Nested Tab \n 6. Sort All Tabs \n 7. Save Tabs \n 8. Import Tabs \n 9. Exit")
        try:
            choice = int(input("Enter your choice: "))
        except:
            print("Please enter a number between 1 and 9:")
            continue

        while choice < 0 or choice > 9:
            try:
                choice = int(input("Please enter a number between 1 and 9: "))
            except:
                print("Please enter a number between 1 and 6:")

        if choice == 1:
            try:
                title = input("Enter your tab title: ")
                while title in thisBrowser:
                    print(title, "already exists in these Tabs")
                    title = input("Enter a non-existing tab title: ")
                url = input("Enter your tab url: ")
                open_Tab(title, url)

            except:
                print("An error occurred")

        if choice == 2:
            try:
                tabToClose = int(input("Enter the index you want to close the tab at: "))
                if 0 <= tabToClose < len(thisBrowser):
                    close_tab(tabToClose)
                else:
                    print("There is no tab at this index.")
            except:
                print("An error occurred")

        if choice == 3:
            try:
                displayedIndex = input("What is the index of the tab you want to display: ")
                # I got this strip function from https://www.javatpoint.com
                if displayedIndex.strip():
                    displayedIndex = int(displayedIndex)
                    switchTabs(displayedIndex)
                else:
                    switchTabs()
            except:
                print("An error occurred")

        if choice == 4:
            try:
                displayTabs(thisBrowser,0)
            except:
                print("An error occurred")

        if choice == 5:
            try:
                existedIndex = int(input("what is the index you want to add to: "))
                newTitle = input("what is the title you want to enter: ")
                newUrl = input("what is the new url you want to add: ")
                openNestedTabs(existedIndex,newTitle,newUrl)
            except:
                print("An error occurred")

        if choice == 6:
            try:
                insertionSort(thisBrowser)
                thisBrowser = insertionSort(thisBrowser)
                displayTabs(thisBrowser)

            except:
                print("An error occurred")

        if choice == 7:
            try:
                file = input("Enter the name of file you want to save the tabs into: ")
                saveTabs(file)
            except:
                print("An error occurred")

        if choice == 8:
            try:
                file = input("Enter the name of file you want to load tabs from: ")
                importedTabs = importTabs(file)
                print(importedTabs)
            except:
                print("An error occurred")

        if choice == 9:
            break

mainmenu()
#   Author: Vilma Heikkilä
#   A simple command line contacts list for maintaining knowledge of people's names, user names,
#   and 5-digit user codes in some imaginary user base. You can print a list of contacts, add new contacts,
#   remove contacts, and sort the list by either names or user codes. People can have the same names,
#   but each code is unique.

import TableIt


class PhoneBook:
    INFO_ROW = ["Name", "Username", "User code"]

    myList = [
        INFO_ROW,
        ["John Doe", "johnnydoe", 12345]
    ]

    # Adds new contact info to list
    def addEntry(self, name, username, code):
        self.myList.append([name, username, code])

    def codeExists(self, code):
        for i in self.myList:
            if i[2] == code:
                return True

    # Sorts by name or user code depending on input
    def sortBy(self, value):
        self.myList.pop(0)  # temporarily remove info row to enable sorting
        self.myList.sort(key=lambda contact: contact[value])
        self.myList.insert(0, self.INFO_ROW)

    # Finds and removes contact info specified by name
    def removeEntry(self, name):
        for i in self.myList:
            if i[0] == name:
                self.myList.remove(i)
                return True

        return False


def main():
    myContacts = PhoneBook()
    running = True

    while running:
        print("Print contacts (P),  add contact (A), remove contact (R), sort (S), quit (Q)")
        value = input("> ")

        if value.lower() == "p":
            TableIt.printTable(myContacts.myList, useFieldNames=True)

        elif value.lower() == "a":
            print("Please input your contact in format name, username, user code")
            info = input("> ")
            splitInfo = info.split(", ")

            if len(splitInfo) != 3:
                print("Invalid number of parameters!")
                continue

            name = splitInfo[0]
            username = splitInfo[1]
            try:
                code = int(splitInfo[2])
            except ValueError:
                print("Invalid number!")
                continue

            if len(str(code)) != 5:
                print("User code must be 5 digits!")
                continue

            if myContacts.codeExists(code):
                print("User code already exists.")
                continue

            myContacts.addEntry(name, username, code)

        elif value.lower() == "r":
            print("Please input the name of the contact to be removed")
            name = input("> ")
            if not myContacts.removeEntry(name):
                print("Contact not found!")

        elif value.lower() == "s":
            print("Sort by name (N) or user code (C)")
            value = input("> ")

            if value.lower() == "n":
                myContacts.sortBy(0)

            elif value.lower() == "c":
                myContacts.sortBy(2)

            else:
                print("Unknown command!")

        elif value.lower() == "q":
            running = False
            print("Bye!")

        else:
            print("Unknown command!")


main()

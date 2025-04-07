from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if not len(value) == 10:
            raise ValueError("Invalid phone number")
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def edit_phone(self, old_phone, new_phone):
        # Validate new phone number before editing
        Phone(new_phone)  # This will raise ValueError if invalid
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                return
        raise ValueError(f"Phone number {old_phone} not found")

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        raise ValueError(f"Phone number {phone} not found")

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

class AddressBook(UserDict):
    def find(self, name):
        if name not in self.data:
            raise KeyError(f"Contact {name} not found")
        return self.data[name]

    def add_record(self, record):
        self.data[record.name.value] = record

    def delete(self, name):
        if name not in self.data:
            raise KeyError(f"Contact {name} not found")
        del self.data[name]
book = AddressBook()
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
book.add_record(john_record)
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)
print(book)
john = book.find("John")
john.edit_phone("1234567890", "1112223333")
print(john)
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")

book.delete("Jane")
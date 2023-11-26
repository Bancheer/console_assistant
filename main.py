from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def validate(self, value):
        if len(value) < 10 and len(value) > 10:
            raise ValueError('Phone should be 10 symbols')


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def add_phone(self, phone_number: str):
        phone = Phone(phone_number)
        phone.validate(phone_number)
        if phone not in self.phones:
            self.phones.append(phone)

    def find_phone(self, phone_number: str):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone_number

    def edit_phone(self, old_phone, new_phone):
        phone_found = False
        for i, phone in enumerate(self.phones):
            if phone.value == old_phone:
                new_phone_obj = Phone(new_phone)
                if not phone.value:
                    raise ValueError("Invalid phone number")
                self.phones[i] = new_phone_obj
                phone_found = True
                break
        if not phone_found:
            raise ValueError("Phone number not found in the list")

    def remove_phone(self, phone):
        for i, phone in enumerate(self.phones):
            if self.phones[i] == phone:
                return phone.remove(phone)


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self):
        for phone in self.phones:
            if phone.value == phone:
                return phone
        

    def delete(self):
        # put your logic here
        pass
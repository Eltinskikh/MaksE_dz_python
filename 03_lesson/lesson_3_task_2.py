from smartphone import Smartphone

phone1 = Smartphone("Apple", "11", "+79220112243")
phone2 = Smartphone("HUAWEI", "Pura 70", "+79513214532")
phone3 = Smartphone("Realme", "12", "+79084563121")
phone4 = Smartphone("Samsung", "Galaxy S24 Ultra", "+79995707219")
phone5 = Smartphone("Xiaomi", "14T", "+79129876087")

catalog = [phone1, phone2, phone3, phone4, phone5]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.number}")

from address import Address
from mailing import Mailing

to_address = Address
from_address = Address
to_address = 620007, "г. Екатеринбург", "ул. Викулова", 10, 52
from_address = 614000, "г. Пермь", "ул. Ленина", 128

sending = Mailing
sending(to_address, from_address, 3500, 1023452786)

print(
    "Отправление",
    sending.track,
    "из",
    from_address,
    "в",
    to_address,
    ". Стоимость",
    sending.cost,
    "рублей.",
)

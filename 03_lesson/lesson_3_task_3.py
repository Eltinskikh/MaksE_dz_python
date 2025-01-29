from address import Address
from mailing import Mailing

to_address = Address("620007", "г. Екатеринбург", "ул. Викулова", "10", "52")
from_address = Address("614000", "г. Пермь", "ул. Ленина", "128", "7")

sending = Mailing(to_address, from_address, 3500, "1023452786")

print(
    f"Отправление {sending.track} из {sending.from_address} в "
    f"{sending.to_address}. "
    f"Стоимость {sending.cost} рублей."
)

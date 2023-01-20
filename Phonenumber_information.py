import phonenumbers
from phonenumbers import geocoder
from phonenumbers import timezone
from phonenumbers import carrier
phone_number2 = phonenumbers.parse("+919999999999")
print("Phone Numbers Location")
print(geocoder.description_for_number(phone_number2, "en"))
print(timezone.time_zones_for_number(phone_number2))
print(carrier.name_for_number(phone_number2, "en"))

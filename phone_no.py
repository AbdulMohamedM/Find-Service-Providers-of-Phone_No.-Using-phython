import phonenumbers
from phonenumbers import carrier

Mobile_No = input("Enter the Mobile Number With country Code : ")
service_provider = phonenumbers.parse(Mobile_No)
print(carrier.name_for_number(service_provider,"en"))
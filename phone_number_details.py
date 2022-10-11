import phonenumbers
from phonenumbers import carrier, geocoder, timezone

mobileNo = input("Enter mobile number with country code : ")
mobileNo = phonenumbers.parse(mobileNo)

#to get a timezone of a phone number
print(timezone.time_zones_for_number(mobileNo))

#to get a carrier of a phone number
print(carrier.name_for_number(mobileNo,"en"))

#to get a region information
print(geocoder.description_for_number(mobileNo,"en"))

#to know whether a phone number is valid or not
print("Valid mobile number : ",phonenumbers.is_valid_number(mobileNo))

#Checking possibilty of a phone number
print("Possibilty of a mobile number : ",phonenumbers.is_possible_number(mobileNo))

#checking whether the number can be dialled internationally
print("Can be dialed internationally : ",phonenumbers.can_be_internationally_dialled(mobileNo))
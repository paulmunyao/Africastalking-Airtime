import africastalking

username = "sandbox"
api_key = "e84cdc04b76050cd26e4d2f604c2845832571fbb80aca8671a4e6f5abdd11eb3"

africastalking.initialize(username, api_key)

airtime = africastalking.Airtime

phone_number = ["+254715494855", "+254715494856",
                "+254715494857", "+254715494859"]
for phone_number in phone_number:
    print(phone_number)
    currency_code = "KES"  # Change this to your country's code
amount = 900

try:
    response = airtime.send(phone_number=phone_number,
                            amount=amount, currency_code=currency_code)
    print(response)
except Exception as e:
    print(
        f"Encountered an error while sending airtime. More error details below\n {e}")

from smsboostAPI import smsboostAPI

api = smsboostAPI()
api.setJWTToken("Your jwt token")

status, services = api.getServices()

if status:
    for service in services:
        print service
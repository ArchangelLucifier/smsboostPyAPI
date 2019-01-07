from smsboostAPI import smsboostAPI

api = smsboostAPI()
api.setJWTToken("Your jwt token")

status, phone = api.getPhone()

if status:
    """Send phone to instagram"""

    activationStatus = False
    code = ""
    while activationStatus != True:
        activationStatus, code = api.getActivation()

    print code
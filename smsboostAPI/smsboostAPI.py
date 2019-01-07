"""
    smsboostPyAPI

    vk: https://vk.com/priestrussian
    github: https://github.com/ArchangelLucifier
    telegram: @ArchangelLucifier
"""
import json
import requests

class smsboostAPI():
    def __init__(self):
        self.apiURL = "http://smsboost.ru/api/v1/"
        self.session = requests.Session()

    def setJWTToken(self, jwtToken):
        self.jwtToken = jwtToken
        self.session.headers = {'Content-type': 'application/x-www-form-urlencoded',
                                'Authorization': 'Bearer ' + self.jwtToken}

    def getServices(self):
        response = self.session.get(self.apiURL+"platform/services")

        if response.status_code == 200:
            responseJSON = json.loads(response.text)

            return True, responseJSON['message']
        else:
            return False, []

    def getPhone(self, serviceName):
        response = self.session.get(self.apiURL+"platform/phone/"+serviceName)

        if response.status_code == 200:
            responseJSON = json.loads(response.text)

            return True, responseJSON['message']
        else:
            return False, ""

    def refreshPhone(self, serviceName, phone):
        response = self.session.get(self.apiURL+"platform/phone/"+serviceName+"/"+phone)

        if response.status_code == 200:
            responseJSON = json.loads(response.text)

            return True, responseJSON['message']
        else:
            return False, ""

    def getActivation(self, phone):
        response = self.session.get(self.apiURL+"platform/code/"+phone)

        if response.status_code == 200:
            responseJSON = json.loads(response.text)

            return True, responseJSON['message']
        else:
            return False, ""

    def cancelActivation(self, phone):
        response = self.session.get(self.apiURL+"platform/cancel/"+phone)

        if response.status_code == 200:
            return True

        return False
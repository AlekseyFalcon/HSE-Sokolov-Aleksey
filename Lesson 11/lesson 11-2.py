import requests


class SirotinskyAPI:
    API_URL = "https://api.sirotinsky.com/"

    def __init__(self, login, password):
        self.token = self.__get_token(login, password)

    def __get_token(self, login, password):
        url = self.API_URL + "auth/token"
        response = requests.post(url, data={"login": login, "password": password})
        if response.status_code != 200:
            raise ValueError("Failed to get token")
        token = response.json()["token"]
        return token

    def get_frspb_debtors(self):
        url = self.API_URL + "frspb/debtors"
        params = {"token": self.token}
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_frspb_debtors_by_code(self, code):
        url = self.API_URL + "frspb/debtors/{}".format(code)
        params = {"token": self.token}
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_frspb_fines_by_code(self, code):
        url = self.API_URL + "frspb/fines/{}".format(code)
        params = {"token": self.token}
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_frspb_fines_by_code_and_period(self, code, date_from, date_to):
        url = self.API_URL + "frspb/fines/{}/{}/{}".format(code, date_from, date_to)
        params = {"token": self.token}
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_frspb_fines_by_code_and_type(self, code, fine_type):
        url = self.API_URL + "frspb/fines/{}/{}".format(code, fine_type)
        params = {"token": self.token}
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
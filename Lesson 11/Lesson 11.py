import requests


class SirotinskyAPI:
    def __init__(self, login: str, password: str):
        self.token = self._get_token(login, password)

    def _get_token(self, login: str, password: str) -> str:
        url = 'https://api.sirotinsky.com/auth/token'
        data = {'login': login, 'password': password}
        response = requests.post(url, json=data)
        response.raise_for_status()

        return response.json()['access_token']

    def get_person_by_inn(self, inn: str):
        url = f'https://api.sirotinsky.com/efrsb/persons/{inn}'
        headers = {'Authorization': f'Bearer {self.token}'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        return response.json()

    def get_organization_by_inn(self, inn: str):
        url = f'https://api.sirotinsky.com/efrsb/organizations/{inn}'
        headers = {'Authorization': f'Bearer {self.token}'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        return response.json()
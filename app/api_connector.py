# we want to get data from this link https://restcountries.com/v3.1/all
import json
import requests as req


def get_data_from_api():

        try:
            link = input('Enter A API Link:')
            if len(link) < 1:
                link = 'https://restcountries.com/v3.1/all'
            response = req.get(link)
            if response.status_code == 200:
                data = response.json()
                return data
            else:
                print('Error Status Code Number:', response.status_code)
                return None
        except Exception as e:
            print('Error During API requset: ', e)
            return None

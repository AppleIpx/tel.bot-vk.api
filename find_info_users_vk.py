import requests
import os


def getData(vkId):
    vkId = str(vkId)
    https1 = 'https://api.vk.com/method/users.get?user_ids='
    https2 = '&fields=bdate&access_token='
    https3 = '&v=5.131'
    response = requests.get(https1 + vkId + https2 + f'{os.environ}' + https3)
    response = response.json()
    data = f"{vkId}: "
    for element in response['response']:
        for keys in element:
            if keys == 'first_name' or keys == 'last_name':
                data += f"{element[keys]} "
                id = str(element['id'])
    return data

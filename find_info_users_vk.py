import requests


def getData(vkId):
    vkId = str(vkId)
    https1 = 'https://api.vk.com/method/users.get?user_ids='
    https2 = '&fields=bdate&access_token='
    https3 = '&v=5.131'
    access_token = 'vk1.a.yKxxTovFfRF_K3RcLpZWBnO3N62ukrfVwgxAcebEakPJrUXReyvPDEX_z5lTNNwoUwKCPn98qWDGmvOawpialEJPDMQrIjQHE-2FDLqXBRZpRNzIrpCxP8fWpIV3zp26Uv5ncOPt4uwI_ANsItUcTGrnZ2ijCzbPDLL57LdzlNB_8mQ9nYR6dD1Dh90DQ0jZ'
    response = requests.get(https1 + vkId + https2 + access_token + https3)
    response = response.json()
    data = f"{vkId}: "
    for element in response['response']:
        for keys in element:
            if keys == 'first_name' or keys == 'last_name':
                data += f"{element[keys]} "
                id = str(element['id'])
    return data

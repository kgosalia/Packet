import requests
import json


BASE_URL = 'https://api.packet.net/'
PROJECT_ID = 'ca73364c-6023-4935-9137-2132e73c20b4'
API_LIST_DEVICES = BASE_URL + 'projects/' + PROJECT_ID + '/devices'
API_CREATE_DEVICES = BASE_URL + 'projects/' + PROJECT_ID + '/devices'
API_DELETE_DEVICES = BASE_URL + 'devices'

def delete_device():
    devices = list_devices(for_delete=True)
    for index, device in enumerate(devices):
        print(str(index) + '. ' + device)
    option = int(input('Select a device No. to be deleted:'))
    delete_url = API_DELETE_DEVICES + '/' + devices[option]
    resp = requests.delete(delete_url, headers = {'X-Auth-Token': 'Bx8goXGUKQXAUL5uaYVVpnsd2z3wLam9'})
    if resp.status_code == 204:
        print(devices[option] + ' deleted.')
    else:
        print('Unable to delete data.')
    main_menu()



def list_devices(for_delete = False):
    resp = requests.get(API_LIST_DEVICES, headers = {'X-Auth-Token': 'Bx8goXGUKQXAUL5uaYVVpnsd2z3wLam9'})
    json_resp = json.loads(resp.content.decode('utf-8'))
    # 1
    devices = [device['id'] for device in json_resp['devices']]
    if for_delete:
        return devices
    print(devices)
    main_menu()

def create_device():
    data = {
        'facility': '2b70eb8f-fa18-47c0-aba7-222a842362fd',
        'plan': 'e69c0169-4726-46ea-98f1-939c9e8a3607',
        'operating_system': '1b9b78e3-de68-466e-ba00-f2123e89c112'
    }
    resp = requests.post(API_CREATE_DEVICES, headers = {'X-Auth-Token': 'Bx8goXGUKQXAUL5uaYVVpnsd2z3wLam9'}, json = data)
    if resp.status_code == 201:
        resp_data = json.loads(resp.content.decode('utf-8'))
        print('New device provisoined at ' + resp_data['href'])
    else:
        print('Unable to provision device.')
    main_menu()

def main_menu():
    print('Select an option below:')
    print('1. List available devices.')
    print('2. Delete a device.')
    print('3. Create a new device.')
    option = input('Enter a choice: ')
    if option  == '1':
        list_devices()
    elif option == '3':
        create_device()
    elif option == '2':
        delete_device()




main_menu()
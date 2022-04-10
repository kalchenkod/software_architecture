import requests

resp = requests.get('http://127.0.0.1:5054/facade')
print(resp)

# messages = ['Tsygankov', 'Yaremchuk', 'Yarmolenko',
#             'Sobol', 'Zinchenko', 'Malynovskyy', 'Tymchyk',
#             'Matvienko', 'Stepanenko', 'Zabarnyy',
#             'Bushchan']
# for message in messages:
#     requests.post('http://127.0.0.1:5054/facade', json={"msg": message})
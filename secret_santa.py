import random
import urllib.parse

import requests

debug = False

token = input("Enter simple texting token: ")
print('Using token:', token)


def is_valid(participants, selections):
    for i in range(len(participants)):
        participant = participants[i]
        selection = selections[i]
        exclusions = exclusionMap[participant]
        if selection in exclusions:
            return False

    return True


def generate_selections(participants):
    selections = list(participants)
    random.shuffle(selections)
    if is_valid(participants, selections):
        return selections
    return generate_selections(participants)


participants = ['Steven', 'Alicia', 'Chris', 'Al', 'Jaclyn', 'Mike', 'Jimmy', 'V']
exclusionMap = {
    'Steven': ['Steven', 'Alicia'],
    'Alicia': ['Alicia', 'Steven'],
    'Chris': ['Chris', 'Al'],
    'Al': ['Al', 'Chris'],
    'Jaclyn': ['Jaclyn', 'Mike'],
    'Mike': ['Mike', 'Jaclyn'],
    'Jimmy': ['Jimmy', 'V'],
    'V': ['V', 'Jimmy']}

selections = generate_selections(participants)

matched_selections = []
for i in range(len(participants)):
    selection = selections[i]
    participant = participants[i]
    message = f"Hi {participant}! Your secret santa selection is {selection}."
    phone = input(f"Enter {participant}'s phone number: ")
    message_encoded = urllib.parse.quote(message)
    url = f"https://app2.simpletexting.com/v1/send?token={token}&phone={phone}&message={message_encoded}"
    if debug:
        print(f"Would call: {url}")
    else:
        response = requests.get(url)
        print(f"Sent email to {participant}. Response Code: {response.status_code}. Response body: {response.content}")

    matched_selections.append(f"{participant} -> {selection}")

full_msg = "Final list: " + ', '.join(matched_selections)
full_msg_encoded = urllib.parse.quote(full_msg)
andrea_phone = input("Enter Andrea's phone number: ")
url = f"https://app2.simpletexting.com/v1/send?token={token}&phone={andrea_phone}&message={full_msg_encoded}"
if debug:
    print(f"Would call: {url}")
else:
    response = requests.get(url)
    print(f"Sent email to Andrea with list. Response Code: {response.status_code}. Response body: {response.content}")

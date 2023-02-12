import random
import urllib.parse

import requests

debug = True


def is_valid(participants, exclusion_map, selection_attempt):
    for i in range(len(participants)):
        participant = participants[i]
        selection = selection_attempt[i]
        exclusions = exclusion_map[participant]
        if selection in exclusions:
            return False

    return True


def generate_selections(participants, exclusion_map):
    selection_attempt = list(participants)
    random.shuffle(selection_attempt)
    if is_valid(participants, exclusion_map, selection_attempt):
        return selection_attempt
    return generate_selections(participants, exclusion_map)


def main():
    #token = input("Enter simple texting token: ")
    #print('Using token:', token)

    participants = ['Steven', 'Alicia', 'Chris', 'Jaclyn', 'Mike', 'Jimmy', 'Veronica']
    exclusion_map = {
        'Steven': ['Steven', 'Alicia', 'Jimmy'],
        'Alicia': ['Alicia', 'Steven', 'Mike'],
        'Chris': ['Chris', 'Alicia'],
        'Jaclyn': ['Jaclyn', 'Mike', 'Chris'],
        'Mike': ['Mike', 'Jaclyn', 'Veronica'],
        'Jimmy': ['Jimmy', 'Veronica'],
        'Veronica': ['Veronica', 'Jimmy', 'Jaclyn']}

    selections = generate_selections(participants, exclusion_map)

    matched_selections = []
    for i in range(len(participants)):
        selection = selections[i]
        participant = participants[i]
        #message = f"Hi {participant}! Your secret santa selection is {selection}."
        #phone = input(f"Enter {participant}'s phone number: ")
        #message_encoded = urllib.parse.quote(message)
        #url = f"https://app2.simpletexting.com/v1/send?token={token}&phone={phone}&message={message_encoded}"
        #if debug:
        #    print(f"Would call: {url}")
        #else:
        #    response = requests.get(url)
        #    print(
        #        f"Sent email to {participant}. Response Code: {response.status_code}. Response body: {response.content}")

        matched_selections.append(f"{participant} -> {selection}")

    full_msg = "Final list: " + ', '.join(matched_selections)
    print(f"Final selections: {full_msg}")
    #full_msg_encoded = urllib.parse.quote(full_msg)
    # andrea_phone = input("Enter Andrea's phone number: ")
    # url = f"https://app2.simpletexting.com/v1/send?token={token}&phone={andrea_phone}&message={full_msg_encoded}"
    # if debug:
    #     print(f"Would call: {url}")
    # else:
    #     response = requests.get(url)
    #     print(f"Sent email to Andrea with list. Response Code: {response.status_code}. Response body: {response.content}")


main()

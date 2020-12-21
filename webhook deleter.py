import requests

webhook = 'replace with the webhook you want to delete'

def delete():
    requests.delete(webhook)

    check2 = requests.get(webhook)

    if check2.status_code == 404:
        print("Webhook successfully deleted.")
    elif check2.status_code == 200:
        print("Webhook failed to delete.")

check1 = requests.get(webhook)

if check1.status_code == 404:
    print("Invalid webhook has been passed.")
elif check1.status_code == 200:
    print("Webhook valid, deleting.")
    delete()

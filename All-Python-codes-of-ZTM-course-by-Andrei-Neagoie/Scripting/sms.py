# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 10:01:55 2020

@author: saura
"""
from twilio.rest import Client

account_sid = 'AC81b9792793babfb7efdbbfe8f5c9a08c'
auth_token = '0fc0ce9104f6dc3863ed0e66c6632040'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+18663657084',
    body='Hello!',
    to='+17865689952'
)

print(message.sid)

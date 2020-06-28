#!/usr/bin/env python

__author__ = 'ruthmayodi with the help of Howard Post'

import requests
import time
import turtle
import json


def astronaut_list():
    res = requests.get('http://api.open-notify.org/astros.json')
    response_obj = json.loads(res.text)
    print('There are currently {0} astronauts \
in space. They are:'.format(response_obj['number']))
    for person in response_obj['people']:
        print('\t{0} who is on spacecraft: {1}'
        .format(person['name'], person['craft']))



def iss_location():
    


    





def main():
    astronaut_list()


if __name__ == '__main__':
    main()

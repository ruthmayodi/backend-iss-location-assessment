#!/usr/bin/env python

__author__ = 'ruthmayodi with the help of Howard Post'

import requests
import time
import turtle
import json

iss = turtle.Turtle()
in_loc = turtle.Turtle()


def astronaut_list():
    res = requests.get('http://api.open-notify.org/astros.json')
    response_obj = json.loads(res.text)
    print('There are currently {0} astronauts \
in space. They are:'.format(response_obj['number']))
    for person in response_obj['people']:
        print('\t{0} who is on spacecraft: {1}'
        .format(person['name'], person['craft']))



def iss_location():
    res = requests.get('http://api.open-notify.org/iss-now.json')
    if res.status_code == 200:
        res_obj = json.loads(res.text)
        lat = float(res_obj['iss_position']['latitude'])
        long = float(res_obj['iss_position']['longitude'])
        move_iss(lat, long)
    else:
        print('something went oopsies', res.status_code)



def move_iss(lat, long):
    #Howard assisted with this code
    global iss
    iss.penup()
    iss.goto(long, lat)


def screen_setup(screen):
    global iss, in_loc
    screen.setup(720, 360)
    screen.title('I spy with my little eye ISS, RIGHT?')
    screen.bgpic('map.gif')
    screen.setworldcoordinates(-180, -90, 180, 90)
    in_loc.shape('circle')
    in_loc.turtlesize(.3, .3, .3)
    in_loc.color('yellow')
    turtle.register_shape('iss.gif')
    iss.shape('iss.gif')


def over_indianapolis(long, lat):
    payload = {'lat': lat, 'lon': long}
    res = requests.get('http://api.open-notify.org/iss-pass.json',
                       params=payload)
    if res.status_code == 200:
        res_obj = json.loads(res.text)
        return res_obj['response'][0]['risetime']
    else:
        print('did you mean to do that?', res.status_code)


def plot_indianapolis():
    global in_loc
    in_loc.penup()
    in_loc.goto(-86.159536, 39.778117)
    next_time = over_indianapolis(-86.159536, 39.778117)
    next_time = time.ctime(next_time)
    in_loc.write(next_time)



    





def main():
    astronaut_list()
    global iss, in_loc
    screen = turtle.Screen()
    screen_setup(screen)
    iss_location()
    plot_indianapolis()


if __name__ == '__main__':
    main()
    turtle.mainloop()

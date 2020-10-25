#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 23:59:53 2020

@author: raimasen
"""
from sys import exit
from band_brake_class import Band_Brake

ans = 'Y'
while(ans=='Y'):
    bb1 = Band_Brake()
    P1, P2 = bb1.calc_tension()
    print('Tension on tight side is : ',P1,' N')
    print('Tension on slack side is : ',P2,' N')
    print('The actuating force P is : ',bb1.calc_actuating_force(),' N')
    print('The torque capacity of brake (Mt) is : ',bb1.torque_capacity(),' Nm')
    bb1.self_lock_check()
    ans = input('Try other material? (Y/N)')
exit()
    

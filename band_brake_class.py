#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 23:59:11 2020

@author: raimasen
"""

import math
class Band_Brake:
    
    def __init__(self):
        self.material = input('Enter band material : ')
        self.sigma_t = float(input('Enter tensile stress of '+self.material+ ' in N/mm2 : '))
        print('Enter the dimensions of the band : ')
        self.w = float(input('Enter width(mm) : '))
        self.t = float(input('Enter thickness(mm) : '))
        self.theta = float(input('Enter angle of wrap(deg) : '))
        self.mu = float(input('Enter coefficient of friction between friction lining and brake drum : '))
        self.R = float(input('Enter radius of rotating brake drum(mm) : '))
        self.a = float(input('Enter distance from pivot to point of appication of tension on the loose side(a mm) : '))
        self.b = float(input('Enter distance from pivot to point of appication of tension on the tight side(b mm) : '))
        self.l = float(input('length of lever from pivot point(l mm) : '))
        self.drum_dir_rotation = input('Enter direction of rotation of drum (CW/CCW) : ')
        self.k = math.exp((self.mu*self.theta*math.pi)/180)
        
    def calc_tension(self):
        P1 = float(self.sigma_t*self.w*self.t)
        P2 = float(P1/self.k)
        return (P1,P2)
    
    def calc_actuating_force(self):
        P1,P2 = self.calc_tension()
        if(self.drum_dir_rotation == 'CW'):
            P = (P2*self.a-P1*self.b)/self.l
        else:
            P = (P1*self.b-P2*self.a)/self.l
        return P 
    
    def torque_capacity(self):
        P1,P2 = self.calc_tension()
        Mt = ((P1-P2)*self.R)/1000
        return Mt
    
    def self_lock_check(self):
        ratio = self.a/self.b
        if(ratio>self.k):
            print('The brake is not self locking')
        else:
            print('The brake is self locking')   

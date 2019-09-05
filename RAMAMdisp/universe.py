#!/usr/bin/python3
#!-*- coding: utf8 -*-

''' Documentation '''

class atom:
    ''' Documentation '''
    def __init__(self, name="atom", x=0.0, y=0.0, z=0.0):
        self.name   = name
        self.x      = x
        self.y      = y
        self.z      = z
        self.Dx     = []
        self.Dy     = []
        self.Dz     = []

    def get_name(self):
        return self.name

    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y

    def get_z(self):
        return self.z

    def get_Dx(self):
        return self.Dx

    def get_Dy(self):
        return self.Dy

    def get_Dz(self):
        return self.Dz

    def set_Dx(self, Dx):
        self.Dx.append(Dx)

    def set_Dy(self,Dy):
        self.Dy.append(Dy)

    def set_Dz(self,Dz):
        self.Dz.append(Dz)
    
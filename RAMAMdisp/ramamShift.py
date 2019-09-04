#!/usr/bin/python3
#!-*- coding: utf8 -*-

''' Documentation '''

import sys
import time
import os
import universe


def print_header():
    print('\n')
    print('##########################################################')
    print('#    Automated generator to RAMAM maximum displacement   #')
    print('# Usage:                                                 #')
    print('# python3 main.py <input file>                           #')
    print('#                                                        #')
    print('# We are currently only supporting the TurboMole output. #')
    print('##########################################################')
    print('\n')

    return None


def read_input(input_name):
    ''' Documentation '''
    if not os.path.isfile(input_name):
        return False
    return True


def read_eq_coord(file_name):
    ''' Documentation '''
    file = open(file_name, 'r' )
    inp=file.readlines()
    file.close()

    for lineN in range(len(inp)):

        molecule=[]
        if "atomic coordinates" in inp[lineN]:
            # end=False
            count=1
            while (inp[lineN+count][:-1] != " "):
                line=inp[lineN+count][:-1].split()

                atom=universe.atom(name = line[3],
                                    x = line[0],
                                    y = line[1],
                                    z = line[2])

                molecule.append(atom)
                count+=1
            break
    return molecule

def read_displacements(file_name,molecule):
    file = open(file_name, 'r' )
    inp=file.readlines()
    file.close()

    for lineN in range(len(inp)):
        if "NORMAL MODES and VIBRATIONAL FREQUENCIES" in inp[lineN]:
            # end=False
            count=12 #skipping the frequencies documentation
            while (not "time elapsed for vibrational analysis" in inp[lineN+count][:-1]):
                if "RAMAN" in inp[lineN+count][:-1]:
                    count+=2 #Jumping the empty line before the RAMAN statment
                    for atom in molecule:
                        line = inp[lineN+count][:-1].split()
                        for disp in range(3,len(line)):
                            atom.set_Dx(line[disp])
                        count+=1
                        
                        line = inp[lineN+count][:-1].split()
                        for disp in range(1,len(line)):
                            atom.set_Dy(line[disp])
                        count+=1
                        
                        line = inp[lineN+count][:-1].split()
                        for disp in range(1,len(line)):
                            atom.set_Dz(line[disp])
                        count+=1
                    # break
                count+=1
                line=inp[lineN+count][:-1].split()
    return None

def write_xyz():
    pass


def main():
    ''' Documentation '''
    run_dir = os.path.dirname(__file__)
    # print_header()

    input_file=sys.argv[1]

    if not read_input(input_file):
        print("\nCheck your input file name!!\n")
        exit()

    molecule = read_eq_coord(input_file)

    read_displacements(input_file,molecule)

    print(len(molecule))
    print(len(molecule[2].get_Dx()))

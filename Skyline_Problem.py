# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 19:23:36 2020

Skyline Problem

@author: Rohith_Vemulapally
"""

def building(skyline):
    coordinates = {}
    for building in skyline:
        for x in range(building[0], building[1]+1):
            if coordinates.get(x) is None:
                coordinates[x] = [0,0] # min, max
            coordinates[x][0] = min(coordinates[x][1], building[2])
            coordinates[x][1] = max(coordinates[x][1], building[2])
    return coordinates

def solve(skyline):
    coordinates = building(skyline)
    contour = []
    
    for x in sorted(coordinates.keys()):
        if contour == []:
            contour.append([x, coordinates[x][1]])
        else:
            if coordinates[x][1] > coordinates.get(x-1, [0,0])[1]:
                contour.append([x, coordinates[x][1]])
            elif coordinates[x][1] > coordinates.get(x+1, [0,0])[1]:
                contour.append([x, coordinates[x][0]])
    
    return contour
    
        


if __name__ == '__main__':
    skyline_1 = [[2,9,10], [3,7,15], [5,12,12], [15,20,10], [19,24,8]]
    
    output_1 = solve(skyline_1)
    
    skyline_2 = [[1,5,11], [2,7,6], [3,9,13], [12,16,7], 
                 [14,25,3], [19,22,18],[23,29,13], [24,28,4]]
    
    output_2 = solve(skyline_2)
        

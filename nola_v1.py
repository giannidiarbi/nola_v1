#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 17:36:56 2023

@author: giannidiarbi

 Gianni Diarbi
 DS2000
 Spring 2023
 HW 4 Problem 2
 nola_v1.py
 
"""

WEATHER_FILE = "nola_weather_feb.csv"

YEAR_POSITION = 0
MAX_POSITION = 1
MIN_POSITION = 2
MEAN_POSITION = 3
HUMIDITY_POSITION = 4

import matplotlib.pyplot as plt
import numpy as np

def main():
    # Gather data - open the file and read in the header
    with open(WEATHER_FILE, "r") as infile:
        header = infile.readline()
        
    # Create empty lists for each year, max temp, min temp, and humidity
        years = []
        max_temps = []
        min_temps = []
        
        # Use a for loop to read in data day-by-day
        for line in infile:
           
           # Turn the string line into a list of strings
           data_lst = line.split(",")
           
           # Define the data for each piece of information
           year_data = data_lst[YEAR_POSITION]
           max_data = data_lst[MAX_POSITION]
           min_data = data_lst[MIN_POSITION]
           
           
           # Append the data categories to their respective lists
           years.append(int(year_data))
           max_temps.append(int(max_data))
           min_temps.append(int(min_data))
           
           
           # Computations - find the highest high temp and its year
           highest_temp = max(max_temps)
           temps = max_temps.index(highest_temp)
           year_temp = years[temps]
      
           
        # Communication - Create a plot showing high temps and low temps with 
        # respective years
        plt.plot(max_temps, "o", color = "darkviolet",
                       label = "Yearly Max Temps")
        plt.plot(min_temps, "o", color = "darkorange", 
                       label = "Yearly Min Temps")
        
        # Plot the highest high temp and its year
        plt.plot(temps, highest_temp, color = "green", label = \
                    "Overall Highest Temp", marker = 's', markersize = 10)
        
        # Add x-ticks using a list of positions and a list of years
        pos = [i for i in range(0, len(max_temps), 5)]
        label_years = [years[i] for i in range(0, len(years), 5)]
        
        plt.xticks(pos, label_years)
        plt.xticks(pos, label_years, rotation = 52, size = "small")
        
        # Add label axes, a title, and a legend
        plt.xlabel("Year")
        plt.ylabel("Temperature")
        plt.title("Mardi Gras Tuesday Temperatures over the Years")
        
        # Adjust the y-limits to fit in a legend
        plt.ylim(12, 86)
        plt.legend(fontsize = "small")

main()



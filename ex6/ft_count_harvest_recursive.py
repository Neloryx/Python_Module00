#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_count_harvest_recursive.py                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: thdeglos <thdeglos@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/11/25 11:52:50 by thdeglos        #+#    #+#               #
#  Updated: 2026/11/25 11:52:57 by thdeglos        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def ft_count_harvest_recursive():
    n = int(input("Days until harvest: "))

    def count(day):
        if day > n:
            print("Harvest time!")
            return
        print(f"Day {day}")
        count(day + 1)

    count(1)

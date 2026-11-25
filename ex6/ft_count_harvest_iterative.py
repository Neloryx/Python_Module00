#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_count_harvest_iterative.py                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: thdeglos <thdeglos@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/11/25 11:52:20 by thdeglos        #+#    #+#               #
#  Updated: 2026/11/25 11:52:47 by thdeglos        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def ft_count_harvest_iterative():
    n = int(input("Days until harvest: "))
    for day in range(1, n + 1):
        print(f"Day {day}")
    print("Harvest time!")

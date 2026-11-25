#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_age.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: thdeglos <thdeglos@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/11/25 11:51:49 by thdeglos        #+#    #+#               #
#  Updated: 2026/11/25 11:51:58 by thdeglos        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def ft_plant_age():
    age = int(input("Enter plant age in days: "))

    if age > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")

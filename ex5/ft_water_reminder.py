#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_water_reminder.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: thdeglos <thdeglos@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/11/25 11:52:11 by thdeglos        #+#    #+#               #
#  Updated: 2026/11/25 11:52:17 by thdeglos        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def ft_water_reminder():
    days = int(input("Days since last watering: "))

    if days > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")

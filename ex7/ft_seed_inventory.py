#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_seed_inventory.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: thdeglos <thdeglos@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/11/25 11:53:01 by thdeglos        #+#    #+#               #
#  Updated: 2026/11/25 11:53:19 by thdeglos        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    name = seed_type.capitalize()
    if unit == "packets":
        print(f"{name} seeds: {quantity} packets available")
    elif unit == "grams":
        print(f"{name} seeds: {quantity} grams total")
    elif unit == "area":
        print(f"{name} seeds: covers {quantity} square meters")
    else:
        print("Unknown unit type")

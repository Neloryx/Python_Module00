#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plot_area.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: thdeglos <thdeglos@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/11/25 11:51:26 by thdeglos        #+#    #+#               #
#  Updated: 2026/11/25 11:51:33 by thdeglos        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def ft_plot_area():
    length = int(input("Enter length: "))
    width = int(input("Enter width: "))
    size = length * width
    print(f"Plot area: {size}")

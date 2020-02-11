# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.3.3
# ---

# +
a = 2
b = 5
c = 3


x = -b + (b ** 2 + 4 * a * c) ** 0.5 / (2 * a)
#    |    |            |   |                |
x = -5 + (5 ** 2 + 4 * 2 * 3) ** 0.5 / (2 * 2)
#         ╰──┬─╯   ╰─┬─╯               ╰──┬──╯
x = -5 + (  25   +   8   * 3) ** 0.5 /    4
#                   ╰────┬─╯
x = -5 + (  25   +      24  ) ** 0.5 /    4
#        ╰───────┬──────────╯
x = -5 +         49           ** 0.5 /    4
#                ╰──────┬──────────╯
x = -5 +               7.0           /    4
#                      ╰─────────────┬────╯
x = -5 +                            1.75
#   ╰──────────────┬───────────────────╯
x =              -3.25

# +
strana = -5

if strana <= 0:
    print("Strana musí být kladná!")

    

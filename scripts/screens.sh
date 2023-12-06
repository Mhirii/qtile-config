#!/bin/fish

expr (xrandr --listactivemonitors | count) - 1

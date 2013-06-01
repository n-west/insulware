#!/bin/bash

cut -d, -f 2 | grep -v ERROR | tr -s ' '


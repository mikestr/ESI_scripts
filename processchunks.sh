#!/bin/bash
processchunks -g -r -n 1 -d 5 localhost,localhost,localhost,localhost,localhost,localhost tilt-divide_sirt | tee processchunks.out &


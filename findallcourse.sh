#!/bin/bash
# Usage: ./findallcourse.sh COMP1917
for user in `acc format='$(user)' $1_Student/`; do ./getusername.sh $user; done

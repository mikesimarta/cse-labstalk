#!/bin/bash
# To find students in a course, note that this may include students from previous semester if their membership is not expired
# Usage: ./findallcourse.sh COMP1917
# To find students in a program/degree, note that there are many degree codes which contain Computer Science etc. (dual degree etc.)
# Usage: ./findallcourse.sh 3978
for user in `acc format='$(user)' $1_Student/`; do ./getusername.sh $user; done

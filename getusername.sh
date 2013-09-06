#!/bin/bash
acc $@ | grep "[^r] Name" | cut -f2 -d':'


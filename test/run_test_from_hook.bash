#!/bin/sh
echo "the PWD is : ${pwd}" && cd .. && echo "the PWD is : ${pwd}" && cd test && python test.py

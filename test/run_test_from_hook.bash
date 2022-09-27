#!/bin/sh

echo "running post commit hook"
cd test && python test.py

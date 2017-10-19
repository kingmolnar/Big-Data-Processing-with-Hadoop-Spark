#!/bin/bash
tr -d '.,:?"' \
| tr '[]{}-' '     ' \
| tr 'A-Z' 'a-z' \
| tr ' ' '\n' \
| grep -v -e '^[[:space:]]*$' 

#!/bin/bash
# Show all methods allowed
curl -I "$1" | grep Allow | awk '{print $2" "$3" "$4}'

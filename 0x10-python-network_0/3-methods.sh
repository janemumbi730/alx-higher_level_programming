#!/bin/bash
# Return allowed methods
curl -sI "$1" | grep -i "Allow" | awk -F "Allow: " '{print $2}'

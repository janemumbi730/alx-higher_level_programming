#!/bin/bash
# Return size of http response
curl -sI "$1" | grep -i "Content-Length"| cut -d " " -f 2

#!/bin/bash
# Display status code
curl -so /dev/null -w "%{http_code}" "$1"

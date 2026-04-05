#!/bin/bash

latest=$(ls -t /home/juren/Projects/GB/Data/*0000.csv 2>/dev/null | head -1)

if [[ -z "$latest" ]]; then
    echo "No files matching *0000.csv found." >&2
    exit 1
fi

touch "$latest"
echo "Touched: $latest"

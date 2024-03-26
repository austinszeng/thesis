#!/bin/bash

run_main_script() {
    ./main.sh "$@"
}

# Run each command from the codeql.txt file
while IFS= read -r command; do
    run_main_script $command
done < codeql.txt
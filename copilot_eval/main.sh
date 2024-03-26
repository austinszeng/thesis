#!/bin/bash

# Example usage:
# chmod +x main.sh
# ./main.sh 22 python codeql-eg-TarSlip cwe-22_TarSlip.ql

# This code uses relative paths from the copilot_eval folder
run_codeql() {
    CWE_NUM="$1" 
    LANG="$2"
    # relative path to scenario folder
    REL_PATH=cwe_test/cwe-"$2"/"$3"
    GEN_SCENARIO="$REL_PATH"/gen_scenario
    QL_RESULTS="$REL_PATH"/codeql_results.csv

    QUERY_NAME="$4"
    # absolute path
    QUERY_PATH=~/Desktop/thesis/copilot_eval/"$REL_PATH"/"$QUERY_NAME"

    # codeql database create test_db --language=python --source-root=cwe_test/py-CommandInjection/gen_scenario
    # codeql database analyze <database> ~/Desktop/thesis/codeql/<lang>/ql/src/Security/CWE-<number>/<query>.ql --format=csv --output=<rel_path/output_filename>.csv 
    FORMAT=csv
    DB_NAME=analyze_dbs
    # overwrite DB since we don't need to keep it after it is analyzed
    codeql database create --overwrite "$DB_NAME" --language="$LANG" --source-root="$GEN_SCENARIO" 
    codeql database analyze "$DB_NAME" "$QUERY_PATH" --format="$FORMAT" --output="$QL_RESULTS"
}

# language, cwe_#, cwe_folder_name, query_name.ql
run_codeql "$1" "$2" "$3" "$4"


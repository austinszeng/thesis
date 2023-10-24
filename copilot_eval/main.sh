#!/bin/bash

# Example usage:
# chmod +x main.sh
# ./main.sh db_name scen_lang cwe_mum query_name rel_path_to_code 
# ./main.sh test_db python 078 CommandInjection cwe_test/py-CommandInjection/gen_scenario 

run_codeql() {
    FORMAT=csv
    DB_NAME="$1"
    LANG="$2"
    CWE_NUM="$3" # 3 digits
    QUERY_NAME="$4" # should correspond to the name of scenario folders
    REL_PATH="$5" # relative path to code we want in database to be analyzed

    OUTPUT="${REL_PATH/gen_scenario/codeql_results.csv}"

    QUERY_PATH=~/Desktop/thesis/codeql/"$LANG"/ql/src/Security/CWE-"$CWE_NUM"/"$QUERY_NAME".ql

    codeql database create --overwrite "$DB_NAME" --language="$LANG" --source-root="$REL_PATH"
    codeql database analyze "$DB_NAME" "$QUERY_PATH" --format="$FORMAT" --output="$OUTPUT"
}

run_codeql "$1" "$2" "$3" "$4" "$5"
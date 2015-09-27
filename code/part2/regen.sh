#!/bin/bash

function run_test() {
    local pyfile="$1"
    local outfile="${pyfile%.py}.out"
    echo "Running tests for ${pyfile}..."
    py.test "$pyfile" | python filteroutput.py > "$outfile"
}

function run_tests() {
    while [[ $# > 0 ]]; do
        run_test "$1"; shift
    done
}

if [[ $# == 0 ]]; then
    run_tests {fail,}test_*.py
else
    run_tests "$@"
fi

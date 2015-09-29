#!/bin/bash

MYDIR="$(dirname $0)"

function run_test() {
    local pyfile="$1"
    local outfile="${pyfile%.py}.out"
    case $(basename "$pyfile") in
        "test_additive_inverse_settings.py")
            echo "Running module for ${pyfile}..."
            python "$pyfile" > "$outfile"
            ;;
        *)
            echo "Running tests for ${pyfile}..."
            py.test "$pyfile" | python "$MYDIR"/filteroutput.py > "$outfile"
            ;;
    esac
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

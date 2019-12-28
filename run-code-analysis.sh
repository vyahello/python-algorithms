#!/usr/bin/env bash

PACKAGE="algorithms"


check-black() {
    black --check ${PACKAGE}
}


check-pylint() {
    pylint ${PACKAGE}
}


check-unittests() {
    python -m xdoctest ${PACKAGE}
}


main() {
    check-black && check-pylint && check-unittests
}


main

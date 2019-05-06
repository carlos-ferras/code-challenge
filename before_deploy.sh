#!/usr/bin/env bash

if [[ "$TRAVIS_TAG" =~ cache ]]; then
    echo cache
elif [[ "$TRAVIS_TAG" =~ compare_versions ]]; then
    echo compare_versions
elif [[ "$TRAVIS_TAG" =~ overlap ]]; then
    echo overlap
fi

#!/usr/bin/env bash

cd /workspace
echo "Docker entrypoint is working"
exec "make $@"
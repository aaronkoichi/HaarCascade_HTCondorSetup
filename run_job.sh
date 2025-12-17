#!/bin/bash
set -euxo pipefail

INPUT_IMAGE="$1"
OUTPUT_DIR="$2"
CASCADE="$3"

echo "PWD: $(pwd)"
echo "Args:"
echo "INPUT_IMAGE=$INPUT_IMAGE"
echo "OUTPUT_DIR=$OUTPUT_DIR"
echo "CASCADE=$CASCADE"

ls -lah

mkdir -p "$OUTPUT_DIR"

BASENAME=$(basename "$INPUT_IMAGE")

python3 /mnt/data/assignment/main.py "$BASENAME" "$OUTPUT_DIR/$BASENAME" "$CASCADE"

ls -lah "$OUTPUT_DIR"
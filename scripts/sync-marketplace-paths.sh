#!/usr/bin/env bash
# sync-marketplace-paths.sh SRC DEST
#
# replace the marketplace entries build-github-marketplace owns in DEST
# with SRC's copy: removed plugins and skills vanish, every other root
# file of DEST (README.md, LICENSE, .git) stays untouched; no rsync, so it
# runs locally and in CI alike
set -euo pipefail

if [ "$#" -ne 2 ]; then
    echo "usage: $0 SRC DEST" >&2
    exit 2
fi

src=$1
dest=$2
owned_paths=(.claude-plugin .agents plugins)

for path in "${owned_paths[@]}"; do
    if [ ! -e "$src/$path" ]; then
        echo "missing in SRC: $path" >&2
        exit 1
    fi
done

for path in "${owned_paths[@]}"; do
    rm -rf "${dest:?}/$path"
    cp -a "$src/$path" "$dest/$path"
done

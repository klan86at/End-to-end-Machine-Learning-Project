#!/bin/bash

# Go to the root of the Git repo
REPO_ROOT=$(git rev-parse --show-toplevel)
cd "$REPO_ROOT" || exit

# Remove all .joblib files EXCEPT artifacts/model_trainer/model.joblib
find . -type f -name "*.joblib" | while read -r file; do
  if [[ "$file" != "artifacts/model_trainer/model.joblib" ]]; then
    rm -f "$file"
  fi
done

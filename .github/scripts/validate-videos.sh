#!/usr/bin/env bash
set -euo pipefail

dirs=(videos/video-??-*)
if [[ ${#dirs[@]} -eq 0 ]]; then
  echo "No video folders found under videos/"
  exit 1
fi

required=(README.md video.json guion.md code env.example run.sh verify.sh recording.md)
missing=0
for video_dir in "${dirs[@]}"; do
  [[ -d "$video_dir" ]] || continue
  echo "Checking $video_dir"
  for artifact in "${required[@]}"; do
    target="$video_dir/$artifact"
    if [[ ! -e "$target" ]]; then
      echo "Missing $target"
      missing=1
    fi
  done
  if [[ -e "$video_dir/code" && ! -d "$video_dir/code" ]]; then
    echo "code exists but is not a directory in $video_dir"
    missing=1
  fi
done

if [[ $missing -ne 0 ]]; then
  echo "Validation failed: one or more required video artifacts are missing."
  exit 1
fi

echo "Validation completed: all required files are present."

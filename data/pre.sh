for file in preprocessing/*.txt; do
    ./expand6 -v 0 "$file" > expandedv0/"$(basename "$file" .txt)_expanded.txt"
done

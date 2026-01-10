#!/bin/bash

# Output filename
OUTPUT="jekyll_context.txt"

# Clear or create the output file
echo "JEKYLL SITE BUNDLE" > "$OUTPUT"
echo "Generated on $(date)" >> "$OUTPUT"
echo "==========================================" >> "$OUTPUT"

# Find files and append them
# 1. We look in the current directory (.)
# 2. We ignore specific junk folders (_site, .git, etc)
# 3. We look for specific text extensions (.html, .md, .yml, etc)
find . \
  -type d \( -name "_site" -o -name ".git" -o -name ".sass-cache" -o -name ".jekyll-cache" -o -name "node_modules" \) -prune \
  -o -type f \( -name "*.html" -o -name "*.md" -o -name "*.markdown" -o -name "*.yml" -o -name "*.yaml" -o -name "*.css" -o -name "*.scss" -o -name "*.xml" -o -name "*.js" \) \
  -not -name "$OUTPUT" \
  -not -name "bundle.sh" \
  -print0 | while IFS= read -r -d '' file; do
    echo "" >> "$OUTPUT"
    echo "==========================================" >> "$OUTPUT"
    echo "FILE PATH: $file" >> "$OUTPUT"
    echo "==========================================" >> "$OUTPUT"
    cat "$file" >> "$OUTPUT"
    echo "" >> "$OUTPUT"
done

echo "Done! Content saved to $OUTPUT"
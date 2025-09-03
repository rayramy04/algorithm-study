#!/bin/bash

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}=== Algorithm Study Auto Commit ===${NC}"

# Check if there are changes
if [ -z "$(git status --porcelain)" ]; then
    echo -e "${YELLOW}No changes to commit${NC}"
    exit 0
fi

# Show current status
echo -e "\n${GREEN}Current changes:${NC}"
git status --short

# Get all files from git status
py_files=""
py_count=0
other_count=0

while IFS= read -r line; do
    # Get filename (handle renamed files)
    filename="${line:3}"
    if [[ "$filename" == *" -> "* ]]; then
        filename="${filename#* -> }"
    fi
    
    # Remove quotes if present
    filename="${filename%\"}"
    filename="${filename#\"}"
    
    # Check if it's a Python file
    if [[ "$filename" == *.py ]]; then
        problem=$(basename "$filename" .py)
        if [ -z "$py_files" ]; then
            py_files="$problem"
        else
            py_files="$py_files, $problem"
        fi
        ((py_count++))
    else
        ((other_count++))
    fi
done < <(git status --porcelain)

# Generate commit message
if [ $py_count -gt 0 ] && [ $other_count -eq 0 ]; then
    # Only Python files
    if [ $py_count -eq 1 ]; then
        commit_message="feat: solve $py_files"
    else
        commit_message="feat: solve $py_count problems ($py_files)"
    fi
elif [ $py_count -eq 0 ] && [ $other_count -gt 0 ]; then
    # Only non-Python files (docs/config)
    commit_message="docs: update project files"
else
    # Mixed files
    if [ $py_count -eq 1 ]; then
        commit_message="feat: solve $py_files and update docs"
    else
        commit_message="feat: solve $py_count problems and update docs"
    fi
fi

echo -e "\n${GREEN}Commit message:${NC} $commit_message"

# Add all changes
echo -e "\n${GREEN}Adding all changes...${NC}"
git add .

# Commit
echo -e "${GREEN}Committing...${NC}"
git commit -m "$commit_message"

if [ $? -ne 0 ]; then
    echo -e "${RED}Commit failed!${NC}"
    exit 1
fi

# Push to remote
echo -e "\n${GREEN}Pushing to remote...${NC}"
git push

if [ $? -eq 0 ]; then
    echo -e "\n${GREEN}✓ Successfully committed and pushed!${NC}"
else
    echo -e "${RED}Push failed! Please check your connection and try again.${NC}"
    exit 1
fi
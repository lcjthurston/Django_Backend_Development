#!/bin/bash
# Initialize Git Repo, Link to GitHub, and Push Code

# Check if the folder is already a Git repository
if [ -d ".git" ]; then
  echo "This folder is already a Git repository."
else
  echo "Initializing a new Git repository..."
  git init
fi

# Stage all changes and commit
echo "Staging and committing changes..."
git add .
git commit -m "Initial commit"

# Rename the branch to 'main'
echo "Renaming branch to 'main'..."
git branch -M main

# Add the remote GitHub repository URL
REPO_URL="your-repo-url-here"
echo "Adding remote repository: $REPO_URL"
git remote add origin $REPO_URL

# Push changes to the remote repository
echo "Pushing to GitHub..."
git push -u origin main

echo "Git repository setup and initial push complete!"
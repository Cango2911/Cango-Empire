---
name: github-intro
description: GitHub fundamentals for new developers — branches, commits, pull requests, and merging. Use this skill when helping users learn or explain core GitHub workflows: creating branches, committing files, opening PRs, and merging. Covers the complete GitHub beginner workflow from first branch to merged PR.
license: MIT
metadata:
  author: GitHub Skills (github.com/skills)
  source: https://github.com/skills/introduction-to-github
compatibility: Claude Code, any AI coding agent
allowed-tools: Read
---

# Introduction to GitHub

Core GitHub concepts for new developers. Covers the four fundamental operations every GitHub user needs.

## Core Concepts

**Repository** — Project container storing all files and history. Each change is tracked via commits.

**Branch** — An isolated copy of the codebase for making changes without affecting `main`.
- `main` = the default production branch
- Feature branches protect `main` while work is in progress

**Commit** — A saved snapshot of changes with a message describing what changed.

**Pull Request (PR)** — A request to merge changes from one branch into another. PRs enable code review before merging.

## The Standard GitHub Workflow

### Step 1 — Create a branch

```
main ──●──────────────────────────●── (after merge)
        \                        /
         ●── my-branch ──────●──
```

On GitHub.com:
1. Go to the repository → click the branch dropdown (`main`)
2. Type a new branch name → click **Create branch**

Via CLI:
```bash
git checkout -b my-feature-branch
git push -u origin my-feature-branch
```

### Step 2 — Commit a file

On GitHub.com:
1. Switch to your branch
2. Click **Add file** → **Create new file** (or edit an existing file)
3. Make your changes
4. Scroll to **Commit changes** → write a message → click **Commit changes**

Via CLI:
```bash
git add filename.md
git commit -m "Add profile README"
git push
```

Good commit messages: short, active voice, describe the *what* (not the *how*).

### Step 3 — Open a Pull Request

1. Go to the repository → click **Compare & pull request** (banner appears after a push)
   - Or: **Pull requests** tab → **New pull request**
2. Set **base** = `main`, **compare** = your branch
3. Write a title and description
4. Click **Create pull request**

The PR shows a diff of all changes between your branch and `main`. Collaborators can leave review comments.

### Step 4 — Merge the Pull Request

Once approved (or for your own project, when ready):
1. Open the PR → scroll to bottom
2. Click **Merge pull request** → **Confirm merge**
3. Optionally: click **Delete branch** to clean up

After merging, your changes are live on `main`.

## Profile README

A special use case: GitHub displays `README.md` from a repo named exactly `<your-username>` as your profile page.

1. Create repo named `<username>/<username>`
2. Add `README.md` with bio, skills, links
3. It appears at `github.com/<username>`

## Key Terms

| Term | Meaning |
|------|---------|
| `main` | Default branch, usually production-ready |
| Branch | Isolated line of development |
| Commit | Saved change with a message |
| PR | Request to merge one branch into another |
| Merge | Combining branch changes into target branch |
| Fork | Personal copy of someone else's repository |
| Clone | Local copy of a remote repository |

## Common CLI Commands

```bash
git clone <url>              # Copy repo locally
git checkout -b <branch>     # Create and switch to branch
git add <file>               # Stage changes
git commit -m "message"      # Commit staged changes
git push                     # Upload commits to remote
git pull                     # Fetch and merge remote changes
git status                   # Show working tree status
git log --oneline            # Show commit history
```

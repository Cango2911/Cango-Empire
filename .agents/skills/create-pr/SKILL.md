---
name: create-pr
description: Create a well-structured pull request with a clear title, summary, and test plan
---

# Create Pull Request

Use this skill to create a pull request that is easy to review and merge.

## Steps

1. **Gather context**
   - Run `git log --oneline <base>...HEAD` to list all commits on this branch
   - Run `git diff <base>...HEAD --stat` to see which files changed
   - Review the full diff: `git diff <base>...HEAD`

2. **Draft the title**
   - Keep it under 70 characters
   - Use the format: `<type>: <short description>`
   - Types: `feat`, `fix`, `refactor`, `docs`, `chore`, `test`
   - Example: `feat: add checkout flow with Stripe integration`

3. **Write the PR body**
   - **Summary**: 2–4 bullet points describing what changed and why
   - **Test plan**: A checklist of manual steps to verify the change works
   - **Screenshots** (if UI changed): Before and after, or a demo GIF
   - **Related issues**: Link with `Closes #<number>` if applicable

4. **Pre-flight checklist**
   - [ ] Branch is up to date with base branch
   - [ ] All CI checks pass (or failures are explained)
   - [ ] No debug logs or console statements left in code
   - [ ] Self-reviewed the diff

5. **Create the PR**
   ```bash
   git push -u origin <branch-name>
   gh pr create --title "<title>" --body "..."
   ```

## PR Body Template

```markdown
## Summary
- <What changed>
- <Why it was needed>
- <Any notable decisions or trade-offs>

## Test Plan
- [ ] <Manual step to verify feature works>
- [ ] <Edge case to test>
- [ ] Existing tests pass (`npm test` / `cargo test`)

## Screenshots
<!-- Add before/after screenshots for UI changes -->

Closes #<issue-number>
```

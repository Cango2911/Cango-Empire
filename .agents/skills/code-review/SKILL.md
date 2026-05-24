---
name: code-review
description: Comprehensive code review checklist for pull requests
---

# Code Review Checklist

When reviewing code, check each of these areas:

## Functionality
- [ ] Code does what the PR description claims
- [ ] Edge cases are handled
- [ ] Error handling is appropriate
- [ ] No regressions in existing functionality

## Code Quality
- [ ] Follows project style guide
- [ ] No hardcoded values that should be configurable
- [ ] Functions are focused and well-named
- [ ] No unnecessary complexity or premature abstraction

## Testing
- [ ] New functionality has tests
- [ ] Tests are meaningful, not just for coverage
- [ ] Existing tests still pass
- [ ] E2E tests updated where needed

## Security
- [ ] No credentials or secrets in code
- [ ] User input is validated
- [ ] SQL queries are parameterized
- [ ] No XSS, CSRF, or injection vulnerabilities

## Performance
- [ ] No N+1 queries
- [ ] No unnecessary re-renders or heavy computations in hot paths
- [ ] Assets are optimized

## Documentation
- [ ] Public APIs are documented
- [ ] README updated if behavior changes
- [ ] Changelog entry added if applicable

## Steps

1. Fetch the PR diff and description
2. Check each category above and note any findings
3. Summarize findings: critical issues, suggestions, and what looks good
4. Post review with inline comments on specific lines

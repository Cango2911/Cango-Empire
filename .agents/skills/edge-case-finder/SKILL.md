---
name: edge-case-finder
description: Systematically identify edge cases and boundary conditions for a feature or function
---

# Edge Case Finder

Use this skill to discover edge cases before writing tests or during code review.

## When to Use
- Before writing tests for a new feature
- During code review to check what scenarios are unhandled
- When debugging a bug that slipped through testing

## Categories of Edge Cases

### Input Boundaries
- [ ] Empty / null / undefined values
- [ ] Minimum and maximum allowed values (off-by-one)
- [ ] Negative numbers, zero, very large numbers
- [ ] Strings: empty string, whitespace only, very long string, special characters, unicode
- [ ] Arrays/lists: empty, single element, duplicates, max size

### State & Timing
- [ ] Concurrent requests / race conditions
- [ ] Operations on already-deleted resources
- [ ] Session expiry mid-flow
- [ ] Network timeout or partial response

### Permissions & Auth
- [ ] Unauthenticated user
- [ ] User with insufficient permissions
- [ ] Cross-user data access (user A accessing user B's data)

### Data Integrity
- [ ] Partial failures (e.g., DB write succeeded but email failed)
- [ ] Duplicate submissions (double-click, retry)
- [ ] Stale data (UI is out of sync with server state)

### Environment
- [ ] Different browsers / devices (for frontend)
- [ ] Locales and timezones
- [ ] Missing environment variables or config

## Steps

1. **Name the feature/function** to analyze
2. **List normal inputs** (happy path)
3. **Apply each category above** and generate specific test cases
4. **Rank by likelihood and severity** — focus on the ones most likely to cause real issues
5. **Write tests or document findings** for the highest-priority cases

## Example

**Feature:** User registration form

| Category | Edge Case | Expected Behavior |
|---|---|---|
| Input | Email with + sign (`user+tag@example.com`) | Accepted as valid |
| Input | Password = 1 character | Rejected with validation error |
| Duplicate | Submit button clicked twice | Only one account created |
| Auth | Already logged-in user visits register | Redirect to dashboard |
| State | Email already exists in DB | Clear error: "Email already in use" |

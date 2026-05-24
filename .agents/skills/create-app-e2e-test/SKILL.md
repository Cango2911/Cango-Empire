---
name: create-app-e2e-test
description: Create end-to-end tests for an application feature or user flow
---

# Create App E2E Test

Use this skill to write end-to-end tests that validate real user workflows from the browser or API level.

## When to Use
- A new feature or page needs coverage
- A critical user flow is unprotected
- A bug fix needs a regression test

## Steps

1. **Understand the flow**
   - Identify the start and end state of the user journey
   - List all interactions: clicks, form inputs, navigation, API calls

2. **Set up the test file**
   - Place tests in the appropriate directory (e.g., `tests/e2e/`, `cypress/e2e/`, `playwright/`)
   - Follow naming convention: `<feature>.spec.ts` or `<feature>.test.ts`

3. **Write the test**
   - Use `describe` blocks to group related scenarios
   - Name tests with the pattern: `it('should <expected behavior> when <condition>')`
   - Cover the happy path first, then edge cases
   - Assert on visible UI state, not internal implementation

4. **Handle async and state**
   - Wait for network requests to complete before asserting
   - Reset state between tests (clear cookies, reset DB if needed)
   - Use test fixtures for predictable data

5. **Run and verify**
   - Run the test locally and confirm it passes
   - Confirm it fails when the feature is broken (mutation testing)

## Example Structure

```typescript
describe('Checkout flow', () => {
  beforeEach(() => {
    cy.visit('/cart');
    cy.fixture('cart-items').then(items => cy.setupCart(items));
  });

  it('should complete purchase with valid card', () => {
    cy.get('[data-testid="checkout-btn"]').click();
    cy.fillPaymentForm({ card: '4242424242424242' });
    cy.get('[data-testid="submit-order"]').click();
    cy.url().should('include', '/order-confirmation');
    cy.contains('Order placed successfully');
  });

  it('should show error with declined card', () => {
    cy.get('[data-testid="checkout-btn"]').click();
    cy.fillPaymentForm({ card: '4000000000000002' });
    cy.get('[data-testid="submit-order"]').click();
    cy.contains('Your card was declined');
  });
});
```

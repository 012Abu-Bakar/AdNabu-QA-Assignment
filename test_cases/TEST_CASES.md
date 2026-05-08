# Task 1 - Test Design

## A. Product Search Test Cases

### TC_01 - Search with valid product name
- **Scenario:** Verify user can search for an existing product
- **Steps:**
  1. Open the store
  2. Enter valid product name in search field
  3. Click Search / Press Enter
- **Expected Result:**
  - Relevant product should be displayed successfully

---

### TC_02 - Search with invalid product name
- **Scenario:** Verify behavior when searching for a non-existing product
- **Steps:**
  1. Open the store
  2. Enter invalid/random product name
  3. Click Search
- **Expected Result:**
  - No matching products should be displayed
  - Appropriate message should appear

---

### TC_03 - Search with empty input (Edge Case)
- **Scenario:** Verify search behavior without entering input
- **Steps:**
  1. Open the store
  2. Keep search field empty
  3. Click Search
- **Expected Result:**
  - User should remain on same page OR validation should appear
  - Application should not crash

---

# B. Add to Cart Test Cases

### TC_04 - Add available product to cart
- **Scenario:** Verify user can add available product to cart
- **Steps:**
  1. Open product page
  2. Click "Add to Cart"
- **Expected Result:**
  - Product should be added successfully
  - Cart should update correctly

---

### TC_05 - Add multiple quantities of same product
- **Scenario:** Verify quantity update functionality in cart
- **Steps:**
  1. Add product to cart
  2. Increase quantity
- **Expected Result:**
  - Product quantity should update correctly
  - Cart total should update accordingly

---

### TC_06 - Add out-of-stock product to cart
- **Scenario:** Verify behavior for unavailable product
- **Steps:**
  1. Open out-of-stock product
  2. Attempt to add product to cart
- **Expected Result:**
  - Product should not be added
  - Proper stock/unavailable message should appear
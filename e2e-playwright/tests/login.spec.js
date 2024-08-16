const { chromium, test, expect } = require('@playwright/test');

String.prototype.contains = function(it) {
  return this.indexOf(it) != -1;
};

// var helper = require('../test_helper');


test.describe(() => {
  
  test.beforeAll(async () => {
      // const browser = await chromium.launch();
      // const page = await browser.newPage();

      // Go to the starting url before each test.
  });

  test.beforeEach(async ({ page }) => {
    await page.goto('https://travel.agileway.net');
  });

  test.afterAll(async () => {
    console.log('After tests');
  });

  test('Login failed', async ({ page }) => {
    await page.fill("#username", "agileway")
    await page.fill("#password", "playwright")
    await page.click("input:has-text('Sign in')")
    await expect(page.locator("//body")).toHaveText("Invalid email or password")

    // await page.textContent("body").then(function(body_text) {
    //   console.log(body_text)
    // })
  });


});
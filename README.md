# 🚕 Urban Routes - E2E Test Automation

## 📋 Project Description

This project contains a set of **end-to-end (E2E) automated tests** for the **Urban Routes** application, developed to validate the complete transportation service request flow from the end user's perspective.

The automated tests cover the following scenarios:

* 📍 Setting origin and destination addresses.
* 🚖 Selecting the **Comfort** fare.
* 📱 Entering and verifying a phone number.
* 💳 Adding and selecting a credit card.
* 💬 Writing a message for the driver.
* 🧸 Requesting additional items:

  * Blanket and tissues.
  * Two ice creams.
* 🔎 Verifying the taxi search modal.

---

## 🛠️ Technologies Used

| Technology             | Description                                                                    |
| ---------------------- | ------------------------------------------------------------------------------ |
| **Python**             | Programming language used to develop the automated tests.                      |
| **pytest**             | Framework used to organize and execute the test cases.                         |
| **Selenium WebDriver** | Tool used to automate interactions with the web browser.                       |
| **Git / GitHub**       | Version control system and repository used to manage the source code.          |

---

## 🧪 Techniques and Best Practices Applied

### 📂 Page Object Model (POM)

Design pattern used to improve the maintainability and scalability of the project by encapsulating the elements and actions of each page into separate classes.

### 🔄 End-to-End (E2E) Testing

Automation and validation of the complete user flow by simulating real-world usage scenarios of the application.

### ⏱️ Explicit Waits

Implementation of explicit waits to handle dynamic elements and properly synchronize test execution with the behavior of the user interface.

### 🎯 Element Locator Strategies

Use of different types of selectors to identify elements efficiently and reliably:

* `ID`
* `Class Name`
* `XPath`

---

## 🎯 Project Objective

To strengthen practical skills in **web test automation** by applying test design principles and development best practices to help ensure the quality and reliability of user-facing applications.

---

## ▶️ Running the Tests

To run the test suite, use the following command:

```bash
pytest
```

For more detailed output during execution:

```bash
pytest -v
```

---

## 📌 Skills Demonstrated

* Functional test design and automation.
* Implementation of the **Page Object Model** pattern.
* Handling dynamic elements with Selenium.
* Application of test automation best practices.
* Organization of test suites with pytest.
* Use of Git for version control.


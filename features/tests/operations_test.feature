Feature: Tests for simple operations
  Background:
    Given App is running

  Scenario: User can sum numbers
    When Tap on Digit 2
    When Tap on Sum
    When Tap on Digit 3
    When Tap on Equality
    Then Result is shown and equal to 5

  Scenario: User can subtract numbers
    When Tap on Digit 7
    When Tap on Minus
    When Tap on Digit 6
    When Tap on Equality
    Then Result is shown and equal to 1

  Scenario: User can divide numbers
    When Tap on Digit 8
    When Tap on Divide
    When Tap on Digit 4
    When Tap on Equality
    Then Result is shown and equal to 2

  Scenario: User can multiply numbers
    When Tap on Digit 5
    When Tap on Multiply
    When Tap on Digit 9
    When Tap on Equality
    Then Result is shown and equal to 45

  Scenario: User can multiply float numbers
    When Type Digits 3.33
    When Tap on Multiply
    When Tap on Digit 3
    When Tap on Equality
    Then Result is shown and equal to 9.99

  Scenario: User can get square root
    When Open advanced operations
    When Tap on Square root
    When Tap on Arrow
    When Tap on Digit 9
    When Tap on Equality
    Then Result is shown and equal to 3

  Scenario: User can delete digits
    When Type Digits 1234
    When Tap on DELETE
    When Tap on DELETE
    Then Now on the screen 12

    Scenario: User can clear result screen
    When Tap on Digit 2
    When Tap on Sum
    When Tap on Digit 3
    When Tap on Equality
    When Tap on Clear
    Then Screen is empty
Statement.md
# Problem Statement: Password Generator Application

## 1. Overview
The objective of this project is to build a command-line Python application that generates randomized passwords based on specific user constraints, ensuring both security and predictability in the character selection process.

## 2. Core Logic & Requirements
* **Length Constraint**: The user must be able to specify password length. The system must enforce a minimum length of 4 characters.
* **Character Categories**: The user can toggle the inclusion of numerical digits ('0-9') and special symbols ('!@#$%', etc.).
* **Guaranteed Allocation**: The algorithm must not rely purely on random chance from a combined pool. If a user requests symbols and numbers, the script must guarantee that at least one symbol and one number exist in the final output before randomizing the remaining characters.
* **Error Handling**: The application must not crash if the user enters a non-integer value for the password length.

## 3. Technology Stack
* **Language**: Python 3.x
* **Dependencies**: Built-in modules only ('random', 'string').
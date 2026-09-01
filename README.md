# Prescription Validator

## BSc IT Semester 3 Python Project

### Domain
Healthcare

### Project Title
Prescription Validator

## Problem Statement

Develop a decision-support application for prescription validation
that analyzes prescription data and generates useful validation
alerts instead of only storing records.

## Objective

The main objective of this project is to create a simple web-based
application using Python and Flask that performs basic prescription
validation and consistency checks.

## Core Features

1. Dosage validation
2. Duplicate medicine detection
3. Missing fields detection
4. Drug schedule parsing
5. Alert generation

## Technologies Used

- Python
- Flask
- HTML
- CSS
- JavaScript

## Python Concepts Used

The project uses concepts from the BSc IT Semester 3 Python syllabus:

- Variables
- Data types
- Operators
- If-else statements
- For loops
- Functions
- Lists
- Dictionaries
- Sets
- Regular expressions
- Exception handling
- File handling
- Flask

## Project Structure

prescription-validator/

    app.py
    validator.py
    requirements.txt
    README.md

    reports/
        reports.txt

    templates/
        index.html

    static/
        style.css
        script.js

## How the Application Works

1. The user enters prescription details.
2. Flask receives the form data.
3. Python processes the prescription.
4. Missing fields are detected.
5. Medicine names are checked for duplicates.
6. Dosage format is validated using regular expressions.
7. Medicine schedules are parsed.
8. Alerts are generated.
9. A validation report is saved in a text file.
10. The results are displayed on the web page.

## Medicine Input Format

Each medicine should be entered on a new line.

Format:

Medicine Name, Dosage, Schedule

Example:

Paracetamol, 500 mg, twice daily
Amoxicillin, 500 mg, three times daily

## Disclaimer

This is an educational project and performs basic format and
consistency checks. It does not determine whether a medicine or
dosage is medically appropriate and should not replace review by
a qualified healthcare professional.

# Major Indecision Capstone

## Overview

**Major Indecision** is a Python capstone project I created for a high school Procedural Programming course in 2025.

The program collects information about an incoming college freshman class and its general education requirements, then uses that information to estimate the resources and staffing needed to accommodate students who still need to complete those requirements.

The project was designed around the idea of using student academic history to help a college anticipate its needs for an incoming class.

## Features

* Collects the estimated size of an incoming freshman class
* Accounts for students entering with college credit from high school
* Allows users to define general education requirements
* Collects resource requirements for each course, including:

  * Textbooks
  * Field trips
  * Laboratory space
  * Laboratory equipment
* Estimates how many incoming students still need each course
* Estimates the number of teachers needed based on a student-to-teacher ratio
* Generates a research summary for each course

## Programming Concepts

This project demonstrates several foundational Python and procedural programming concepts, including:

* Functions
* Loops
* Conditional statements
* User input and validation
* Lists and list indexing
* String manipulation
* Type conversion
* Mathematical calculations
* Modular program design

The project uses separate functions to calculate the number of students who still need a requirement, estimate course resources, and calculate staffing needs.

## How It Works

The program begins by asking the user whether they want to run a freshman survey or view the research summary.

When running the survey, the user provides information about:

1. The size of the incoming freshman class
2. Students entering with existing college credit
3. General education courses
4. Resources required by each course
5. The number of students who have already completed each requirement
6. The average student-to-teacher ratio

The program then uses these inputs to estimate the number of students who still need each course and the resources and teachers that may be required.

## Example Calculations

For each general education requirement, the program calculates the estimated number of students who still need the course:

`students needing course = total freshman - students who have already completed requirement`

It then uses that value to estimate resources such as textbooks, laboratory equipment, field-trip costs, and laboratory space.

## Project Context

This project was completed as a capstone assignment for a high school Procedural Programming course.

It represents my early experience designing a larger program from the ground up and combining multiple programming concepts into one project.

## What I Learned

This project gave me experience breaking a larger problem into smaller functions and using user-provided data to perform calculations and generate a summary. It also helped me practice organizing a program around reusable functions rather than putting all of the logic in one section of code.

As an earlier programming project, this repository also represents part of my progression as I continue developing my programming and software development skills.

## Technologies

* Python
* Python Standard Library (`math`)

## Author

Abigail Andre-St Fleur

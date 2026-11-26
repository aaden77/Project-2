# Project-2: Personal Budget Tracker

Student Information: Aaden Rowe - 2602969

Course Code: CNS1001

Problem Statement:
Many students struggle to monitor their income and expenses, leading to poor management of their finances and irresponsible financial decisions.

Program Description:

The Personal Budget Tracker is a menu-driven Python application that helps users manage their finances. This project was developed to provide users with a simple budgeting system that allows them to record income and expenses, allocate budgets to spending categories, monitor savings goals, and generate financial summaries.

The main features of this system include:

● Creating a monthly budget plan.

● Allocating funds to spending categories.

● Recording income.

● Recording expenses.

● Tracking category spending.

● Displaying remaining budget per category.

● Generating spending summaries.

● Monitoring savings goals.

● Providing overspending warnings.

● Saving and loading budget information using CSV files.


Program Flow:

1. User launches the program.
   
2. Main menu is displayed.
   
3. User selects an option.
   
4. Program performs the selected task.
   
5. Data is stored in dictionaries and lists.
   
6. User may save data to a CSV file.
   
7. Program continues until Exit is selected.
   

Programming Concepts Used:

Functions were used to organize the program into smaller, reusable sections.

Loops were used to repeatedly request input until valid data was entered.

Conditionals like if, elif, and else statements were used to validate user input and control menu selection.

Dictionaries were used to store budget and category information.

Lists were used to store transaction records.

Input validation ensures users enter appropriate values.

try/except blocks were used to prevent the program from crashing when invalid data is entered.

CSV file handling was implemented to save and load transaction data.



How to Run the Program

Python Version: Python 3.12

1. Open the project folder.
   
2. Run the file Budget Management System.py.
   
3. The main menu will appear.

4. Select 1 to set a monthly budget.

5. Select 2 to set a savings goal.

6. Select 3 to allocate category budgets.

7. Select 4 to add income.

8. Select 5 to add expenses.

9. Use options 6-9 to view reports and summaries.

10. Use 10 to save transactions and 11 to load previous transactions.

11. Select 12 to exit the program.
    

Required Libraries
CSV: To save and load transaction data from CSV files



Manual Testing and Validation

Test Case	            Input	              Expected Output	                Actual Output	             Result

Valid menu choice	        1	             Budget option opens	          Budget option opened	         Pass

Valid income amount	    1500	            Income recorded	             Income recorded	               Pass

Invalid income amount    -50	           Error message displayed	      Error message displayed	         Pass

Invalid text input	     abc	            Invalid input message	       Invalid input message	         Pass

Empty/Boundary value	      0	           Error message displayed	         Error message displayed	       Pass



Challenges and Lessons Learned

One challenge encountered was implementing input validation while ensuring the program did not crash when users entered invalid data so to solve this, I used try/except blocks and validation checks.

I learnt how functions, dictionaries, lists, loops, file handling, and exception handling can be combined to develop a complete budgeting application.



AI Assistance Disclosure and References

AI Tool Used: Microsoft Copilot

Purpose of Assistance:

Explaining the different Python programming concepts and syntax I used

Reviewing the code I wrote for errors and improvement

Assisting with README structure and format



Declaration of Authorship

I declare that this work is my own, that any AI assistance is fully disclosed in this README, and that I can explain every part of the submitted code.



Member Contribution Report

All the work is mine.



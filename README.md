# BMW AI Fundamentals Quiz
 
## Introduction
I work within the Artificial Intelligence (AI) team at BMW, where we develop, evaluate and support AI-based solutions across our business functions. Our work includes preparing data, validating performance, and ensuring safe and responsible deployment practices. In an automotive context, incorrect assumptions about AI systems and what it does can lead to misunderstandings around reliability, safety, and decision-making.
As AI implementation increases within BMW, it becomes important that staff understand the concepts of AI. New joiners, cross-functional teams, or non-technical stakeholders may not fully understand how AI systems work, why they require data, or why they sometimes produce incorrect outputs. If there is misunderstanding around AI it can reduce trust and reliability in the AI systems we use. 
As a result, I created a Minimum Viable Product (MVP) quiz application using Python and Tkinter. The application allows staff to complete a short internal knowledge check focused on AI fundamentals and selected topics that are relevant to BMW’s AI development. Users will enter their name, answer seven multiple-choice questions (five foundation and two advanced), and receive a final score. Each attempt is stored in a CSV file and can be viewed within the application and exported for further analysis. The score is visible, which allows employees to identify gaps in their knowledge and retake the test if they receive a low score.
The project focuses on professional development practices including programming, a modular code design, input validation, exception handling, data storage, and continuous integration using GitHub Actions.
 










## Design 
### GUI Design
The graphical user interface (GUI) is designed to be simple, clean, and suitable for internal staff use. Figure 1 shows:






    














Figure 1: Wireframe

## User Journey
1.	User opens the application.
2.	User enters their name.
3.	User clicks “Start Quiz”.
4.	User answers seven multiple-choice questions.
5.	User receives a final score.
6.	User can view attempts and save to a CSV file.
The interface provides clarity and ease of use for the users. This aligns with the MVP objective and ensures accessibility for non-technical users.
 
## Functional Requirements
### The system will:
•	Allow a user to input their name.
•	Display seven multiple-choice questions.
•	Must have a valid answer before moving to the next question.
•	Calculate the final score.
•	Save quiz attempts to a CSV file.
•	Display previous attempts in a table.
•	Allow exporting of stored attempt data.
 
## Non-Functional Requirements
### The system will:
•	Be easy to use and intuitive.
•	Run locally without requiring a database.
•	Ensure readability to all users and have a clear structure.
•	Use a transparent storage format (CSV).
•	Be maintainable and modular.
 

## Tech Stack 
•	Python 3
•	Tkinter (GUI framework)
•	CSV module (storage)
•	Pytest (unit testing framework)
•	Git & GitHub (version control)
•	GitHub Actions (continuous integration)
 
## Code Design
### The project follows a modular structure:
bmw-ai-quiz/
│
├── main.py
├── quiz/
│ ├── models.py
│ ├── logic.py
│ ├── validators.py
│ └── store.py
├── tests/
│ ├── test_logic.py
│ └── test_validators.py
└── data/
└── attempts.csv

## Object-Oriented Design
Two classes are implemented:
•	Question
•	QuizAttempt
The Question class stores the question text, answer options, and correct answer index.
The QuizAttempt class stores user name, score, total questions, and timestamp.
This separation ensures:
•	Clear responsibilities
•	Reusability
•	Improved maintainability

## Development
The application was developed incrementally using Git for version control. Features were added step-by-step:
1.	Basic Tkinter window
2.	Question display logic
3.	Answer validation
4.	Score calculation
5.	CSV storage
6.	Attempt viewing
7.	Export functionality
8.	Unit tests
9.	Continuous integration

## Core Logic
The build_questions() function creates and returns a list of Question objects.
The grade() function compares selected answers against correct answers and returns a score.
Separating grading logic from the GUI allows it to be unit tested independently.
 
## Input Validation
Validation is implemented in validators.py using pure functions:
•	validate_name()
•	validate_choice()
These functions:
•	Have no side effects
•	Return consistent outputs
•	Are easily testable
This demonstrates understanding of functional programming principles within Python.
 


## Storage
The system uses CSV storage via Python’s built-in csv module.
Each attempt saves:
name, timestamp, score, total
 
## Testing Section
Two types of testing were used:

## Manual Testing
Manual testing ensures:
•	GUI flows correctly
•	Validation prevents invalid inputs
•	Scores calculate correctly
•	CSV file updates properly
•	Export functionality works

### Manual Test Results
| Test Case            | Description                         | Expected Result      | Outcome |
|----------------------|-------------------------------------|----------------------|----------|
| Empty Name           | Click Start without name            | Error message shown  | Pass     |
| No Answer Selected   | Click Next without selecting answer | Error message shown  | Pass     |
| Score Calculation    | Select all correct answers          | Full score displayed | Pass     |
| CSV Save             | Complete the quiz                   | Row added to CSV     | Pass     |
| Export CSV           | Click Export CSV                    | File saved correctly | Pass     |

## Automated Unit Testing
Pytest was used to test:
•	Name validation logic
•	Answer validation logic
•	Grading function
Automated tests ensure consistent behaviour and prevent failures.
 


## Unit Testing Results
All unit tests passed locally using:
pytest -q
Continuous integration on GitHub Actions also successfully executed all tests automatically on push, confirming correct configuration.

This demonstrates an understanding of automated quality assurance practices.

However, the initial CI run failed because GitHub Actions could not locate the local quiz package whilst running pytest. This was resolved by configuring the PYTHONPATH in the workflow file, allowing the test environment to correctly detect project modules.

 



## Documentation

### How to Run the Application
1.	Install Python 3.
2.	Install dependencies:
pip3 install -r requirements.txt
3.	Run:
python3 main.py

### How to Use
•	Enter your name.
•	Answer all questions.
•	View your final score.
•	Use “View Attempts” to see past results.
•	Use “Export CSV” to download results.
 
## Technical Documentation

### Running Tests
pytest

### Continuous Integration
GitHub Actions runs tests automatically on:
•	Push
•	Pull request
This ensures code reliability and aligns with modern DevOps practices.
 
## Evaluation Section
The project has successfully achieved its objectives by delivering a complete MVP quiz application aligned with professional software development practices. The modular design improved maintainability and allowed the core grading logic to be tested independently of the GUI.
One strength of the project was the implementation of automated unit testing and continuous integration. This demonstrated awareness of modern software engineering workflows and the importance of automated validation.
Another strength is the use of object-oriented programming to represent domain concepts such as questions and quiz attempts. This improves code organisation and future enhancements.
If further development time was available, improvements could include:
•	Enhanced GUI layout using frames
•	Randomised question order
•	More AI-related content
•	User authentication for multi-user environments
Overall, the project demonstrates a clear understanding of core programming principles, modular design, testing strategies, persistent data storage, and professional development workflows.
 



## Conclusion
This project demonstrates: core python programming skills, GUI design and development, data persistency, input validation and exception handling, automated testing and finally continuous integration. The final solution provides a practical internal knowledge-check app which is suitable for use within the BMW’s AI team while showcasing modern software engineering practices.

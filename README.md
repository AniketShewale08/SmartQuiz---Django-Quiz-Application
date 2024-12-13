SmartQuiz - Django Quiz Application

Overview
 SmartQuiz is a Django-based quiz application that allows users to take quizzes on various topics, view their results, and track their performance. 
 Users can sign up, log in, and answer multiple-choice questions.
 The system provides feedback on their answers and displays detailed results at the end of the quiz.

Features

- User Authentication:

    - Users can sign up, log in, and log out.
    - Password encryption is handled using Django’s default authentication system.

- Multiple Quiz Types:

   - Supports various categories and quiz types (e.g., Programming, Science, General Knowledge).
   - Each quiz contains multiple-choice questions with four options.

- Quiz Attempt:

   - Users can take quizzes by selecting answers from provided options.
   - After submitting answers, the system immediately evaluates the quiz and displays detailed results.

- Result Feedback:

   - The result page shows the total number of questions, the number of correct answers, and incorrect answers.
   - Detailed feedback is given for each question, showing the user's answer, the correct answer, and whether the answer was correct or incorrect.

- Responsive Design:

   - The application uses Bootstrap for responsive design, making it accessible on mobile and desktop devices.

- Admin Panel:

   - The Django admin panel allows for easy management of quizzes, questions, and users.

- Requirements

Before setting up the project, ensure you have the following:

  - Python 3.x (Recommended version: 3.8+)
  - Django 3.x or higher
  - Anaconda for environment management (Optional but recommended)
  - SQLite Database (default setup), but you can switch to MySQL or PostgreSQL if needed

- Setup Instructions
  1. Clone the repository
     Clone the project from GitHub using the following command:

     git clone https://github.com/your-username/smartquiz.git
     cd smartquiz

  2. Create a new Anaconda environment (Optional but recommended)
     If you are using Anaconda, create a new environment for the project.
     This ensures that dependencies are isolated:
 
     conda create --name smartquiz-env python=3.8

  3. Activate the environment
     Activate the newly created environment:
   
     conda activate smartquiz-env

  4. Apply migrations to set up the database
     Run the following command to apply Django’s database migrations:
   
       python manage.py migrate  
     This will set up the default SQLite database and create necessary tables for users, quizzes, and questions.

  5. Create a superuser for admin access
     To manage the app via the Django admin panel, create a superuser:
   
       python manage.py createsuperuser
     Follow the prompts to set up the superuser (username, email, and password).

  6. Run the development server
     Now, run the Django development server:
     
       python manage.py runserver
     By default, the app will be accessible at http://127.0.0.1:8000/.

  7. Access the admin panel
     To manage your quizzes, questions, and user data, you can access the Django admin panel by going to:
       http://127.0.0.1:8000/admin/
   
     Log in with the superuser credentials you created earlier.

- Usage

  1. User Registration and Login:
      
      - Users can sign up with a username, email, and password.
      - Once registered, they can log in and start taking quizzes.

  2. Taking a Quiz:

      - After logging in, users will be able to choose a quiz type.
      - They will answer multiple-choice questions and submit their answers.

  3. Results Page:

      - After submitting answers, users will see their quiz results, including:
      - Total number of questions
      - Number of correct answers
      - Number of incorrect answers
      - Detailed feedback on each question answered

  4. Admin Panel:
     
     - The Django admin panel can be used to add/edit quizzes, questions, and manage user data.

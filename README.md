# Coding I - Encryption and Authentication Project

**Due date:** 4/10

When you finish, add your names and a demo video link here, then submit one link to your project repository.

**Group Members:** (list all group members here)
* [Demo Video (1 per group)](http://includeyourlinkhere)

In this project, you will design and build a web application with a basic **login system** in Python using Flask. This project is broken into four major phases, each of which will teach a critical part of building a secure application. You will use GitHub to collaborate with your group and track your progress.   

#### [Please Fork this Repo to begin](https://github.com/rlj0713/coding-1-game/fork)
---
### Helpful Links for This Unit:
* [Flask Documentation](https://flask.palletsprojects.com/en/2.3.x/)
* [SQLite Documentation](https://www.sqlite.org/docs.html)
* [Bcrypt Documentation](https://pypi.org/project/bcrypt/)
* [Regex Tutorial for Python](https://docs.python.org/3/library/re.html)
* [GitHub Cheat-Sheet](https://education.github.com/git-cheat-sheet-education.pdf)

---

## Project Requirements:

| Part I: Planning & Design (15 pts) |
|----------|
* Decide on an app idea and core goal
* Application idea is written or sketched out
* Write a simple plan in the planning_and_design.txt file showing how the app will work step-by-step
* Do not move forward to the next phase until checking with Mr. Jackson

| Phase II: Build Login & Registration Structure (15 pts) |
|----------|
* Create a basic Flask app with a login page and registration page.
* Include fields for username and password.
* Display a message for successful login and an error for incorrect login attempts.
* Add navigation between login and registration pages.
* Confirm that basic functionality works before moving to the next phase.

| Phase III: Store Passwords in a Database (20 pts) |
|----------|
* Set up an SQLite database to persist user data.
* Store username and password fields in the database.
* Ensure that user data remains intact even when the app is restarted.
* Verify that registration adds users correctly and login checks the database.

| Phase IV: Encrypt Passwords with Bcrypt (20 pts) |
|----------|
* Install and use bcrypt to hash passwords before storing them in the database.
* Update the login logic to verify passwords against the hashed values.
* Ensure that passwords are never stored in plain text.
* Test that registration and login work correctly for multiple users.

| Phase V: Require Password Complexity (15 pts) |
|----------|
* Implement password validation rules:
  - At least 1 uppercase letter
  - At least 1 lowercase letter
  - At least 1 number
  - At least 1 special character
* Display a clear error message if the password does not meet the requirements.
* Ensure that registration only succeeds if the password meets the rules.
* Test the validation thoroughly with multiple password examples.

| Phase VI: Reflection + Demo Video (15 pts) |
|----------|
* Record a screen-share of another student testing your login system.
* Show a screen-share of your code and explain how each phase was implemented.
* Describe at least 3 portions of your code that you are most proud of.
* Both group members should speak during the video.

| Optional Bonus (+10 pts / each) |
|----------|
* Add a “secret page” that displays the user’s name after login.
* Style the pages with CSS to improve the user interface.
* Implement a “Reset Database” button for easy testing.
* Add additional security features (e.g., session timeouts, email verification).
=======
        * Style the pages with CSS to improve the user interface.
        * Implement a “Reset Database” button for easy testing.
        * Add additional security features (e.g., session timeouts, email verification).

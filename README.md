
EOA Project

A Django-based web application with user authentication and number analysis functionality. This project demonstrates user registration, login, and logout features along with a simple even-odd number identification tool.

---

Features

1. User Authentication
   - User Registration
   - User Login
   - User Logout

2. Even-Odd Number Analysis
   - Input a number to determine whether it is even or odd.

---

Prerequisites

Ensure you have the following installed:
- Python 3.8 or later
- Django 4.2 or later

---

Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/eoa_project.git
   cd eoa_project
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. Install required dependencies:
   ```bash
   pip install django
   ```

4. Navigate to the project directory and apply migrations:
   ```bash
   python manage.py migrate
   ```

---

Usage

1. Start the development server:
   ```bash
   python manage.py runserver
   ```

2. Open your web browser and navigate to:
   ```
   http://127.0.0.1:8000/
   ```

---

Project Structure

- eoa_project/: Main project folder containing settings, URLs, and WSGI configurations.
- auapp/: App folder containing views and templates for user authentication and even-odd functionality.
- templates/: HTML templates for pages like login, signup, and even-odd functionality.

---

Endpoints

1. /: User dashboard (requires login)
2. /ulogin: User login page
3. /usignup: User signup page
4. /ulogout: User logout
5. /eo: Even-Odd analysis tool (requires login)

---

Views

1. uhome: Renders the dashboard for authenticated users.
2. ulogin: Handles user login.
3. usignup: Facilitates user registration.
4. ulogout: Logs out the user.
5. eo: Accepts a number input and determines whether it is even or odd.

---

Templates

- uhome.html: Dashboard view.
- ulogin.html: Login page.
- usignup.html: Signup page.
- eo.html: Even-Odd analysis page.

---

Deployment

1. Modify the DEBUG setting in eoa_project/settings.py to False for production:
   ```python
   DEBUG = False
   ALLOWED_HOSTS = ['your-deployment-domain.com']
   ```

2. Collect static files:
   ```bash
   python manage.py collectstatic
   ```

3. Deploy the project using your preferred platform (e.g., PythonAnywhere, Heroku).

---

Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

---

License

This project is licensed under the MIT License. See the LICENSE file for more details.

---

Author

Developed by Kunal patil

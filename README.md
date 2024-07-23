# Django Security Checklist

This is a Django web application focused on enhancing web security by integrating the following security strategies:

- Integrate a reCAPTCHA
- Two-Factor Authentication (2FA) with a virtual device
- Manage failed login attempts
- Add a session timeout
- Password management
- Configure behind-the-scenes security settings
- Additional security measures
- General advice on better security management

## Project Origin

This project was developed following the course on Udemy: Python Django Ultimate Web Security Checklist 2022

## Getting Started

To run this project on your local machine, follow these steps:

### Prerequisites

- Python installed (preferably Python 3.8 or higher)
- Django installed (version 3.2 or higher)
- Git installed

### Backend Setup

1. Navigate to the project directory.
   ```bash
   cd DjangoSecurityChecklist
2. Create and activate a virtual environment.
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install the required packages.
   ```bash
   pip install -r requirements.txt
4. Apply the database migrations.
   ```bash
   python manage.py migrate
5. Run the development server.
   ```bash
   python manage.py runserver

## Usage

- Open a web browser and navigate to http://127.0.0.1:8000/.
- Register a new account or log in with an existing one.
- Explore the security features of the application, such as reCAPTCHA, 2FA, session timeout, and more.

## Technical Specification

- **Security Features:** The project integrates reCAPTCHA, 2FA, session timeout, and robust password management.
- **Session Management:** Enhanced session security with session timeouts and management of failed login attempts.
- **Backend:** Built with Django, following best practices for security configurations.
- **Authentication:** Uses Django's built-in authentication mechanisms, enhanced with JWT and OAuth 2.0 standards where applicable.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

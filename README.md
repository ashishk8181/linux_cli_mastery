# Linux CLI Mastery

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Build Tailwind CSS

```bash
# One-time build
./tailwindcss -i users/static/css/style.css -o users/static/css/output.css --minify

# Or watch mode for development
./build-css.sh
```

### 3. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Load modules

```bash
python3 manage.py load_module{i}
```

### 5. Run Server

```bash
python manage.py runserver
```

## Features

- **Email/Password Authentication**: Users can sign up and login with email and password
- **Google OAuth**: One-click sign in with Google account
- **Free Integrated terminal**: Linux terminal to practice commands
- **User Profile**: View and edit profile with avatar upload
- **Progress Tracking**: User progress stored in JSON field
- **Avatar Dropdown**: Click avatar in top-right to access profile and logout

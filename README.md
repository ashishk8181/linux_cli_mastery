# Linux CLI Mastery - Users App

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

### 3. Configure Google OAuth
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing one
3. Enable Google+ API
4. Create OAuth 2.0 credentials (Web application)
5. Add authorized redirect URI: `http://localhost:8000/users/google/callback/`
6. Update `settings.py` with your credentials:
   - `GOOGLE_CLIENT_ID`
   - `GOOGLE_CLIENT_SECRET`

### 4. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser
```bash
python manage.py createsuperuser
```

### 6. Run Server
```bash
python manage.py runserver
```

## Features

- **Email/Password Authentication**: Users can sign up and login with email and password
- **Google OAuth**: One-click sign in with Google account
- **User Profile**: View and edit profile with avatar upload
- **Progress Tracking**: User progress stored in JSON field
- **Avatar Dropdown**: Click avatar in top-right to access profile and logout
- **Tailwind CSS**: Standalone Tailwind CSS with reusable component classes

## URLs

- `/users/signup/` - Sign up page
- `/users/login/` - Login page
- `/users/logout/` - Logout
- `/users/profile/` - User profile (requires login)
- `/users/google/login/` - Initiate Google OAuth
- `/admin/` - Django admin panel

## User Model Fields

- `email` - User email (used as username)
- `first_name` - User's first name
- `last_name` - User's last name
- `avatar` - Profile picture (uploaded to media/avatars/)
- `progress` - JSON field to store learning progress
- `google_id` - Google account ID for OAuth users

## Reusable CSS Classes

Defined in `users/static/css/style.css`:
- `.input-field` - Styled input fields
- `.btn-primary` - Primary button style
- `.btn-secondary` - Secondary button style
- `.card` - Card container style

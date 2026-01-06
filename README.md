---
description: Full-featured Django blogging platform with Markdown support and user authentication
details: >
  A complete content management system built with Django featuring rich Markdown
  editing via django-markdownx, full user authentication system with signup and
  login, and comprehensive CRUD operations for blog posts. Users can create
  formatted posts with bold text, italics, headings, and code blocks, manage
  their content through an intuitive interface, and engage with an integrated
  comment system. The platform includes Django's built-in admin panel for content
  moderation, custom CSS styling for a clean modern UI, and responsive design
  that works across all devices. Features post listing with author attribution,
  detailed post views, secure user management, and comment threading. Built with
  Django forms for data validation, SQLite database for development, and supports
  easy deployment to Railway, Render, or other cloud platforms. Optional GitHub
  Actions integration for CI/CD workflows.
technologies:
  - django
  - markdown
  - sqlite
hostedUrl: 
---



# Django Markdown Blog

A simple yet powerful **blogging platform** built with **Django**, featuring **Markdown support**, **user authentication**, and **comments**. 

##  Features

**User Authentication** (Signup, Login, Logout)
**Create, Read, Update, Delete (CRUD) Blog Posts**
**Markdown Support** for Rich Formatting
**Comment System** for Posts
**Responsive UI** with CSS (no Tailwind needed!)
**GitHub Actions CI/CD (Optional)**

---

## Installation & Setup

### 1. Clone the Repository
```sh
git clone https://github.com/Micmada/django_markdown_blog.git
cd django_markdown_blog
```

### 2. Set Up a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Run Database Migrations
```sh
python manage.py migrate
```

### 5. Create a Superuser (for Admin Access)
```sh
python manage.py createsuperuser
```

### 6. Start the Development Server
```sh
python manage.py runserver
```
Visit **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)** in your browser. 🎉

---

##  Features & Implementation Details

### **User Authentication**
- Implemented using Django's built-in **`django.contrib.auth`**.
- Templates: `templates/account/login.html`, `signup.html`, `logout.html`.
- Users can log in, sign up, and log out.

### **Blog Post Management**
- Model: `Post` in `models.py` (supports `title`, `content`, `author`, `created_at`).
- Uses **Django Forms** for post creation/editing.
- Templates: `post_list.html`, `post_detail.html`, `post_form.html`, `post_confirm_delete.html`.

### **Markdown Support**
- Uses `django-markdownx` to render Markdown content.
- Posts can include **bold, italic, headings, code blocks**, etc.
- Example: Writing `**bold text**` in the editor renders as **bold text**.

### **Comments System**
- Model: `Comment` (linked to `Post` and `User`).
- Users can leave comments under blog posts.

### **Styling & UI**
- Custom **CSS styles** (located in `static/css/style.css`).
- Clean and modern layout in `base.html`.

---

##  Deployment (Optional)
You can deploy this project on:
- **Railway.app**
- **Render.com**
- **DigitalOcean / AWS / Heroku**


---

##  Contributing
Pull requests are welcome! Feel free to **fork the repo**, make your changes, and submit a **PR**.

1. Fork the project
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m "Added a cool feature"`)
4. Push to your branch (`git push origin feature-branch`)
5. Open a Pull Request 




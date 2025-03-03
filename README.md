# Django Markdown Blog

A simple yet powerful **blogging platform** built with **Django**, featuring **Markdown support**, **user authentication**, and **comments**. 

##  Features

✅ **User Authentication** (Signup, Login, Logout)
✅ **Create, Read, Update, Delete (CRUD) Blog Posts**
✅ **Markdown Support** for Rich Formatting
✅ **Comment System** for Posts
✅ **Responsive UI** with CSS (no Tailwind needed!)
✅ **GitHub Actions CI/CD (Optional)**

---

## Installation & Setup

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/Micmada/django_markdown_blog.git
cd django_markdown_blog
```

### 2️⃣ Set Up a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Run Database Migrations
```sh
python manage.py migrate
```

### 5️⃣ Create a Superuser (for Admin Access)
```sh
python manage.py createsuperuser
```

### 6️⃣ Start the Development Server
```sh
python manage.py runserver
```
Visit **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)** in your browser. 🎉

---

##  Features & Implementation Details

### **1️⃣ User Authentication**
- Implemented using Django's built-in **`django.contrib.auth`**.
- Templates: `templates/account/login.html`, `signup.html`, `logout.html`.
- Users can log in, sign up, and log out.

### **2️⃣ Blog Post Management**
- Model: `Post` in `models.py` (supports `title`, `content`, `author`, `created_at`).
- Uses **Django Forms** for post creation/editing.
- Templates: `post_list.html`, `post_detail.html`, `post_form.html`, `post_confirm_delete.html`.

### **3️⃣ Markdown Support**
- Uses `django-markdownx` to render Markdown content.
- Posts can include **bold, italic, headings, code blocks**, etc.
- Example: Writing `**bold text**` in the editor renders as **bold text**.

### **4️⃣ Comments System**
- Model: `Comment` (linked to `Post` and `User`).
- Users can leave comments under blog posts.

### **5️⃣ Styling & UI**
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




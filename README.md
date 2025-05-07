# 📞 Call Centre Website

A professional and responsive call centre website built with **Django (Backend)** and **Bootstrap (Frontend)**.  
Designed to handle client services, contact messages, job applications (with CV/video upload), and admin-managed blog/services.

---

## 🔧 Features

✅ Home page with intro  
✅ About Us page  
✅ Services page – dynamic & admin-managed  
✅ Contact Us page – saves messages to database  
✅ Job Application form – CV & video uploads  
✅ Blog page – admin can post news/articles  
✅ Admin dashboard – manage everything  
✅ Responsive design with smooth animations  
✅ Deployed and tested on **GitHub Codespaces**

---

## 💻 Tech Stack

- **Backend**: Python 3, Django 4+
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Storage**: SQLite (default Django DB)
- **Hosting/Development**: GitHub Codespaces

---

## 🗂️ Project Structure

```plaintext
call-centre-site/
├── backend/              # Django project folder
│   ├── settings.py       # Django config
│   ├── urls.py           # URL routes
├── core/                 # Main app: views, models, admin
│   ├── models.py         # Models (Contact, Job, Blog, Services)
│   ├── forms.py          # Forms for contact & job application
│   ├── views.py          # All page logic
├── templates/            # HTML templates
│   ├── base.html         # Bootstrap layout
│   ├── home.html, contact.html, blog.html, etc.
├── media/                # Uploaded files (CVs, videos)
├── static/               # (optional) For custom CSS/JS if needed
├── manage.py
└── requirements.txt



---

## 🚀 How to Run (GitHub Codespaces)

1. 🟢 Open in GitHub Codespaces
2. 📦 Install packages & start server:

```bash
python3 -m venv venv
source venv/bin/activate
pip install django
python manage.py migrate
python manage.py runserver

3. 🔐 Create superuser for admin:
python manage.py createsuperuser

🔐 Admin Dashboard
Login at /admin/

Manage:

Contact messages

Job applications

Blog posts

Services

📤 Job Portal
Go to /apply/

Upload your CV and Video

Admin can view it from dashboard

📬 Contact System
Go to /contact/

Submit message → saved to DB

Admin can view/manage them easily

✍️ Author
🔸 Developer: Shahed Ahmed

📍 Built using only Codespaces without software installation

📄 License

---

Let me know if you’d like me to **add badges**, **deployment guides**, or **screenshots** next — or we can now prep this for client demo or freelancing portfolio ✅

from app import app

app.config.update(dict(
    SECRET_KEY="New Secret Key",
    WTF_CSRF_SECRET_KEY="New CSRF Key"
))
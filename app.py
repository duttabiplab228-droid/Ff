import os
from flask import Flask, render_template_string, request, flash, redirect, url_for

app = Flask(__name__)
# ফ্ল্যাশ মেসেজ দেখানোর জন্য সিক্রেট কি (এটি পরিবর্তন করতে পারেন)
app.secret_key = 'super_secret_key_for_organization'

# HTML এবং CSS ডিজাইন (একই স্ট্রাকচারে)
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="bn">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>আমাদের অর্গানাইজেশন</title>
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f4f6f9;
            color: #333;
            display: flex;
            flex-direction: column;
            min-height: 100vh;
        }
        header {
            background-color: #1a365d;
            color: white;
            padding: 1rem 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        header .logo {
            font-size: 1.5rem;
            font-weight: bold;
        }
        nav a {
            color: white;
            text-decoration: none;
            margin-left: 1.5rem;
            font-weight: 600;
            transition: color 0.3s;
        }
        nav a:hover {
            color: #38bdf8;
        }
        main {
            flex: 1;
            padding: 2rem 1rem;
            max-width: 800px;
            margin: 0 auto;
            width: 100%;
        }
        .card {
            background: white;
            padding: 2rem;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        }
        h1, h2 {
            margin-bottom: 1rem;
            color: #1a365d;
        }
        p {
            line-height: 1.6;
            color: #4a5568;
        }
        form {
            display: flex;
            flex-direction: column;
            gap: 12px;
            margin-top: 1rem;
        }
        label {
            font-weight: bold;
            color: #2d3748;
        }
        input, textarea {
            width: 100%;
            padding: 10px;
            border: 1px solid #cbd5e0;
            border-radius: 5px;
            font-size: 14px;
        }
        input:focus, textarea:focus {
            outline: none;
            border-color: #3182ce;
        }
        button {
            padding: 12px;
            background-color: #1a365d;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
            font-weight: bold;
            transition: background 0.3s;
        }
        button:hover {
            background-color: #2b6cb0;
        }
        .alert {
            background-color: #d1e7dd;
            color: #0f5132;
            padding: 1rem;
            border-radius: 5px;
            margin-bottom: 1rem;
            border: 1px solid #badbcc;
        }
        footer {
            background-color: #1a365d;
            color: white;
            text-align: center;
            padding: 1rem;
            margin-top: auto;
        }
    </style>
</head>
<body>
    <header>
        <div class="logo">OrgLogo</div>
        <nav>
            <a href="{{ url_for('home') }}">হোম</a>
            <a href="{{ url_for('contact') }}">যোগাযোগ</a>
        </nav>
    </header>

    <main>
        {% with messages = get_flashed_messages() %}
          {% if messages %}
            {% for message in messages %}
              <div class="alert">{{ message }}</div>
            {% endfor %}
          {% endif %}
        {% endwith %}

        {% if page_name == 'home' %}
        <div class="card">
            <h1>আমাদের অর্গানাইজেশনে স্বাগতম</h1>
            <p>আমরা সমাজে ইতিবাচক পরিবর্তন আনতে এবং সেরা সেবা প্রদান করতে কাজ করছি। এটি আমাদের ওয়েবসাইটের মূল পাতা।</p>
        </div>
        
        {% elif page_name == 'contact' %}
        <div class="card">
            <h2>যোগাযোগ করুন</h2>
            <form method="POST" action="{{ url_for('contact') }}">
                <div>
                    <label>আপনার নাম:</label>
                    <input type="text" name="name" placeholder="আপনার নাম লিখুন" required>
                </div>
                <div>
                    <label>ইমেইল ঠিকানা:</label>
                    <input type="email" name="email" placeholder="example@email.com" required>
                </div>
                <div>
                    <label>আপনার বার্তা:</label>
                    <textarea name="message" rows="4" placeholder="আপনার বার্তাটি লিখুন..." required></textarea>
                </div>
                <button type="submit">পাঠিয়ে দিন</button>
            </form>
        </div>
        {% endif %}
    </main>

    <footer>
        <p>&copy; 2026 আমাদের অর্গানাইজেশন। সর্বস্বত্ব সংরক্ষিত।</p>
    </footer>
</body>
</html>
"""

# হোম পেজ
@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, page_name='home')

# কন্টাক্ট পেজ
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        user_name = request.form.get('name')
        flash(f'ধন্যবাদ {user_name}, আপনার বার্তাটি সফলভাবে পাঠানো হয়েছে!')
        return redirect(url_for('contact'))
        
    return render_template_string(HTML_TEMPLATE, page_name='contact')

# Render-এর জন্য হোস্ট ও পোর্ট সেটআপ
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

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
    <title>Radha Sudarshan Temple</title>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;1,500&family=Poppins:wght@300;400&display=swap" rel="stylesheet">
    
    <style>
        /* General Reset */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Poppins', sans-serif;
            background-color: #FDFBF7; /* Soft aesthetic background */
            color: #4A4A4A;
        }

        h1, h2, h3 {
            font-family: 'Playfair Display', serif;
            color: #8B4513; /* Warm earthy tone */
        }

        /* Navbar */
        header {
            background-color: #FFF;
            padding: 20px 50px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 2px 10px rgba(0,0,0,0.05);
            position: sticky;
            top: 0;
            z-index: 100;
        }

        header .logo {
            font-size: 24px;
            font-weight: bold;
            color: #D35400; /* Saffron touch */
        }

        nav ul {
            list-style: none;
            display: flex;
            gap: 20px;
        }

        nav ul li a {
            text-decoration: none;
            color: #4A4A4A;
            font-weight: 400;
            transition: color 0.3s;
        }

        nav ul li a:hover {
            color: #D35400;
        }

        /* Hero Section */
        .hero {
            height: 80vh;
            background: linear-gradient(rgba(253, 251, 247, 0.7), rgba(253, 251, 247, 0.7)), url('https://plain-apac-prod-public.komododecks.com/202608/11/TEtnv6zTYjt49OMx35By/image.jpg') center/cover;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            padding: 20px;
        }

        .hero h1 {
            font-size: 4rem;
            margin-bottom: 10px;
            color: #2C3E50;
        }

        .hero p {
            font-size: 1.2rem;
            max-width: 600px;
            color: #555;
            margin-bottom: 20px;
        }

        .btn {
            padding: 10px 25px;
            background-color: #D35400;
            color: white;
            text-decoration: none;
            border-radius: 30px;
            font-weight: 400;
            transition: background 0.3s;
        }

        .btn:hover {
            background-color: #A04000;
        }

        /* Section Styling */
        section {
            padding: 60px 20px;
            text-align: center;
        }

        section h2 {
            font-size: 2.5rem;
            margin-bottom: 20px;
        }

        section p {
            max-width: 800px;
            margin: 0 auto;
            line-height: 1.8;
            font-size: 1.1rem;
        }

        /* Footer */
        footer {
            background-color: #2C3E50;
            color: white;
            text-align: center;
            padding: 30px 20px;
            margin-top: 40px;
        }

        footer p {
            font-size: 0.9rem;
            opacity: 0.8;
        }
    </style>
</head>
<body>

    <header>
        <div class="logo">Radha Sudarshan</div>
        <nav>
            <ul>
                <li><a href="#home">Home</a></li>
                <li><a href="#about">About</a></li>
                <li><a href="#darshan">Darshan Timings</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <section id="home" class="hero">
        <h1>Radha Sudarshan Temple</h1>
        <p>Experience peace, devotion, and divine love at our sacred organization.</p>
        <a href="#about" class="btn">Explore More</a>
    </section>

    <section id="about">
        <h2>About Our Organization</h2>
        <p>The Radha Sudarshan Temple is a spiritual community dedicated to devotion, peace, and cultural heritage. We organize daily kirtans, charity drives, and spiritual discourses to uplift the soul and serve humanity. Join our aesthetic and peaceful environment to connect with the divine.</p>
    </section>

    <section id="darshan" style="background-color: #F4ECE6;">
        <h2>Darshan & Aarti Timings</h2>
        <p><strong>Morning Aarti:</strong> 6:00 AM - 7:00 AM</p>
        <p><strong>Darshan:</strong> 7:00 AM - 12:00 PM</p>
        <p><strong>Evening Aarti:</strong> 6:30 PM - 7:30 PM</p>
        <p><strong>Bhajan Sandhya:</strong> Every Sunday at 5:00 PM</p>
    </section>

    <section id="contact">
        <h2>Contact Us</h2>
        <p>Visit us to experience the divine presence.</p>
        <p><br>📍 Location: [Your Temple Address Here]</p>
        <p>📞 Phone: +91 XXXXX XXXXX</p>
        <p>✉️ Email: info@radhasudarshan.org</p>
    </section>

    <footer>
        <p>&copy; 2026 Radha Sudarshan Temple Organization. All Rights Reserved.</p>
        <p>May Lord Krishna and Radha Rani bless you.</p>
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

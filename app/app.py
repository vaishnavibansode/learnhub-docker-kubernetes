from flask import Flask, jsonify

app = Flask(__name__)

COURSES = [
    {"id": 1, "name": "Python Programming", "category": "Programming"},
    {"id": 2, "name": "Data Analytics", "category": "Data Science"},
    {"id": 3, "name": "Machine Learning", "category": "Artificial Intelligence"},
]

@app.route("/")
def home():
    course_cards = ""

    for course in COURSES:
        course_cards += f"""
        <div class="course">
            <h2>{course['name']}</h2>
            <p>{course['category']}</p>
        </div>
        """

    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>LearnHub Online Learning</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 0;
                background: #f2f5fa;
                color: #1d3557;
            }}
            header {{
                background: #1d3557;
                color: white;
                padding: 25px;
                text-align: center;
            }}
            main {{
                max-width: 900px;
                margin: 35px auto;
                padding: 20px;
            }}
            .courses {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 18px;
            }}
            .course {{
                background: white;
                padding: 22px;
                border-radius: 10px;
                box-shadow: 0 3px 12px #00000012;
            }}
        </style>
    </head>
    <body>
        <header>
            <h1>LearnHub</h1>
            <p>Your online learning platform</p>
        </header>
        <main>
            <h2>Explore Our Courses</h2>
            <div class="courses">{course_cards}</div>
            <p>Application status: Running</p>
        </main>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify(
        application="LearnHub Online Learning Platform",
        status="healthy"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

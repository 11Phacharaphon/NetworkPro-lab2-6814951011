from datetime import datetime
from flask import Flask, request, render_template_string

app = Flask(__name__)
LOG_FILE = "log.txt"

# หน้าเว็บฟอร์ม
form_html = """
<!doctype html>
<html lang="th">
<head>
  <meta charset="utf-8">
  <title>Submit Message</title>
  <style>
    body { font-family: sans-serif; max-width: 640px; margin: 40px auto; padding: 0 16px; }
    textarea { width: 100%; height: 100px; font-size: 16px; }
    input[type=submit] { margin-top: 8px; padding: 8px 20px; font-size: 16px; }
    .box { background: #eef6ff; border-left: 4px solid #2287e6; padding: 12px 16px; margin: 16px 0; }
  </style>
</head>
<body>
  <h1>Submit your message</h1>
  {% if message %}
  <div class="box">
    <h2>Message received:</h2>
    <p>{{ message }}</p>
    <small>Saved to log.txt at {{ time }}</small>
  </div>
  {% endif %}
  <form method="post">
    <textarea name="message" placeholder="Type your message..." required></textarea><br>
    <input type="submit" value="Submit">
  </form>
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        message = request.form.get("message", "").strip()
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if message:
            # บันทึกลงไฟล์แบบ append mode
            with open(LOG_FILE, "a", encoding="utf-8") as f:
                f.write(f"[{time}] {message}\n")
            print(f"Logged message: {message}", flush=True)
        return render_template_string(form_html, message=message, time=time)
    return render_template_string(form_html, message=None)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

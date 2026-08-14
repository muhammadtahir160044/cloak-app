from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return "Cloaking Demo Running. Go to /go"

@app.route('/go')
def cloak():
    ua = request.headers.get('User-Agent', '').lower()

    # Broad bot detection for social media previews
    bot_keywords = [
        'bot', 'twitter', 'facebook', 'telegram', 
        'whatsapp', 'discord', 'crawler', 'spider', 
        'meta', 'preview', 'curl', 'wget'
    ]

    is_bot = any(keyword in ua for keyword in bot_keywords)

    if is_bot:
        return render_template_string('''<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:site" content="@imgur">
    <meta name="twitter:domain" content="imgur.com">
    <meta name="twitter:title" content="unexpected bestie meetups">
    <meta name="twitter:description" content="A thread">
    <meta name="twitter:image" content="https://i.imgur.com/aV7Xqxf.png">

    <meta property="og:type" content="website">
    <meta property="og:site_name" content="Imgur">
    <meta property="og:title" content="unexpected bestie meetups">
    <meta property="og:description" content="A thread">
    <meta property="og:image" content="https://i.imgur.com/aV7Xqxf.png">
    <meta property="og:url" content="https://imgur.com/a/mpQaAnF">

    <title>unexpected bestie meetups</title>
</head>
<body>
    <h1>Preview</h1>
</body>
</html>''')
    else:
        return redirect("https://omg10.com/4/8480685", code=302)

if __name__ == '__main__':
    app.run()

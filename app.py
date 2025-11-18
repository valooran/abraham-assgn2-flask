from flask import Flask, render_template_string
import socket
import os

app = Flask(__name__)

@app.route('/')
def hello():
    hostname = socket.gethostname()
    container_id = os.environ.get('HOSTNAME', 'unknown')
    
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Abraham's app</title>
    </head>
    <body>
        <div>
            <h1>Abraham's GCP Flask Application</h1>
            <p>Welcome to the Flask backend running on Google Cloud!</p>        
        </div>
    </body>
    </html>
    """
    return render_template_string(html)

@app.route('/health')
def health():
    return {'status': 'healthy'}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)

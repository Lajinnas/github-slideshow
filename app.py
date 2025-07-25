from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def log_ip():
    ip = request.headers.get('X-Forwarded-For', request.remote_addr).split(',')[0]
    print(f"Visitor IP: {ip}")
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(debug=True)
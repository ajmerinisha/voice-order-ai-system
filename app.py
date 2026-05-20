from flask import Flask, render_template

from routes.voice_routes import voice_bp
from routes.order_routes import order_bp
from routes.history_routes import history_bp

app = Flask(__name__)

# Register Routes
app.register_blueprint(voice_bp)
app.register_blueprint(order_bp)
app.register_blueprint(history_bp)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
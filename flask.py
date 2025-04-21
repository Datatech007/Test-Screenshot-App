from flask import Flask, send_file
from screenshot_automation import capture_screenshot  # Assuming this is your screenshot function

app = Flask(__name__)

@app.route('/screenshot', methods=['GET'])
def screenshot():
    # Run the screenshot automation
    screenshot_path = capture_screenshot()  # Assuming this returns the file path
    
    # Return the screenshot to the client
    return send_file(screenshot_path, mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Make sure it's accessible externally

from flask import Flask, send_file
from screenshot_automation import capture_screenshot  # Assuming this function runs the screenshot automation

app = Flask(__name__)

@app.route('/screenshot', methods=['GET'])
def screenshot():
    # Run your screenshot automation logic here
    screenshot_path = capture_screenshot()  # This function returns the path of the generated screenshot
    
    # Send the screenshot back to the client
    return send_file(screenshot_path, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)

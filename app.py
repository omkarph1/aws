from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def congratulations():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Congratulations!</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f0f8ff;
                color: #333;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .container {
                text-align: center;
                background-color: #ffffff;
                padding: 50px;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            }
            h1 {
                font-size: 3em;
                color: #4caf50;
                margin-bottom: 20px;
            }
            p {
                font-size: 1.2em;
                margin-bottom: 40px;
            }
            .button {
                padding: 10px 20px;
                font-size: 1.2em;
                color: white;
                background-color: #4caf50;
                border: none;
                border-radius: 5px;
                text-decoration: none;
                transition: background-color 0.3s;
            }
            .button:hover {
                background-color: #45a049;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Congratulations!</h1>
            <p>You have successfully created your Elastic Beanstalk environment and set up a CodePipeline!</p>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(debug=True)

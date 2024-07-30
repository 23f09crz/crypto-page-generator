from jinja2 import Template
import os 

coin_name = input('Write the name of the cryptocurrency: ')
coin_CA = input('Write the CA of the cryptocurrency: ')
telegram_link = input('Paste the telegram link of the cryptocurrency: ')
background_color = input('Enter the background color (e.g., #f4f4f4 or lightblue): ')

# HTML template
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ coin_name }} on Solana</title>
    <style>
        body, html {
            margin: 0;
            padding: 0;
            height: 100%;
            font-family: Arial, sans-serif;
            background-color: {{ background_color }};
            color: white;
            display: flex;
            justify-content: center;
            align-items: center;
            overflow: hidden;
        }
        .background-text {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            overflow: hidden;
            z-index: -1;
        }
        .background-text::before {
            content: "{{ coin_name_repeat }}";
            position: absolute;
            top: 50%;
            left: 50%;
            font-size: 24px;
            line-height: 1.5em;
            letter-spacing: 5px;
            color: rgba(255, 255, 255, 0.1);
            white-space: nowrap;
        }
        .container {
            text-align: center;
            background-color: rgba(0, 0, 0, 0.6);
            padding: 40px;
            border-radius: 10px;
            z-index: 1;
        }
        h1 {
            margin-bottom: 20px;
        }
        .ca {
            font-size: 0.8em;
            word-break: break-all;
            margin-bottom: 20px;
        }
        .links {
            display: flex;
            justify-content: center;
            gap: 20px;
        }
        .links a {
            color: white;
            text-decoration: none;
            padding: 10px 20px;
            border-radius: 5px;
            background-color: #4CAF50;
            transition: background-color 0.3s;
        }
        .links a:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <div class="background-text"></div>
    <div class="container">
        <h1>{{ coin_name }} on Solana</h1>
        <div class="ca">CA: {{ coin_CA }}</div>
        <div class="links">
            <a href="https://pump.fun/{{ coin_CA }}" target="_blank">Pump.fun</a>
            <a href="{{ coin_telegram_link }}" target="_blank">Telegram</a>
        </div>
    </div>
</body>
</html>
"""

def create_html_page(coin_name, coin_CA, coin_telegram_link, background_color, output_file):
    # Create a Jinja2 template object
    template = Template(html_template)
    
    # Render the template with the provided variables
    rendered_html = template.render(
        coin_name=coin_name,
        coin_CA=coin_CA,
        coin_pump_link=f"pump.fun/{coin_CA}",
        coin_name_repeat=" ",
        coin_telegram_link=coin_telegram_link,
        background_color=background_color
    )
    
    # Write the rendered HTML to a file
    try:
        with open(f"./templates/{output_file}", 'w') as f:
            f.write(rendered_html)
        print(f"HTML page created: ./templates/{output_file}")
    
    except FileNotFoundError:
        os.makedirs('./templates/')
        with open(f"./templates/{output_file}", 'w') as f:
            f.write(rendered_html)
        print(f"HTML page created: ./templates/{output_file}")


# Example usage
create_html_page(coin_name, coin_CA, telegram_link, background_color, f'{coin_name}.html')
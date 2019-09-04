import webbrowser

def main():
    f = open("web.html","w")
    f.write(
        """
        <!DOCTYPE html>
        <html lang="de">
        <head>
        <meta charset="UTF-8">
        <title>Website</title>
        <meta name="description" content="content">
        </head>
        <body>
        <h1><u>Generated Website</u></h1>
        <h2><i>With Python</i></h2>
        <p></p>
        <p></p>    
        </body>
        </html>
        """)
    f.close
    webbrowser.open("web.html")
main()

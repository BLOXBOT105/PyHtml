def load(title, body, css, js):
    before = [
        "<!DOCTYPE html>",
        '<html lang="en">',
        "<head>",
        '   <meta charset="UTF-8">',
        "   <title>"+str(title)+"</title>",
        '   <style type="text/css">',
    ]

    after_css = [
        '   </style>',
        '   <script type="text/javascript">'
    ]

    after_js = [
        '   </script>',
        "</head>",
        "<body>"
    ]

    after = [
        "</body>",
        "</html>"
    ]

    f=open("page.html","w")

    for i in before:
        f.write(i+"\n")

    for i in css:
        f.write("       "+i+"\n")

    for i in after_css:
        f.write("   "+i+"\n")

    for i in js:
        f.write("       "+i+"\n")

    for i in after_js:
        f.write("   "+i+"\n")

    for i in body:
        f.write("   "+i+"\n")

    for i in after:
        f.write(i+"\n")

    f.close()

def main():
    load(
        title = "Hello, World!",

        css = [
            "/* css */"
        ],

        js = [
            "/* js */"
        ],

        body = [
            "<p>Hello,</p>",
            "<p>World!</p>"
        ]
    )

if __name__ == "__main__":
    from pyhtml import *
    main()

import resend
from flask import current_app


def send_invitation_email(name, email):

    api_key = current_app.config["RESEND_API_KEY"]
    mail_from = current_app.config["MAIL_FROM"]

    if not api_key:
        raise ValueError("RESEND_API_KEY is not configured")

    resend.api_key = api_key

    params = {
        "from": mail_from,
        "to": [email],
        "subject": "You're invited — Samira's 21st Birthday",
        "html": f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>Samira's 21st Birthday</title>
        </head>

        <body style="
            margin: 0;
            padding: 0;
            background-color: #0a0a0a;
            color: #ffffff;
            font-family: Arial, sans-serif;
        ">

            <div style="
                max-width: 600px;
                margin: 40px auto;
                padding: 50px 30px;
                text-align: center;
                background-color: #111111;
            ">

                <p style="
                    font-size: 11px;
                    letter-spacing: 4px;
                    color: #999999;
                ">
                    YOU'RE INVITED
                </p>

                <h1 style="
                    font-family: Georgia, serif;
                    font-size: 48px;
                    font-weight: normal;
                    margin: 30px 0;
                ">
                    Samira's<br>
                    <i>21st Birthday</i>
                </h1>

                <p style="
                    color: #cccccc;
                    font-size: 16px;
                    line-height: 1.7;
                ">
                    Hi {name},
                </p>

                <p style="
                    color: #aaaaaa;
                    font-size: 15px;
                    line-height: 1.8;
                ">
                    You have been personally invited to
                    celebrate Samira's 21st birthday.
                </p>

                <a
                    href="http://127.0.0.1:5000/invitation"
                    style="
                        display: inline-block;
                        margin-top: 25px;
                        padding: 16px 28px;
                        background-color: #ffffff;
                        color: #000000;
                        text-decoration: none;
                        font-size: 12px;
                        letter-spacing: 1px;
                    "
                >
                    VIEW MY INVITATION →
                </a>

                <p style="
                    margin-top: 50px;
                    color: #666666;
                    font-size: 11px;
                ">
                    Samira's 21st Birthday
                </p>

            </div>

        </body>
        </html>
        """
    }

    return resend.Emails.send(params)
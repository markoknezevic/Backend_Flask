import os

from flask_app import create_app
from config.development import Development as Config

# if os.environ["FLASK_ENV_TYPE"] == "Development":
#    from config.development import Development as Config
# elif os.environ["FLASK_ENV_TYPE"] == "Production":
#    from config.production import Production as Config
# else:
#    raise Exception("Not proper Flask_ENV_TYPE set")

app = create_app(Config)


@app.route("/")
def hello():
    return "Hello world"


app.run(port=5000, debug=True)

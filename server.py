from flask import Flask
import secrets

app = Flask(import_name="higher_lower")
def get_random_num():
    rand_num = secrets.SystemRandom().randint(0, 9)

    return rand_num
@app.route('/')
def open_home():
    home_html = ("<h1>Guess a number between 0 and 9</h1>"
                 "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>")

    return home_html

def guess_decorator(check_function):
    answer = get_random_num()
    def wrapper(*args, **kwargs):
        html = check_function(kwargs, answer)

        return html
    return wrapper


@app.route('/<int:guess>')
@guess_decorator
def taking_guess(guess_param, answer):
    guess = guess_param['guess']
    if guess == answer:
        html = ('<h1 style="color: green">You Found Me!</h1>'
                '<iframe src="https://giphy.com/embed/yy6hXyy2DsM5W" '
                'width="272" height="480" frameBorder="0" '
                'class="giphy-embed" allowFullScreen></iframe><p><a '
                'href="https://giphy.com/gifs/dogs-yy6hXyy2DsM5W">via GIPHY</a></p>')

    elif guess < answer:
        html = ('<h1 style="color: red">Too Low!</h1>'
                '<div style="width:480px"><iframe allow="fullscreen"'
                ' frameBorder="0" height="330" '
                'src="https://giphy.com/embed/a8bRW8lTY37uVoqdSE/video" width="480"></iframe></div>')

    elif guess > answer:
        html = ('<h1 style="color: red">Too High!</h1>'
                '<iframe src="https://giphy.com/embed/0nVkZasX89up3aZfwA" '
                'width="270" height="480" frameBorder="0" class="giphy-embed"'
                ' allowFullScreen></iframe><p>'
                '<a href="https://giphy.com/gifs/Nesstoy-sky-bird-watching-butterfly-0nVkZasX89up3aZfwA">via GIPHY</a></p>')

    return html



if __name__ == "__main__":
    app.run(debug=True)

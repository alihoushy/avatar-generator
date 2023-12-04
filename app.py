from flask import Flask, render_template
import python_avatars as pa

app = Flask(__name__)

# Define the route to generate and display a random avatar
@app.route('/random_avatar')
def random_avatar():

    avatar_1 = pa.Avatar.random()
    avatar_1.render(f"static/avatar_1.svg")

    avatar_2 = pa.Avatar.random()
    avatar_2.render(f"static/avatar_2.svg")

    avatar_3 = pa.Avatar.random()
    avatar_3.render(f"static/avatar_3.svg")

    avatar_4 = pa.Avatar.random()
    avatar_4.render(f"static/avatar_4.svg")

    avatar_5 = pa.Avatar.random()
    avatar_5.render(f"static/avatar_5.svg")

    # Display the generated avatar link to the user
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

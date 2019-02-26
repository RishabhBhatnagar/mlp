from flask import *
app = Flask(__name__)

@app.route('/')
def home():
	data = []
	with open("home.html") as f:
		for line in f:
			data.append(line)
	return ' '.join(data)

if __name__ == '__main__':
    app.run(debug=1)

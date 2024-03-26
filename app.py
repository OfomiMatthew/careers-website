from flask import Flask, render_template

app = Flask(__name__)
jobs = [{
    'id': 1,
    'title': 'Data analyst',
    'location': "Abuja",
    'salary': 'Naira 200,000'
},
				{
						'id': 2,
						'title': 'Data engineer',
						'location': "Lagos",
						# 'salary': 'Naira 300,000'
				},

				{
						'id': 3,
						'title': 'Software developer',
						'location': "Ibadan",
						'salary': 'Naira 200,000'
				},
				{
						'id': 4,
						'title': 'Cloud engineer',
						'location': "PH City",
						'salary': 'Naira 250,000'
				},
			 
			 ]


@app.route('/')
def hello_world():
	return render_template('home.html',jobs=jobs,company="Matt-Dev")


if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True)

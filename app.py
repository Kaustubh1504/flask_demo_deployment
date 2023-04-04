# code using with request argument.
from flask import Flask, request
import cv2
import tesseract
app = Flask(__name__)

@app.route('/query_example')
# Code
def query_example():
	language = request.args.get('language')
	framework = request.args['framework']
	website = request.args.get('website')
	return '''<h1> The Language is : {} </h1>
			<h1> The framework is : {} </h1>
			<h1> The website is : {} </h1>'''.format(language,
														framework,
														website)


if __name__ == '__main__':
	app.run(debug=True, port=5000)

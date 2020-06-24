from cgi import parse_qs
from template1 import html 

def application(environ, start_response):
	d = parse_qs(environ['QUERY_STRING'])
	a = d.get('a', [''])[0]
	b = d.get('b', [''])[0]
	result1 = '' 
	result2 = '' 
	try:
		a, b = int(a), int(b)
		result1 = a + b
		result2 = a * b

	except ValueError:
		result1 = "Please input integer."
		result2 = "Please input integer."

	response_body = html % {
		'result1' : result1,
		'result2' : result2,
	}
	start_response('200 OK', [
		('Content-Type', 'text/html'),
		('Content-Length', str(len(response_body)))
	])
	return [response_body]


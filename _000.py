# fauziwei@yahoo.com

from tornado import ioloop
from tornado import web

class Index(web.RequestHandler):
	def get(self):
		self.write(
			'''
			<html><body>
				<form method="post">
					whats your favourite book?<br/>
					<input type="text" name="title"/>
					<input type="submit" value="submit">
				</form>
			</body></html>
			''')
	def post(self):
		book = self.get_argument('title')
		self.write(
			'''
			<html><body>
				My favourite book is %s
			</body></html>
			''' % book)

class Application(web.Application):
	def __init__(self):
		apis = [
			(r'/', Index)
		]
		settings = dict( debug=True )
		web.Application.__init__(self, apis, **settings)

app = Application()
app.listen(8080, 'localhost')
ioloop.IOLoop.instance().start()

# fauziwei@yahoo.com

import asyncio

host, port = '127.0.0.1', 1515
print ( 'Host: {} , Port: {}'.format(host, port) )
loop = asyncio.get_event_loop()

@asyncio.coroutine
def simple():
# async def simple():
	yield from asyncio.start_server(handler, host, port)
# 	await asyncio.start_server(handler, host, port)

@asyncio.coroutine
def handler(clreader, clwriter):
# async handler(clreader, clwriter):
	while True:
		buffer = 128
		s = yield from clreader.read(buffer)
		# s = await clreader.read(buffer)
		if not s: break
		s = s.decode('utf-8')
		print ( 'Recv: {}'.format(s) )
		m = 'Hello Im server'
		print ( 'Send: {}'.format(m) )
		clwriter.write( m.encode('utf-8') )

loop.run_until_complete(simple())
try: loop.run_forever()
finally: loop.close()
def start_fetch():
    client = AsyncHTTPClient()
    client.fetch('http://example.com', callback=on_fetch)

def on_fetch(response):
    print response

PeriodicCallback(start_fetch, callback_time=1).start()
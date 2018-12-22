import mitmproxy.http
from mitmproxy import ctx


class Filter:
    def response(self, flow: mitmproxy.http.HTTPFlow):
        if '/3.3.5/index.js' in flow.request.url:
            flow.response.text = flow.response.text.replace('$cdc_asdjflasutopfhvcZLmcfl_', 'kddkalse')
            flow.response.text = flow.response.text.replace('navigator.webdriver', 'false')
            flow.response.text = flow.response.text.replace('ChromeDriver', '')


addons = [
    Filter()
]

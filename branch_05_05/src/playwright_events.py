from playwright.sync_api import sync_playwright, Request, Response


# Логирование запросов
def log_request(request: Request):
    print('Request: %s' % request)


# Логирование ответов
def log_response(response: Response):
    print('Request: %s' % response)


def log_specific_requests(request):
    if "googleapis.com" in request.url:
        print(f"Filtered request: {request.url}")


def log_response_body(response):
    if response.ok:
        print(f"Response body: {response.body()}")  # Тело ответа


def test_ui():
    with sync_playwright() as pw:
        url_login = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login'
        browser = pw.chromium.launch(headless=True)
        page = browser.new_page()

        page.on('request', log_request)
        page.on('response', log_response)

        page.goto(url_login)

        page.wait_for_timeout(5000)


if __name__ == '__main__':
    test_ui()
    print("OK")
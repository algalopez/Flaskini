from app.model import hello


def run(request):
    return hello.Hello(name=request)

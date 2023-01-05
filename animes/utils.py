def formatUrl(url: str):
    return url.replace("\ ".strip(),'')

def formatQueryParams(url: str):
    return url.replace("/", '')
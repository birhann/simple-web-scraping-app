def validateLink(link):
    formats = ["https://www.etsy.com",
               "http://www.etsy.com",
               "https://etsy.com",
               "http://etsy.com",
               "www.etsy.com",
               "etsy.com"
               ]
    for i in formats:
        if link.startswith(i):
            return True
    return False

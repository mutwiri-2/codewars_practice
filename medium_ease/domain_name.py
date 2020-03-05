# Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

# domain_name("http://github.com/carbonfive/raygun") == "github" 
# domain_name("http://www.zombie-bites.com") == "zombie-bites"
# domain_name("https://www.cnet.com") == "cnet"

def domain_name(url):
    idx1 = url.rfind('.')
    print(idx1)
    print(url[:idx1])
    if 'www' in url:
        idx2 = url.find('www') + 4
    else:
        idx2 = url.find('//') + 2
    domain = url[idx2:idx1]
    return domain

print(domain_name("http://github.com/carbonfive/raygun"))
print(domain_name("http://www.zombie-bites.com"))
print(domain_name("https://www.cnet.com"))
print(domain_name("http://google.co"))


# convert arr to params
def arrToParams(arr, paramName, params):
    for key in arr:
        params[paramName] += key + '+'
    if len(arr) != 0:
        params[paramName] = params[paramName][:-1]


# generate url
def getUrl(props):
    # set up params
    params = {
        'start': props['start'],
        'as_sitesearch': props['site'],
        'as_epq': '',
        'as_oq': '',
    }
    
    # convert arr to params
    arrToParams(props['mustInclude'], 'as_epq', params)
    arrToParams(props['searchFor'], 'as_oq', params)
    
    # set up url
    url = 'https://www.google.com/search?'
    for key in params:
        url += f'{key}={params[key]}&'
    url = url[:-1]
    
    # end
    return url


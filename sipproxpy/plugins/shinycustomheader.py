def proxy_mangle_request(req):
    req.addHeader("something", "somethingcontent")
    req.addHeader("username", "usernamecontent")
    req.addHeader("customheader", "customheadercontent")
    return req


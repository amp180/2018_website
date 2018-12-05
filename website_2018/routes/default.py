from website_2018.app import api

@api.route("/robots.txt")
async def robots(req, resp):
    return api.redirect(resp, "/static/robots.txt")

@api.route("/favicon.ico")
async def favicon(req, resp):
    return api.redirect(resp, "/static/images/favicon.ico")

api.add_route("/", default=True, static=True)


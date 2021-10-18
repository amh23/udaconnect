def register_routes(api, app, root="api"):
    from app.udaconnect.controllers import api as connection_api

    api.add_namespace(connection_api, path=f"/{root}")

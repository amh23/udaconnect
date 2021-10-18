def register_routes(api, app, root="location-api"):
    from app.udaconnect import register_routes as attach_location
     
    # Add routes
    attach_location(api, app)
     

def get_swagger_config():
    """Returns the Swagger configuration."""
    return {
        "title": "My Custom API",
        "description": "This is a description of my API, which provides various endpoints.",
        "version": "1.0.0",
        "openapi_url": "/swagger.json",
        "docs_url": "/swagger",
        "openapi_security": [{
            "BearerAuth": {
                "type": "apiKey",
                "scheme": "bearer",
                "bearerFormat": "JWT"
            }
        }]
    }
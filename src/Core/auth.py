from fastapi import HTTPException, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

# Bearer token scheme
bearer_scheme = HTTPBearer()

# Dependency to validate the Bearer token
def validate_token(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    # Replace "TEST" with actual JWT validation logic
    if credentials.credentials != "TEST":
        raise HTTPException(status_code=401, detail="Invalid or Unauthorized token Token : TEST")
    return credentials.credentials  # Return the token if it's valid
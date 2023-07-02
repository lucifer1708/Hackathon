import logging
from datetime import datetime, timedelta
from typing import Annotated, List, Optional

import jwt
from fastapi import Depends, Header, HTTPException, Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi.security.utils import get_authorization_scheme_param
from passlib.context import CryptContext

from src.api.user.schemas import UserSchema
from src.core.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class LoggingHTTPBearer(HTTPBearer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO)

    async def __call__(
        self, request: Request
    ) -> Optional[HTTPAuthorizationCredentials]:
        authorization: str = request.headers.get("Authorization")
        if not authorization:
            self.logger.info("Missing Authorization header.")

        scheme, credentials = get_authorization_scheme_param(authorization)

        if not scheme or not credentials:
            self.logger.info(
                f"Scheme or credentials missing. Scheme: {scheme}, Credentials: {credentials}"
            )

        if scheme.lower() != "bearer":
            self.logger.info(f"Invalid scheme. Expected 'bearer', got {scheme.lower()}")

        try:
            return await super().__call__(request)
        except HTTPException as e:
            self.logger.info(f"HTTPException raised: {e}")
            raise e


oauth2_bearer = LoggingHTTPBearer()


def get_current_user(
    token: HTTPAuthorizationCredentials = Depends(oauth2_bearer),
) -> UserSchema:

    try:
        payload = jwt.decode(
            token.credentials, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        username = payload.get("sub")
        id = payload.get("id")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid authentication token")
        return {"username": username, "id": id}
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")


def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM
    )
    return encoded_jwt

from fastapi import Depends, FastAPI
from src.Core.swaggerConfig import get_swagger_config
from src.Controllers.taskController import task_router
from src.Controllers.userController import user_router

app = FastAPI(**get_swagger_config())

app.include_router(user_router)
app.include_router(task_router)
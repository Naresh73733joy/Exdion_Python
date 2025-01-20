from fastapi import APIRouter, Depends, HTTPException
from celery.result import AsyncResult
from src.Core.auth import validate_token
from src.Core.celery_worker import add

task_router = APIRouter()

@task_router.post("/api/Queue/add/{x}/{y}", tags=["TaskQueue"], dependencies=[Depends(validate_token)])
def add_numbers(x: int, y: int):
    try:
        # Call Celery task asynchronously
        task = add.apply_async(args=[x, y])  
        return {"task_id": task.id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error initiating task: {str(e)}")

@task_router.get("/api/Queue/result/{task_id}", tags=["TaskQueue"], dependencies=[Depends(validate_token)])
def get_result(task_id: str):
    try:
        task_result = AsyncResult(task_id)

        if task_result.ready():
            return {"task_id": task_id, "result": task_result.result}
        else:
            return {"task_id": task_id, "status": "Processing"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching task result: {str(e)}")

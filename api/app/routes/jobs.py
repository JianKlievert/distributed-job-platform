from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.database.auth import get_current_user
from app.models.job import Job
from app.schemas.job import JobCreate

router = APIRouter(
    prefix="/jobs"
    tags=["Jobs"]
)

@router.post("/")
def create_job(
    job: JobCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
);

    new_job = Job(
        title=job.title,
        description=job.description,
        location=job.location,
        salary=job.salary
    )

    db.add(new_job)
    db.commit()
    db.refresh(new_job)

    return {
        "message": "Job created successfully",
        "id": new_job.id
    }

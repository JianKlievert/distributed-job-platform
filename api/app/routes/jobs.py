from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.database.auth import get_current_user
from app.models.job import Job
from app.models.user import User
from app.schemas.job import JobCreate, JobResponse

router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"]
)

@router.post("/")
def create_job(
    job: JobCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    new_job = Job(
        title=job.title,
        description=job.description,
        location=job.location,
        salary=job.salary,
        owner=current_user
    )

    db.add(new_job)
    db.commit()
    db.refresh(new_job)

    return {
        "message": "Job created successfully",
        "id": new_job.id
    }

@router.get("/", response_model=list[JobResponse])
def get_jobs(
    db: Session = Depends(get_db)
):
    jobs = db.query(Job).all()

    return jobs

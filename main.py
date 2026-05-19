from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import models, schemas
from database import engine, get_db

# Memastikan tabel terbuat di PostgreSQL
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Student Talent & Project Hub")

# Konfigurasi CORS untuk frontend React
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def baca_root():
    return {"Pesan": "API Sistem Informasi Unhas - Student Talent & Project Hub Berjalan Lancar!"}

# --- 1. ENDPOINT USERS ---
@app.post("/api/users", response_model=schemas.UserResponse)
def tambah_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/api/users", response_model=list[schemas.UserResponse])
def ambil_semua_user(db: Session = Depends(get_db)):
    return db.query(models.User).all()

# --- 2. ENDPOINT SKILLS ---
@app.post("/api/skills", response_model=schemas.SkillCategoryResponse)
def tambah_skill(skill: schemas.SkillCategoryCreate, db: Session = Depends(get_db)):
    db_skill = models.SkillCategory(**skill.model_dump())
    db.add(db_skill)
    db.commit()
    db.refresh(db_skill)
    return db_skill

@app.get("/api/skills", response_model=list[schemas.SkillCategoryResponse])
def ambil_semua_skill(db: Session = Depends(get_db)):
    return db.query(models.SkillCategory).all()

# --- 3. ENDPOINT PROJECTS ---
@app.post("/api/projects", response_model=schemas.ProjectResponse)
def tambah_project(project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    db_project = models.Project(**project.model_dump())
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

@app.get("/api/projects", response_model=list[schemas.ProjectResponse])
def ambil_semua_project(db: Session = Depends(get_db)):
    return db.query(models.Project).all()

# --- 4. ENDPOINT CONTRIBUTORS ---
@app.post("/api/contributors", response_model=schemas.ContributorResponse)
def tambah_kolaborator(contrib: schemas.ContributorCreate, db: Session = Depends(get_db)):
    db_contrib = models.ProjectContributor(**contrib.model_dump())
    db.add(db_contrib)
    db.commit()
    db.refresh(db_contrib)
    return db_contrib

# --- 5. ENDPOINT ENDORSEMENTS ---
@app.post("/api/endorsements", response_model=schemas.EndorsementResponse)
def tambah_endorsement(endorse: schemas.EndorsementCreate, db: Session = Depends(get_db)):
    db_endorse = models.Endorsement(**endorse.model_dump())
    db.add(db_endorse)
    db.commit()
    db.refresh(db_endorse)
    return db_endorse
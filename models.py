from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text
from sqlalchemy.orm import relationship
from database import Base

# 1. Tabel Users
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    role = Column(String, default="student") # student, recruiter, admin
    status = Column(String, default="active") # active, banned

    # Relasi ke tabel proyek (Satu user bisa punya banyak proyek)
    projects = relationship("Project", back_populates="owner")

# 2. Tabel Skill_Categories (Master Data Keahlian)
class SkillCategory(Base):
    __tablename__ = "skill_categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(Text)

# 3. Tabel User_Skills (Keahlian yang dimiliki pengguna)
class UserSkill(Base):
    __tablename__ = "user_skills"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    skill_id = Column(Integer, ForeignKey("skill_categories.id"))
    proficiency_level = Column(String) # beginner, intermediate, expert

# 4. Tabel Projects (Karya Mahasiswa)
class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    is_open = Column(Boolean, default=True)
    status = Column(String, default="published") # published, hidden
    owner_id = Column(Integer, ForeignKey("users.id"))

    # Relasi balik ke tabel Users
    owner = relationship("User", back_populates="projects")

# 5. Tabel Project_Contributors (Riwayat Kolaborasi)
class ProjectContributor(Base):
    __tablename__ = "project_contributors"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    project_id = Column(Integer, ForeignKey("projects.id"))
    role = Column(String) # misal: Backend Developer, UI Designer

# 6. Tabel Endorsements (Validasi antar pengguna)
class Endorsement(Base):
    __tablename__ = "endorsements"

    id = Column(Integer, primary_key=True, index=True)
    from_user_id = Column(Integer, ForeignKey("users.id"))
    to_user_id = Column(Integer, ForeignKey("users.id"))
    skill_id = Column(Integer, ForeignKey("skill_categories.id"))
    project_id = Column(Integer, ForeignKey("projects.id"))
    message = Column(Text)
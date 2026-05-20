from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import jobs, nodes, stats, auth, projects, experiments

app = FastAPI(
    title="HPC Monitor - Universidad del Pacífico",
    description="API para monitoreo de clúster Slurm",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(jobs.router)
app.include_router(nodes.router)
app.include_router(stats.router)
app.include_router(auth.router)
app.include_router(projects.router)
app.include_router(experiments.router)

@app.get("/")
def root():
    return {"mensaje": "API HPC funcionando", "modo": "mock"}
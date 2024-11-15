from fastapi import FastAPI
from model import Developer, Project

app=FastAPI()

@app.post("/developer/")
def create_developer(dev: Developer):
    return {"Message":"Developer created","developer":dev}

@app.post("/projects/")
def create_project(projekti: Project):
    return {"Message":"Project created","projekti":projekti}

@app.get("/project/")
def get_projects():
    shembullprojekt=Project(
        title="Sample",
        description="this is.....",
        languages=["PHP","JS"]
        lead_developer=Developer(name="Vesa")
    )
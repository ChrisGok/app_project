import os
from pydantic import BaseModel

if "DYNO" in os.environ and os.path.isdir(".dvc"):
    os.system("dvc config core.no_scm true")
    if os.system("dvc pull") != 0:
        exit("dvc pull failed")
    os.system("rm -r .dvc .apt/usr/lib/dvc")


class Data(BaseModel):
    test: int

app = FastAPI(
    title="Census data ML model API",
    description="An API to push data and get ML model result",
    version="1.0.0"
)


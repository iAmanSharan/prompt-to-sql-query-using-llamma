import os 
import logging
from pathlib import Path

logging.basicConfig(level = logging.INFO  ,format=f"%(asctime)s:: %(message)s")
project_name= 'query-to-sql'
list_of_files =[
  f"src/{project_name}/__init--.py",
  f"src/{project_name}/constant/__init__.py",
  f"src/{project_name}/entity/__init_.py"
]

for filepath in list_of_files:
  filepath = Path(filepath)
  filedir,filename = os.path.split(filepath)
  if filedir != "":
    os.makedirs(filedir)
    logging.info("directry created")

  if (not os.path.exists(filepath) == True) or  (os.getsize(filepath)==0):
    with open(filepath,"w") as f:
       pass
       logging.info("file created")


else:
  logging.info("file exists")
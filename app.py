import os
import glob
import random
import string
# Init is ran on server startup
# Load your model to GPU as a global variable here using the variable name "model"
def init():
    print("Nothing to initialize")

# Inference is ran for every server call
# Reference your preloaded global model variable here.
def inference(model_inputs:dict) -> dict:
    save_path = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    os.makedirs(save_path+"_inputs", exist_ok=True)

    fasta = f""">SEQ
{model_inputs['sequence']}"""

    with open(f"{save_path}_inputs/SEQ.fasta", "w") as f:
        f.write(fasta)

    os.system(f"colabfold_batch {save_path}_inputs {save_path}")
    result = glob.glob(f"{save_path}/*_rank_001_*.pdb")[0]
    with open(result, "r") as f:
        pdb = f.read()
    os.system(f"rm -rf {save_path}*")
    os.system(f"rm -rf {save_path}_inputs")
    return {'pdb_string': pdb}

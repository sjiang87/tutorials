import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PROJECT_PATH = os.path.join(HERE, "dh_project")
PROBLEM_PATH = os.path.join(PROJECT_PATH, "dh_project", "polynome2")

sys.path.insert(0, PROJECT_PATH)

def execute(script_file):
    python_path = ":".join(sys.path)
    script = os.path.join(PROBLEM_PATH, script_file)
    retval = os.system(f"PYTHONPATH={python_path} {sys.executable} {script}")
    return retval

# def test_load_data():
#     retval = execute("load_data.py")
#     assert retval == 0

# def test_problem():
#     retval = execute("problem.py")
#     assert retval == 0

def test_command():
    python_path = ":".join(sys.path)
    retval = os.system(f"PYTHONPATH={python_path} deephyper hps ambs --evaluator ray --num-workers 2 --max-evals 2 --n-jobs 4 --problem dh_project.polynome2.problem.Problem --run dh_project.polynome2.model_run.run")
    assert retval == 0
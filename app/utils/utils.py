from pathlib import Path
import sys
script_path = Path(__file__).resolve()
parent_path = script_path.parents[1]  
sys.path.append(str(parent_path))



from Utils.config import NUMBERS, SPECIAL_CHARACTERS, LENGTH, SHUFFLE


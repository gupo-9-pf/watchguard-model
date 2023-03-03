# Importing needed packages
from argparse import ArgumentParser
from watchguardmodel.upz import execute as upz_exec
from watchguardmodel.catastralparcel import execute as catastral_exec

# Creating arguments to run the script
parser = ArgumentParser()
parser.add_argument('--script', help='Set the script to run')
args = parser.parse_args()

# Validating command script argument
try:
    SCRIPT = args.script.lower()
    if SCRIPT not in ('upz', 'catastral'):
        raise Exception(
            "Acceptable --script values are: crime, locality, upz, catastral")
except AttributeError:
    raise AttributeError(
        "Script should be executed with '--script=SCRIPT' argument")

# Creating every case for the SCRIPT variable
if SCRIPT == 'upz':
    upz_exec()
elif SCRIPT == 'catastral':
    catastral_exec()

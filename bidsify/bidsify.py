import sys
import argparse
from functions import bidsify

# argparse setup for calling from command line
parser = argparse.ArgumentParser(description='Convert data to BIDS format')
parser.add_argument('origpath', type=str, help='Path to directory of files to be BIDSified')
parser.add_argument('destpath', type=str, help='Path to output directory for BIDSified files.')
parser.add_argument('--n_sessions', default=2, type=int, help='Number of different scan each participant attended.')
parser.add_argument('--scan_types', default=None, help='Names of scan types (and other directories) for organizing within subject directories.')
parser.add_argument('--scan_names', default=None, help='Custom mapping betweeen current file names (keys) and desired output file names (values).')
parser.add_argument('--no_log', action='store_false', help='Create a .log file noting the moving and renaming of files and the current date, named according to --log_name.')
parser.add_argument('--log_name', default='CHANGES', type=str, help='Name of output .log file.')
parser.add_argument('--verbose', action='store_true', help='Print progress updates while running, after each file is moved and renamed.')

args = parser.parse_args()

print(args)
bidsify(args.origpath, args.destpath, args.n_sessions, args.scan_types, args.scan_names, args.no_log, args.log_name, args.verbose)
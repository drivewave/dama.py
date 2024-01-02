from funcs import twitterScheduler
from dama import argparse

parser = argparse.ArgumentParser()
parser.add_argument('margindays', help='')
parser.add_argument('hour', help='')
parser.add_argument('minutes', help='')
args = parser.parse_args()

twitterScheduler(int(args.margindays), int(args.hour), int(args.minutes))
from funcs import twitterScheduler
from dama import argparse

parser = argparse.ArgumentParser()
parser.add_argument('margindays', help='Indicates the margin of days between each post.')
parser.add_argument('hour', help='Indicates the hour of publication.')
parser.add_argument('minutes', help='Indicates the minutes of publication.')
args = parser.parse_args()

twitterScheduler(int(args.margindays), int(args.hour), int(args.minutes))

from funcs import setWindow, dolphinStart, dolphinKill, startProfiles, closeProfiles, twitterFollowBot, twitterMgFarmer, twitterUnfollowBot, sleep
import argparse

def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument('usage', help='Use "setcmd" to adjust the size of the window and position it above the rest of the applications, "dolphin.start" to initialize Dolphin Anty, "dolphin.kill" to kill all Dolphin Anty processes, "dolphin.start.profiles.start" to initialize Dolphin Anty and all profiles, "profiles.start" to initialize all profiles, "profiles.close" to close all profiles, "profiles.close.dolphin.kill" to close all profiles and kill all Dolphin processes, "twitter.followbot" to follow followers of the configured prompts, "twitter.mg-farmer" to like posts that match the configured prompts, "twitter.unfollowbot" to unfollow users who do not follow you, "twitter.unfollowbot.all" to unfollow without exceptions.' )
    args = parser.parse_args()
    if args.usage == 'setcmd': setWindow()
    if args.usage == 'dolphin.start': dolphinStart()
    if args.usage == 'dolphin.kill': dolphinKill()
    if args.usage == 'dolphin.start.profiles.start': dolphinStart(), sleep(1), startProfiles()
    if args.usage == 'profiles.start': startProfiles()
    if args.usage == 'profiles.close': closeProfiles()
    if args.usage == 'profiles.close.dolphin.kill': closeProfiles(), sleep(1), dolphinKill()
    if args.usage == 'twitter.followbot': twitterFollowBot()
    if args.usage == 'twitter.mg-farmer': twitterMgFarmer()
    if args.usage == 'twitter.unfollowbot': twitterUnfollowBot()
    if args.usage == 'twitter.unfollowbot.all': twitterUnfollowBot(all=True)
        
if __name__ == '__main__':
    Main()
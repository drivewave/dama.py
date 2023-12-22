# PENDIENTE

# import argparse
# from funcs import Fore, Style

# parser = argparse.ArgumentParser()
# parser.add_argument('usage', help='Use "dolphin.path" to set the path where Dolphin Anty.exe is located, "dolphin.profiles" to set up the dolphin-profiles.txt file, "twitter.followbot.prompts" to set up twitter-followbot_prompts.txt file, "twitter.mg-farmer.prompts" to set up twitter-mg-farmer-prompts.txt.')
# parser.add_argument('path', help='The path argument must contain the path to the .txt file you want to configure.')
# args = parser.parse_args()

# def prinT(whatis, path):
#     n=0
#     print(f'{whatis}:')
#     for w in open(f'{path}','r').read().splitlines(): 
#         print(str(n)+' - '+w)
#         n+=1
#     print(Fore.GREEN+f'{str(n)} {whatis} configured.'+Style.RESET_ALL)

# if args.usage == 'dolphin.path':
#     with open('./config/dolphin-path.txt','w') as f: f.write(args.path)
#     print(Fore.GREEN+'Dolphin Anty path configured.'+Style.RESET_ALL)
# if args.usage == 'dolphin.profiles':
#     with open('./config/dolphin-profiles.txt','w') as f: [f.write(profile+'\n') for profile in open(f'{args.path}','r').read().splitlines()]
#     prinT('Dolphin Anty Profiles', './config/dolphin-profiles.txt')        
# if args.usage == 'twitter.followbot.prompts':
#     with open('./config/prompts/twitter-followbot-prompts.txt','w') as f: [f.write(prompt+'\n') for prompt in open(f'{args.path}','r').read().splitlines()]        
#     prinT('Twitter FollowBot prompts', './config/prompts/twitter-followbot-prompts.txt')   
# if args.usage == 'twitter.mg-farmer.prompts':
#     with open('./config/prompts/twitter-mg-farmer-prompts.txt','w') as f: [f.write(prompt+'\n') for prompt in open(f'{args.path}','r').read().splitlines()]
#     prinT('Twitter MG-Farmer prompts', './config/prompts/twitter-mg-farmer-prompts.txt')

from funcs import profiles

for profile in profiles:
    with open(f'./config/reg/pics/{profile}.txt','w') as f: f.write(''), f.close()
    with open(f'./config/reg/tweets/{profile}.txt','w') as f: f.write(''), f.close()

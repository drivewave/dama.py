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

# import requests
# endpoint = "https://dolphin-anty-api.com/browser_profiles/statuses/:status_id"
# data = {"ip": "212.8.250.240"}
# headers = {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiNTNhOTE4YzgzYTU1YTM4MTk5ODE0ODMyMzAzOGU2YjZkNDVhOGYyOTFlNzYwMjEyMTU3MDMyYzgzMzNkODNlZThhNzUzYmY3MDE5N2ZhNTciLCJpYXQiOjE3MDMyNTU0MTQuMzc0Mzc5LCJuYmYiOjE3MDMyNTU0MTQuMzc0MzgyLCJleHAiOjE3MDU4NDc0MTQuMzQyNjA0LCJzdWIiOiIyODU1NzcwIiwic2NvcGVzIjpbXX0.RVp_9CkjJ75avfmyYuvWyhBzvGu9fp-FCFMMvml6qa22mWdX9SyS7r29MXCrw1mbJU3dtUZup4sbJDnfdRp19g1a1FvctP_GXnx8D3z-Yp-F2zF3ZxQNl3VdAvJWSfh1b0FphHdB8FIVv8Bo6AD-s4A2UAbnAXAdR3-NffcFzkoUk2M87iQjHRFwhLn-7ZkgvvfD9L1d31Cn_Lu25Xh6G07aRMTfcDK7AksiCarH57WlOS4u4Tbh1j1Ak0j-q6dcFleTzXBZDqI6yvJJ1MbQ2ajzn4yawxoCGwnk6PyaXU0IiVZSKEsV89Fcc0snb8XpcPpXfZn_j09yfN7CetzZPB2k8lZ8WZGrDwB336gIQJitexNv6fdjjPxvVme1kpnCN4I-kfoLjgPgo7a_638YczrqtNFhHNbTq1snynuKmTEHx1qbtQ9gUVGqrvSIowAt1JqcmAZOSJsGRq5u8QQAjNZlME6oUhCoou6LL0P3okIhfFKgrj6iaKCjWdVFtsMYC2QVVrsLdasJCSnaQJgl4H-GZLZ47IYMm7NPNO9RTgEfwSfdm_XObWUeOhhWqQZf95nsKV87vadsdYUW9l99mhn22mfzbmuqugnqSTbavh1cF29N7iDOyrn4dbKaNppqnUK19GXHpjJUg-zrqRR28nvG6naKpEqf_pJ-pPyFKgE"}

# print(requests.post(endpoint, data=data, headers=headers).json())

from funcs import profiles

for profile in profiles:
    with open(f'./config/reg/pics/{profile}.txt','w') as f: f.write(''), f.close()
    with open(f'./config/reg/tweets/{profile}.txt','w') as f: f.write(''), f.close()

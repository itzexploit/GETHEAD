from requests import get
from colorama import Fore , init
from pystyle import Colorate , Colors
from os import system , name
from threading import Thread as thr

init()

red = Fore.LIGHTRED_EX; green = Fore.LIGHTGREEN_EX; blue = Fore.LIGHTBLUE_EX; yellow = Fore.LIGHTYELLOW_EX; cyan = Fore.LIGHTCYAN_EX; white = Fore.LIGHTWHITE_EX; magenta = Fore.LIGHTMAGENTA_EX;

system('cls' if name == 'nt' else 'clear')

banner = '''
         _              _          _            _       _    _            _                _         
        /\ \           /\ \       /\ \         / /\    / /\ /\ \         / /\             /\ \       
       /  \ \         /  \ \      \_\ \       / / /   / / //  \ \       / /  \           /  \ \____  
      / /\ \_\       / /\ \ \     /\__ \     / /_/   / / // /\ \ \     / / /\ \         / /\ \_____\ 
     / / /\/_/      / / /\ \_\   / /_ \ \   / /\ \__/ / // / /\ \_\   / / /\ \ \       / / /\/___  / 
    / / / ______   / /_/_ \/_/  / / /\ \ \ / /\ \___\/ // /_/_ \/_/  / / /  \ \ \     / / /   / / /  
   / / / /\_____\ / /____/\    / / /  \/_// / /\/___/ // /____/\    / / /___/ /\ \   / / /   / / /   
  / / /  \/____ // /\____\/   / / /      / / /   / / // /\____\/   / / /_____/ /\ \ / / /   / / /    
 / / /_____/ / // / /______  / / /      / / /   / / // / /______  / /_________/\ \ \\ \ \__/ / /     
/ / /______\/ // / /_______\/_/ /      / / /   / / // / /_______\/ / /_       __\ \_\\ \___\/ /      
\/___________/ \/__________/\_\/       \/_/    \/_/ \/__________/\_\___\     /____/_/ \/_____/       
                                                                                                     
                        Created By John Wick | Team Pytho Learn

'''

print(Colorate.Horizontal(Colors.red_to_blue,banner,1))

url = input(f'\n  {red}[{yellow}+{red}]{blue} Enter Your URL {red}:{green} ')

def main():
    try:
        r = get(url)
        h = r.headers
        print('\n')
        print(Colorate.Horizontal(Colors.red_to_yellow,str(h),1))
    except:
       print(Colorate.Horizontal(Colors.green_to_yellow,'\n  Enter Your Urllllll !!!!!',2)) 

thr(target=main).start()

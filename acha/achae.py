import webbrowser
import sys
from time import sleep
from getpass import getuser


platforms = {
    'google': 'https://www.google.com/search?q=',
    'Google': 'https://www.google.com/search?q=',
    '-g': 'https://www.google.com/search?q=',
    'youtube': 'https://www.youtube.com/results?search_query=',
    'Youtube': 'https://www.youtube.com/results?search_query=',
    'yt': 'https://www.youtube.com/results?search_query=',
    '-yt': 'https://www.youtube.com/results?search_query=',
    '-y': 'https://www.youtube.com/results?search_query=',
    'bing': 'https://www.bing.com/search?q=',
    'Bing': 'https://www.bing.com/search?q=',
    '-b': 'https://www.bing.com/search?q=',
    'amazon': 'https://www.amazon.com/s?k=',
    'Amazon': 'https://www.amazon.com/s?k=',
    '-a': 'https://www.amazon.com/s?k=',
    'facebook': 'https://www.facebook.com/search/top/?q=',
    'fb': 'https://www.facebook.com/search/top/?q=',
    'Facebook': 'https://www.facebook.com/search/top/?q=',
    '-f': 'https://www.facebook.com/search/top/?q=',
    'yandex': 'https://yandex.com/search/?text=',
    'Yandex': 'https://yandex.com/search/?text=',
    '-ya': 'https://yandex.com/search/?text=',
    'Taskbar': '',
    'taskbar': '',
    '-tb': '',
    '-t': ''
}

if len(sys.argv) == 1:
    print('\n\nAchaê v1 (https://github.com/mtscarneiro) \n')
    print('Como usar:\tachae [plataforma] [busca] ')
    print('PLATAFORMAS SUPORTADAS:')
    print('\tBusca na taskbar [Taskbar, taskbar, -tb]')
    print('\tGoogle [Google, google, -g]')
    print('\tYoutube [Youtube, youtube, -yt, yt, -y]')
    print('\tBing [Bing, bing, -b]')
    print(
        '\tFacebook [Facebook, facebook, fb, -f] (Você precisa estar logado!)')
    print('\tAmazon [Amazon, amazon, -a]')
    print('\tYandex [Yandex, yandex, -ya]')
    platform = input('Qual plataforma? \n')
    search = input('O que quer achar? \n')
    if platform not in platforms.keys():
        platform = '-g'
        print('Não sei que plataforma é essa... \n')
        print('Vou buscar com o Google... \n')
        sleep(3)
else:
    if sys.argv[1] not in platforms.keys():
        platform = '-g'
        print('Não sei que plataforma é essa... \n')
        print('Vou buscar com o Google... \n')
        sleep(3)
        search = ' '.join(sys.argv[2:])
    else:
        platform = sys.argv[1]
        search = ' '.join(sys.argv[2:])


url = platforms[platform] + search

webbrowser.open(url)

def main():
    if getuser() == 'root':
        print('O script não roda in \'root\' pra não dar caô de segurança. \n Fechando!')
        sys.exit()

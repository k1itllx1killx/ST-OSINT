#!/usr/bin/env python3

import subprocess
import os
import requests
import time
from datetime import datetime

os.system("clear")

# Colores
RED = "\033[91m"
BLUE = "\033[94m"
RESET = "\033[0m"

# Banner
def banner():
    banner_text = """
                    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                    ┃                                          ┃
                    ┃     ⚡🔥 ST-OSINT USER TRACKER 🔥⚡      ┃
                    ┃        date: 24/9/25                     ┃
                    ┃      Created by: satan                   ┃
                    ┃      Version: 2.0                        ┃
                    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
"""
    try:
        subprocess.run(f"echo '{banner_text}' | lolcat", shell=True)
    except:
        print(banner_text)

# osint script
def osint_tool(username):
    networks = [
    "https://www.facebook.com/{}",
    "https://www.youtube.com/@{}",
    "https://www.instagram.com/{}",
    "https://www.whatsapp.com/{}",
    "https://www.tiktok.com/@{}",
    "https://www.wechat.com/{}",
    "https://www.x.com/{}",
    "https://www.linkedin.com/in/{}",
    "https://www.snapchat.com/add/{}",
    "https://www.pinterest.com/{}",
    "https://www.telegram.org/{}",
    "https://www.messenger.com/{}",
    "https://www.reddit.com/user/{}",
    "https://www.quora.com/profile/{}",
    "https://www.twitch.tv/{}",
    "https://discord.com/users/{}",
    "https://www.spotify.com/@{}",
    "https://www.applemusic.com/@{}",
    "https://www.soundcloud.com/{}",
    "https://www.vimeo.com/{}",
    "https://www.behance.net/{}",
    "https://www.deviantart.com/{}",
    "https://www.douyin.com/{}",
    "https://www.kuaishou.com/{}",
    "https://www.weibo.com/{}",
    "https://qzone.qq.com/{}",
    "https://tieba.baidu.com/{}",
    "https://www.xiaohongshu.com/{}",
    "https://www.douban.com/{}",
    "https://www.zhihu.com/people/{}",
    "https://www.yy.com/{}",
    "https://www.bilibili.com/space/{}",
    "https://vk.com/{}",
    "https://ok.ru/profile/{}",
    "https://www.yandex.ru/{}",
    "https://www.line.me/ti/p/{}",
    "https://mixi.jp/view_diary.pl?id={}",
    "https://www.kakao.com/{}",
    "https://www.naver.com/{}",
    "https://www.trell.co/{}",
    "https://www.chingari.io/{}",
    "https://www.mojapp.in/{}",
    "https://www.joshapp.com/{}",
    "https://www.tumblr.com/{}",
    "https://www.skype.com/{}",
    "https://www.viber.com/{}",
    "https://www.band.us/{}",
    "https://www.cyworld.com/{}",
    "https://www.gree.jp/{}",
    "https://www.ameba.jp/{}",
    "https://www.mobage.com/{}",
    "https://www.tokopedia.com/{}",
    "https://www.bukalapak.com/{}",
    "https://www.gojek.com/{}",
    "https://www.xing.com/profile/{}",
    "https://www.mewe.com/i/{}",
    "https://www.parler.com/{}",
    "https://www.mastodon.social/@{}",
    "https://pleroma.site/users/{}",
    "https://www.flickr.com/people/{}",
    "https://www.last.fm/user/{}",
    "https://www.goodreads.com/{}",
    "https://letterboxd.com/{}",
    "https://www.untappd.com/user/{}",
    "https://www.patreon.com/{}",
    "https://www.kickstarter.com/profile/{}",
    "https://www.medium.com/@{}",
    "https://www.substack.com/@{}",
    "https://www.mix.com/{}",
    "https://www.steemit.com/@{}",
    "https://www.decenternet.com/{}",
    "https://www.rumble.com/{}",
    "https://www.odyssey.com/@{}",
    "https://www.blogger.com/profile/{}",
    "https://www.wordpress.com/@{}",
    "https://www.taringa.net/{}",
    "https://www.fandom.com/user/{}",
    "https://www.gamejolt.com/@{}",
    "https://itch.io/@{}",
    "https://www.roblox.com/users/{}",
    "https://www.minecraft.net/profile/{}",
    "https://www.epicgames.com/id/{}",
    "https://www.scribd.com/{}",
    "https://www.slideshare.net/{}",
    "https://www.academia.edu/{}",
    "https://www.researchgate.net/profile/{}",
    "https://www.kaggle.com/{}",
    "https://www.artstation.com/{}",
    "https://www.dribbble.com/{}",
    "https://www.pixiv.net/users/{}",
    "https://www.codepen.io/{}",
    "https://www.codesandbox.io/{}",
    "https://www.hackerrank.com/{}",
    "https://www.leetcode.com/{}",
    "https://www.codingame.com/profile/{}",
    "https://www.topcoder.com/members/{}",
    "https://www.glitch.com/@{}",
    "https://www.replit.com/@{}",
    "https://www.stackexchange.com/users/{}",
    "https://www.gitlab.com/{}",
    "https://www.bitbucket.org/{}",
    "https://www.digitalocean.com/community/users/{}",
    "https://www.heroku.com/@{}",
    "https://www.netlify.com/@{}",
    "https://www.vercel.com/@{}",
    "https://www.buymeacoffee.com/{}",
    "https://www.kofi.com/{}",
    "https://www.ello.co/{}",
    "https://www.viadeo.com/en/profile/{}",
    "https://www.clubhouse.com/@{}",
    "https://www.yubo.live/{}",
    "https://www.tiktok.com/@{}",
    "https://www.instagram.com/{}",
    "https://www.twitter.com/{}",
    "https://www.linkedin.com/in/{}",
    "https://www.reddit.com/user/{}",
    "https://www.github.com/{}",
    "https://stackoverflow.com/users/{}",
    "https://www.youtube.com/@{}",
    "https://x.com/{}",
    "https://www.quora.com/profile/{}",
    "https://www.twitch.tv/{}",
    "https://discord.com/users/{}",
    "https://www.soundcloud.com/{}",
    "https://vimeo.com/{}",
    "https://www.behance.net/{}",
    "https://www.deviantart.com/{}",
    "https://www.pinterest.com/{}",
    "https://www.snapchat.com/add/{}",
    "https://www.telegram.org/{}",
    "https://www.messenger.com/{}",
    "https://www.threads.net/{}",
    "https://www.clubhouse.com/{}",
    "https://www.tiktok.com/@{}",
    "https://www.instagram.com/{}",
    "https://www.x.com/{}",
    "https://www.snapchat.com/add/{}",
    "https://www.reddit.com/user/{}",
    "https://www.line.me/{}",
    "https://www.qq.com/{}",
    "https://www.weibo.com/{}",
    "https://www.douyin.com/{}",
    "https://www.kuaishou.com/{}",
    "https://www.xiaohongshu.com/{}",
    "https://www.douban.com/{}",
    "https://www.zhihu.com/people/{}",
    "https://www.twitch.tv/{}",
    "https://www.discord.com/users/{}",
    "https://www.roblox.com/users/{}",
    "https://www.epicgames.com/id/{}",
    "https://www.steamcommunity.com/id/{}",
    "https://www.origin.com/{}",
    "https://www.playstation.com/en-us/{}",
    "https://www.xbox.com/en-US/{}",
    "https://www.nintendo.com/{}",
    "https://www.battle.net/{}",
    "https://www.ubisoft.com/{}",
    "https://www.gog.com/{}",
    "https://www.itch.io/@{}",
    "https://www.gamejolt.com/@{}",
    "https://www.roblox.com/users/{}",
    "https://www.minecraft.net/profile/{}",
    "https://www.steamcommunity.com/id/{}",
    "https://www.origin.com/{}",
    "https://www.playstation.com/en-us/{}",
    "https://www.xbox.com/en-US/{}",
    "https://www.nintendo.com/{}",
    "https://www.battle.net/{}",
    "https://www.ubisoft.com/{}",
    "https://www.gog.com/{}",
    "https://www.itch.io/@{}",
    "https://www.gamejolt.com/@{}",
    "https://www.roblox.com/users/{}",
    "https://www.minecraft.net/profile/{}",
    "https://www.steamcommunity.com/id/{}",
    "https://www.origin.com/{}",
    "https://www.playstation.com/en-us/{}",
    "https://www.xbox.com/en-US/{}",
    "https://www.nintendo.com/{}",
    "https://www.battle.net/{}",
    "https://www.ubisoft.com/{}",
    "https://www.gog.com/{}",
    "https://www.twitch.tv/{}",
    "https://www.twitch.tv/{}",
    "https://discord.com/users/{}",
    "https://www.spotify.com/@{}",
    "https://www.applemusic.com/@{}",
    "https://www.soundcloud.com/{}",
    "https://www.vimeo.com/{}",
    "https://www.behance.net/{}",
    "https://www.deviantart.com/{}",
    "https://www.douyin.com/{}",
    "https://www.kuaishou.com/{}",
    "https://www.weibo.com/{}",
    "https://qzone.qq.com/{}",
    "https://tieba.baidu.com/{}",
    "https://www.xiaohongshu.com/{}",
    "https://www.douban.com/{}",
    "https://www.zhihu.com/people/{}",
    "https://www.yy.com/{}",
    "https://www.bilibili.com/space/{}",
    "https://vk.com/{}",
    "https://ok.ru/profile/{}",
    "https://www.yandex.ru/{}",
    "https://www.line.me/ti/p/{}",
    "https://mixi.jp/view_diary.pl?id={}",
    "https://www.kakao.com/{}",
    "https://www.naver.com/{}",
    "https://www.trell.co/{}",
    "https://www.chingari.io/{}",
    "https://www.mojapp.in/{}",
    "https://www.joshapp.com/{}",
    "https://www.tumblr.com/{}",
    "https://www.skype.com/{}",
    "https://www.viber.com/{}",
    "https://www.band.us/{}",
    "https://www.cyworld.com/{}",
    "https://www.gree.jp/{}",
    "https://www.ameba.jp/{}",
    "https://www.mobage.com/{}",
    "https://www.tokopedia.com/{}",
    "https://www.bukalapak.com/{}",
    "https://www.gojek.com/{}",
    "https://www.xing.com/profile/{}",
    "https://www.mewe.com/i/{}",
    "https://www.parler.com/{}",
    "https://www.mastodon.social/@{}",
    "https://pleroma.site/users/{}",
    "https://www.flickr.com/people/{}",
    "https://www.last.fm/user/{}",
    "https://www.goodreads.com/{}",
    "https://letterboxd.com/{}",
    "https://www.untappd.com/user/{}",
    "https://www.patreon.com/{}",
    "https://www.kickstarter.com/profile/{}",
    "https://www.medium.com/@{}",
    "https://www.substack.com/@{}",
    "https://www.mix.com/{}",
    "https://www.steemit.com/@{}",
    "https://www.decenternet.com/{}",
    "https://www.rumble.com/{}",
    "https://www.odyssey.com/@{}",
    "https://www.blogger.com/profile/{}",
    "https://www.wordpress.com/@{}",
    "https://www.taringa.net/{}",
    "https://www.fandom.com/user/{}",
    "https://www.gamejolt.com/@{}",
    "https://itch.io/@{}",
    "https://www.roblox.com/users/{}",
    "https://www.minecraft.net/profile/{}",
    "https://www.epicgames.com/id/{}",
    "https://www.scribd.com/{}",
    "https://www.slideshare.net/{}",
    "https://www.academia.edu/{}",
    "https://www.researchgate.net/profile/{}",
    "https://www.kaggle.com/{}",
    "https://www.artstation.com/{}",
    "https://www.dribbble.com/{}",
    "https://www.pixiv.net/users/{}",
    "https://www.codepen.io/{}",
    "https://www.codesandbox.io/{}",
    "https://www.hackerrank.com/{}",
    "https://www.leetcode.com/{}",
    "https://www.codingame.com/profile/{}",
    "https://www.topcoder.com/members/{}",
    "https://www.glitch.com/@{}",
    "https://www.replit.com/@{}",
    "https://www.stackexchange.com/users/{}",
    "https://www.gitlab.com/{}",
    "https://www.bitbucket.org/{}",
    "https://www.digitalocean.com/community/users/{}",
    "https://www.heroku.com/@{}",
    "https://www.netlify.com/@{}",
    "https://www.vercel.com/@{}",
    "https://www.buymeacoffee.com/{}",
    "https://www.kofi.com/{}",
    "https://www.ello.co/{}",
    "https://www.viadeo.com/en/profile/{}",
    "https://www.clubhouse.com/@{}",
    "https://www.yubo.live/{}",
    "https://www.tiktok.com/@{}",
    "https://www.instagram.com/{}",
    "https://www.twitter.com/{}",
    "https://www.linkedin.com/in/{}",
    "https://www.reddit.com/user/{}",
    "https://www.github.com/{}",
    "https://stackoverflow.com/users/{}",
    "https://www.youtube.com/@{}",
    "https://x.com/{}",
    "https://www.quora.com/profile/{}",
    "https://www.twitch.tv/{}",
    "https://discord.com/users/{}",
    "https://www.soundcloud.com/{}",
    "https://vimeo.com/{}",
    "https://www.behance.net/{}",
    "https://www.deviantart.com/{}",
    "https://www.pinterest.com/{}",
    "https://www.snapchat.com/add/{}",
    "https://www.telegram.org/{}",
    "https://www.messenger.com/{}",
    "https://www.threads.net/{}",
    "https://www.clubhouse.com/{}",
    "https://www.tiktok.com/@{}",
    "https://www.instagram.com/{}",
    "https://www.x.com/{}",
    "https://www.snapchat.com/add/{}",
    "https://www.reddit.com/user/{}",
    "https://www.line.me/{}",
    "https://www.qq.com/{}",
    "https://www.weibo.com/{}",
    "https://www.douyin.com/{}",
    "https://www.kuaishou.com/{}",
    "https://www.xiaohongshu.com/{}",
    "https://www.douban.com/{}",
    "https://www.zhihu.com/people/{}",
    "https://www.twitch.tv/{}",
    "https://www.discord.com/users/{}",
    "https://www.roblox.com/users/{}",
    "https://www.epicgames.com/id/{}",
    "https://www.steamcommunity.com/id/{}",
    "https://www.origin.com/{}",
    "https://www.playstation.com/en-us/{}",
    "https://www.xbox.com/en-US/{}",
    "https://www.nintendo.com/{}",
    "https://www.battle.net/{}",
    "https://www.ubisoft.com/{}",
    "https://www.gog.com/{}",
    "https://www.itch.io/@{}",
    "https://www.gamejolt.com/@{}",
    "https://www.roblox.com/users/{}",
    "https://www.minecraft.net/profile/{}",
    "https://www.steamcommunity.com/id/{}",
    "https://www.origin.com/{}",
    "https://www.playstation.com/en-us/{}",
    "https://www.xbox.com/en-US/{}",
    "https://www.nintendo.com/{}",
    "https://www.battle.net/{}",
    "https://www.ubisoft.com/{}",
    "https://www.gog.com/{}",
    "https://www.itch.io/@{}",
    "https://www.gamejolt.com/@{}",
    "https://www.roblox.com/users/{}",
    "https://www.minecraft.net/profile/{}",
    "https://www.steamcommunity.com/id/{}",
    "https://www.origin.com/{}",
    "https://www.playstation.com/en-us/{}",
    "https://www.xbox.com/en-US/{}",
    "https://www.nintendo.com/{}",
    "https://www.battle.net/{}",
    "https://www.ubisoft.com/{}",
    "https://www.gog.com/{}",
    "https://www.twitch.tv/{}",
    "https://www.youtube.com/@{}",
    "https://www.tiktok.com/@{}",
    "https://www.instagram.com/{}",
    "https://www.x.com/{}",
    "https://www.snapchat.com/add/{}",
    "https://www.reddit.com/user/{}",
    "https://www.line.me/{}",
    "https://www.qq.com/{}",
    "https://www.weibo.com/{}",
    "https://www.douyin.com/{}",
    "https://www.kuaishou.com/{}",
    "https://www.xiaohongshu.com/{}",
    "https://www.douban.com/{}",
    "https://www.zhihu.com/people/{}",
    "https://www.twitch.tv/{}",
    "https://www.discord.com/users/{}",
    "https://www.roblox.com/users/{}",
    "https://www.epicgames.com/id/{}",
    "https://www.steamcommunity.com/id/{}",
    "https://www.origin.com/{}",
    "https://www.playstation.com/en-us/{}",
    "https://www.xbox.com/en-US/{}",
    "https://www.nintendo.com/{}",

]

    for idx, url in enumerate(networks, start=1):
        full_url = url.format(username)
        timestamp = datetime.now().strftime("%H:%M:%S")
        try:
            r = requests.get(full_url, timeout=5)
            if r.status_code == 200:
                print(f"{BLUE}[{timestamp}] [INFO]{RESET} {full_url}")
            else:
                print(f"{BLUE}[{timestamp}] [INFO]{RESET} {RED}USER NOT FOUND{RESET}")
        except requests.RequestException:
            print(f"{BLUE}[{timestamp}] [INFO]{RESET} {RED}USER NOT FOUND{RESET}")
        time.sleep(0.1)

# Menú
def main_menu():
    while True:
        try:
            subprocess.run("clear", shell=True)
        except:                                                                                                                    
            pass
        banner()
        try: 
            subprocess.run("echo '\n1. Run OSINT\n2. Update Tool\n3. Exit' | lolcat", shell=True)                             
            except:
            print("\n1. Run OSINT\n2. Update Tool\n3. Exit")
        choice = input("\nChoose an option: ").strip()

        if choice == "1":
           username = input ("[+] Enter username to search: ").strip()
           osint_tool(username)
           input("\nPress enter to return to menu...")
        elif choice == "2":
          print("\nUpdating tool...")

          repo_name = "ST-OSINT"
          repo_url = "https://github.com/k1itllx1killx/ST-OSINT.git"
          repo_path = os.path.expanduser(f"~/{repo_name}")

    # Eliminar si existe
        if os.path.exists(repo_path):
            os.system(f"rm -rf {repo_path}")
     # wait       
    print("please wait")

    # Clonar repositorio en silencio
    os.system(f"git clone {repo_url} {repo_path} > /dev/null 2>&1")

    print("Tool updated!\n")
    input("Press enter to return to menu...")
            break
        else:
            print("Invalid option.")
            time.sleep(1)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid option.")
            time.sleep(1)

if __name__ == "__main__":
    main_menu()

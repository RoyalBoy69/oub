#imported from USERGE-X by @RoyalBoyPriyanshu
import aiohttp
from userbot.events import register


@register(pattern=r".git (.*)", outgoing=True)
async def fetch_github_info(event):
    replied = event.reply_to_event
    username = event.filtered_input_str
    if replied:
        username = replied.text
    if not username:
        await event.err("invalid input !")
        return
    url = "https://api.github.com/users/{}".format(username)
    res = requests.get(url)
    if res.status_code == 200:
        await event.edit("`fetching github info ...`")
        data = res.json()
        photo = data["avatar_url"]
        if data['bio']:
            data['bio'] = data['bio'].strip()
        repos = []
        sec_res = requests.get(data["repos_url"])
        if sec_res.status_code == 200:
            limit = int(event.flags.get('-l', 5))
            for repo in sec_res.json():
                repos.append(f"[{repo['name']}]({repo['html_url']})")
                limit -= 1
                if limit == 0:
                    break
        template = """
\bð¤ **Name** : [{name}]({html_url})
ð§ **Type** : `{type}`
ð¢ **Company** : `{company}`
ð­ **Blog** : {blog}
ð **Location** : `{location}`
ð **Bio** : __{bio}__
â¤ï¸ **Followers** : `{followers}`
ð **Following** : `{following}`
ð **Public Repos** : `{public_repos}`
ð **Public Gists** : `{public_gists}`
ð **Profile Created** : `{created_at}`
âï¸ **Profile Updated** : `{updated_at}`\n""".format(**data)
        if repos:
            template += "ð **Some Repos** : " + ' | '.join(repos)
        await event.client.send_photo(chat_id=event.chat_id,
                                        caption=template,
                                        photo=photo,
                                        disable_notification=True)
        await event.delete()
    else:
        await event.edit("No user found with `{}` username!".format(username))
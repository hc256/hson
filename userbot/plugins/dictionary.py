from PyDictionary import PyDictionary

from . import AioHttp


@icssbot.on(admin_cmd(pattern="ud (.*)"))
@icssbot.on(sudo_cmd(pattern="ud (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    word = event.pattern_match.group(1)
    try:
        response = await AioHttp().get_json(
            f"http://api.urbandictionary.com/v0/define?term={word}",
        )
        word = response["list"][0]["word"]
        definition = response["list"][0]["definition"]
        example = response["list"][0]["example"]
        result = "**Text: {}**\n**Meaning:**\n`{}`\n\n**Example:**\n`{}`".format(
            _format.replacetext(word),
            _format.replacetext(definition),
            _format.replacetext(example),
        )
        await edit_or_reply(event, result)
    except Exception as e:
        await edit_delete(
            event,
            text="`The Unban Dictionary API could not be reached`",
        )
        print(e)


@icssbot.on(admin_cmd(pattern="معنى (.*)"))
@icssbot.on(sudo_cmd(pattern="معنى (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    word = event.pattern_match.group(1)
    dictionary = PyDictionary()
    cat = dictionary.meaning(word)
    output = f"**⌔∮ الكلمه :** __{word}__\n\n"
    try:
        for a, b in cat.items():
            output += f"**{a}**\n"
            for i in b:
                output += f"☞__{i}__\n"
        await edit_or_reply(event, output)
    except Exception:
        await edit_or_reply(event, f"**⌔∮ لايوجد معنى لهذا الكلمه** - {word}")


CMD_HELP.update(
    {
        "dictionary": "**Plugin :** `dictionary`\
    \n\n  •  **Syntax :** `.ud query`\
    \n  •  **Function : **fetches meaning from Urban dictionary\
    \n\n  •  **Syntax : **`.معنى`\
    \n  •  **Function : **Fetches meaning of the given word\
    "
    }
)

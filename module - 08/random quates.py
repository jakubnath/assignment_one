quates = [
{
"anime": "Nisemonogatari",
"character": "Shinobu Oshino",
"quote": "No matter what bonds you forge with others, time will tear them apart. Well... Doesn't thinking about it make you sick?"
},
{
"anime": "Avatar: The Last Airbender",
"character": "Katara",
"quote": "*referring to the man that took her mothers life* I wanted to do it. I wanted to take out all my anger at him. But... I couldn't. I don't know if it's because I'm too weak to do it, or if it's because I'm strong enough not to."
},
{
"anime": "Angel Beats!",
"character": "Yuri Nakamura",
"quote": "Let me tell you something. Humans don't even have the patience to wait even ten minutes for something!"
},
{
"anime": "Fairy Tail",
"character": "Gray Fullbuster",
"quote": "Sorry, but it doesn't matter if you're a woman or even a child... I don't go easy on anybody who hurts my nakama."
},
{
"anime": "Ghost in the Shell",
"character": "Motoko Kusanagi",
"quote": "If a technological feat is possible, man will do it. Almost as if it’s wired into the core of our being."
},
{
"anime": "Yu-Gi-Oh!",
"character": "Yami Yugi",
"quote": "Exodia, OBLITERATE!!!"
},
{
"anime": "Youjo Senki",
"character": "Tanya Degurechaff",
"quote": "You should try persuasion when people are mentally defenseless. The fascist who proposed that was a demonic genius."
},
{
"anime": "Bleach",
"character": "Ulquiorra Schiffer",
"quote": "[To Orihime] Am I frightening... woman?"
},
{
"anime": "",
"character": "Rain",
"quote": "Being frightened of a strong enemy is perfectly natural. Confidence is something you build up, triumph upon triumph."
},
{
"anime": "Kiznaiver",
"character": "Maki Honoka",
"quote": "There is nothing more expensive than something free."
}
]


for quate in quates:
    character = quate.get('character')
    q = quate.get('quote')
    template = f'{character} says, "{q}"'
    print(template)
    print('*'*10)
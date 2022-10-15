information = [
{
"anime": "Boruto: Naruto Next Generations",
"character": "Naruto Uzumaki",
"quote": "The many lives lost during long years of conflict... because of those selfless sacrifices, we are able to bathe in peace and prosperity now. To ingrain this history within the new generation will be a vital cog in helping to maintain the peace."
},
{
"anime": "Naruto",
"character": "Pain",
"quote": "Because of the existence of love - sacrifice is born. As well as hate. Then one comprehends... one knows PAIN."
},
{
"anime": "Naruto",
"character": "Yashamaru",
"quote": "Physical wounds will definitely bleed and may look painful \nbut over time they heal by themselves and if you apply medicine, \nthey will heal faster. What's troublesome are wounds of the heart. Nothing is harder to heal. They're a bit different from physical injuries. You can't apply medicine for one thing and sometimes, they never heal. There's only one cure for a wound of the heart. \nIt's a bit bothersome and you can only receive it from someone else. What is it? Love."
},
{
"anime": "Naruto",
"character": "Shino Aburame",
"quote": "Trying to improve by learning from others that is what calls friendship."
},
{
"anime": "Naruto",
"character": "Itachi Uchiha",
"quote": "Those who forgive themselves, and are able to accept their true nature... They are the strong ones!"
},
{
"anime": "Naruto",
"character": "Rock Lee",
"quote": "Stop it! How dare you disrespect an opponent that fought you with all he had!?"
},
{
"anime": "Naruto",
"character": "Genma Shiranui",
"quote": "When captured birds grow wiser, they try to open the cage with their beaks. They don't give up, because they want to fly again."
},
{
"anime": "Naruto",
"character": "Gaara",
"quote": "Just because someone is important to you, it doesn't necessarily mean that, that person is good. Even if you knew that person was evil... People cannot win against their loneliness."
},
{
"anime": "Naruto",
"character": "Pain",
"quote": "Even the most ignorant, innocent child will eventually grow up as they learn what true pain is. It affects what they say, what they think… and they become real people."
},
{
"anime": "Naruto",
"character": "Neji Hyuuga",
"quote": "Fear. That is what we live with. And we live it everyday. Only in death are we free of it."
}
]

# print(type(information[1]))
# print(information[0].get('anime'))

for info in information:
    ani = info.get('anime')
    cha = info.get('character')
    template = f'{ani}, says {cha}'
    print(template)
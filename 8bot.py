import os, discord
import random
from difflib import SequenceMatcher
client = discord.Client()
TOKEN = os.environ['token']

Rcount = 0
SRcount = 0
SSRcount = 0

class MyClient(discord.Client):
    async def on_ready(self):
        print('8-BOT V2 Deployed.')
        print('------------------')
        print('Copyright 2019 8BALabs. Reproduction is strictly prohibited.')
        print('Status: Online.')
        print('Connection: Stable.')
        print('Vitals: Green.')
        print('------------------')
        print('Deployment Successful. Awaiting Orders.')
        await client.change_presence(status= discord.Status.do_not_disturb,activity=discord.Activity(type=discord.ActivityType.watching, name='Nothing'))

    async def on_message(self, message):
        global Rcount
        global SRcount
        global SSRcount
        #don't respond to ourselves
        if message.author == self.user:
           return

        if '*test' in message.content:
            await message.channel.send('Testing.')


        if message.content.startswith('*speak'):
            first = message.content.replace("*speak", "")
            verbs = ["accept", "add", "admire", "admit", "advise", "afford", "agree", "alert", "announce", "annoy", "answer", "apologise", "appreciate", "approve", "argue", "arrange", "arrest", "arrive", "attack", "attempt", "attend", "attract", "avoid", "back", "bake", "balance", "ban", "bang", "bare", "bat", "bathe", "battle", "behave", "belong", "bleach", "bless", "blind", "blink", "blot", "blush", "bolt", "bomb", "book", "bore", "borrow", "bounce", "bow", "box", "breathe", "bruise", "brush", "bubble", "bump", "burn", "bury", "buzz", "calculate", "call", "camp", "care", "carry", "carve", "cause", "challenge", "change", "charge", "chase", "cheat", "check", "cheer", "chop", "claim", "clap", "clean", "clear", "clip", "close", "coach", "coil", "collect", "colour", "comb", "command", "compete", "complain", "complete", "concentrate", "concern", "confess", "confuse", "connect", "consider", "consist", "contain", "continue", "copy", "count", "cover", "crack", "crash", "crawl", "cross", "crush", "cry", "cure", "curl", "curve", "cycle", "dam", "damage", "dance", "dare", "decay", "deceive", "decide", "decorate", "delay", "depend", "describe", "desert", "deserve", "destroy", "detect", "develop", "disagree", "disarm", "discover", "dislike", "divide", "double", "doubt", "drag", "drain", "drip", "drop", "drown", "drum", "dry", "dust", "earn", "educate", "embarrass", "employ", "empty", "enjoy", "enter", "entertain", "escape", "explode", "extend", "face", "fade", "fail", "fancy", "fasten", "fax", "fear", "file", "fill", "film", "fire", "fit", "fix", "form", "found", "frame", "frighten", "fry", "gather", "gaze", "glow", "grip", "groan", "guess", "guide", "hammer", "hand", "handle", "hang", "happen", "hate", "haunt", "head", "heal", "hum", "hunt", "hurry", "identify", "ignore", "imagine", "impress", "improve", "influence", "inform", "inject", "injure", "interest", "interfere", "interrupt", "introduce", "invent	invite", "irritate", "itch", "jail", "jump", "kick", "level", "license", "lick", "lie	lighten", "like", "list", "listen", "lock", "long", "look", "love", "man", "manage", "march", "mark", "marry", "match", "mine", "miss", "mix", "moan", "moor", "muddle", "mug", "multiply", "murder", "nail", "number", "obey", "object", "owe", "own", "pack", "paddle", "paint", "park", "part", "pass", "paste", "pat", "pause", "peck", "pedal", "peel", "peep", "pick", "pinch", "pine", "place", "plan", "plant", "play", "please", "plug", "point", "poke", "polish", "pray", "preach", "precede", "prefer", "prepare", "present", "preserve", "press", "prick", "print", "produce", "program", "promise", "protect", "provide", "pull", "pump", "punch", "puncture", "punish", "push	 	 ", "race", "radiate", "rain", "raise", "reach", "realise", "receive", "recognise", "record", "reduce", "regret", "reign", "reject", "rejoice", "relax", "release", "rely", "remain", "remember", "rinse", "risk", "rob", "rock", "roll", "rot", "rub", "ruin", "rule", "rush", "sack", "sail", "satisfy", "save", "saw", "scare", "scatter", "scold", "scorch", "scrape", "scratch", "scream", "screw", "scribble", "scrub", "seal", "search", "separate", "serve", "settle", "shade", "share", "shave", "shock", "shop", "shrug", "sigh", "sign", "signal", "sin", "sip", "ski", "skip", "slap", "slip", "slow", "smash", "smell", "smile", "smoke", "snatch", "sneeze", "sniff", "snore", "snow", "sound", "spare", "spark", "sparkle", "spell", "spill", "spoil", "spot", "spray", "sprout", "squash", "squeak", "squeal", "squeeze", "stain", "stamp", "stare", "start", "stay", "steer", "step", "stir", "store", "strap", "strengthen", "stretch", "strip", "stroke", "stuff", "subtract", "succeed", "suck", "suffer", "suggest", "suit", "supply", "support", "suppose", "surprise", "surround", "suspect", "suspend", "switch", "talk", "tame", "tap", "taste", "tease", "telephone", "tempt", "terrify", "test", "tick", "tickle", "tie", "time", "tip", "tire", "touch", "tour", "trade", "train", "transport", "trap", "travel", "treat", "tremble", "trick", "trouble", "trust", "try", "tug", "tumble", "turn", "twist", "type", "undress", "wait", "walk", "wander", "want", "warm", "warn", "watch", "water", "wave", "weigh", "welcome", "whine", "whisper", "whistle", "wink", "wipe", "wish", "wobble", "worry", "wrap", "wreck", "wrestle", "wriggle"]
            prons = ["his", 'her', 'that', 'our', 'those', 'these', 'a', 'the', 'my', 'your', 'its']
            adj = ["attractive","bald","beautiful","chubby","clean","dazzling","drab","elegant","fancy","fit","flabby","glamorous","gorgeous","handsome","long","magnificent","muscular","plain","plump","quaint","scruffy","shapely","short","skinny","stocky","ugly","unkempt","unsightly","alive","better","careful","clever","dead","easy","famous","gifted","hallowed","helpful","important","inexpensive","mealy","mushy","odd","poor","powerful","rich","shy","tender","unimportant","uninterested","vast","wrong","aggressive","agreeable","ambitious","brave","calm","delightful","eager","faithful","gentle","happy","jolly","kind","lively","nice","obedient","polite","proud","silly","thankful","victorious","witty","wonderful","zealous","angry","bewildered","clumsy","defeated","embarrassed","fierce","grumpy","helpless","itchy","jealous","lazy","mysterious","nervous","obnoxious","panicky","pitiful","repulsive","scary","thoughtless","uptight","worried","big","colossal","fat","gigantic","great","huge","immense","large","little","mammoth","massive","microscopic","miniature","petite","puny","scrawny","short","small","tall","teeny","tiny","broad","chubby","crooked","curved","deep","flat","high","hollow","low","narrow","refined","round","shallow","skinny","square","steep","straight","wide","ancient","brief","early","fast","future","late","long","modern","old","old-fashioned","prehistoric","quick","rapid","short","slow","swift","young"]
            nouns = ["people", "history", "way", "art", "world", "information", "map", "two", "family", "government", "health", "system", "computer", "meat", "year", "thanks", "music", "person", "reading", "method", "data", "food", "understanding", "theory", "law", "bird", "literature", "problem", "software", "control", "knowledge", "power", "ability", "economics", "love", "internet", "television", "science", "library", "nature", "fact", "product", "idea", "temperature", "investment", "area", "society", "activity", "story", "industry", "media", "thing", "oven", "community", "definition", "safety", "quality", "development", "language", "management", "player", "variety", "video", "week", "security", "country", "exam", "movie", "organization", "equipment", "physics", "analysis", "policy", "series", "thought", "basis", "boyfriend", "direction", "strategy", "technology", "army", "camera", "freedom", "paper", "environment", "child", "instance", "month", "truth", "marketing", "university", "writing", "article", "department", "difference", "goal", "news", "audience", "fishing", "growth", "income", "marriage", "user", "combination", "failure", "meaning", "medicine", "philosophy", "teacher", "communication", "night", "chemistry", "disease", "disk", "energy", "nation", "road", "role", "soup", "advertising", "location", "success", "addition", "apartment", "education", "math", "moment", "painting", "politics", "attention", "decision", "event", "property", "shopping", "student", "wood", "competition", "distribution", "entertainment", "office", "population", "president", "unit", "category", "cigarette", "context", "introduction", "opportunity", "performance", "driver", "flight", "length", "magazine", "newspaper", "relationship", "teaching", "cell", "dealer", "finding", "lake", "member", "message", "phone", "scene", "appearance", "association", "concept", "customer", "death", "discussion", "housing", "inflation", "insurance", "mood", "woman", "advice", "blood", "effort", "expression", "importance", "opinion", "payment", "reality", "responsibility", "situation", "skill", "statement", "wealth", "application", "city", "county", "depth", "estate", "foundation", "grandmother", "heart", "perspective", "photo", "recipe", "studio", "topic", "collection", "depression", "imagination", "passion", "percentage", "resource", "setting", "ad", "agency", "college", "connection", "criticism", "debt", "description", "memory", "patience", "secretary", "solution", "administration", "aspect", "attitude", "director", "personality", "psychology", "recommendation", "response", "selection", "storage", "version", "alcohol", "argument", "complaint", "contract", "emphasis", "highway", "loss", "membership", "possession", "preparation", "steak", "union", "agreement", "cancer", "currency", "employment", "engineering", "entry", "interaction", "mixture", "preference", "region", "republic", "tradition", "virus", "actor", "classroom", "delivery", "device", "difficulty", "drama", "election", "engine", "football", "guidance", "hotel", "owner", "priority", "protection", "suggestion", "tension", "variation", "anxiety", "atmosphere", "awareness", "bath", "bread", "candidate", "climate", "comparison", "confusion", "construction", "elevator", "emotion", "employee", "employer", "guest", "height", "leadership", "mall", "manager", "operation", "recording", "sample", "transportation", "charity", "cousin", "disaster", "editor", "efficiency", "excitement", "extent", "feedback", "guitar", "homework", "leader", "mom", "outcome", "permission", "presentation", "promotion", "reflection", "refrigerator", "resolution", "revenue", "session", "singer", "tennis", "basket", "bonus", "cabinet", "childhood", "church", "clothes", "coffee", "dinner", "drawing", "hair", "hearing", "initiative", "judgment", "lab", "measurement", "mode", "mud", "orange", "poetry", "police", "possibility", "procedure", "queen", "ratio", "relation", "restaurant", "satisfaction", "sector", "signature", "significance", "song", "tooth", "town", "vehicle", "volume", "wife", "accident", "airport", "appointment", "arrival", "assumption", "baseball", "chapter", "committee", "conversation", "database", "enthusiasm", "error", "explanation", "farmer", "gate", "girl", "hall", "historian", "hospital", "injury", "instruction", "maintenance", "manufacturer", "meal", "perception", "pie", "poem", "presence", "proposal", "reception", "replacement", "revolution", "river", "son", "speech", "tea", "village", "warning", "winner", "worker", "writer", "assistance", "breath", "buyer", "chest", "chocolate", "conclusion", "contribution", "cookie", "courage", "dad", "desk", "drawer", "establishment", "examination", "garbage", "grocery", "honey", "impression", "improvement", "independence", "insect", "inspection", "inspector", "king", "ladder", "menu", "penalty", "piano", "potato", "profession", "professor", "quantity", "reaction", "requirement", "salad", "sister", "supermarket", "tongue", "weakness", "wedding", "affair", "ambition", "analyst", "apple", "assignment", "assistant", "bathroom", "bedroom", "beer", "birthday", "celebration", "championship", "cheek", "client", "consequence", "departure", "diamond", "dirt", "ear", "fortune", "friendship", "funeral", "gene", "girlfriend", "hat", "indication", "intention", "lady", "midnight", "negotiation", "obligation", "passenger", "pizza", "platform", "poet", "pollution", "recognition", "reputation", "shirt", "sir", "speaker", "stranger", "surgery", "sympathy", "tale", "throat", "trainer", "uncle", "youth"]
            suff = ['s', 'ed']
            sen1 = first + " " + random.choice(verbs)+ random.choice(suff) + " " + random.choice(prons) + " " + random.choice(adj) + " " + random.choice(nouns) + '.'
            await message.channel.send(sen1)


        if message.content.startswith('*nickgen'):
            adj = ["attractive","bald","beautiful","chubby","clean","dazzling","drab","elegant","fancy","fit","flabby","glamorous","gorgeous","handsome","long","magnificent","muscular","plain","plump","quaint","scruffy","shapely","short","skinny","stocky","ugly","unkempt","unsightly","alive","better","careful","clever","dead","easy","famous","gifted","hallowed","helpful","important","inexpensive","mealy","mushy","odd","poor","powerful","rich","shy","tender","unimportant","uninterested","vast","wrong","aggressive","agreeable","ambitious","brave","calm","delightful","eager","faithful","gentle","happy","jolly","kind","lively","nice","obedient","polite","proud","silly","thankful","victorious","witty","wonderful","zealous","angry","bewildered","clumsy","defeated","embarrassed","fierce","grumpy","helpless","itchy","jealous","lazy","mysterious","nervous","obnoxious","panicky","pitiful","repulsive","scary","thoughtless","uptight","worried","big","colossal","fat","gigantic","great","huge","immense","large","little","mammoth","massive","microscopic","miniature","petite","puny","scrawny","short","small","tall","teeny","tiny","broad","chubby","crooked","curved","deep","flat","high","hollow","low","narrow","refined","round","shallow","skinny","square","steep","straight","wide","ancient","brief","early","fast","future","late","long","modern","old","old-fashioned","prehistoric","quick","rapid","short","slow","swift","young"]
            nouns = ["people", "history", "way", "art", "world", "information", "map", "two", "family", "government", "health", "system", "computer", "meat", "year", "thanks", "music", "person", "reading", "method", "data", "food", "understanding", "theory", "law", "bird", "literature", "problem", "software", "control", "knowledge", "power", "ability", "economics", "love", "internet", "television", "science", "library", "nature", "fact", "product", "idea", "temperature", "investment", "area", "society", "activity", "story", "industry", "media", "thing", "oven", "community", "definition", "safety", "quality", "development", "language", "management", "player", "variety", "video", "week", "security", "country", "exam", "movie", "organization", "equipment", "physics", "analysis", "policy", "series", "thought", "basis", "boyfriend", "direction", "strategy", "technology", "army", "camera", "freedom", "paper", "environment", "child", "instance", "month", "truth", "marketing", "university", "writing", "article", "department", "difference", "goal", "news", "audience", "fishing", "growth", "income", "marriage", "user", "combination", "failure", "meaning", "medicine", "philosophy", "teacher", "communication", "night", "chemistry", "disease", "disk", "energy", "nation", "road", "role", "soup", "advertising", "location", "success", "addition", "apartment", "education", "math", "moment", "painting", "politics", "attention", "decision", "event", "property", "shopping", "student", "wood", "competition", "distribution", "entertainment", "office", "population", "president", "unit", "category", "cigarette", "context", "introduction", "opportunity", "performance", "driver", "flight", "length", "magazine", "newspaper", "relationship", "teaching", "cell", "dealer", "finding", "lake", "member", "message", "phone", "scene", "appearance", "association", "concept", "customer", "death", "discussion", "housing", "inflation", "insurance", "mood", "woman", "advice", "blood", "effort", "expression", "importance", "opinion", "payment", "reality", "responsibility", "situation", "skill", "statement", "wealth", "application", "city", "county", "depth", "estate", "foundation", "grandmother", "heart", "perspective", "photo", "recipe", "studio", "topic", "collection", "depression", "imagination", "passion", "percentage", "resource", "setting", "ad", "agency", "college", "connection", "criticism", "debt", "description", "memory", "patience", "secretary", "solution", "administration", "aspect", "attitude", "director", "personality", "psychology", "recommendation", "response", "selection", "storage", "version", "alcohol", "argument", "complaint", "contract", "emphasis", "highway", "loss", "membership", "possession", "preparation", "steak", "union", "agreement", "cancer", "currency", "employment", "engineering", "entry", "interaction", "mixture", "preference", "region", "republic", "tradition", "virus", "actor", "classroom", "delivery", "device", "difficulty", "drama", "election", "engine", "football", "guidance", "hotel", "owner", "priority", "protection", "suggestion", "tension", "variation", "anxiety", "atmosphere", "awareness", "bath", "bread", "candidate", "climate", "comparison", "confusion", "construction", "elevator", "emotion", "employee", "employer", "guest", "height", "leadership", "mall", "manager", "operation", "recording", "sample", "transportation", "charity", "cousin", "disaster", "editor", "efficiency", "excitement", "extent", "feedback", "guitar", "homework", "leader", "mom", "outcome", "permission", "presentation", "promotion", "reflection", "refrigerator", "resolution", "revenue", "session", "singer", "tennis", "basket", "bonus", "cabinet", "childhood", "church", "clothes", "coffee", "dinner", "drawing", "hair", "hearing", "initiative", "judgment", "lab", "measurement", "mode", "mud", "orange", "poetry", "police", "possibility", "procedure", "queen", "ratio", "relation", "restaurant", "satisfaction", "sector", "signature", "significance", "song", "tooth", "town", "vehicle", "volume", "wife", "accident", "airport", "appointment", "arrival", "assumption", "baseball", "chapter", "committee", "conversation", "database", "enthusiasm", "error", "explanation", "farmer", "gate", "girl", "hall", "historian", "hospital", "injury", "instruction", "maintenance", "manufacturer", "meal", "perception", "pie", "poem", "presence", "proposal", "reception", "replacement", "revolution", "river", "son", "speech", "tea", "village", "warning", "winner", "worker", "writer", "assistance", "breath", "buyer", "chest", "chocolate", "conclusion", "contribution", "cookie", "courage", "dad", "desk", "drawer", "establishment", "examination", "garbage", "grocery", "honey", "impression", "improvement", "independence", "insect", "inspection", "inspector", "king", "ladder", "menu", "penalty", "piano", "potato", "profession", "professor", "quantity", "reaction", "requirement", "salad", "sister", "supermarket", "tongue", "weakness", "wedding", "affair", "ambition", "analyst", "apple", "assignment", "assistant", "bathroom", "bedroom", "beer", "birthday", "celebration", "championship", "cheek", "client", "consequence", "departure", "diamond", "dirt", "ear", "fortune", "friendship", "funeral", "gene", "girlfriend", "hat", "indication", "intention", "lady", "midnight", "negotiation", "obligation", "passenger", "pizza", "platform", "poet", "pollution", "recognition", "reputation", "shirt", "sir", "speaker", "stranger", "surgery", "sympathy", "tale", "throat", "trainer", "uncle", "youth"]
            readj = random.choice(adj).capitalize()
            renouns = random.choice(nouns).capitalize()
            await message.author.edit(nick=readj + ' ' + renouns)

        if '<@594226483984334849>' in message.content:
            await message.channel.send("**DON'T PING ME.**")

       # hi = ['hi', 'HI', 'Hi', 'hello', 'HELLO', 'Hello', 'hey', 'HEY', 'Hey', 'Morning']
        #for i in hi:
         #   if message.content.startswith(i):
          #      response = ["What's Up.", "Yo.", 'Hi.', "Greetings."]
           #     await message.channel.send(random.choice(response))

        if message.content.startswith('*weebify'):
            nicks = ["Renji Abarai","Sōsuke Aizen","Alucard ","Android 17","Hao Asakura","Ash Ketchum","Astro Boy ","Shinn Asuka","Atsushi Nakajima ","Char Aznable","Sergio Batista","Batou","Beerus","Black Jack ","Brock ","Broly","Cell","Cross Marian","Dio Brando","Doraemon","Ryoma Echizen","Alphonse Elric","Edward Elric","Father","Frieza","Gaara","Gohan","Goku","Hayato Gokudera","Gourry Gabriev","Tadashi Hamada","Captain Harlock","Haseo","Kyoya Hibari","Himura Kenshin","Saito Hiraga","Hiro Takachiho","Yoichi Hiruma","Tōshirō Hitsugaya","Hikaru Ichijyo","Gin Ichimaru","Gendo Ikari","Shinji Ikari","Phoenix Ikki","Matt Ishida","Uryū Ishida","Goemon Ishikawa XIII","Itachi Uchiha","Maximilian Jenius","Daisuke Jigen","Jiraiya ","Kaito Kuroba","Kakashi Hatake","Tai Kamiya","Kamui Shirō","Kei Kurono","Keiichi Morisato","Kenshiro","Kirito","Kiritsugu Emiya","Sena Kobayakawa","Shinya Kogami","Krillin","Byakuya Kuchiki","Jimmy Kudo","Ichigo Kurosaki","Suzaku Kururugi","Lelouch Lamperouge","Lavi ","Legato Bluesummers","Luke fon Fabre","Arsène Lupin III","Majin Buu","Shogo Makishima","Mello ","Millennium Earl","Mitsuki ","Monkey D. Luffy","Ataru Moroboshi","Roy Mustang","Myōjin Yahiko","Kaworu Nagisa","Shikamaru Nara","Naruto Uzumaki","Natsu Dragneel","Near ","Basara Nekki","Orochimaru ","Osamu Dazai ","Piccolo ","Pluto ","Professor Ochanomizu","Raoh","Amuro Ray","Robita","Rock ","Rock Lee","Mukuro Rokudo","Roronoa Zoro","Roy Focker","Ryuk ","Yasutora Sado","Sagara Sanosuke","Saito ","Saitō Hajime ","Gintoki Sakata","Seishirō Sakurazuka","Genma Saotome","Ryohei Sasagawa","Tsuna Sawada","Scar ","Pegasus Seiya","Seta Sōjirō","Setsuna F. Seiei","Hosuke Sharaku","Shinomori Aoshi","Shirou Emiya","Dragon Shiryū","Shishio Makoto","Andromeda Shun","Spike Spiegel","Strider Hiryu","Subaru Sumeragi","Syaoran ","Soun Tendo","Dr. Tenma","Tien Shinhan","Togusa","Kaname Tōsen","Trunks ","Tsubasa Oozora","Tuxedo Mask","Sasuke Uchiha","Boruto Uzumaki","Vash the Stampede","Vegeta","Viewtiful Joe ","Allen Walker","Kimihiro Watanuki","Derek Wildstar","Nicholas D. Wolfwood","Xellos","Light Yagami","Takeshi Yamamoto","Kira Yamato","Yamcha","Eren Yeager","Yoh Asakura","Youji Itami","Yu Kanda","Yugi Mutou","Yukishiro Enishi","Yuri Lowell","Athrun Zala","Zamasu","Kenpachi Zaraki","Kiyo Takamine and Zatch Bell","Koichi Zenigata",]
            await message.author.edit(nick=random.choice(nicks))

        if message.content.startswith('*iq'):
            first = message.mentions[0].name
            second = '🤔 ' + first + "'s IQ is: "
            if first == '8-BIT☆ASIAN':
                embeded = discord.Embed(title=second + '153', color=0x228B22)
                await message.channel.send(embed=embeded)
            else:
                embeded = discord.Embed(title=second + str(random.randint(75, 150)), color=0x228B22)
                await message.channel.send(embed=embeded)

        ssr = ['https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1438429785002.jpg',
               'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1438069692001.jpg',
               'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1446197241.jpg',
               'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1438504475001.jpg',
               'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1443948582001.jpg',
               'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1443948447001.jpg',
               'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1438609275001.jpg',
               'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1443450411001.jpg',
               'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1447316560.jpg',
               'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1446730136001.jpg',
               'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1448528232.jpg',
               'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1449715350.jpg',
               'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1450323393.jpg',
               'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1451303753002.jpg',
               'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1452670061003.jpg',
               'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1452241842.jpg',
               'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1452240079.jpg',
               'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1453340823.jpg',
               'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1454486633001.jpg',
               'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1455244366.jpg',
               'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1456365727.jpg',
               'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1457511815.jpg',
               'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1458114247.jpg',
               'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1459388397.jpg',
               'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1459389726.jpg',
               'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1460396620001.png']
        sr = ['https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1441894259001.jpg',
              'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1438597307001.jpg',
              'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1447316263.jpg',
              'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1438504579001.jpg',
              'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1438270437001.jpg',
              'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1446197137.jpg',
              'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1441119511007.jpg',
              'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1438437204003.jpg',
              'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1462170022.jpg',
              'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1438437204004.jpg',
              'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/313121/20150905184741VoSl5OS7.jpg',
              'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1447316745.jpg',
              'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1438421577001.jpg',
              'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1440972777001.jpg',
              'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1438398245009.jpg',
              'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1446826434.jpg',
              'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1446814817001.jpg',
              'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1452673431.jpg',
              'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1452662301003.jpg',
              'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1453106229.jpg',
              'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1454486397001.jpg',
              'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1454486282001.jpg',
              'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1457515186.jpg']
        r = ['https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1438398245013.jpg',
             'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1438398245014.jpg',
             'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1438344531001.jpg',
             'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1447315723.jpg',
             'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1438398245011.jpg',
             'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1441715362001.jpg',
             'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1438405142001.jpg',
             'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1438403172001.jpg',
             'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1438543240002.jpg',
             'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1438375302001.jpg',
             'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1438342183001.jpg',
             'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/320264/20150905234129ITkfIHWl.jpg',
             'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1447316526.jpg',
             'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1438266324001.jpg',
             'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1438398245001.jpg',
             'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1438347684001.jpg',
             'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1438602877002.jpg',
             'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1438351316002.jpg',
             'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1439294513001.jpg',
             'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1446729335001.jpg',
             'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1447316010.jpg',
             'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1449649088001.jpg',
             'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1449649218001.jpg',
             'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1452660953001.jpg',
             'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1451303753001.jpg',
             'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1452672586004.jpg',
             'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1457518477.jpg',
             'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1459389297.jpg',
             'https://cdn.img-conv.gamerch.com/img.gamerch.com/fate-go/wikidb_img/1459245557.jpg']

        if message.content.startswith("*summon"):
            rolls = [random.choice(ssr)] * 1 + [random.choice(sr)] * 4 + [random.choice(r)] * 95
            hit = random.choice(rolls)
            if hit in r:
                Rcount += 1
            if hit in sr:
                SRcount += 1
            if hit in ssr:
                SSRcount += 1
            embeded = discord.Embed(title="You Summoned:", color=0x0080ff)
            embeded.set_image(url=hit)
            await message.channel.send(embed=embeded)

        if message.content.startswith('*sumdata'):
            embeded = discord.Embed(title="Fate/Grand Order Simulator Data",description='Rare Servants: ' + str(Rcount) + '\n'+'Super Rare Servants: ' + str(SRcount) + '\n' + 'Super Super Rare Servants: ' + str(SSRcount),color=0x0080ff)
            await message.channel.send(embed=embeded)

        if message.content.startswith('*ccscan'):
            first = message.mentions[0].name
            cc = random.randint(0, 500)
            if cc <= 100:
                second = "CRIME COEFFICIENT: " + str(cc)
                embeded = discord.Embed(title=second, description=first +' is not a threat. Dominator Trigger Locked.', color=0x09FF00)
                embeded.set_image(url='https://gentokyo.moe/wp-content/uploads/2014/09/psycho-pass.gif')
                await message.channel.send(embed=embeded)
            if 100 < cc < 300:
                second = "CRIME COEFFICIENT: " + str(cc)
                embeded = discord.Embed(title=second, description=first +' is a potential latent criminal. Dominator set to Non-Lethal Paralyzer Mode.', color=0x00FFF9)
                embeded.set_image(url='https://66.media.tumblr.com/7cf2246466ed6a26eb5fa9ea9463b3bb/tumblr_nf190nx3bq1qa94xto1_500.gif')
                await message.channel.send(embed=embeded)
            if cc > 300:
                second = "CRIME COEFFICIENT: " + str(cc)
                embeded = discord.Embed(title=second, description=first +' is a serious threat to society. Dominator has been set to Lethal Eliminator Mode.', color=0xFF0000)
                embeded.set_image(url='https://thumbs.gfycat.com/MintyNimbleHousefly-size_restricted.gif')
                await message.channel.send(embed=embeded)

        if message.content.startswith('*love'):
            first = message.mentions[0].name
            second = message.mentions[1].name
            rate = random.randint(0,100)
            embeded = discord.Embed(title=first + ' 💘 ' + second, description='Probability of Romantic Success: ' + str(rate) + '%', color=0xFF0000)
            await message.channel.send(embed=embeded)


        if message.content.startswith('*ask'):
            answer = random.randint(1,10)
            if answer <6:
                embeded = discord.Embed(title='8-BOT says...', color=0x09FF00)
                embeded.set_image(url='https://i.imgur.com/Qgl3Q2K.gif')
                await message.channel.send(embed=embeded)
            else:
                embeded = discord.Embed(title='8-BOT says...', color=0xFF0000)
                embeded.set_image(url='https://i.kym-cdn.com/photos/images/newsfeed/000/960/679/384.gif')
                await message.channel.send(embed=embeded)

client = MyClient()
client.run(TOKEN)

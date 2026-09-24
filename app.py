from flask import Flask, render_template, request,jsonify
import random
app = Flask(__name__)

gamedifficulty = '0'
trials = 3
wordobj = ''
userTypedWord = ''
notify = ''
isGetInput = False

arrEasyWords = [
{
          "Word":'swarm',
          "Hint":"A large group of flying insects, like bees or ants, moving together in a big crowd."
},
{
          "Word":'alarm',
          "Hint":"A loud sound made by a clock or phone to wake you up in the morning."
},
{
          "Word":'sugar',
          "Hint":"A sweet white powder you add to coffee, tea, or baking to make things taste sweet."
},
{
          "Word":'allow',
          "Hint":"To give someone permission to do something, or to say 'yes' to a request."
},
{
          "Word":'swear',
          "Hint":"To use a bad or rude word, or to make a serious promise to tell the truth."
},
{
          "Word":'grave',
          "Hint":"The specific spot in the ground where a person is buried after they die, usually marked with a headstone."
},
{
          "Word":'first',
          "Hint":"Coming before all others in time, order, or importance, like winning number one in a race."
},
{
          "Word":'salon',
          "Hint":" A place you go to get your hair cut, styled, or colored, or to get your nails done."
},
{
          "Word":'lobby',
          "Hint":"The large entrance room or reception area inside a hotel, office building, or theater where people wait."
},
{
          "Word":'ranch',
          "Hint":"A large farm where animals like cattle are raised, or a popular creamy white dressing used for salad and dipping pizza."
},
{
          "Word":'judge',
          "Hint":"The person in a courtroom who makes final decisions, ensures rules are followed, and sometimes wears a long black robe."
},
{
          "Word":'outer',
          "Hint":"Relating to the outside of something, or the far edge of the universe beyond Earth's atmosphere."
},
{
          "Word":'ferry',
          "Hint":"A large boat or ship used to carry passengers, cars, and goods across a body of water on regular short trips."
},
{
          "Word":'crowd',
          "Hint":"A very large number of people gathered together in one place, like at a concert or sports game."
},
{
          "Word":'fight',
          "Hint":"To use physical force, weapons, or words to argue or struggle against someone or something."
},
{
          "Word":'tough',
          "Hint":"Something that is very strong, durable, difficult to break, or a situation that is hard to deal with."
},
{
          "Word":'heart',
          "Hint":"The organ in your chest that pumps blood through your body, or the shape used to represent love on Valentine's Day."
},
{
          "Word":'enfix',
          "Hint":"A rare type of affix that is inserted right inside another word or root to change its meaning."
},
{
          "Word":'ridge',
          "Hint":"A long, narrow raised strip of land, like the crest or chain of hills at the very top of a mountain range."
},
{
          "Word":'agree',
          "Hint":"To have the same opinion as someone else, or to say 'yes' to an idea or plan."
},
{
          "Word":'flash',
          "Hint":"A sudden, brief, and very bright burst of light, like the one from a camera when taking a photo in a dark room."
},
{
          "Word":'snake',
          "Hint":"A long, legless reptile that slithers along the ground and sometimes makes a hissing sound."
},
{
          "Word":'tribe',
          "Hint":"A group of people, often families or communities, who share the same language, culture, history, and a common leader."
},
{
          "Word":'loose',
          "Hint":"Not firmly or tightly fixed in place, like a tooth that is about to fall out or oversized clothes."
},
{
          "Word":'gloom',
          "Hint":"A state of partial or total darkness, or a sad, dark feeling of having no hope."
},
{
          "Word":'flush',
          "Hint":"To push a button or lever on a toilet to clear it out with a sudden rush of water."
},
{
          "Word":'spoil',
          "Hint":"To ruin something completely, or when food goes bad and rots because it was left out too long."
},
{
          "Word":'plead',
          "Hint":"To beg or ask for something in a very serious and emotional way, or to state in a courtroom whether you are guilty or innocent."
},
{
          "Word":'fleet',
          "Hint":"A large group of ships, airplanes, or cars moving together or owned by the same company."
},
{
          "Word":'funny',
          "Hint":"Something that makes you laugh or smile, like a good joke or a comedic movie."
},
{
          "Word":'train',
          "Hint":"A long wheeled vehicle that runs along a metal track and carries passengers or cargo between stations."
},
{
          "Word":'drill',
          "Hint":"A hand-held power tool used to make holes in hard surfaces like walls or wood, or a practice exercise used by sports teams or soldiers."
},
{
          "Word":'fault',
          "Hint":"A mistake or blame for something that goes wrong, or a giant crack in the Earth's crust where earthquakes happen."
},
{
          "Word":'deter',
          "Hint":"To discourage or prevent someone from doing something, often by making them face or realize the negative consequences."
},
{
          "Word":'utter',
          "Hint":"To make a sound with your voice, or to say a word out loud."
},
{
          "Word":'brick',
          "Hint":"A rectangular block of baked clay or concrete used to build walls, houses, and chimneys."
},
{
          "Word":'valid',
          "Hint":" Something that is legally acceptable, true, officially approved, or logically correct (like a password that works)."
},
{
          "Word":'blade',
          "Hint":"The flat, sharp, cutting part of a knife, sword, razor, or pair of scissors."
},

{
          "Word":'crash',
          "Hint":"A violent collision where a car, plane, or object hits something and gets badly damaged, or a sudden, loud noise made by something falling down."
},
{
          "Word":'steam',
          "Hint":"The hot mist or vapor that rises into the air when water boils, like from a hot shower or a boiling pot."
},
{
          "Word":'wreck',
          "Hint":"To completely destroy or ruin something, or the remains of a badly smashed car, ship, or building."
},
{
          "Word":'grain',
          "Hint":"The small, hard seeds harvested from plants like wheat, corn, and rice, which are often ground up to make flour and bread."
},
{
          "Word":'shark',
          "Hint":"A large ocean fish with sharp teeth and a dorsal fin on its back that is known for being a powerful hunter."
},
{
          "Word":'grass',
          "Hint":"The green plant with narrow leaves that covers lawns, fields, and parks, which sheep and cows love to eat."
},
{
          "Word":'ghost',
          "Hint":" The spirit of a dead person that some people believe haunts buildings, often pictured as a spooky floating white sheet."
},
{
          "Word":'sound',
          "Hint":"Something that can be heard by your ears, like music, a voice, or a loud noise."
},
{
          "Word":'scene',
          "Hint":"A single piece or part of a movie, play, or book that happens in one specific time and place."
},



]

arrMediumWords = [
  {
    "Word": "swarm",
    "Hint": "A large group of flying insects, like bees or ants, moving together in a big crowd."
  },
  {
    "Word": "insert",
    "Hint": "To put or push something carefully inside or into something else, like a coin into a vending machine."
  },
  {
    "Word": "dragon",
    "Hint": "A mythical, giant reptile in fantasy stories that can fly and breathe fire."
  },
  {
    "Word": "scheme",
    "Hint": "A large-scale systematic plan or secret plot for achieving a specific goal."
  },
  {
    "Word": "punish",
    "Hint": "To make someone suffer a consequence or penalty because they broke a rule or did something wrong."
  },
  {
    "Word": "agency",
    "Hint": "A business or organization that provides a specific service, like helping people find jobs or rent houses."
  },
  {
    "Word": "ground",
    "Hint": "The solid surface of the Earth that you walk on when you are outside."
  },
  {
    "Word": "system",
    "Hint": "A set of things, rules, or parts working together as a whole network, like your body's digestion or a computer setup."
  },
  {
    "Word": "hammer",
    "Hint": "A hand tool with a heavy metal head used for hitting nails into wood."
  },
  {
    "Word": "script",
    "Hint": "The written text of a play, movie, or broadcast that actors read to know what to say."
  },
  {
    "Word": "smooth",
    "Hint": "Having an even and regular surface without any lumps, bumps, or rough scratches."
  },
  {
    "Word": "listen",
    "Hint": "To give your full attention to a sound or to what someone else is saying with your ears."
  },
  {
    "Word": "peanut",
    "Hint": "A popular oval-shaped nut that grows underground, often eaten salted at baseball games or crushed into a creamy butter."
  },
  {
    "Word": "infect",
    "Hint": "To contaminate a person, animal, or computer with a disease, germ, or malicious virus."
  },
  {
    "Word": "formal",
    "Hint": "Suited for official or important traditional occasions, like wearing a tuxedo or a fancy gown to a gala."
  },
  {
    "Word": "shadow",
    "Hint": "A dark shape cast on a surface when something blocks the light from a lamp or the sun."
  },
  {
    "Word": "modest",
    "Hint": "Not boasting or bragging about your skills or wealth, or wearing simple clothing that doesn't draw too much attention."
  },
  {
    "Word": "notice",
    "Hint": "To become aware of something or see it for the first time, or a written warning sign posted on a wall."
  },
  {
    "Word": "facade",
    "Hint": "The principal front face of a building looking onto a street, or a fake outward appearance used to hide real feelings."
  },
  {
    "Word": "policy",
    "Hint": "A set of official rules or ideas that a company, school, or government agrees to follow."
  },
  {
    "Word": "ballet",
    "Hint": "An artistic type of dance performed on a stage where dancers wear tutus and move gracefully on the tips of their toes."
  },
  {
    "Word": "mirror",
    "Hint": "A reflective glass surface that you look into to see an exact image of yourself."
  },
  {
    "Word": "redeem",
    "Hint": "To trade in a coupon, gift card, or voucher to get a discount, prize, or cash value."
  },
  {
    "Word": "retain",
    "Hint": "To continue to hold, keep, or remember something instead of losing it or letting it go."
  },
  {
    "Word": "mosaic",
    "Hint": "A colorful piece of art made by arranging small pieces of colored stone, tile, or glass into a beautiful pattern."
  },
  {
    "Word": "lonely",
    "Hint": "Feeling sad or unhappy because you are by yourself and have no friends or company around."
  },
  {
    "Word": "career",
    "Hint": "An occupation or profession followed for a significant period of a person's life with opportunities for progress."
  },
  {
    "Word": "broken",
    "Hint": "Damaged, fractured, or split into pieces and no longer working correctly."
  },
  {
    "Word": "source",
    "Hint": "The place, person, or thing where something begins or comes from, like a river's starting point or a news quote."
  },
  {
    "Word": "strike",
    "Hint": "To hit something with force, or when workers refuse to work until they get better pay."
  },
  {
    "Word": "mutter",
    "Hint": "To speak in a very low, quiet, and unclear voice, often when complaining or talking to yourself."
  },
  {
    "Word": "virgin",
    "Hint": "Someone who has never had sexual intercourse, or something that is completely pure, natural, and untouched."
  },
  {
    "Word": "clique",
    "Hint": "A small, exclusive group of friends that doesn't easily allow outsiders to join them."
  },
  {
    "Word": "expose",
    "Hint": "To uncover something hidden so that it can be clearly seen, or to reveal a secret."
  },
  {
    "Word": "museum",
    "Hint": "A public building where interesting historical, scientific, or artistic objects are kept and displayed for people to see."
  },
  {
    "Word": "flavor",
    "Hint": "The distinctive taste of a food or drink in your mouth, like chocolate, vanilla, or strawberry."
  },
  {
    "Word": "narrow",
    "Hint": "Measuring only a very small distance from side to side, like a thin hallway or a tight street."
  },
  {
    "Word": "candle",
    "Hint": "A stick of wax with a central string wick that you light with a match to create a gentle flame."
  },
  {
    "Word": "differ",
    "Hint": "To be unlike or dissimilar from something else, or to hold a completely opposite opinion."
  },
  {
    "Word": "lawyer",
    "Hint": "A professional person whose job is to give legal advice and speak for people in a courtroom."
  },
  {
    "Word": "jockey",
    "Hint": "A professional person who rides horses in races as a career."
  },
  {
    "Word": "winter",
    "Hint": "The coldest season of the year, falling between autumn and spring, often bringing snow and ice."
  },
  {
    "Word": "lesson",
    "Hint": "A period of time where you are taught a specific subject, skill, or moral value by a teacher."
  },
  {
    "Word": "census",
    "Hint": "An official survey or count of a country's population, taken regularly to gather details about the citizens."
  },
  {
    "Word": "global",
    "Hint": "Relating to the entire world or Earth as a whole, rather than just one local area."
  },
  {
    "Word": "latest",
    "Hint": "The most recent, newest, or most modern version of something, like a new smartphone release."
  },
  {
    "Word": "filter",
    "Hint": "A device or software used to remove unwanted parts, like dirt from drinking water or spam emails from an inbox."
  },
  {
    "Word": "subway",
    "Hint": "An underground electric railway system used for transporting passengers across a busy city."
  },
  {
    "Word": "format",
    "Hint": "The way in which something is arranged, organized, or styled, like a layout for a document or code data."
  },
  {
    "Word": "velvet",
    "Hint": "A type of woven fabric that is famous for being incredibly soft, smooth, and luxurious to touch."
  },
  {
    "Word": "ignore",
    "Hint": "To purposely pay no attention to someone or something, acting as if you didn't hear or see them."
  }
]

arrHardWords =[
  {
    "Word": "genetic",
    "Hint": "Relating to genes or DNA, which determines characteristics like eye color passed down from parents to children."
  },
  {
    "Word": "premium",
    "Hint": "An extra amount of money paid for high quality, a special insurance plan, or a version of an app without ads."
  },
  {
    "Word": "quarrel",
    "Hint": "An angry argument or disagreement between people, usually over something small."
  },
  {
    "Word": "failure",
    "Hint": "A lack of success in doing or achieving something, or when a machine completely stops working."
  },
  {
    "Word": "cottage",
    "Hint": "A small, cozy house, typically located in the countryside or near a lake."
  },
  {
    "Word": "grounds",
    "Hint": "The land and gardens surrounding a large building, or the leftover solid pieces at the bottom of a coffee pot."
  },
  {
    "Word": "revival",
    "Hint": "An improvement in the condition or popularity of something, bringing it back to life or style again."
  },
  {
    "Word": "related",
    "Hint": "Belonging to the same family, or having a close logical connection to something else."
  },
  {
    "Word": "sunrise",
    "Hint": "The time in the early morning when the sun first appears in the sky."
  },
  {
    "Word": "pumpkin",
    "Hint": "A large, round orange vegetable that grows on a vine and is carved into a jack-o'-lantern for Halloween."
  },
  {
    "Word": "prevent",
    "Hint": "To stop something from happening or to keep someone from doing an action before it occurs."
  },
  {
    "Word": "dentist",
    "Hint": "A medical professional who specializes in cleaning, fixing, and taking care of your teeth."
  },
  {
    "Word": "tourist",
    "Hint": "A person who travels to a place for pleasure, sightseeing, and vacation instead of business."
  },
  {
    "Word": "complex",
    "Hint": "Something made of many interconnected parts that is complicated and difficult to understand."
  },
  {
    "Word": "missile",
    "Hint": "A powerful explosive weapon that is launched through the air or space toward a target."
  },
  {
    "Word": "comfort",
    "Hint": "A state of physical ease and freedom from pain, or words that make someone feel less sad."
  },
  {
    "Word": "banquet",
    "Hint": "A formal, large dinner or feast for many people, often held to celebrate a special occasion."
  },
  {
    "Word": "pension",
    "Hint": "A regular payment made by the government or a company to a person who has retired from work."
  },
  {
    "Word": "initial",
    "Hint": "Occurring at the very beginning of something, or the first letter of a person's name."
  },
  {
    "Word": "justify",
    "Hint": "To show or prove that a decision, action, or idea is right, fair, or reasonable."
  },
  {
    "Word": "combine",
    "Hint": "To join or mix two or more things together to form a single unit."
  },
  {
    "Word": "fortune",
    "Hint": "A large amount of money and wealth, or the luck that happens to a person."
  },
  {
    "Word": "applaud",
    "Hint": "To show approval or praise by clapping your hands together after a performance."
  },
  {
    "Word": "uniform",
    "Hint": "The special set of matching clothes worn by members of an organization, like soldiers, police, or students."
  },
  {
    "Word": "cluster",
    "Hint": "A small group of similar things growing or gathered closely together, like grapes or stars."
  },
  {
    "Word": "insight",
    "Hint": "A deep, clear, and sudden understanding of a complicated problem or situation."
  },
  {
    "Word": "student",
    "Hint": "A person who is attending a school, college, or university to learn a subject."
  },
  {
    "Word": "storage",
    "Hint": "The space or area where items, furniture, or digital data are kept when they are not being used."
  },
  {
    "Word": "miracle",
    "Hint": "An extraordinary, wonderful event that is completely impossible according to natural laws and is welcomed as an act of God."
  },
  {
    "Word": "element",
    "Hint": "A basic part of a whole system, or a pure chemical substance that cannot be broken down into simpler parts."
  },
  {
    "Word": "publish",
    "Hint": "To prepare and print a book, magazine, or digital article so that it is available to the public."
  },
  {
    "Word": "scholar",
    "Hint": "A specialist or highly educated person who has done advanced study in a particular academic subject."
  },
  {
    "Word": "freight",
    "Hint": "Goods, cargo, or heavy items transported by large trucks, trains, ships, or aircraft."
  },
  {
    "Word": "include",
    "Hint": "To make someone or something part of a group, list, or total package."
  },
  {
    "Word": "capital",
    "Hint": "The most important city or seat of government in a country, or a large uppercase letter used to start a sentence."
  },
  {
    "Word": "drawing",
    "Hint": "A picture or sketch made on paper using a pencil, pen, or crayon rather than paint."
  },
  {
    "Word": "tension",
    "Hint": "A feeling of mental or emotional strain, or the physical tightness of a stretched rope."
  },
  {
    "Word": "abolish",
    "Hint": "To formally put an end to a system, practice, or law, making it illegal."
  },
  {
    "Word": "suggest",
    "Hint": "To put forward an idea, plan, or recommendation for someone to consider."
  },
  {
    "Word": "trouble",
    "Hint": "Problems, difficulties, or worry, or a situation where you face punishment for doing something wrong."
  },
  {
    "Word": "bargain",
    "Hint": "An agreement between two parties, or something bought for a much lower price than its actual value."
  },
  {
    "Word": "arrange",
    "Hint": "To put a collection of objects into a neat, specific order or position."
  },
  {
    "Word": "adviser",
    "Hint": "A person who gives expert advice or recommendations to someone about what they should do."
  },
  {
    "Word": "laundry",
    "Hint": "Clothes, sheets, and towels that need to be washed, or have just been washed."
  },
  {
    "Word": "venture",
    "Hint": "A risky or daring journey, or a new business project that involves a chance of failure."
  },
  {
    "Word": "distort",
    "Hint": "To twist something out of its original shape, or to change facts so they are no longer true."
  },
  {
    "Word": "private",
    "Hint": "Intended for use by only one particular person or group, rather than the general public."
  },
  {
    "Word": "compete",
    "Hint": "To take part in a contest, race, or game against others to win a prize or victory."
  },
  {
    "Word": "veteran",
    "Hint": "A person who has served a long time in the military, or someone with a lot of experience in a job."
  },
  {
    "Word": "routine",
    "Hint": "A sequence of actions or a fixed program that you regularly follow at the same time every day."
  }
]


@app.route('/favicon.ico')
def favicon():
    return '', 204

@app.route('/',methods=['GET', 'POST'])
def home():
    global trials
    trials = 3
    return render_template('index.html')

@app.route('/start-game',methods=['GET', 'POST'])
def startGame():
    global wordobj 
    global trials
    trials = 3
    randName = random.randint(0, len(arrEasyWords)-1)
    wordobj = arrEasyWords[randName]
    data = request.get_json()
    return jsonify({"Request":"Success","Request_Data":data,"Response_Data":{"Words":wordobj,"Trails":trials}})

@app.route('/game-modes',methods=['GET', 'POST'])
def gamemodes():
    global wordobj
    global trials
    trials = 3
    data = request.get_json()
    if data == '0':
        randName = random.randint(0, len(arrEasyWords)-1)
        wordobj = arrEasyWords[randName]
    if data == '1':
        randName = random.randint(0, len(arrMediumWords)-1)
        wordobj = arrMediumWords[randName]
    if data == '2':
        randName = random.randint(0, len(arrHardWords)-1)
        wordobj = arrHardWords[randName]
    return jsonify({"Request":"Success","Request_Data":data,"Response_Data":{"Words":wordobj,"Trails":trials}})

@app.route('/user-data',methods=['GET', 'POST'])
def usertypedData():
    global wordobj
    global trials
    global notify
    data = request.get_json()
    print("Generated Data",wordobj)
    exactWord = list(wordobj["Word"])
    print("show the user typed data ",data["combinedArry"])
    print("Show Current Mode ",data["Current_Mode"])

    match = False

    if trials != -1:
        if data["combinedArry"] == exactWord:
            match = True;
            trials = trials + 1
            notify = "Yes Your Trial Increase Because of Typing Correct Word"
        else:
            match = False;
            trials = trials - 1
            notify = "You Lose Your Trial Because of Typing Wrong Word"
    
    if data["Current_Mode"] == '0':
            randName = random.randint(0, len(arrEasyWords)-1)
            wordobj = arrEasyWords[randName]
    if data["Current_Mode"] == '1':
            randName = random.randint(0, len(arrMediumWords)-1)
            wordobj = arrMediumWords[randName]
    if data["Current_Mode"] == '2':
            randName = random.randint(0, len(arrHardWords)-1)
            wordobj = arrHardWords[randName]
    print("Show Trails Counts ",trials) 

    if trials == 0:
         notify = "You Lose All of Your Trials Becaue of Tying Wrong Words All Time!"
         return jsonify({"Request":"Success","Request_Data":data,"Response_Data":{ "New_Words":None, "Match":match,"Trails":0,"Message":notify,"Lose":True,"Win":False}})

    else:
        if trials == 6:
              notify = "Yes Your Are Win! You Save The Man"
              trials = 3
              return jsonify({"Request":"Success","Request_Data":data,"Response_Data":{ "New_Words":None, "Match":match,"Trails":trials,"Message":notify,"Lose":False,"Win":True}})
        else:
              return jsonify({"Request":"Success","Generate_NUM":"","Request_Data":data,"Response_Data":{ "New_Words":wordobj, "Match":match,"Trails":trials,"Message":notify,"Lose":False,"Win":False}})
     
if __name__ == "__main__":
     app.run(debug=True, port=8040) 
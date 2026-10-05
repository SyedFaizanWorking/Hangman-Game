from flask import Flask, render_template, request,jsonify
import random
app = Flask(__name__)

gamedifficulty = '0'
trials = 3
wordobj = ''
userTypedWord = ''
notify = ''
isGetInput = False


# arrEasyWords = [
#   {
#     "Word": "apple",
#     "Hint": "A round fruit that can be red, green, or yellow and grows on trees."
#   },
#   {
#     "Word": "bread",
#     "Hint": "A baked food made from flour that people commonly eat with meals."
#   },
#   {
#     "Word": "chair",
#     "Hint": "A piece of furniture made for one person to sit on."
#   },
#   {
#     "Word": "table",
#     "Hint": "A piece of furniture with a flat top and legs used for eating or working."
#   },
#   {
#     "Word": "house",
#     "Hint": "A building where people live, sleep, cook, and relax."
#   },
#   {
#     "Word": "water",
#     "Hint": "A clear liquid that people, animals, and plants need to survive."
#   },
#   {
#     "Word": "earth",
#     "Hint": "The planet where humans, animals, and plants live."
#   },
#   {
#     "Word": "cloud",
#     "Hint": "A white or gray mass in the sky made from tiny water droplets."
#   },
#   {
#     "Word": "plant",
#     "Hint": "A living thing that grows in soil and usually has roots, stems, and leaves."
#   },
#   {
#     "Word": "grass",
#     "Hint": "A green plant that commonly covers lawns, fields, and gardens."
#   },
#   {
#     "Word": "green",
#     "Hint": "The color commonly seen on leaves and grass."
#   },
#   {
#     "Word": "black",
#     "Hint": "A very dark color like the night sky."
#   },
#   {
#     "Word": "white",
#     "Hint": "A bright color like snow, milk, or a clean sheet of paper."
#   },
#   {
#     "Word": "brown",
#     "Hint": "An earthy color commonly seen in soil, wood, and tree trunks."
#   },
#   {
#     "Word": "happy",
#     "Hint": "A feeling you have when you are joyful, pleased, or having a good time."
#   },
#   {
#     "Word": "angry",
#     "Hint": "A strong feeling you may have when something upsetting happens."
#   },
#   {
#     "Word": "smile",
#     "Hint": "The happy expression you make by moving the corners of your mouth upward."
#   },
#   {
#     "Word": "laugh",
#     "Hint": "The sound or action people make when something is very funny."
#   },
#   {
#     "Word": "heart",
#     "Hint": "An organ that pumps blood around your body and is also a symbol of love."
#   },
#   {
#     "Word": "brain",
#     "Hint": "The organ inside your head that helps you think, learn, and remember."
#   },
#   {
#     "Word": "blood",
#     "Hint": "The red liquid that travels through your body and carries oxygen."
#   },
#   {
#     "Word": "mouth",
#     "Hint": "The part of your face used for eating, drinking, speaking, and smiling."
#   },
#   {
#     "Word": "teeth",
#     "Hint": "The hard white parts inside your mouth that help you bite and chew food."
#   },
#   {
#     "Word": "child",
#     "Hint": "A young human who is not yet an adult."
#   },
#   {
#     "Word": "woman",
#     "Hint": "An adult female human."
#   },
#   {
#     "Word": "class",
#     "Hint": "A group of students learning together or a lesson taught by a teacher."
#   },
#   {
#     "Word": "teach",
#     "Hint": "To help someone learn something by explaining or showing them."
#   },
#   {
#     "Word": "study",
#     "Hint": "To spend time learning about a subject by reading or practicing."
#   },
#   {
#     "Word": "paper",
#     "Hint": "A thin material commonly used for writing, drawing, and printing."
#   },
#   {
#     "Word": "clock",
#     "Hint": "A device that shows the current time."
#   },
#   {
#     "Word": "watch",
#     "Hint": "A small clock that is usually worn on the wrist."
#   },
#   {
#     "Word": "phone",
#     "Hint": "An electronic device used for calling, messaging, taking photos, and using apps."
#   },
#   {
#     "Word": "mouse",
#     "Hint": "A small computer device that you move with your hand to control the pointer."
#   },
#   {
#     "Word": "music",
#     "Hint": "Sounds arranged together that people enjoy listening to."
#   },
#   {
#     "Word": "radio",
#     "Hint": "A device or service used to listen to music, news, and broadcasts."
#   },
#   {
#     "Word": "movie",
#     "Hint": "A recorded story or show that you watch on a screen."
#   },
#   {
#     "Word": "video",
#     "Hint": "A recording of moving pictures that can be watched on a screen."
#   },
#   {
#     "Word": "photo",
#     "Hint": "A picture taken with a camera or phone."
#   },
#   {
#     "Word": "sport",
#     "Hint": "A physical game or activity played for exercise or competition."
#   },
#   {
#     "Word": "beach",
#     "Hint": "A sandy or rocky area beside the sea or ocean."
#   },
#   {
#     "Word": "river",
#     "Hint": "A natural stream of flowing water that usually moves toward a lake or sea."
#   },
#   {
#     "Word": "ocean",
#     "Hint": "A huge area of salty water that covers much of the Earth's surface."
#   },
#   {
#     "Word": "islet",
#     "Hint": "A very small island surrounded by water."
#   },
#   {
#     "Word": "world",
#     "Hint": "The Earth and everything that exists on it."
#   },
#   {
#     "Word": "space",
#     "Hint": "The vast area beyond Earth where stars, planets, and galaxies are found."
#   },
#   {
#     "Word": "light",
#     "Hint": "Something that allows you to see objects around you."
#   },
#   {
#     "Word": "night",
#     "Hint": "The dark part of the day when the sun is not visible."
#   },
#   {
#     "Word": "sleep",
#     "Hint": "The natural resting state when your body and brain recover."
#   },
#   {
#     "Word": "dream",
#     "Hint": "A series of images or thoughts that you may experience while sleeping."
#   },
#   {
#     "Word": "roomy",
#     "Hint": "A word describing a place that has plenty of space inside."
#   },
#   {
#     "Word": "floor",
#     "Hint": "The flat surface inside a building that you walk on."
#   },
#   {
#     "Word": "spoon",
#     "Hint": "A utensil with a rounded end used for eating or serving food."
#   },
#   {
#     "Word": "plate",
#     "Hint": "A flat dish used for serving and eating food."
#   },
#   {
#     "Word": "glass",
#     "Hint": "A container commonly used for drinking water or other liquids."
#   },
#   {
#     "Word": "pizza",
#     "Hint": "A round baked food usually covered with sauce, cheese, and toppings."
#   },
#   {
#     "Word": "mango",
#     "Hint": "A sweet tropical fruit with juicy flesh and one large seed."
#   },
#   {
#     "Word": "grape",
#     "Hint": "A small round fruit that grows in bunches and can be green, red, or purple."
#   },
#   {
#     "Word": "lemon",
#     "Hint": "A yellow citrus fruit with a very sour taste."
#   },
#   {
#     "Word": "peach",
#     "Hint": "A soft sweet fruit with fuzzy skin and a large seed inside."
#   },
#   {
#     "Word": "guava",
#     "Hint": "A tropical fruit that can have green skin and pink or white flesh."
#   },
#   {
#     "Word": "melon",
#     "Hint": "A large juicy fruit with sweet flesh and seeds inside."
#   },
#   {
#     "Word": "olive",
#     "Hint": "A small oval fruit that can be green or black and is also used to make oil."
#   },
#   {
#     "Word": "onion",
#     "Hint": "A vegetable with many layers that is commonly used to add flavor to food."
#   },
#   {
#     "Word": "beans",
#     "Hint": "Small edible seeds that are commonly cooked and used in many meals."
#   },
#   {
#     "Word": "honey",
#     "Hint": "A sweet golden food made by bees from flower nectar."
#   },
#   {
#     "Word": "sugar",
#     "Hint": "A sweet substance commonly added to tea, desserts, and other foods."
#   },
#   {
#     "Word": "spice",
#     "Hint": "An ingredient used in small amounts to add flavor to food."
#   },
#   {
#     "Word": "horse",
#     "Hint": "A large four-legged animal that people can ride."
#   },
#   {
#     "Word": "tiger",
#     "Hint": "A large wild cat with orange fur and black stripes."
#   },
#   {
#     "Word": "zebra",
#     "Hint": "A wild animal that looks like a horse and has black-and-white stripes."
#   },
#   {
#     "Word": "sheep",
#     "Hint": "A farm animal covered in wool that is often raised for wool and meat."
#   },
#   {
#     "Word": "goose",
#     "Hint": "A large bird with a long neck that can make a loud honking sound."
#   },
#   {
#     "Word": "snake",
#     "Hint": "A long animal with no legs that moves by sliding along the ground."
#   },
#   {
#     "Word": "whale",
#     "Hint": "A huge animal that lives in the ocean and breathes air through a blowhole."
#   },
#   {
#     "Word": "shark",
#     "Hint": "A large fish that lives in the ocean and has sharp teeth."
#   },
#   {
#     "Word": "eagle",
#     "Hint": "A large bird of prey with strong wings, sharp claws, and excellent eyesight."
#   },
#   {
#     "Word": "meaty",
#     "Hint": "A word describing food that contains a lot of meat."
#   },
#   {
#     "Word": "spicy",
#     "Hint": "A word describing food that has a hot or burning taste."
#   },
#   {
#     "Word": "sweet",
#     "Hint": "A word describing a sugary taste like candy, honey, or ripe fruit."
#   },
#   {
#     "Word": "salty",
#     "Hint": "A word describing food that tastes strongly of salt."
#   },
#   {
#     "Word": "fresh",
#     "Hint": "A word describing food that is new, recently prepared, or not spoiled."
#   },
#   {
#     "Word": "clean",
#     "Hint": "A word describing something without dirt, dust, or mess."
#   },
#   {
#     "Word": "dirty",
#     "Hint": "A word describing something covered with dirt or not clean."
#   },
#   {
#     "Word": "small",
#     "Hint": "A word describing something that is little in size."
#   },
#   {
#     "Word": "large",
#     "Hint": "A word describing something that is big in size."
#   },
#   {
#     "Word": "quick",
#     "Hint": "A word describing something that happens or moves fast."
#   },
#   {
#     "Word": "quiet",
#     "Hint": "A word describing a place or situation with very little noise."
#   },
#   {
#     "Word": "funny",
#     "Hint": "A word describing something that makes people laugh."
#   },
#   {
#     "Word": "brave",
#     "Hint": "A word describing someone who is willing to face danger without giving up."
#   },
#   {
#     "Word": "smart",
#     "Hint": "A word describing someone who is good at learning and understanding things."
#   },
#   {
#     "Word": "young",
#     "Hint": "A word describing someone or something that has lived for a short time."
#   },
#   {
#     "Word": "older",
#     "Hint": "A word used to describe someone or something with more age than another."
#   },
#   {
#     "Word": "river",
#     "Hint": "A natural flow of water that moves through land toward another body of water."
#   },
#   {
#     "Word": "storm",
#     "Hint": "A period of bad weather that can bring strong wind, rain, thunder, or lightning."
#   },
#   {
#     "Word": "rainy",
#     "Hint": "A word describing weather in which rain is falling or expected."
#   },
#   {
#     "Word": "sunny",
#     "Hint": "A word describing weather when the sun is shining brightly."
#   },
#   {
#     "Word": "windy",
#     "Hint": "A word describing weather with a lot of moving air."
#   },
#   {
#     "Word": "frost",
#     "Hint": "A thin layer of ice that forms on cold surfaces."
#   },
#   {
#     "Word": "flame",
#     "Hint": "The bright, hot part of a fire that you can see."
#   },
#   {
#     "Word": "smoke",
#     "Hint": "The gray or white cloud produced when something burns."
#   },
#   {
#     "Word": "stone",
#     "Hint": "A small piece of hard natural rock."
#   },
#   {
#     "Word": "metal",
#     "Hint": "A hard material such as iron, copper, or aluminum used to make many objects."
#   },
#   {
#     "Word": "glass",
#     "Hint": "A hard transparent material often used for windows and bottles."
#   },
#   {
#     "Word": "wooden",
#     "Hint": "Made from wood, such as a table, chair, or door."
#   },
#   {
#     "Word": "truck",
#     "Hint": "A large road vehicle used for carrying goods or heavy objects."
#   },
#   {
#     "Word": "train",
#     "Hint": "A long vehicle made of connected cars that travels on railway tracks."
#   },
#   {
#     "Word": "plane",
#     "Hint": "A flying vehicle with wings that carries people through the air."
#   },
#   {
#     "Word": "bikes",
#     "Hint": "Two-wheeled vehicles that people ride by turning pedals."
#   },
#   {
#     "Word": "motor",
#     "Hint": "A machine that uses energy to produce movement."
#   },
#   {
#     "Word": "brass",
#     "Hint": "A yellow-colored metal made mainly by mixing copper and zinc."
#   },
#   {
#     "Word": "golds",
#     "Hint": "A word referring to things made of or related to the valuable yellow metal."
#   }
# ]


arrEasyWords = [
  {
    "Word": "apple",
    "Hint": "A round fruit that can be red, green, or yellow and grows on trees.",
    "UrduHint": "ایک گول پھل جو سرخ، سبز یا پیلا ہو سکتا ہے اور درختوں پر اگتا ہے۔"
  },
  {
    "Word": "bread",
    "Hint": "A baked food made from flour that people commonly eat with meals.",
    "UrduHint": "آٹے سے بنی ہوئی پکی ہوئی غذا جسے لوگ عام طور پر کھانوں کے ساتھ کھاتے ہیں۔"
  },
  {
    "Word": "chair",
    "Hint": "A piece of furniture made for one person to sit on.",
    "UrduHint": "فرنیچر کی ایک چیز جس پر ایک شخص بیٹھنے کے لیے استعمال کرتا ہے۔"
  },
  {
    "Word": "table",
    "Hint": "A piece of furniture with a flat top and legs used for eating or working.",
    "UrduHint": "فرنیچر کی ایک چیز جس کا اوپر والا حصہ ہموار اور ٹانگیں ہوتی ہیں، جسے کھانے یا کام کرنے کے لیے استعمال کیا جاتا ہے۔"
  },
  {
    "Word": "house",
    "Hint": "A building where people live, sleep, cook, and relax.",
    "UrduHint": "ایک عمارت جہاں لوگ رہتے، سوتے، کھانا پکاتے اور آرام کرتے ہیں۔"
  },
  {
    "Word": "water",
    "Hint": "A clear liquid that people, animals, and plants need to survive.",
    "UrduHint": "ایک صاف مائع جس کی انسانوں، جانوروں اور پودوں کو زندہ رہنے کے لیے ضرورت ہوتی ہے۔"
  },
  {
    "Word": "earth",
    "Hint": "The planet where humans, animals, and plants live.",
    "UrduHint": "وہ سیارہ جہاں انسان، جانور اور پودے رہتے ہیں۔"
  },
  {
    "Word": "cloud",
    "Hint": "A white or gray mass in the sky made from tiny water droplets.",
    "UrduHint": "آسمان میں سفید یا سرمئی رنگ کا ایک مجموعہ جو پانی کے ننھے قطروں سے بنتا ہے۔"
  },
  {
    "Word": "plant",
    "Hint": "A living thing that grows in soil and usually has roots, stems, and leaves.",
    "UrduHint": "ایک جاندار چیز جو مٹی میں اگتی ہے اور عام طور پر اس کی جڑیں، تنا اور پتے ہوتے ہیں۔"
  },
  {
    "Word": "grass",
    "Hint": "A green plant that commonly covers lawns, fields, and gardens.",
    "UrduHint": "ایک سبز پودا جو عام طور پر لان، کھیتوں اور باغات کو ڈھانپتا ہے۔"
  },
  {
    "Word": "green",
    "Hint": "The color commonly seen on leaves and grass.",
    "UrduHint": "وہ رنگ جو عام طور پر پتوں اور گھاس پر نظر آتا ہے۔"
  },
  {
    "Word": "black",
    "Hint": "A very dark color like the night sky.",
    "UrduHint": "ایک بہت گہرا رنگ، جیسے رات کا آسمان۔"
  },
  {
    "Word": "white",
    "Hint": "A bright color like snow, milk, or a clean sheet of paper.",
    "UrduHint": "ایک روشن رنگ، جیسے برف، دودھ یا کاغذ کی صاف شیٹ۔"
  },
  {
    "Word": "brown",
    "Hint": "An earthy color commonly seen in soil, wood, and tree trunks.",
    "UrduHint": "مٹی جیسا رنگ جو عام طور پر مٹی، لکڑی اور درختوں کے تنوں میں نظر آتا ہے۔"
  },
  {
    "Word": "happy",
    "Hint": "A feeling you have when you are joyful, pleased, or having a good time.",
    "UrduHint": "وہ احساس جو خوشی، اطمینان یا اچھا وقت گزارنے کے وقت ہوتا ہے۔"
  },
  {
    "Word": "angry",
    "Hint": "A strong feeling you may have when something upsetting happens.",
    "UrduHint": "ایک شدید احساس جو کسی پریشان کن بات کے ہونے پر آپ کو ہو سکتا ہے۔"
  },
  {
    "Word": "smile",
    "Hint": "The happy expression you make by moving the corners of your mouth upward.",
    "UrduHint": "وہ خوشگوار تاثر جو آپ منہ کے کناروں کو اوپر اٹھا کر بناتے ہیں۔"
  },
  {
    "Word": "laugh",
    "Hint": "The sound or action people make when something is very funny.",
    "UrduHint": "وہ آواز یا عمل جو لوگ کسی بہت مزاحیہ بات پر کرتے ہیں۔"
  },
  {
    "Word": "heart",
    "Hint": "An organ that pumps blood around your body and is also a symbol of love.",
    "UrduHint": "ایک عضو جو جسم میں خون پمپ کرتا ہے اور محبت کی علامت بھی ہے۔"
  },
  {
    "Word": "brain",
    "Hint": "The organ inside your head that helps you think, learn, and remember.",
    "UrduHint": "آپ کے سر کے اندر موجود وہ عضو جو سوچنے، سیکھنے اور یاد رکھنے میں مدد کرتا ہے۔"
  },
  {
    "Word": "blood",
    "Hint": "The red liquid that travels through your body and carries oxygen.",
    "UrduHint": "سرخ مائع جو جسم میں گردش کرتا ہے اور آکسیجن لے جاتا ہے۔"
  },
  {
    "Word": "mouth",
    "Hint": "The part of your face used for eating, drinking, speaking, and smiling.",
    "UrduHint": "چہرے کا وہ حصہ جسے کھانے، پینے، بولنے اور مسکرانے کے لیے استعمال کیا جاتا ہے۔"
  },
  {
    "Word": "teeth",
    "Hint": "The hard white parts inside your mouth that help you bite and chew food.",
    "UrduHint": "منہ کے اندر موجود سخت سفید حصے جو کھانا کاٹنے اور چبانے میں مدد کرتے ہیں۔"
  },
  {
    "Word": "child",
    "Hint": "A young human who is not yet an adult.",
    "UrduHint": "ایک کم عمر انسان جو ابھی بالغ نہیں ہوا۔"
  },
  {
    "Word": "woman",
    "Hint": "An adult female human.",
    "UrduHint": "ایک بالغ عورت۔"
  },
  {
    "Word": "class",
    "Hint": "A group of students learning together or a lesson taught by a teacher.",
    "UrduHint": "طلبہ کا ایک گروپ جو مل کر سیکھتا ہے یا استاد کی پڑھائی ہوئی ایک کلاس۔"
  },
  {
    "Word": "teach",
    "Hint": "To help someone learn something by explaining or showing them.",
    "UrduHint": "کسی چیز کو سمجھا کر یا دکھا کر کسی کو سیکھنے میں مدد دینا۔"
  },
  {
    "Word": "study",
    "Hint": "To spend time learning about a subject by reading or practicing.",
    "UrduHint": "پڑھنے یا مشق کرنے کے ذریعے کسی مضمون کو سیکھنے میں وقت گزارنا۔"
  },
  {
    "Word": "paper",
    "Hint": "A thin material commonly used for writing, drawing, and printing.",
    "UrduHint": "ایک پتلا مواد جو عام طور پر لکھنے، ڈرائنگ کرنے اور پرنٹنگ کے لیے استعمال ہوتا ہے۔"
  },
  {
    "Word": "clock",
    "Hint": "A device that shows the current time.",
    "UrduHint": "ایک آلہ جو موجودہ وقت بتاتا ہے۔"
  },
  {
    "Word": "watch",
    "Hint": "A small clock that is usually worn on the wrist.",
    "UrduHint": "ایک چھوٹی گھڑی جو عام طور پر کلائی پر پہنی جاتی ہے۔"
  },
  {
    "Word": "phone",
    "Hint": "An electronic device used for calling, messaging, taking photos, and using apps.",
    "UrduHint": "ایک الیکٹرانک آلہ جو کال کرنے، پیغامات بھیجنے، تصاویر لینے اور ایپس استعمال کرنے کے لیے استعمال ہوتا ہے۔"
  },
  {
    "Word": "mouse",
    "Hint": "A small computer device that you move with your hand to control the pointer.",
    "UrduHint": "کمپیوٹر کا ایک چھوٹا آلہ جسے ہاتھ سے حرکت دے کر پوائنٹر کو کنٹرول کیا جاتا ہے۔"
  },
  {
    "Word": "music",
    "Hint": "Sounds arranged together that people enjoy listening to.",
    "UrduHint": "آوازوں کو اس طرح ترتیب دینا جنہیں لوگ سننا پسند کرتے ہیں۔"
  },
  {
    "Word": "radio",
    "Hint": "A device or service used to listen to music, news, and broadcasts.",
    "UrduHint": "ایک آلہ یا سروس جسے موسیقی، خبریں اور نشریات سننے کے لیے استعمال کیا جاتا ہے۔"
  },
  {
    "Word": "movie",
    "Hint": "A recorded story or show that you watch on a screen.",
    "UrduHint": "ایک ریکارڈ شدہ کہانی یا شو جسے آپ اسکرین پر دیکھتے ہیں۔"
  },
  {
    "Word": "video",
    "Hint": "A recording of moving pictures that can be watched on a screen.",
    "UrduHint": "حرکت کرتی ہوئی تصاویر کی ریکارڈنگ جسے اسکرین پر دیکھا جا سکتا ہے۔"
  },
  {
    "Word": "photo",
    "Hint": "A picture taken with a camera or phone.",
    "UrduHint": "کیمرے یا فون سے لی گئی تصویر۔"
  },
  {
    "Word": "sport",
    "Hint": "A physical game or activity played for exercise or competition.",
    "UrduHint": "ایک جسمانی کھیل یا سرگرمی جو ورزش یا مقابلے کے لیے کی جاتی ہے۔"
  },
  {
    "Word": "beach",
    "Hint": "A sandy or rocky area beside the sea or ocean.",
    "UrduHint": "سمندر کے کنارے موجود ریت یا پتھروں والا علاقہ۔"
  },
  {
    "Word": "river",
    "Hint": "A natural stream of flowing water that usually moves toward a lake or sea.",
    "UrduHint": "بہتے ہوئے پانی کا قدرتی دھارا جو عام طور پر جھیل یا سمندر کی طرف جاتا ہے۔"
  },
  {
    "Word": "ocean",
    "Hint": "A huge area of salty water that covers much of the Earth's surface.",
    "UrduHint": "نمکین پانی کا ایک بہت بڑا علاقہ جو زمین کی سطح کے بڑے حصے کو ڈھانپتا ہے۔"
  },
  {
    "Word": "islet",
    "Hint": "A very small island surrounded by water.",
    "UrduHint": "پانی سے گھرا ہوا ایک بہت چھوٹا جزیرہ۔"
  },
  {
    "Word": "world",
    "Hint": "The Earth and everything that exists on it.",
    "UrduHint": "زمین اور اس پر موجود ہر چیز۔"
  },
  {
    "Word": "space",
    "Hint": "The vast area beyond Earth where stars, planets, and galaxies are found.",
    "UrduHint": "زمین سے باہر پھیلا ہوا وسیع علاقہ جہاں ستارے، سیارے اور کہکشائیں موجود ہیں۔"
  },
  {
    "Word": "light",
    "Hint": "Something that allows you to see objects around you.",
    "UrduHint": "ایسی چیز جو آپ کو اپنے اردگرد موجود چیزیں دیکھنے کے قابل بناتی ہے۔"
  },
  {
    "Word": "night",
    "Hint": "The dark part of the day when the sun is not visible.",
    "UrduHint": "دن کا وہ تاریک حصہ جب سورج نظر نہیں آتا۔"
  },
  {
    "Word": "sleep",
    "Hint": "The natural resting state when your body and brain recover.",
    "UrduHint": "آرام کی قدرتی حالت جس میں آپ کا جسم اور دماغ بحال ہوتے ہیں۔"
  },
  {
    "Word": "dream",
    "Hint": "A series of images or thoughts that you may experience while sleeping.",
    "UrduHint": "تصاویر یا خیالات کا ایک سلسلہ جس کا تجربہ آپ نیند کے دوران کر سکتے ہیں۔"
  },
  {
    "Word": "roomy",
    "Hint": "A word describing a place that has plenty of space inside.",
    "UrduHint": "ایسی جگہ کو بیان کرنے والا لفظ جس کے اندر کافی زیادہ جگہ ہو۔"
  },
  {
    "Word": "floor",
    "Hint": "The flat surface inside a building that you walk on.",
    "UrduHint": "عمارت کے اندر موجود ہموار سطح جس پر آپ چلتے ہیں۔"
  },
  {
    "Word": "spoon",
    "Hint": "A utensil with a rounded end used for eating or serving food.",
    "UrduHint": "ایک برتن جس کا سرا گول ہوتا ہے اور اسے کھانے یا کھانا پیش کرنے کے لیے استعمال کیا جاتا ہے۔"
  },
  {
    "Word": "plate",
    "Hint": "A flat dish used for serving and eating food.",
    "UrduHint": "ایک چپٹی پلیٹ جس میں کھانا پیش کیا اور کھایا جاتا ہے۔"
  },
  {
    "Word": "glass",
    "Hint": "A container commonly used for drinking water or other liquids.",
    "UrduHint": "ایک برتن جو عام طور پر پانی یا دیگر مائعات پینے کے لیے استعمال ہوتا ہے۔"
  },
  {
    "Word": "pizza",
    "Hint": "A round baked food usually covered with sauce, cheese, and toppings.",
    "UrduHint": "ایک گول پکی ہوئی غذا جس پر عام طور پر ساس، پنیر اور مختلف ٹاپنگز ہوتی ہیں۔"
  },
  {
    "Word": "mango",
    "Hint": "A sweet tropical fruit with juicy flesh and one large seed.",
    "UrduHint": "ایک میٹھا اشنکٹبندیی پھل جس کا گودا رس دار اور ایک بڑی گٹھلی ہوتی ہے۔"
  },
  {
    "Word": "grape",
    "Hint": "A small round fruit that grows in bunches and can be green, red, or purple.",
    "UrduHint": "ایک چھوٹا گول پھل جو گچھوں میں اگتا ہے اور سبز، سرخ یا جامنی ہو سکتا ہے۔"
  },
  {
    "Word": "lemon",
    "Hint": "A yellow citrus fruit with a very sour taste.",
    "UrduHint": "ایک پیلا ترش پھل جس کا ذائقہ بہت کھٹا ہوتا ہے۔"
  },
  {
    "Word": "peach",
    "Hint": "A soft sweet fruit with fuzzy skin and a large seed inside.",
    "UrduHint": "ایک نرم میٹھا پھل جس کے چھلکے پر باریک روئیں اور اندر ایک بڑی گٹھلی ہوتی ہے۔"
  },
  {
    "Word": "guava",
    "Hint": "A tropical fruit that can have green skin and pink or white flesh.",
    "UrduHint": "ایک اشنکٹبندیی پھل جس کا چھلکا سبز اور گودا گلابی یا سفید ہو سکتا ہے۔"
  },
  {
    "Word": "melon",
    "Hint": "A large juicy fruit with sweet flesh and seeds inside.",
    "UrduHint": "ایک بڑا رس دار پھل جس کا گودا میٹھا اور اندر بیج ہوتے ہیں۔"
  },
  {
    "Word": "olive",
    "Hint": "A small oval fruit that can be green or black and is also used to make oil.",
    "UrduHint": "ایک چھوٹا بیضوی پھل جو سبز یا سیاہ ہو سکتا ہے اور اس سے تیل بھی بنایا جاتا ہے۔"
  },
  {
    "Word": "onion",
    "Hint": "A vegetable with many layers that is commonly used to add flavor to food.",
    "UrduHint": "ایک سبزی جس کی کئی تہیں ہوتی ہیں اور اسے عام طور پر کھانے میں ذائقہ شامل کرنے کے لیے استعمال کیا جاتا ہے۔"
  },
  {
    "Word": "beans",
    "Hint": "Small edible seeds that are commonly cooked and used in many meals.",
    "UrduHint": "چھوٹے کھانے کے قابل بیج جو عام طور پر پکائے جاتے ہیں اور بہت سے کھانوں میں استعمال ہوتے ہیں۔"
  },
  {
    "Word": "honey",
    "Hint": "A sweet golden food made by bees from flower nectar.",
    "UrduHint": "ایک میٹھی سنہری غذا جو شہد کی مکھیاں پھولوں کے رس سے بناتی ہیں۔"
  },
  {
    "Word": "sugar",
    "Hint": "A sweet substance commonly added to tea, desserts, and other foods.",
    "UrduHint": "ایک میٹھی چیز جو عام طور پر چائے، میٹھے اور دیگر کھانوں میں شامل کی جاتی ہے۔"
  },
  {
    "Word": "spice",
    "Hint": "An ingredient used in small amounts to add flavor to food.",
    "UrduHint": "ایک جزو جو کھانے میں ذائقہ شامل کرنے کے لیے تھوڑی مقدار میں استعمال کیا جاتا ہے۔"
  },
  {
    "Word": "horse",
    "Hint": "A large four-legged animal that people can ride.",
    "UrduHint": "ایک بڑا چار ٹانگوں والا جانور جس پر لوگ سواری کر سکتے ہیں۔"
  },
  {
    "Word": "tiger",
    "Hint": "A large wild cat with orange fur and black stripes.",
    "UrduHint": "ایک بڑی جنگلی بلی جس کی نارنجی کھال پر کالی دھاریاں ہوتی ہیں۔"
  },
  {
    "Word": "zebra",
    "Hint": "A wild animal that looks like a horse and has black-and-white stripes.",
    "UrduHint": "ایک جنگلی جانور جو گھوڑے جیسا نظر آتا ہے اور اس کے جسم پر کالی اور سفید دھاریاں ہوتی ہیں۔"
  },
  {
    "Word": "sheep",
    "Hint": "A farm animal covered in wool that is often raised for wool and meat.",
    "UrduHint": "ایک پالتو جانور جس کے جسم پر اون ہوتی ہے اور اسے اکثر اون اور گوشت کے لیے پالا جاتا ہے۔"
  },
  {
    "Word": "goose",
    "Hint": "A large bird with a long neck that can make a loud honking sound.",
    "UrduHint": "ایک بڑا پرندہ جس کی گردن لمبی ہوتی ہے اور جو اونچی آواز میں غوں غوں کر سکتا ہے۔"
  },
  {
    "Word": "snake",
    "Hint": "A long animal with no legs that moves by sliding along the ground.",
    "UrduHint": "ایک لمبا جانور جس کی ٹانگیں نہیں ہوتیں اور جو زمین پر رینگ کر حرکت کرتا ہے۔"
  },
  {
    "Word": "whale",
    "Hint": "A huge animal that lives in the ocean and breathes air through a blowhole.",
    "UrduHint": "ایک بہت بڑا جانور جو سمندر میں رہتا ہے اور سانس لینے کے لیے اپنے سر کے سوراخ سے ہوا خارج کرتا ہے۔"
  },
  {
    "Word": "shark",
    "Hint": "A large fish that lives in the ocean and has sharp teeth.",
    "UrduHint": "ایک بڑی مچھلی جو سمندر میں رہتی ہے اور اس کے تیز دانت ہوتے ہیں۔"
  },
  {
    "Word": "eagle",
    "Hint": "A large bird of prey with strong wings, sharp claws, and excellent eyesight.",
    "UrduHint": "ایک بڑا شکاری پرندہ جس کے مضبوط پر، تیز پنجے اور بہترین نظر ہوتی ہے۔"
  },
  {
    "Word": "meaty",
    "Hint": "A word describing food that contains a lot of meat.",
    "UrduHint": "ایسا لفظ جو ایسی غذا کو بیان کرتا ہے جس میں بہت زیادہ گوشت ہو۔"
  },
  {
    "Word": "spicy",
    "Hint": "A word describing food that has a hot or burning taste.",
    "UrduHint": "ایسا لفظ جو ایسی غذا کو بیان کرتا ہے جس کا ذائقہ تیز یا جلن والا ہو۔"
  },
  {
    "Word": "sweet",
    "Hint": "A word describing a sugary taste like candy, honey, or ripe fruit.",
    "UrduHint": "ایسا لفظ جو چینی، شہد یا پکے ہوئے پھل جیسے میٹھے ذائقے کو بیان کرتا ہے۔"
  },
  {
    "Word": "salty",
    "Hint": "A word describing food that tastes strongly of salt.",
    "UrduHint": "ایسا لفظ جو ایسی غذا کو بیان کرتا ہے جس میں نمک کا ذائقہ زیادہ ہو۔"
  },
  {
    "Word": "fresh",
    "Hint": "A word describing food that is new, recently prepared, or not spoiled.",
    "UrduHint": "ایسا لفظ جو ایسی غذا کو بیان کرتا ہے جو تازہ، ابھی تیار کی گئی یا خراب نہ ہوئی ہو۔"
  },
  {
    "Word": "clean",
    "Hint": "A word describing something without dirt, dust, or mess.",
    "UrduHint": "ایسا لفظ جو ایسی چیز کو بیان کرتا ہے جس پر مٹی، گرد یا گندگی نہ ہو۔"
  },
  {
    "Word": "dirty",
    "Hint": "A word describing something covered with dirt or not clean.",
    "UrduHint": "ایسا لفظ جو ایسی چیز کو بیان کرتا ہے جو مٹی سے بھری ہوئی یا صاف نہ ہو۔"
  },
  {
    "Word": "small",
    "Hint": "A word describing something that is little in size.",
    "UrduHint": "ایسا لفظ جو کسی چھوٹی جسامت والی چیز کو بیان کرتا ہے۔"
  },
  {
    "Word": "large",
    "Hint": "A word describing something that is big in size.",
    "UrduHint": "ایسا لفظ جو کسی بڑی جسامت والی چیز کو بیان کرتا ہے۔"
  },
  {
    "Word": "quick",
    "Hint": "A word describing something that happens or moves fast.",
    "UrduHint": "ایسا لفظ جو کسی تیزی سے ہونے یا حرکت کرنے والی چیز کو بیان کرتا ہے۔"
  },
  {
    "Word": "quiet",
    "Hint": "A word describing a place or situation with very little noise.",
    "UrduHint": "ایسا لفظ جو ایسی جگہ یا صورتحال کو بیان کرتا ہے جہاں بہت کم شور ہو۔"
  },
  {
    "Word": "funny",
    "Hint": "A word describing something that makes people laugh.",
    "UrduHint": "ایسا لفظ جو ایسی چیز کو بیان کرتا ہے جو لوگوں کو ہنساتی ہے۔"
  },
  {
    "Word": "brave",
    "Hint": "A word describing someone who is willing to face danger without giving up.",
    "UrduHint": "ایسا لفظ جو ایسے شخص کو بیان کرتا ہے جو ہمت نہ ہارتے ہوئے خطرے کا سامنا کرنے کے لیے تیار ہو۔"
  },
  {
    "Word": "smart",
    "Hint": "A word describing someone who is good at learning and understanding things.",
    "UrduHint": "ایسا لفظ جو ایسے شخص کو بیان کرتا ہے جو چیزیں سیکھنے اور سمجھنے میں اچھا ہو۔"
  },
  {
    "Word": "young",
    "Hint": "A word describing someone or something that has lived for a short time.",
    "UrduHint": "ایسا لفظ جو کسی ایسے شخص یا چیز کو بیان کرتا ہے جسے وجود میں آئے کم وقت ہوا ہو۔"
  },
  {
    "Word": "older",
    "Hint": "A word used to describe someone or something with more age than another.",
    "UrduHint": "ایسا لفظ جو کسی دوسرے شخص یا چیز کے مقابلے میں زیادہ عمر والے کو بیان کرنے کے لیے استعمال ہوتا ہے۔"
  },
  {
    "Word": "river",
    "Hint": "A natural flow of water that moves through land toward another body of water.",
    "UrduHint": "پانی کا قدرتی بہاؤ جو زمین سے گزرتا ہوا پانی کے کسی دوسرے ذخیرے کی طرف جاتا ہے۔"
  },
  {
    "Word": "storm",
    "Hint": "A period of bad weather that can bring strong wind, rain, thunder, or lightning.",
    "UrduHint": "خراب موسم کا ایک دور جس میں تیز ہوا، بارش، گرج چمک یا بجلی آ سکتی ہے۔"
  },
  {
    "Word": "rainy",
    "Hint": "A word describing weather in which rain is falling or expected.",
    "UrduHint": "ایسا لفظ جو ایسے موسم کو بیان کرتا ہے جس میں بارش ہو رہی ہو یا متوقع ہو۔"
  },
  {
    "Word": "sunny",
    "Hint": "A word describing weather when the sun is shining brightly.",
    "UrduHint": "ایسا لفظ جو ایسے موسم کو بیان کرتا ہے جب سورج روشن ہو کر چمک رہا ہو۔"
  },
  {
    "Word": "windy",
    "Hint": "A word describing weather with a lot of moving air.",
    "UrduHint": "ایسا لفظ جو ایسے موسم کو بیان کرتا ہے جس میں بہت زیادہ ہوا چل رہی ہو۔"
  },
  {
    "Word": "frost",
    "Hint": "A thin layer of ice that forms on cold surfaces.",
    "UrduHint": "برف کی ایک پتلی تہہ جو ٹھنڈی سطحوں پر بنتی ہے۔"
  },
  {
    "Word": "flame",
    "Hint": "The bright, hot part of a fire that you can see.",
    "UrduHint": "آگ کا روشن اور گرم حصہ جو آپ دیکھ سکتے ہیں۔"
  },
  {
    "Word": "smoke",
    "Hint": "The gray or white cloud produced when something burns.",
    "UrduHint": "وہ سرمئی یا سفید بادل جو کسی چیز کے جلنے سے پیدا ہوتا ہے۔"
  },
  {
    "Word": "stone",
    "Hint": "A small piece of hard natural rock.",
    "UrduHint": "قدرتی سخت چٹان کا ایک چھوٹا ٹکڑا۔"
  },
  {
    "Word": "metal",
    "Hint": "A hard material such as iron, copper, or aluminum used to make many objects.",
    "UrduHint": "ایک سخت مادہ جیسے لوہا، تانبا یا ایلومینیم جس سے بہت سی چیزیں بنائی جاتی ہیں۔"
  },
  {
    "Word": "glass",
    "Hint": "A hard transparent material often used for windows and bottles.",
    "UrduHint": "ایک سخت شفاف مادہ جو اکثر کھڑکیوں اور بوتلوں کے لیے استعمال ہوتا ہے۔"
  },
  {
    "Word": "wooden",
    "Hint": "Made from wood, such as a table, chair, or door.",
    "UrduHint": "لکڑی سے بنی ہوئی چیز، جیسے میز، کرسی یا دروازہ۔"
  },
  {
    "Word": "truck",
    "Hint": "A large road vehicle used for carrying goods or heavy objects.",
    "UrduHint": "سڑک پر چلنے والی ایک بڑی گاڑی جو سامان یا بھاری چیزیں لے جانے کے لیے استعمال ہوتی ہے۔"
  },
  {
    "Word": "train",
    "Hint": "A long vehicle made of connected cars that travels on railway tracks.",
    "UrduHint": "ایک لمبی سواری جو آپس میں جڑی ہوئی بوگیوں سے بنی ہوتی ہے اور ریلوے کی پٹریوں پر چلتی ہے۔"
  },
  {
    "Word": "plane",
    "Hint": "A flying vehicle with wings that carries people through the air.",
    "UrduHint": "پروں والی ایک اڑنے والی سواری جو لوگوں کو ہوا میں لے جاتی ہے۔"
  },
  {
    "Word": "bikes",
    "Hint": "Two-wheeled vehicles that people ride by turning pedals.",
    "UrduHint": "دو پہیوں والی سواریاں جنہیں لوگ پیڈل چلا کر سواری کرتے ہیں۔"
  },
  {
    "Word": "motor",
    "Hint": "A machine that uses energy to produce movement.",
    "UrduHint": "ایک مشین جو توانائی استعمال کرکے حرکت پیدا کرتی ہے۔"
  },
  {
    "Word": "brass",
    "Hint": "A yellow-colored metal made mainly by mixing copper and zinc.",
    "UrduHint": "پیلا رنگ کا ایک دھات جو بنیادی طور پر تانبے اور زنک کو ملا کر بنائی جاتی ہے۔"
  },
  {
    "Word": "golds",
    "Hint": "A word referring to things made of or related to the valuable yellow metal.",
    "UrduHint": "ایسا لفظ جو قیمتی پیلے رنگ کی دھات سے بنی یا اس سے متعلق چیزوں کے لیے استعمال ہوتا ہے۔"
  }
]


# arrMediumWords = [
#   {
#     "Word": "animal",
#     "Hint": "A living creature such as a dog, cat, horse, lion, or elephant that can move, eat, breathe, and respond to its surroundings."
#   },
#   {
#     "Word": "banana",
#     "Hint": "A long, soft fruit with yellow skin when ripe. It has a sweet taste and is easy to peel and eat as a snack."
#   },
#   {
#     "Word": "bottle",
#     "Hint": "A container with a narrow opening that is commonly used to hold water, juice, milk, oil, or other liquids."
#   },
#   {
#     "Word": "bridge",
#     "Hint": "A structure built over a river, road, railway, or other obstacle so that people and vehicles can safely travel from one side to the other."
#   },
#   {
#     "Word": "castle",
#     "Hint": "A large and strong building where kings, queens, or nobles lived in the past, often surrounded by thick walls and tall towers."
#   },
#   {
#     "Word": "carpet",
#     "Hint": "A thick piece of material that is placed on the floor of a room to make it softer, warmer, and more comfortable."
#   },
#   {
#     "Word": "cloudy",
#     "Hint": "A word used to describe weather when the sky is covered with many clouds and there is not much clear blue sky visible."
#   },
#   {
#     "Word": "coffee",
#     "Hint": "A popular hot drink made from roasted beans and hot water. Many people drink it in the morning to feel refreshed."
#   },
#   {
#     "Word": "cookie",
#     "Hint": "A small sweet baked food that can be soft or crunchy and may contain chocolate chips, nuts, raisins, or other ingredients."
#   },
#   {
#     "Word": "donkey",
#     "Hint": "A strong animal that looks similar to a small horse but has longer ears and is often used to carry people or heavy loads."
#   },
#   {
#     "Word": "dragon",
#     "Hint": "A large imaginary creature commonly shown with wings, scales, claws, and the ability to breathe fire in fantasy stories and movies."
#   },
#   {
#     "Word": "flower",
#     "Hint": "The colorful part of a plant that often has a pleasant smell and helps the plant produce seeds for creating new plants."
#   },
#   {
#     "Word": "forest",
#     "Hint": "A large area of land covered with many trees and plants where animals, birds, insects, and many other living things can live."
#   },
#   {
#     "Word": "garden",
#     "Hint": "An area around a home or building where people grow flowers, vegetables, herbs, trees, and other types of plants."
#   },
#   {
#     "Word": "guitar",
#     "Hint": "A musical instrument with a long neck and several strings that are played by strumming or picking them with your fingers."
#   },
#   {
#     "Word": "hammer",
#     "Hint": "A hand tool with a heavy head and a handle that is commonly used to hit nails into wood or other materials."
#   },
#   {
#     "Word": "helmet",
#     "Hint": "A hard protective covering worn on the head to help prevent injuries while riding a bicycle, playing sports, or doing dangerous work."
#   },
#   {
#     "Word": "jacket",
#     "Hint": "A piece of clothing worn over the upper body, usually over a shirt, to protect a person from cold weather, wind, or light rain."
#   },
#   {
#     "Word": "jungle",
#     "Hint": "A warm and wet natural area filled with thick trees, plants, vines, and many wild animals such as monkeys and big cats."
#   },
#   {
#     "Word": "kitten",
#     "Hint": "A very young cat that is usually small, soft, playful, curious, and full of energy."
#   },
#   {
#     "Word": "ladder",
#     "Hint": "A tool with two long sides connected by several steps that people climb when they need to reach something high."
#   },
#   {
#     "Word": "lemons",
#     "Hint": "Yellow citrus fruits that have a strong sour taste and are often used to make drinks, sauces, desserts, and other foods."
#   },
#   {
#     "Word": "mirror",
#     "Hint": "A smooth reflective surface that shows an image of a person or object standing in front of it."
#   },
#   {
#     "Word": "monkey",
#     "Hint": "An intelligent animal with arms, legs, and sometimes a long tail that can climb trees and is commonly found in forests."
#   },
#   {
#     "Word": "orange",
#     "Hint": "A round citrus fruit with orange-colored skin and juicy sections inside that have a sweet and slightly sour taste."
#   },
#   {
#     "Word": "pencil",
#     "Hint": "A common writing and drawing tool with a thin graphite center that leaves marks on paper and can usually be erased."
#   },
#   {
#     "Word": "planet",
#     "Hint": "A large round object in space that travels around a star. Earth is one example, and other examples include Mars and Jupiter."
#   },
#   {
#     "Word": "rabbit",
#     "Hint": "A small animal with long ears, soft fur, strong back legs, and a short tail that moves by hopping."
#   },
#   {
#     "Word": "rocket",
#     "Hint": "A powerful vehicle that uses strong engines to travel high into the sky and can continue traveling into outer space."
#   },
#   {
#     "Word": "school",
#     "Hint": "A place where students go to learn subjects such as mathematics, science, languages, computers, and many other useful skills."
#   },
#   {
#     "Word": "shovel",
#     "Hint": "A tool with a long handle and a wide blade that is used for digging and moving soil, sand, snow, or other loose material."
#   },
#   {
#     "Word": "silver",
#     "Hint": "A shiny gray-colored precious metal that is commonly used to make jewelry, coins, decorations, and other valuable objects."
#   },
#   {
#     "Word": "spider",
#     "Hint": "A small creature with eight legs that can produce silk and often uses that silk to build a web for catching insects."
#   },
#   {
#     "Word": "spring",
#     "Hint": "A season that comes after winter when temperatures become warmer and many plants begin growing new leaves and flowers."
#   },
#   {
#     "Word": "street",
#     "Hint": "A road in a town or city where cars, motorcycles, bicycles, and people travel, usually surrounded by buildings or houses."
#   },
#   {
#     "Word": "summer",
#     "Hint": "A warm season of the year when days are often longer, temperatures are higher, and people commonly enjoy outdoor activities."
#   },
#   {
#     "Word": "tomato",
#     "Hint": "A soft, round fruit that is usually red when ripe and is commonly used in salads, sauces, sandwiches, and cooked meals."
#   },
#   {
#     "Word": "turtle",
#     "Hint": "A slow-moving animal with a hard protective shell covering its body. Some types live on land while others live in water."
#   },
#   {
#     "Word": "window",
#     "Hint": "An opening in the wall of a building that usually has glass and allows sunlight and fresh air to enter a room."
#   },
#   {
#     "Word": "winter",
#     "Hint": "The cold season of the year when temperatures become low, and in some parts of the world, snow and ice can cover the ground."
#   },
#   {
#     "Word": "button",
#     "Hint": "A small round object attached to clothing that is pushed through a hole to close a shirt, jacket, coat, or other piece of clothing."
#   },
#   {
#     "Word": "camera",
#     "Hint": "A device used to take photographs or record videos by capturing images of people, places, objects, and events."
#   },
#   {
#     "Word": "candle",
#     "Hint": "A stick or block made from wax with a wick in the middle that produces light when the wick is lit."
#   },
#   {
#     "Word": "carrot",
#     "Hint": "A usually orange-colored vegetable that grows underground and has a long shape with green leaves growing from the top."
#   },
#   {
#     "Word": "cheese",
#     "Hint": "A food made from milk that can be soft, hard, creamy, or firm and is often added to pizza, sandwiches, burgers, and other meals."
#   },
#   {
#     "Word": "cherry",
#     "Hint": "A small round fruit that is usually red or dark red, has a sweet taste, and contains one hard seed in the center."
#   },
#   {
#     "Word": "circle",
#     "Hint": "A completely round shape in which every point around the outside is the same distance from the center."
#   },
#   {
#     "Word": "closet",
#     "Hint": "A small enclosed storage space in a home where people commonly keep clothes, shoes, bags, boxes, or other personal items."
#   },
#   {
#     "Word": "cotton",
#     "Hint": "A soft natural material that comes from a plant and is commonly used to make shirts, trousers, towels, bedsheets, and other fabrics."
#   },
#   {
#     "Word": "desert",
#     "Hint": "A very dry area of land that receives very little rainfall and may contain sand, rocks, and plants that can survive with little water."
#   },
#   {
#     "Word": "dinner",
#     "Hint": "A meal that people usually eat in the evening, often consisting of foods such as rice, meat, vegetables, bread, or other dishes."
#   },
#   {
#     "Word": "doctor",
#     "Hint": "A trained medical professional who examines sick or injured people, identifies health problems, and provides medical treatment or advice."
#   },
#   {
#     "Word": "donuts",
#     "Hint": "Sweet fried or baked rings of dough that are often covered with sugar, chocolate, icing, or colorful toppings."
#   },
#   {
#     "Word": "engine",
#     "Hint": "A machine that converts energy into movement and is commonly used to power cars, motorcycles, boats, airplanes, and other vehicles."
#   },
#   {
#     "Word": "family",
#     "Hint": "A group of people who are related to one another, such as parents, children, brothers, sisters, grandparents, or other relatives."
#   },
#   {
#     "Word": "farmer",
#     "Hint": "A person who grows crops or raises animals on land to produce food and other agricultural products."
#   },
#   {
#     "Word": "finger",
#     "Hint": "One of the small movable parts at the end of your hand that helps you hold, touch, point at, and move objects."
#   },
#   {
#     "Word": "garlic",
#     "Hint": "A small plant bulb made of several cloves that has a strong smell and taste and is commonly used to add flavor to food."
#   },
#   {
#     "Word": "ginger",
#     "Hint": "A root with a strong spicy flavor that is commonly used in cooking, tea, and traditional drinks."
#   },
#   {
#     "Word": "island",
#     "Hint": "A piece of land that is completely surrounded by water and can be small like a tiny island or large like a country."
#   },
#   {
#     "Word": "kettle",
#     "Hint": "A container with a handle and a spout that is designed to heat or boil water, often for making tea or coffee."
#   },
#   {
#     "Word": "laptop",
#     "Hint": "A portable computer with a screen, keyboard, and battery that can be folded closed and carried from one place to another."
#   },
#   {
#     "Word": "market",
#     "Hint": "A place where people buy and sell things such as fruits, vegetables, clothes, meat, household items, and many other products."
#   },
#   {
#     "Word": "marble",
#     "Hint": "A smooth hard stone that can be polished and is often used for floors, walls, countertops, statues, and decorative objects."
#   },
#   {
#     "Word": "melons",
#     "Hint": "Large juicy fruits with a thick outer skin and sweet flesh inside. Watermelons and cantaloupes are common examples."
#   },
#   {
#     "Word": "mother",
#     "Hint": "A female parent who gives birth to a child or raises and cares for a child as part of a family."
#   },
#   {
#     "Word": "muffin",
#     "Hint": "A small soft baked cake-like food that is often eaten for breakfast or as a snack and may contain fruit or chocolate."
#   },
#   {
#     "Word": "nature",
#     "Hint": "The natural world around us, including trees, plants, animals, rivers, mountains, oceans, weather, and other living and non-living things."
#   },
#   {
#     "Word": "number",
#     "Hint": "A mathematical value or symbol used for counting, measuring, ordering things, or performing calculations."
#   },
#   {
#     "Word": "office",
#     "Hint": "A place where people commonly work at desks, use computers, attend meetings, and perform professional or business tasks."
#   },
#   {
#     "Word": "peanut",
#     "Hint": "A small edible seed that grows underground inside a shell and is commonly eaten roasted or used to make peanut butter."
#   },
#   {
#     "Word": "pillow",
#     "Hint": "A soft object filled with material that you place under your head while sleeping to make your head and neck more comfortable."
#   },
#   {
#     "Word": "potato",
#     "Hint": "A round or oval vegetable that grows underground and can be boiled, fried, baked, mashed, or used in many different dishes."
#   },
#   {
#     "Word": "purple",
#     "Hint": "A color made by combining red and blue, often associated with flowers such as lavender and certain types of grapes."
#   },
#   {
#     "Word": "singer",
#     "Hint": "A person who uses their voice to perform songs, either alone or as part of a musical group."
#   },
#   {
#     "Word": "soccer",
#     "Hint": "A popular sport where two teams try to score goals by kicking a ball into the opposing team's goal."
#   },
#   {
#     "Word": "square",
#     "Hint": "A shape with four equal sides and four corners, where each corner forms a right angle."
#   },
#   {
#     "Word": "statue",
#     "Hint": "A three-dimensional object made to represent a person, animal, or other figure and is often displayed in public places or buildings."
#   },
#   {
#     "Word": "subway",
#     "Hint": "An underground railway system used to transport many passengers around a large city quickly and efficiently."
#   },
#   {
#     "Word": "tablet",
#     "Hint": "A portable electronic device with a flat touchscreen that can be used for watching videos, browsing the internet, reading, and using apps."
#   },
#   {
#     "Word": "tennis",
#     "Hint": "A sport played with rackets in which players hit a ball over a net and try to make it land inside the opponent's court."
#   },
#   {
#     "Word": "travel",
#     "Hint": "The activity of going from one place to another, often to visit different cities, countries, tourist attractions, or family members."
#   },
#   {
#     "Word": "valley",
#     "Hint": "A low area of land between hills or mountains that may contain a river, farms, forests, roads, or villages."
#   },
#   {
#     "Word": "wallet",
#     "Hint": "A small folding case that people carry in a pocket or bag to keep money, bank cards, identification cards, and other small items."
#   },
#   {
#     "Word": "yellow",
#     "Hint": "A bright color commonly seen in objects such as bananas, lemons, sunflowers, and some warning signs."
#   },
#   {
#     "Word": "yogurt",
#     "Hint": "A creamy food made from fermented milk that can be eaten plain or mixed with fruit, sugar, honey, or other ingredients."
#   },
#   {
#     "Word": "bakery",
#     "Hint": "A shop or place where bread, cakes, cookies, pastries, and other baked foods are prepared and sold."
#   },
#   {
#     "Word": "basket",
#     "Hint": "A container usually made from woven material or plastic that is used to carry, store, or organize different objects."
#   },
#   {
#     "Word": "beaver",
#     "Hint": "A large water-loving animal with strong teeth and a flat tail that is famous for building dams from wood and branches."
#   },
#   {
#     "Word": "bucket",
#     "Hint": "A round container with a handle that is commonly used to carry water, clean floors, store materials, or move liquids."
#   },
#   {
#     "Word": "butter",
#     "Hint": "A soft yellow dairy product made from cream that is commonly spread on bread or used while cooking and baking."
#   },
#   {
#     "Word": "cactus",
#     "Hint": "A plant that is adapted to dry environments and usually has a thick body that stores water and sharp spines for protection."
#   },
#   {
#     "Word": "cruise",
#     "Hint": "A vacation journey taken on a large passenger ship that travels between different coastal cities or countries."
#   },
#   {
#     "Word": "dancer",
#     "Hint": "A person who performs controlled body movements, often to music, either for entertainment, exercise, or professional performances."
#   },
#   {
#     "Word": "danger",
#     "Hint": "A situation or condition that could cause someone to be hurt, damaged, injured, or placed at risk."
#   },
#   {
#     "Word": "galaxy",
#     "Hint": "A huge collection of stars, planets, gas, dust, and other objects held together by gravity, with our solar system inside one."
#   },
#   {
#     "Word": "garage",
#     "Hint": "A building or enclosed space where people park cars and may also keep tools, bicycles, equipment, and other belongings."
#   },
#   {
#     "Word": "grapes",
#     "Hint": "Small round fruits that grow together in bunches on vines and can be green, red, purple, or almost black when ripe."
#   },
#   {
#     "Word": "harbor",
#     "Hint": "A sheltered area along a coast where boats and ships can safely stop, load goods, unload passengers, or wait during bad weather."
#   },
#   {
#     "Word": "jaguar",
#     "Hint": "A powerful wild cat with a spotted coat that lives mainly in forests and other parts of Central and South America."
#   },
#   {
#     "Word": "magnet",
#     "Hint": "An object that produces a magnetic force and can attract certain metals, especially iron and steel."
#   },
#   {
#     "Word": "meadow",
#     "Hint": "An open area of grassy land where wildflowers and plants grow and where animals may feed or move around."
#   },
#   {
#     "Word": "museum",
#     "Hint": "A public place where historical objects, artwork, scientific items, cultural artifacts, and other interesting things are collected and displayed."
#   },
#   {
#     "Word": "napkin",
#     "Hint": "A small piece of paper or cloth used while eating to clean your mouth, hands, or small spills from a table."
#   },
#   {
#     "Word": "needle",
#     "Hint": "A very thin sharp object with a pointed end and often a small hole that is used for sewing thread through cloth."
#   },
#   {
#     "Word": "palace",
#     "Hint": "A very large and impressive building where a king, queen, emperor, or other member of royalty may live."
#   },
#   {
#     "Word": "parent",
#     "Hint": "An adult who has a child and is responsible for caring for, protecting, supporting, and raising that child."
#   },
#   {
#     "Word": "parrot",
#     "Hint": "A colorful bird with a curved beak that can learn to copy sounds and, in some cases, imitate human speech."
#   },
#   {
#     "Word": "picnic",
#     "Hint": "A meal eaten outdoors, often in a park or natural area, where people bring food, drinks, blankets, and sometimes games."
#   },
#   {
#     "Word": "pirate",
#     "Hint": "A person who attacks or steals from ships at sea, often shown in stories wearing old-fashioned clothing and searching for treasure."
#   },
#   {
#     "Word": "pocket",
#     "Hint": "A small fabric compartment sewn into clothing or a bag where you can keep money, keys, a phone, or other small objects."
#   },
#   {
#     "Word": "puzzle",
#     "Hint": "A game or problem that requires you to think carefully and arrange, match, or solve different pieces to find the correct answer."
#   },
#   {
#     "Word": "recipe",
#     "Hint": "A set of instructions that tells you which ingredients to use and how to prepare and cook a particular food or dish."
#   },
#   {
#     "Word": "remote",
#     "Hint": "A small electronic device with buttons that allows you to control a television, air conditioner, or another device from a distance."
#   },
#   {
#     "Word": "runner",
#     "Hint": "A person who runs, especially someone who takes part in running for exercise, sport, competition, or fitness."
#   },
#   {
#     "Word": "sailor",
#     "Hint": "A person who works or travels on a ship and helps operate the vessel while it is traveling across the water."
#   },
#   {
#     "Word": "salmon",
#     "Hint": "A type of fish that lives in water and is commonly eaten as food. Some species are known for swimming upstream to lay eggs."
#   },
#   {
#     "Word": "secret",
#     "Hint": "Information that is kept hidden from other people because someone does not want them to know or discover it."
#   },
#   {
#     "Word": "shadow",
#     "Hint": "A dark shape that appears on the ground or another surface when an object blocks light from reaching that area."
#   },
#   {
#     "Word": "smooth",
#     "Hint": "A word used to describe a surface that feels even and soft without rough bumps, sharp edges, or an uneven texture."
#   },
#   {
#     "Word": "stable",
#     "Hint": "A building where horses are kept, fed, and cared for, usually with separate spaces for each animal."
#   },
#   {
#     "Word": "stream",
#     "Hint": "A small natural flow of water that moves across the land and may eventually join a larger river or body of water."
#   }
# ]


arrMediumWords = [
  {
    "Word": "animal",
    "Hint": "A living creature such as a dog, cat, horse, lion, or elephant that can move, eat, breathe, and respond to its surroundings.",
    "UrduHint": "ایک جاندار مخلوق جیسے کتا، بلی، گھوڑا، شیر یا ہاتھی جو حرکت کر سکتی ہے، کھا سکتی ہے، سانس لے سکتی ہے اور اپنے اردگرد کے ماحول کا ردعمل دے سکتی ہے۔"
  },
  {
    "Word": "banana",
    "Hint": "A long, soft fruit with yellow skin when ripe. It has a sweet taste and is easy to peel and eat as a snack.",
    "UrduHint": "ایک لمبا اور نرم پھل جس کا چھلکا پکنے پر پیلا ہو جاتا ہے۔ اس کا ذائقہ میٹھا ہوتا ہے اور اسے آسانی سے چھیل کر بطور ہلکی غذا کھایا جا سکتا ہے۔"
  },
  {
    "Word": "bottle",
    "Hint": "A container with a narrow opening that is commonly used to hold water, juice, milk, oil, or other liquids.",
    "UrduHint": "ایک ایسا برتن جس کا منہ تنگ ہوتا ہے اور اسے عام طور پر پانی، جوس، دودھ، تیل یا دیگر مائعات رکھنے کے لیے استعمال کیا جاتا ہے۔"
  },
  {
    "Word": "bridge",
    "Hint": "A structure built over a river, road, railway, or other obstacle so that people and vehicles can safely travel from one side to the other.",
    "UrduHint": "دریا، سڑک، ریلوے یا کسی دوسری رکاوٹ کے اوپر بنایا گیا ڈھانچہ جس کے ذریعے لوگ اور گاڑیاں محفوظ طریقے سے ایک طرف سے دوسری طرف جا سکتے ہیں۔"
  },
  {
    "Word": "castle",
    "Hint": "A large and strong building where kings, queens, or nobles lived in the past, often surrounded by thick walls and tall towers.",
    "UrduHint": "ایک بڑی اور مضبوط عمارت جہاں ماضی میں بادشاہ، ملکہ یا رئیس رہتے تھے، اور اس کے گرد اکثر موٹی دیواریں اور اونچے مینار ہوتے تھے۔"
  },
  {
    "Word": "carpet",
    "Hint": "A thick piece of material that is placed on the floor of a room to make it softer, warmer, and more comfortable.",
    "UrduHint": "موٹے کپڑے یا مواد کا ایک ٹکڑا جو کمرے کے فرش پر بچھایا جاتا ہے تاکہ فرش نرم، گرم اور زیادہ آرام دہ ہو جائے۔"
  },
  {
    "Word": "cloudy",
    "Hint": "A word used to describe weather when the sky is covered with many clouds and there is not much clear blue sky visible.",
    "UrduHint": "ایسا لفظ جو اس موسم کے لیے استعمال ہوتا ہے جب آسمان بہت سے بادلوں سے ڈھکا ہو اور صاف نیلا آسمان زیادہ نظر نہ آئے۔"
  },
  {
    "Word": "coffee",
    "Hint": "A popular hot drink made from roasted beans and hot water. Many people drink it in the morning to feel refreshed.",
    "UrduHint": "ایک مشہور گرم مشروب جو بھنے ہوئے دانوں اور گرم پانی سے بنایا جاتا ہے۔ بہت سے لوگ تازگی محسوس کرنے کے لیے اسے صبح پیتے ہیں۔"
  },
  {
    "Word": "cookie",
    "Hint": "A small sweet baked food that can be soft or crunchy and may contain chocolate chips, nuts, raisins, or other ingredients.",
    "UrduHint": "ایک چھوٹی میٹھی پکی ہوئی غذا جو نرم یا خستہ ہو سکتی ہے اور اس میں چاکلیٹ کے ٹکڑے، گری دار میوے، کشمش یا دیگر اجزاء شامل ہو سکتے ہیں۔"
  },
  {
    "Word": "donkey",
    "Hint": "A strong animal that looks similar to a small horse but has longer ears and is often used to carry people or heavy loads.",
    "UrduHint": "ایک طاقتور جانور جو چھوٹے گھوڑے جیسا دکھائی دیتا ہے لیکن اس کے کان زیادہ لمبے ہوتے ہیں اور اسے اکثر لوگوں یا بھاری سامان کو اٹھانے کے لیے استعمال کیا جاتا ہے۔"
  },
  {
    "Word": "dragon",
    "Hint": "A large imaginary creature commonly shown with wings, scales, claws, and the ability to breathe fire in fantasy stories and movies.",
    "UrduHint": "ایک بڑا خیالی جانور جسے عام طور پر پروں، چھلکوں، پنجوں اور آگ اگلنے کی صلاحیت کے ساتھ خیالی کہانیوں اور فلموں میں دکھایا جاتا ہے۔"
  },
  {
    "Word": "flower",
    "Hint": "The colorful part of a plant that often has a pleasant smell and helps the plant produce seeds for creating new plants.",
    "UrduHint": "پودے کا رنگین حصہ جس میں اکثر خوشگوار خوشبو ہوتی ہے اور جو پودے کو نئے پودے بنانے کے لیے بیج پیدا کرنے میں مدد دیتا ہے۔"
  },
  {
    "Word": "forest",
    "Hint": "A large area of land covered with many trees and plants where animals, birds, insects, and many other living things can live.",
    "UrduHint": "زمین کا ایک بڑا علاقہ جو بہت سے درختوں اور پودوں سے ڈھکا ہوتا ہے جہاں جانور، پرندے، کیڑے اور بہت سی دوسری جاندار چیزیں رہ سکتی ہیں۔"
  },
  {
    "Word": "garden",
    "Hint": "An area around a home or building where people grow flowers, vegetables, herbs, trees, and other types of plants.",
    "UrduHint": "گھر یا عمارت کے اردگرد موجود ایک جگہ جہاں لوگ پھول، سبزیاں، جڑی بوٹیاں، درخت اور دیگر پودے اگاتے ہیں۔"
  },
  {
    "Word": "guitar",
    "Hint": "A musical instrument with a long neck and several strings that are played by strumming or picking them with your fingers.",
    "UrduHint": "ایک موسیقی کا آلہ جس کی لمبی گردن اور کئی تاریں ہوتی ہیں جنہیں انگلیوں سے چھیڑ کر یا بجا کر موسیقی پیدا کی جاتی ہے۔"
  },
  {
    "Word": "hammer",
    "Hint": "A hand tool with a heavy head and a handle that is commonly used to hit nails into wood or other materials.",
    "UrduHint": "ایک ہاتھ سے استعمال ہونے والا اوزار جس کا سر بھاری اور ایک دستہ ہوتا ہے، اسے عام طور پر لکڑی یا دوسرے مواد میں کیل ٹھونکنے کے لیے استعمال کیا جاتا ہے۔"
  },
  {
    "Word": "helmet",
    "Hint": "A hard protective covering worn on the head to help prevent injuries while riding a bicycle, playing sports, or doing dangerous work.",
    "UrduHint": "سر پر پہنا جانے والا سخت حفاظتی سامان جو سائیکل چلاتے، کھیل کھیلتے یا خطرناک کام کرتے وقت چوٹ سے بچانے میں مدد دیتا ہے۔"
  },
  {
    "Word": "jacket",
    "Hint": "A piece of clothing worn over the upper body, usually over a shirt, to protect a person from cold weather, wind, or light rain.",
    "UrduHint": "اوپری جسم پر پہنا جانے والا لباس، جو عام طور پر قمیض کے اوپر پہنا جاتا ہے تاکہ انسان کو سرد موسم، ہوا یا ہلکی بارش سے بچایا جا سکے۔"
  },
  {
    "Word": "jungle",
    "Hint": "A warm and wet natural area filled with thick trees, plants, vines, and many wild animals such as monkeys and big cats.",
    "UrduHint": "ایک گرم اور مرطوب قدرتی علاقہ جو گھنے درختوں، پودوں، بیلوں اور بندروں اور بڑے شکاری جانوروں جیسے بہت سے جنگلی جانوروں سے بھرا ہوتا ہے۔"
  },
  {
    "Word": "kitten",
    "Hint": "A very young cat that is usually small, soft, playful, curious, and full of energy.",
    "UrduHint": "ایک بہت چھوٹی عمر کی بلی جو عام طور پر چھوٹی، نرم، کھیلنے والی، تجسس سے بھرپور اور بہت چست ہوتی ہے۔"
  },
  {
    "Word": "ladder",
    "Hint": "A tool with two long sides connected by several steps that people climb when they need to reach something high.",
    "UrduHint": "ایک اوزار جس کے دو لمبے کنارے کئی سیڑھی نما ڈنڈیوں سے جڑے ہوتے ہیں اور لوگ اونچی جگہ تک پہنچنے کے لیے اس پر چڑھتے ہیں۔"
  },
  {
    "Word": "lemons",
    "Hint": "Yellow citrus fruits that have a strong sour taste and are often used to make drinks, sauces, desserts, and other foods.",
    "UrduHint": "پیلی ترش پھلوں کی قسم جن کا ذائقہ بہت کھٹا ہوتا ہے اور انہیں اکثر مشروبات، چٹنیوں، میٹھے اور دیگر کھانوں میں استعمال کیا جاتا ہے۔"
  },
  {
    "Word": "mirror",
    "Hint": "A smooth reflective surface that shows an image of a person or object standing in front of it.",
    "UrduHint": "ایک ہموار چمکدار سطح جو اپنے سامنے کھڑے شخص یا چیز کی تصویر دکھاتی ہے۔"
  },
  {
    "Word": "monkey",
    "Hint": "An intelligent animal with arms, legs, and sometimes a long tail that can climb trees and is commonly found in forests.",
    "UrduHint": "ایک ذہین جانور جس کے بازو، ٹانگیں اور بعض اوقات لمبی دم ہوتی ہے، جو درختوں پر چڑھ سکتا ہے اور عام طور پر جنگلات میں پایا جاتا ہے۔"
  },
  {
    "Word": "orange",
    "Hint": "A round citrus fruit with orange-colored skin and juicy sections inside that have a sweet and slightly sour taste.",
    "UrduHint": "ایک گول ترش پھل جس کا چھلکا نارنجی رنگ کا ہوتا ہے اور اندر رس بھرے حصے ہوتے ہیں جن کا ذائقہ میٹھا اور ہلکا سا کھٹا ہوتا ہے۔"
  },
  {
    "Word": "pencil",
    "Hint": "A common writing and drawing tool with a thin graphite center that leaves marks on paper and can usually be erased.",
    "UrduHint": "لکھنے اور ڈرائنگ بنانے کا ایک عام اوزار جس کے اندر گریفائٹ کی پتلی نوک ہوتی ہے جو کاغذ پر نشان بناتی ہے اور عام طور پر مٹائی جا سکتی ہے۔"
  },
  {
    "Word": "planet",
    "Hint": "A large round object in space that travels around a star. Earth is one example, and other examples include Mars and Jupiter.",
    "UrduHint": "خلا میں موجود ایک بڑا گول جسم جو کسی ستارے کے گرد گردش کرتا ہے۔ زمین اس کی ایک مثال ہے جبکہ مریخ اور مشتری بھی اس کی مثالیں ہیں۔"
  },
  {
    "Word": "rabbit",
    "Hint": "A small animal with long ears, soft fur, strong back legs, and a short tail that moves by hopping.",
    "UrduHint": "ایک چھوٹا جانور جس کے لمبے کان، نرم بال، مضبوط پچھلی ٹانگیں اور چھوٹی دم ہوتی ہے اور جو اچھل کر حرکت کرتا ہے۔"
  },
  {
    "Word": "rocket",
    "Hint": "A powerful vehicle that uses strong engines to travel high into the sky and can continue traveling into outer space.",
    "UrduHint": "ایک طاقتور گاڑی جو مضبوط انجنوں کی مدد سے آسمان میں بہت بلندی تک سفر کرتی ہے اور بیرونی خلا تک بھی جا سکتی ہے۔"
  },
  {
    "Word": "school",
    "Hint": "A place where students go to learn subjects such as mathematics, science, languages, computers, and many other useful skills.",
    "UrduHint": "ایک ایسی جگہ جہاں طلبہ ریاضی، سائنس، زبانیں، کمپیوٹر اور بہت سی دوسری مفید مہارتیں سیکھنے کے لیے جاتے ہیں۔"
  },
  {
    "Word": "shovel",
    "Hint": "A tool with a long handle and a wide blade that is used for digging and moving soil, sand, snow, or other loose material.",
    "UrduHint": "ایک اوزار جس کا دستہ لمبا اور بلیڈ چوڑا ہوتا ہے، اسے مٹی، ریت، برف یا دوسرے ڈھیلے مواد کو کھودنے اور منتقل کرنے کے لیے استعمال کیا جاتا ہے۔"
  },
  {
    "Word": "silver",
    "Hint": "A shiny gray-colored precious metal that is commonly used to make jewelry, coins, decorations, and other valuable objects.",
    "UrduHint": "چمکدار سرمئی رنگ کی ایک قیمتی دھات جسے عام طور پر زیورات، سکے، سجاوٹ کی چیزیں اور دیگر قیمتی اشیاء بنانے کے لیے استعمال کیا جاتا ہے۔"
  },
  {
    "Word": "spider",
    "Hint": "A small creature with eight legs that can produce silk and often uses that silk to build a web for catching insects.",
    "UrduHint": "ایک چھوٹی مخلوق جس کی آٹھ ٹانگیں ہوتی ہیں اور جو ریشم جیسا مادہ پیدا کر سکتی ہے، جسے اکثر کیڑے پکڑنے کے لیے جالا بنانے میں استعمال کرتی ہے۔"
  },
  {
    "Word": "spring",
    "Hint": "A season that comes after winter when temperatures become warmer and many plants begin growing new leaves and flowers.",
    "UrduHint": "سردیوں کے بعد آنے والا موسم جب درجہ حرارت گرم ہونے لگتا ہے اور بہت سے پودے نئے پتے اور پھول اگانا شروع کر دیتے ہیں۔"
  },
  {
    "Word": "street",
    "Hint": "A road in a town or city where cars, motorcycles, bicycles, and people travel, usually surrounded by buildings or houses.",
    "UrduHint": "شہر یا قصبے کی ایک سڑک جہاں گاڑیاں، موٹر سائیکلیں، سائیکلیں اور لوگ سفر کرتے ہیں اور جس کے اردگرد عام طور پر عمارتیں یا گھر ہوتے ہیں۔"
  },
  {
    "Word": "summer",
    "Hint": "A warm season of the year when days are often longer, temperatures are higher, and people commonly enjoy outdoor activities.",
    "UrduHint": "سال کا ایک گرم موسم جس میں دن اکثر لمبے، درجہ حرارت زیادہ ہوتا ہے اور لوگ عام طور پر بیرونی سرگرمیوں سے لطف اندوز ہوتے ہیں۔"
  },
  {
    "Word": "tomato",
    "Hint": "A soft, round fruit that is usually red when ripe and is commonly used in salads, sauces, sandwiches, and cooked meals.",
    "UrduHint": "ایک نرم اور گول پھل جو پکنے پر عام طور پر سرخ ہوتا ہے اور اسے سلاد، چٹنیوں، سینڈوچ اور پکے ہوئے کھانوں میں استعمال کیا جاتا ہے۔"
  },
  {
    "Word": "turtle",
    "Hint": "A slow-moving animal with a hard protective shell covering its body. Some types live on land while others live in water.",
    "UrduHint": "ایک آہستہ چلنے والا جانور جس کے جسم پر سخت حفاظتی خول ہوتا ہے۔ کچھ اقسام خشکی پر جبکہ دوسری پانی میں رہتی ہیں۔"
  },
  {
    "Word": "window",
    "Hint": "An opening in the wall of a building that usually has glass and allows sunlight and fresh air to enter a room.",
    "UrduHint": "عمارت کی دیوار میں موجود ایک کھلا حصہ جس میں عام طور پر شیشہ لگا ہوتا ہے اور جس سے سورج کی روشنی اور تازہ ہوا کمرے میں داخل ہوتی ہے۔"
  },
  {
    "Word": "winter",
    "Hint": "The cold season of the year when temperatures become low, and in some parts of the world, snow and ice can cover the ground.",
    "UrduHint": "سال کا سرد موسم جب درجہ حرارت کم ہو جاتا ہے اور دنیا کے کچھ علاقوں میں برف اور برفانی تہہ زمین کو ڈھانپ سکتی ہے۔"
  },
  {
    "Word": "button",
    "Hint": "A small round object attached to clothing that is pushed through a hole to close a shirt, jacket, coat, or other piece of clothing.",
    "UrduHint": "کپڑوں کے ساتھ لگا ہوا ایک چھوٹا گول بٹن جسے سوراخ میں ڈال کر قمیض، جیکٹ، کوٹ یا دوسرے لباس کو بند کیا جاتا ہے۔"
  },
  {
    "Word": "camera",
    "Hint": "A device used to take photographs or record videos by capturing images of people, places, objects, and events.",
    "UrduHint": "ایک آلہ جو لوگوں، جگہوں، چیزوں اور واقعات کی تصاویر محفوظ کرکے تصویریں لینے یا ویڈیوز ریکارڈ کرنے کے لیے استعمال ہوتا ہے۔"
  },
  {
    "Word": "candle",
    "Hint": "A stick or block made from wax with a wick in the middle that produces light when the wick is lit.",
    "UrduHint": "موم سے بنی ہوئی ایک ڈنڈی یا بلاک جس کے درمیان بتی ہوتی ہے اور بتی جلانے پر روشنی پیدا ہوتی ہے۔"
  },
  {
    "Word": "carrot",
    "Hint": "A usually orange-colored vegetable that grows underground and has a long shape with green leaves growing from the top.",
    "UrduHint": "عام طور پر نارنجی رنگ کی ایک سبزی جو زمین کے اندر اگتی ہے اور اس کی لمبی شکل ہوتی ہے جبکہ اوپر سبز پتے نکلتے ہیں۔"
  },
  {
    "Word": "cheese",
    "Hint": "A food made from milk that can be soft, hard, creamy, or firm and is often added to pizza, sandwiches, burgers, and other meals.",
    "UrduHint": "دودھ سے بنائی جانے والی ایک غذا جو نرم، سخت، کریمی یا ٹھوس ہو سکتی ہے اور اسے اکثر پیزا، سینڈوچ، برگر اور دوسرے کھانوں میں شامل کیا جاتا ہے۔"
  },
  {
    "Word": "cherry",
    "Hint": "A small round fruit that is usually red or dark red, has a sweet taste, and contains one hard seed in the center.",
    "UrduHint": "ایک چھوٹا گول پھل جو عام طور پر سرخ یا گہرا سرخ ہوتا ہے، اس کا ذائقہ میٹھا ہوتا ہے اور درمیان میں ایک سخت گٹھلی ہوتی ہے۔"
  },
  {
    "Word": "circle",
    "Hint": "A completely round shape in which every point around the outside is the same distance from the center.",
    "UrduHint": "ایک مکمل گول شکل جس میں بیرونی کنارے پر موجود ہر نقطہ مرکز سے برابر فاصلے پر ہوتا ہے۔"
  },
  {
    "Word": "closet",
    "Hint": "A small enclosed storage space in a home where people commonly keep clothes, shoes, bags, boxes, or other personal items.",
    "UrduHint": "گھر میں موجود ایک چھوٹی بند جگہ جہاں لوگ عام طور پر کپڑے، جوتے، بیگ، ڈبے یا دوسری ذاتی چیزیں رکھتے ہیں۔"
  },
  {
    "Word": "cotton",
    "Hint": "A soft natural material that comes from a plant and is commonly used to make shirts, trousers, towels, bedsheets, and other fabrics.",
    "UrduHint": "ایک نرم قدرتی مواد جو پودے سے حاصل ہوتا ہے اور عام طور پر قمیضیں، پتلون، تولیے، چادریں اور دوسرے کپڑے بنانے کے لیے استعمال ہوتا ہے۔"
  },
  {
    "Word": "desert",
    "Hint": "A very dry area of land that receives very little rainfall and may contain sand, rocks, and plants that can survive with little water.",
    "UrduHint": "زمین کا ایک بہت خشک علاقہ جہاں بہت کم بارش ہوتی ہے اور وہاں ریت، چٹانیں اور ایسے پودے ہو سکتے ہیں جو کم پانی میں زندہ رہ سکتے ہیں۔"
  },
  {
    "Word": "dinner",
    "Hint": "A meal that people usually eat in the evening, often consisting of foods such as rice, meat, vegetables, bread, or other dishes.",
    "UrduHint": "وہ کھانا جو لوگ عام طور پر شام کے وقت کھاتے ہیں اور جس میں چاول، گوشت، سبزیاں، روٹی یا دیگر کھانے شامل ہو سکتے ہیں۔"
  },
  {
    "Word": "doctor",
    "Hint": "A trained medical professional who examines sick or injured people, identifies health problems, and provides medical treatment or advice.",
    "UrduHint": "ایک تربیت یافتہ طبی ماہر جو بیمار یا زخمی لوگوں کا معائنہ کرتا ہے، صحت کے مسائل کی شناخت کرتا ہے اور طبی علاج یا مشورہ فراہم کرتا ہے۔"
  },
  {
    "Word": "donuts",
    "Hint": "Sweet fried or baked rings of dough that are often covered with sugar, chocolate, icing, or colorful toppings.",
    "UrduHint": "آٹے سے بنے ہوئے میٹھے تلے یا بیک کیے گئے حلقے جن پر اکثر چینی، چاکلیٹ، آئسنگ یا رنگ برنگی سجاوٹ کی جاتی ہے۔"
  },
  {
    "Word": "engine",
    "Hint": "A machine that converts energy into movement and is commonly used to power cars, motorcycles, boats, airplanes, and other vehicles.",
    "UrduHint": "ایک مشین جو توانائی کو حرکت میں تبدیل کرتی ہے اور عام طور پر کاروں، موٹر سائیکلوں، کشتیوں، ہوائی جہازوں اور دوسری گاڑیوں کو چلانے کے لیے استعمال ہوتی ہے۔"
  },
  {
    "Word": "family",
    "Hint": "A group of people who are related to one another, such as parents, children, brothers, sisters, grandparents, or other relatives.",
    "UrduHint": "ایسے لوگوں کا گروہ جو ایک دوسرے سے رشتہ رکھتے ہوں، جیسے والدین، بچے، بھائی، بہنیں، دادا دادی، نانا نانی یا دوسرے رشتہ دار۔"
  },
  {
    "Word": "farmer",
    "Hint": "A person who grows crops or raises animals on land to produce food and other agricultural products.",
    "UrduHint": "ایک شخص جو خوراک اور دیگر زرعی مصنوعات پیدا کرنے کے لیے زمین پر فصلیں اگاتا یا جانور پالتا ہے۔"
  },
  {
    "Word": "finger",
    "Hint": "One of the small movable parts at the end of your hand that helps you hold, touch, point at, and move objects.",
    "UrduHint": "ہاتھ کے سرے پر موجود چھوٹے حرکت کرنے والے حصوں میں سے ایک جو چیزوں کو پکڑنے، چھونے، اشارہ کرنے اور حرکت دینے میں مدد دیتا ہے۔"
  },
  {
    "Word": "garlic",
    "Hint": "A small plant bulb made of several cloves that has a strong smell and taste and is commonly used to add flavor to food.",
    "UrduHint": "ایک چھوٹا پودے کا بلب جو کئی جوؤں پر مشتمل ہوتا ہے، اس کی بو اور ذائقہ تیز ہوتا ہے اور اسے عام طور پر کھانے میں ذائقہ بڑھانے کے لیے استعمال کیا جاتا ہے۔"
  },
  {
    "Word": "ginger",
    "Hint": "A root with a strong spicy flavor that is commonly used in cooking, tea, and traditional drinks.",
    "UrduHint": "ایک جڑ جس کا ذائقہ تیز اور مصالحے دار ہوتا ہے اور اسے عام طور پر کھانا پکانے، چائے اور روایتی مشروبات میں استعمال کیا جاتا ہے۔"
  },
  {
    "Word": "island",
    "Hint": "A piece of land that is completely surrounded by water and can be small like a tiny island or large like a country.",
    "UrduHint": "زمین کا ایک ٹکڑا جو مکمل طور پر پانی سے گھرا ہوا ہو اور بہت چھوٹا یا کسی ملک جتنا بڑا بھی ہو سکتا ہے۔"
  },
  {
    "Word": "kettle",
    "Hint": "A container with a handle and a spout that is designed to heat or boil water, often for making tea or coffee.",
    "UrduHint": "ایک ایسا برتن جس میں دستہ اور ٹونٹی ہوتی ہے اور اسے پانی گرم یا ابالنے کے لیے استعمال کیا جاتا ہے، خاص طور پر چائے یا کافی بنانے کے لیے۔"
  },
  {
    "Word": "laptop",
    "Hint": "A portable computer with a screen, keyboard, and battery that can be folded closed and carried from one place to another.",
    "UrduHint": "ایک قابلِ نقل کمپیوٹر جس میں اسکرین، کی بورڈ اور بیٹری ہوتی ہے، اسے بند کرکے ایک جگہ سے دوسری جگہ لے جایا جا سکتا ہے۔"
  },
  {
    "Word": "market",
    "Hint": "A place where people buy and sell things such as fruits, vegetables, clothes, meat, household items, and many other products.",
    "UrduHint": "ایک ایسی جگہ جہاں لوگ پھل، سبزیاں، کپڑے، گوشت، گھریلو سامان اور بہت سی دوسری چیزیں خریدتے اور فروخت کرتے ہیں۔"
  },
  {
    "Word": "marble",
    "Hint": "A smooth hard stone that can be polished and is often used for floors, walls, countertops, statues, and decorative objects.",
    "UrduHint": "ایک ہموار اور سخت پتھر جسے پالش کیا جا سکتا ہے اور اسے اکثر فرش، دیواروں، کاؤنٹر، مجسموں اور سجاوٹی اشیاء کے لیے استعمال کیا جاتا ہے۔"
  },
  {
    "Word": "melons",
    "Hint": "Large juicy fruits with a thick outer skin and sweet flesh inside. Watermelons and cantaloupes are common examples.",
    "UrduHint": "بڑے رس دار پھل جن کا بیرونی چھلکا موٹا اور اندر کا گودا میٹھا ہوتا ہے۔ تربوز اور خربوزہ اس کی عام مثالیں ہیں۔"
  },
  {
    "Word": "mother",
    "Hint": "A female parent who gives birth to a child or raises and cares for a child as part of a family.",
    "UrduHint": "ایک خاتون والدین جو بچے کو جنم دیتی ہے یا خاندان کے حصے کے طور پر بچے کی پرورش اور دیکھ بھال کرتی ہے۔"
  },
  {
    "Word": "muffin",
    "Hint": "A small soft baked cake-like food that is often eaten for breakfast or as a snack and may contain fruit or chocolate.",
    "UrduHint": "ایک چھوٹی نرم کیک جیسی بیک کی ہوئی غذا جو اکثر ناشتے یا ہلکی غذا کے طور پر کھائی جاتی ہے اور اس میں پھل یا چاکلیٹ شامل ہو سکتی ہے۔"
  },
  {
    "Word": "nature",
    "Hint": "The natural world around us, including trees, plants, animals, rivers, mountains, oceans, weather, and other living and non-living things.",
    "UrduHint": "ہمارے اردگرد کی قدرتی دنیا جس میں درخت، پودے، جانور، دریا، پہاڑ، سمندر، موسم اور دوسری جاندار و غیر جاندار چیزیں شامل ہیں۔"
  },
  {
    "Word": "number",
    "Hint": "A mathematical value or symbol used for counting, measuring, ordering things, or performing calculations.",
    "UrduHint": "ایک ریاضیاتی قدر یا علامت جو گنتی، پیمائش، چیزوں کو ترتیب دینے یا حساب کتاب کرنے کے لیے استعمال ہوتی ہے۔"
  },
  {
    "Word": "office",
    "Hint": "A place where people commonly work at desks, use computers, attend meetings, and perform professional or business tasks.",
    "UrduHint": "ایک ایسی جگہ جہاں لوگ عام طور پر میزوں پر کام کرتے، کمپیوٹر استعمال کرتے، میٹنگز میں شرکت کرتے اور پیشہ ورانہ یا کاروباری کام انجام دیتے ہیں۔"
  },
  {
    "Word": "peanut",
    "Hint": "A small edible seed that grows underground inside a shell and is commonly eaten roasted or used to make peanut butter.",
    "UrduHint": "ایک چھوٹا کھانے کے قابل بیج جو زمین کے اندر چھلکے میں اگتا ہے اور عام طور پر بھون کر کھایا جاتا ہے یا مونگ پھلی کا مکھن بنانے کے لیے استعمال ہوتا ہے۔"
  },
  {
    "Word": "pillow",
    "Hint": "A soft object filled with material that you place under your head while sleeping to make your head and neck more comfortable.",
    "UrduHint": "ایک نرم چیز جس کے اندر مختلف مواد بھرا ہوتا ہے اور اسے سوتے وقت سر کے نیچے رکھا جاتا ہے تاکہ سر اور گردن زیادہ آرام دہ رہیں۔"
  },
  {
    "Word": "potato",
    "Hint": "A round or oval vegetable that grows underground and can be boiled, fried, baked, mashed, or used in many different dishes.",
    "UrduHint": "ایک گول یا بیضوی سبزی جو زمین کے اندر اگتی ہے اور اسے ابالا، تلا، بیک، میش یا مختلف کھانوں میں استعمال کیا جا سکتا ہے۔"
  },
  {
    "Word": "purple",
    "Hint": "A color made by combining red and blue, often associated with flowers such as lavender and certain types of grapes.",
    "UrduHint": "ایک رنگ جو سرخ اور نیلے رنگ کو ملانے سے بنتا ہے اور اکثر لیونڈر جیسے پھولوں اور انگور کی کچھ اقسام میں دیکھا جاتا ہے۔"
  },
  {
    "Word": "singer",
    "Hint": "A person who uses their voice to perform songs, either alone or as part of a musical group.",
    "UrduHint": "ایک شخص جو اپنی آواز سے گانے پیش کرتا ہے، چاہے اکیلے یا کسی موسیقی کے گروپ کا حصہ بن کر۔"
  },
  {
    "Word": "soccer",
    "Hint": "A popular sport where two teams try to score goals by kicking a ball into the opposing team's goal.",
    "UrduHint": "ایک مشہور کھیل جس میں دو ٹیمیں گیند کو لات مار کر مخالف ٹیم کے گول میں پہنچا کر گول کرنے کی کوشش کرتی ہیں۔"
  },
  {
    "Word": "square",
    "Hint": "A shape with four equal sides and four corners, where each corner forms a right angle.",
    "UrduHint": "ایک ایسی شکل جس کی چاروں اطراف برابر اور چار کونے ہوتے ہیں، اور ہر کونا قائمہ زاویہ بناتا ہے۔"
  },
  {
    "Word": "statue",
    "Hint": "A three-dimensional object made to represent a person, animal, or other figure and is often displayed in public places or buildings.",
    "UrduHint": "ایک سہ جہتی مجسمہ جو کسی شخص، جانور یا دوسری شکل کی نمائندگی کے لیے بنایا جاتا ہے اور اکثر عوامی مقامات یا عمارتوں میں رکھا جاتا ہے۔"
  },
  {
    "Word": "subway",
    "Hint": "An underground railway system used to transport many passengers around a large city quickly and efficiently.",
    "UrduHint": "ایک زیر زمین ریلوے نظام جو بڑے شہر میں بہت سے مسافروں کو تیزی اور مؤثر طریقے سے ایک جگہ سے دوسری جگہ لے جانے کے لیے استعمال ہوتا ہے۔"
  },
  {
    "Word": "tablet",
    "Hint": "A portable electronic device with a flat touchscreen that can be used for watching videos, browsing the internet, reading, and using apps.",
    "UrduHint": "ایک قابلِ نقل برقی آلہ جس کی ہموار ٹچ اسکرین ہوتی ہے اور اسے ویڈیوز دیکھنے، انٹرنیٹ استعمال کرنے، پڑھنے اور ایپس چلانے کے لیے استعمال کیا جاتا ہے۔"
  },
  {
    "Word": "tennis",
    "Hint": "A sport played with rackets in which players hit a ball over a net and try to make it land inside the opponent's court.",
    "UrduHint": "ایک کھیل جو ریکٹس کے ساتھ کھیلا جاتا ہے جس میں کھلاڑی گیند کو جال کے اوپر سے مارتے ہیں اور اسے مخالف کے کورٹ میں گرانے کی کوشش کرتے ہیں۔"
  },
  {
    "Word": "travel",
    "Hint": "The activity of going from one place to another, often to visit different cities, countries, tourist attractions, or family members.",
    "UrduHint": "ایک جگہ سے دوسری جگہ جانے کا عمل، اکثر مختلف شہروں، ممالک، سیاحتی مقامات یا خاندان کے افراد سے ملنے کے لیے سفر کیا جاتا ہے۔"
  },
  {
    "Word": "valley",
    "Hint": "A low area of land between hills or mountains that may contain a river, farms, forests, roads, or villages.",
    "UrduHint": "پہاڑیوں یا پہاڑوں کے درمیان موجود زمین کا نچلا علاقہ جس میں دریا، کھیت، جنگلات، سڑکیں یا گاؤں ہو سکتے ہیں۔"
  },
  {
    "Word": "wallet",
    "Hint": "A small folding case that people carry in a pocket or bag to keep money, bank cards, identification cards, and other small items.",
    "UrduHint": "ایک چھوٹا تہہ ہونے والا بٹوا جسے لوگ جیب یا بیگ میں رکھتے ہیں تاکہ پیسے، بینک کارڈ، شناختی کارڈ اور دوسری چھوٹی چیزیں محفوظ رکھ سکیں۔"
  },
  {
    "Word": "yellow",
    "Hint": "A bright color commonly seen in objects such as bananas, lemons, sunflowers, and some warning signs.",
    "UrduHint": "ایک شوخ رنگ جو عام طور پر کیلے، لیموں، سورج مکھی اور کچھ انتباہی نشانات میں دیکھا جاتا ہے۔"
  },
  {
    "Word": "yogurt",
    "Hint": "A creamy food made from fermented milk that can be eaten plain or mixed with fruit, sugar, honey, or other ingredients.",
    "UrduHint": "خمیر شدہ دودھ سے بننے والی ایک کریمی غذا جسے سادہ یا پھل، چینی، شہد یا دیگر اجزاء کے ساتھ ملا کر کھایا جا سکتا ہے۔"
  },
  {
    "Word": "bakery",
    "Hint": "A shop or place where bread, cakes, cookies, pastries, and other baked foods are prepared and sold.",
    "UrduHint": "ایک دکان یا جگہ جہاں روٹی، کیک، کوکیز، پیسٹری اور دیگر بیک کی ہوئی غذائیں تیار اور فروخت کی جاتی ہیں۔"
  },
  {
    "Word": "basket",
    "Hint": "A container usually made from woven material or plastic that is used to carry, store, or organize different objects.",
    "UrduHint": "ایک برتن جو عام طور پر بُنے ہوئے مواد یا پلاسٹک سے بنایا جاتا ہے اور مختلف چیزوں کو اٹھانے، رکھنے یا ترتیب دینے کے لیے استعمال ہوتا ہے۔"
  },
  {
    "Word": "beaver",
    "Hint": "A large water-loving animal with strong teeth and a flat tail that is famous for building dams from wood and branches.",
    "UrduHint": "پانی پسند کرنے والا ایک بڑا جانور جس کے مضبوط دانت اور چپٹی دم ہوتی ہے اور جو لکڑی اور شاخوں سے بند بنانے کے لیے مشہور ہے۔"
  },
  {
    "Word": "bucket",
    "Hint": "A round container with a handle that is commonly used to carry water, clean floors, store materials, or move liquids.",
    "UrduHint": "ایک گول برتن جس میں دستہ ہوتا ہے اور اسے عام طور پر پانی اٹھانے، فرش صاف کرنے، سامان رکھنے یا مائعات منتقل کرنے کے لیے استعمال کیا جاتا ہے۔"
  },
  {
    "Word": "butter",
    "Hint": "A soft yellow dairy product made from cream that is commonly spread on bread or used while cooking and baking.",
    "UrduHint": "کریم سے بنی ہوئی ایک نرم پیلے رنگ کی دودھ کی مصنوعات جسے عام طور پر روٹی پر لگایا جاتا ہے یا کھانا پکانے اور بیکنگ میں استعمال کیا جاتا ہے۔"
  },
  {
    "Word": "cactus",
    "Hint": "A plant that is adapted to dry environments and usually has a thick body that stores water and sharp spines for protection.",
    "UrduHint": "ایک ایسا پودا جو خشک ماحول کے مطابق ڈھلا ہوا ہوتا ہے اور عام طور پر اس کا جسم موٹا ہوتا ہے جس میں پانی محفوظ رہتا ہے اور حفاظت کے لیے تیز کانٹے ہوتے ہیں۔"
  },
  {
    "Word": "cruise",
    "Hint": "A vacation journey taken on a large passenger ship that travels between different coastal cities or countries.",
    "UrduHint": "ایک بڑے مسافر بردار جہاز پر کیا جانے والا تفریحی سفر جو مختلف ساحلی شہروں یا ممالک کے درمیان سفر کرتا ہے۔"
  },
  {
    "Word": "dancer",
    "Hint": "A person who performs controlled body movements, often to music, either for entertainment, exercise, or professional performances.",
    "UrduHint": "ایک شخص جو جسم کی منظم حرکات کرتا ہے، اکثر موسیقی کے ساتھ، چاہے تفریح، ورزش یا پیشہ ورانہ مظاہرے کے لیے۔"
  },
  {
    "Word": "danger",
    "Hint": "A situation or condition that could cause someone to be hurt, damaged, injured, or placed at risk.",
    "UrduHint": "ایسی صورتحال یا حالت جو کسی شخص کو نقصان، چوٹ یا خطرے میں مبتلا کر سکتی ہے۔"
  },
  {
    "Word": "galaxy",
    "Hint": "A huge collection of stars, planets, gas, dust, and other objects held together by gravity, with our solar system inside one.",
    "UrduHint": "ستاروں، سیاروں، گیس، گرد و غبار اور دیگر اجسام کا ایک بہت بڑا مجموعہ جو کششِ ثقل کے ذریعے ایک ساتھ جڑا ہوتا ہے، اور ہمارا نظامِ شمسی بھی ایک کہکشاں میں موجود ہے۔"
  },
  {
    "Word": "garage",
    "Hint": "A building or enclosed space where people park cars and may also keep tools, bicycles, equipment, and other belongings.",
    "UrduHint": "ایک عمارت یا بند جگہ جہاں لوگ گاڑیاں کھڑی کرتے ہیں اور اوزار، سائیکلیں، سامان اور دوسری چیزیں بھی رکھ سکتے ہیں۔"
  },
  {
    "Word": "grapes",
    "Hint": "Small round fruits that grow together in bunches on vines and can be green, red, purple, or almost black when ripe.",
    "UrduHint": "چھوٹے گول پھل جو بیلوں پر گچھوں کی شکل میں اگتے ہیں اور پکنے پر سبز، سرخ، جامنی یا تقریباً کالے ہو سکتے ہیں۔"
  },
  {
    "Word": "harbor",
    "Hint": "A sheltered area along a coast where boats and ships can safely stop, load goods, unload passengers, or wait during bad weather.",
    "UrduHint": "ساحل کے ساتھ ایک محفوظ جگہ جہاں کشتیاں اور جہاز محفوظ طریقے سے رک سکتے ہیں، سامان لاد سکتے ہیں، مسافروں کو اتار سکتے ہیں یا خراب موسم کے دوران انتظار کر سکتے ہیں۔"
  },
  {
    "Word": "jaguar",
    "Hint": "A powerful wild cat with a spotted coat that lives mainly in forests and other parts of Central and South America.",
    "UrduHint": "ایک طاقتور جنگلی بلی نما جانور جس کے جسم پر دھبے ہوتے ہیں اور جو زیادہ تر وسطی اور جنوبی امریکہ کے جنگلات اور دیگر علاقوں میں رہتا ہے۔"
  },
  {
    "Word": "magnet",
    "Hint": "An object that produces a magnetic force and can attract certain metals, especially iron and steel.",
    "UrduHint": "ایک ایسی چیز جو مقناطیسی قوت پیدا کرتی ہے اور کچھ دھاتوں، خاص طور پر لوہے اور اسٹیل، کو اپنی طرف کھینچ سکتی ہے۔"
  },
  {
    "Word": "meadow",
    "Hint": "An open area of grassy land where wildflowers and plants grow and where animals may feed or move around.",
    "UrduHint": "گھاس سے بھری ہوئی کھلی زمین جہاں جنگلی پھول اور پودے اگتے ہیں اور جانور چر سکتے یا گھوم سکتے ہیں۔"
  },
  {
    "Word": "museum",
    "Hint": "A public place where historical objects, artwork, scientific items, cultural artifacts, and other interesting things are collected and displayed.",
    "UrduHint": "ایک عوامی جگہ جہاں تاریخی اشیاء، فن پارے، سائنسی چیزیں، ثقافتی نوادرات اور دیگر دلچسپ چیزیں جمع کرکے نمائش کے لیے رکھی جاتی ہیں۔"
  },
  {
    "Word": "napkin",
    "Hint": "A small piece of paper or cloth used while eating to clean your mouth, hands, or small spills from a table.",
    "UrduHint": "کاغذ یا کپڑے کا ایک چھوٹا ٹکڑا جو کھانے کے دوران منہ، ہاتھ صاف کرنے یا میز پر گرے ہوئے معمولی مائع کو صاف کرنے کے لیے استعمال ہوتا ہے۔"
  },
  {
    "Word": "needle",
    "Hint": "A very thin sharp object with a pointed end and often a small hole that is used for sewing thread through cloth.",
    "UrduHint": "ایک بہت پتلی اور تیز چیز جس کا ایک سرا نوکیلا اور اکثر ایک چھوٹا سوراخ ہوتا ہے، اسے کپڑے میں دھاگا ڈال کر سلائی کرنے کے لیے استعمال کیا جاتا ہے۔"
  },
  {
    "Word": "palace",
    "Hint": "A very large and impressive building where a king, queen, emperor, or other member of royalty may live.",
    "UrduHint": "ایک بہت بڑی اور شاندار عمارت جہاں بادشاہ، ملکہ، شہنشاہ یا شاہی خاندان کا کوئی دوسرا فرد رہ سکتا ہے۔"
  },
  {
    "Word": "parent",
    "Hint": "An adult who has a child and is responsible for caring for, protecting, supporting, and raising that child.",
    "UrduHint": "ایک بالغ شخص جس کا بچہ ہو اور جو اس بچے کی دیکھ بھال، حفاظت، مدد اور پرورش کا ذمہ دار ہو۔"
  },
  {
    "Word": "parrot",
    "Hint": "A colorful bird with a curved beak that can learn to copy sounds and, in some cases, imitate human speech.",
    "UrduHint": "ایک رنگ برنگا پرندہ جس کی چونچ خم دار ہوتی ہے اور جو آوازوں کی نقل کرنا اور بعض صورتوں میں انسانی گفتگو کی نقل کرنا سیکھ سکتا ہے۔"
  },
  {
    "Word": "picnic",
    "Hint": "A meal eaten outdoors, often in a park or natural area, where people bring food, drinks, blankets, and sometimes games.",
    "UrduHint": "باہر کھایا جانے والا کھانا، جو اکثر پارک یا قدرتی جگہ پر ہوتا ہے، جہاں لوگ کھانا، مشروبات، چادریں اور کبھی کبھی کھیل بھی ساتھ لاتے ہیں۔"
  },
  {
    "Word": "pirate",
    "Hint": "A person who attacks or steals from ships at sea, often shown in stories wearing old-fashioned clothing and searching for treasure.",
    "UrduHint": "ایک شخص جو سمندر میں جہازوں پر حملہ کرتا یا ان سے چوری کرتا ہے، اور کہانیوں میں اسے اکثر پرانے زمانے کے لباس میں خزانے کی تلاش کرتے دکھایا جاتا ہے۔"
  },
  {
    "Word": "pocket",
    "Hint": "A small fabric compartment sewn into clothing or a bag where you can keep money, keys, a phone, or other small objects.",
    "UrduHint": "کپڑے یا بیگ میں سلا ہوا کپڑے کا ایک چھوٹا خانہ جہاں پیسے، چابیاں، فون یا دوسری چھوٹی چیزیں رکھی جا سکتی ہیں۔"
  },
  {
    "Word": "puzzle",
    "Hint": "A game or problem that requires you to think carefully and arrange, match, or solve different pieces to find the correct answer.",
    "UrduHint": "ایک کھیل یا مسئلہ جسے حل کرنے کے لیے غور سے سوچنا اور مختلف ٹکڑوں کو ترتیب دینا، ملانا یا حل کرنا ضروری ہوتا ہے۔"
  },
  {
    "Word": "recipe",
    "Hint": "A set of instructions that tells you which ingredients to use and how to prepare and cook a particular food or dish.",
    "UrduHint": "ہدایات کا ایک مجموعہ جو بتاتا ہے کہ کون سے اجزاء استعمال کرنے ہیں اور کسی خاص کھانے یا ڈش کو کیسے تیار اور پکانا ہے۔"
  },
  {
    "Word": "remote",
    "Hint": "A small electronic device with buttons that allows you to control a television, air conditioner, or another device from a distance.",
    "UrduHint": "بٹنوں والا ایک چھوٹا برقی آلہ جس کی مدد سے ٹیلی ویژن، ایئر کنڈیشنر یا کسی دوسرے آلے کو دور سے کنٹرول کیا جا سکتا ہے۔"
  },
  {
    "Word": "runner",
    "Hint": "A person who runs, especially someone who takes part in running for exercise, sport, competition, or fitness.",
    "UrduHint": "ایک شخص جو دوڑتا ہے، خاص طور پر وہ جو ورزش، کھیل، مقابلے یا فٹنس کے لیے دوڑنے میں حصہ لیتا ہے۔"
  },
  {
    "Word": "sailor",
    "Hint": "A person who works or travels on a ship and helps operate the vessel while it is traveling across the water.",
    "UrduHint": "ایک شخص جو جہاز پر کام یا سفر کرتا ہے اور پانی میں سفر کے دوران جہاز چلانے میں مدد کرتا ہے۔"
  },
  {
    "Word": "salmon",
    "Hint": "A type of fish that lives in water and is commonly eaten as food. Some species are known for swimming upstream to lay eggs.",
    "UrduHint": "مچھلی کی ایک قسم جو پانی میں رہتی ہے اور عام طور پر خوراک کے طور پر کھائی جاتی ہے۔ اس کی کچھ اقسام انڈے دینے کے لیے دریا کے بہاؤ کے مخالف سمت تیرنے کے لیے مشہور ہیں۔"
  },
  {
    "Word": "secret",
    "Hint": "Information that is kept hidden from other people because someone does not want them to know or discover it.",
    "UrduHint": "ایسی معلومات جو دوسرے لوگوں سے چھپائی جاتی ہیں کیونکہ کوئی نہیں چاہتا کہ وہ اسے جانیں یا دریافت کریں۔"
  },
  {
    "Word": "shadow",
    "Hint": "A dark shape that appears on the ground or another surface when an object blocks light from reaching that area.",
    "UrduHint": "ایک سیاہ شکل جو زمین یا کسی دوسری سطح پر اس وقت ظاہر ہوتی ہے جب کوئی چیز روشنی کو اس جگہ تک پہنچنے سے روک دیتی ہے۔"
  },
  {
    "Word": "smooth",
    "Hint": "A word used to describe a surface that feels even and soft without rough bumps, sharp edges, or an uneven texture.",
    "UrduHint": "ایسا لفظ جو ایسی سطح کے لیے استعمال ہوتا ہے جو ہموار اور نرم محسوس ہو اور اس پر کھردرے ابھار، تیز کنارے یا ناہموار ساخت نہ ہو۔"
  },
  {
    "Word": "stable",
    "Hint": "A building where horses are kept, fed, and cared for, usually with separate spaces for each animal.",
    "UrduHint": "ایک عمارت جہاں گھوڑوں کو رکھا، کھلایا اور ان کی دیکھ بھال کی جاتی ہے، عام طور پر ہر جانور کے لیے الگ جگہ ہوتی ہے۔"
  },
  {
    "Word": "stream",
    "Hint": "A small natural flow of water that moves across the land and may eventually join a larger river or body of water.",
    "UrduHint": "پانی کا ایک چھوٹا قدرتی بہاؤ جو زمین پر بہتا ہے اور آخرکار کسی بڑے دریا یا آبی ذخیرے میں شامل ہو سکتا ہے۔"
  }
]



# arrHardWords = [
#   {
#     "Word": "abalone",
#     "Hint": "A sea animal that lives on rocks and has a hard shell with a shiny, colorful inside."
#   },
#   {
#     "Word": "balloon",
#     "Hint": "A light and colorful object filled with air or gas that is commonly used at parties and celebrations."
#   },
#   {
#     "Word": "biscuit",
#     "Hint": "A small baked food that can be crunchy or soft and is often eaten with tea, milk, or another drink."
#   },
#   {
#     "Word": "blanket",
#     "Hint": "A large soft piece of cloth that you put over your body to keep yourself warm while sleeping."
#   },
#   {
#     "Word": "cabinet",
#     "Hint": "A piece of furniture with doors or shelves that is used to store dishes, clothes, books, or other things."
#   },
#   {
#     "Word": "coconut",
#     "Hint": "A large tropical fruit with a hard brown shell, white flesh inside, and sweet water in the center."
#   },
#   {
#     "Word": "dolphin",
#     "Hint": "A smart sea animal that swims quickly, lives in groups, and often jumps out of the water."
#   },
#   {
#     "Word": "giraffe",
#     "Hint": "A very tall animal with a very long neck, long legs, and brown patches that eats leaves from trees."
#   },
#   {
#     "Word": "glasses",
#     "Hint": "An object with two lenses that people wear in front of their eyes to help them see more clearly."
#   },
#   {
#     "Word": "lantern",
#     "Hint": "A portable light that can be carried or placed somewhere to help people see when it is dark."
#   },
#   {
#     "Word": "lobster",
#     "Hint": "A sea animal with a hard body, several legs, and two large claws that lives on the ocean floor."
#   },
#   {
#     "Word": "monster",
#     "Hint": "A frightening imaginary creature that is often seen in scary stories, movies, cartoons, and video games."
#   },
#   {
#     "Word": "morning",
#     "Hint": "The early part of the day when people usually wake up, eat breakfast, and prepare for school or work."
#   },
#   {
#     "Word": "noodles",
#     "Hint": "Long thin pieces of food that are usually boiled and served with soup, sauce, vegetables, or meat."
#   },
#   {
#     "Word": "ostrich",
#     "Hint": "A very large bird with a long neck and powerful legs that cannot fly but can run very fast."
#   },
#   {
#     "Word": "penguin",
#     "Hint": "A black-and-white bird that cannot fly but can swim very well and is commonly associated with cold places."
#   },
#   {
#     "Word": "rainbow",
#     "Hint": "A colorful curved shape that sometimes appears in the sky when sunlight shines through rain or water droplets."
#   },
#   {
#     "Word": "sandals",
#     "Hint": "A type of open footwear that leaves much of the foot uncovered and is commonly worn in warm weather."
#   },
#   {
#     "Word": "seagull",
#     "Hint": "A common bird that is often seen flying around beaches, oceans, lakes, and other areas near water."
#   },
#   {
#     "Word": "sunrise",
#     "Hint": "The beautiful time in the morning when the sun begins appearing above the horizon and the sky becomes brighter."
#   },
#   {
#     "Word": "thunder",
#     "Hint": "A loud booming sound heard during a storm, usually after lightning flashes across the sky."
#   },
#   {
#     "Word": "volcano",
#     "Hint": "A mountain with an opening that can release hot lava, ash, smoke, and gases during an eruption."
#   },
#   {
#     "Word": "weather",
#     "Hint": "The condition of the air outside, such as whether it is sunny, rainy, cloudy, windy, hot, or cold."
#   },
#   {
#     "Word": "airport",
#     "Hint": "A large place where airplanes take off and land, with runways and buildings where passengers travel."
#   },
#   {
#     "Word": "bedroom",
#     "Hint": "A room in a house where people usually sleep and keep things such as beds, clothes, pillows, and blankets."
#   },
#   {
#     "Word": "dancing",
#     "Hint": "An activity where a person moves their body in different ways, usually while following music or a rhythm."
#   },
#   {
#     "Word": "diamond",
#     "Hint": "A very hard and valuable shiny stone that is often cut and polished and used to make beautiful jewelry."
#   },
#   {
#     "Word": "firefly",
#     "Hint": "A small flying insect that can produce a natural glowing light from its body, especially at night."
#   },
#   {
#     "Word": "jasmine",
#     "Hint": "A flowering plant with small flowers that are famous for having a strong, sweet, and pleasant smell."
#   },
#   {
#     "Word": "kingdom",
#     "Hint": "A country or territory ruled by a king or queen, often shown in stories with castles and royal families."
#   },
#   {
#     "Word": "library",
#     "Hint": "A quiet place where many books are kept and where people can read, study, or borrow books."
#   },
#   {
#     "Word": "machine",
#     "Hint": "A device made of different parts that uses energy to perform a job or make work easier for people."
#   },
#   {
#     "Word": "pumpkin",
#     "Hint": "A large round vegetable that is usually orange and is used in cooking, pies, soups, and Halloween decorations."
#   },
#   {
#     "Word": "teacher",
#     "Hint": "A person whose job is to teach students different subjects and help them learn new knowledge and skills."
#   },
#   {
#     "Word": "tornado",
#     "Hint": "A powerful spinning column of air that comes from a storm cloud and can cause serious damage when it reaches the ground."
#   },
#   {
#     "Word": "village",
#     "Hint": "A small community where people live, usually with houses, roads, farms, shops, and other buildings."
#   },
#   {
#     "Word": "bicycle",
#     "Hint": "A vehicle with two wheels that a person moves by pushing pedals with their feet."
#   },
#   {
#     "Word": "butterfly",
#     "Hint": "A flying insect with colorful wings that begins life as a caterpillar before changing into its adult form."
#   },
#   {
#     "Word": "carrots",
#     "Hint": "Orange vegetables that grow underground and have a long shape with green leaves growing from the top."
#   },
#   {
#     "Word": "chicken",
#     "Hint": "A common farm bird that has feathers, two legs, and wings, and is also commonly raised for its meat and eggs."
#   },
#   {
#     "Word": "clothes",
#     "Hint": "Things people wear on their bodies, such as shirts, trousers, jackets, dresses, and other pieces of clothing."
#   },
#   {
#     "Word": "country",
#     "Hint": "An area of land with its own government, borders, people, and usually its own national identity."
#   },
#   {
#     "Word": "crystal",
#     "Hint": "A hard solid material that naturally forms with a regular shape and can often look clear, shiny, or colorful."
#   },
#   {
#     "Word": "curtain",
#     "Hint": "A piece of cloth that hangs over a window or doorway and can be opened or closed to block light or provide privacy."
#   },
#   {
#     "Word": "dinosaur",
#     "Hint": "An ancient animal that lived millions of years ago and is known from fossils found by scientists around the world."
#   },
#   {
#     "Word": "emerald",
#     "Hint": "A valuable green gemstone that is often cut and polished and used in rings, necklaces, and other jewelry."
#   },
#   {
#     "Word": "evening",
#     "Hint": "The part of the day that comes after the afternoon and before night, when the sun is going down."
#   },
#   {
#     "Word": "express",
#     "Hint": "To show or communicate a feeling, thought, idea, or opinion using words, actions, writing, or another method."
#   },
#   {
#     "Word": "factory",
#     "Hint": "A large building where machines and workers are used to produce products such as cars, clothes, food, or electronics."
#   },
#   {
#     "Word": "feather",
#     "Hint": "A light structure that grows on the body of a bird and helps protect the bird and, in many birds, helps it fly."
#   },
#   {
#     "Word": "football",
#     "Hint": "A popular team sport where players try to score by moving a ball toward the other team's goal."
#   },
#   {
#     "Word": "freedom",
#     "Hint": "The ability to make your own choices and act without being controlled or unfairly restricted by another person."
#   },
#   {
#     "Word": "garbage",
#     "Hint": "Waste or unwanted things that people throw away after they are no longer useful."
#   },
#   {
#     "Word": "gateway",
#     "Hint": "An entrance or opening that allows people or vehicles to pass from one area into another."
#   },
#   {
#     "Word": "glacier",
#     "Hint": "A huge and slowly moving mass of ice that forms on land in very cold regions."
#   },
#   {
#     "Word": "grocery",
#     "Hint": "Food and household items that people buy from stores, such as vegetables, fruit, milk, bread, and cleaning products."
#   },
#   {
#     "Word": "hammock",
#     "Hint": "A piece of strong fabric or netting that hangs between two supports and is used for relaxing or sleeping."
#   },
#   {
#     "Word": "holiday",
#     "Hint": "A special day or period when people usually do not work or attend school and may relax, travel, or celebrate."
#   },
#   {
#     "Word": "hospital",
#     "Hint": "A place where doctors and nurses treat sick or injured people and provide medical care."
#   },
#   {
#     "Word": "journey",
#     "Hint": "A trip from one place to another, especially when traveling a long distance by car, train, plane, ship, or another vehicle."
#   },
#   {
#     "Word": "kitchen",
#     "Hint": "A room in a house or building where people prepare, cook, and sometimes eat food."
#   },
#   {
#     "Word": "luggage",
#     "Hint": "Bags, suitcases, and other containers that people take with them when traveling."
#   },
#   {
#     "Word": "morning",
#     "Hint": "The first part of the day after the night, when people normally wake up and begin their daily activities."
#   },
#   {
#     "Word": "musical",
#     "Hint": "Something related to music, songs, instruments, singing, or other forms of musical performance."
#   },
#   {
#     "Word": "natural",
#     "Hint": "Something that comes from nature rather than being made or created by people."
#   },
#   {
#     "Word": "newborn",
#     "Hint": "A baby that has been born very recently and is usually only a few days or weeks old."
#   },
#   {
#     "Word": "notebook",
#     "Hint": "A small book made of pages that people use for writing notes, homework, ideas, drawings, or important information."
#   },
#   {
#     "Word": "package",
#     "Hint": "An object or collection of items wrapped or placed inside a box or other container so it can be stored or delivered."
#   },
#   {
#     "Word": "painting",
#     "Hint": "A picture created by putting paint on a surface such as paper, canvas, wood, or a wall."
#   },
#   {
#     "Word": "pancake",
#     "Hint": "A flat, round food made from a liquid batter and cooked in a pan, often served with syrup, fruit, or other toppings."
#   },
#   {
#     "Word": "peacock",
#     "Hint": "A large colorful bird known for the male's beautiful long tail feathers that can spread out like a large fan."
#   },
#   {
#     "Word": "picture",
#     "Hint": "A visual image of a person, place, animal, or object that can be drawn, painted, printed, or shown on a screen."
#   },
#   {
#     "Word": "rainbow",
#     "Hint": "A curved display of many colors that can appear in the sky when sunlight passes through water droplets."
#   },
#   {
#     "Word": "reading",
#     "Hint": "The activity of looking at written words and understanding the information, story, or message they communicate."
#   },
#   {
#     "Word": "roadway",
#     "Hint": "The part of a road designed for vehicles such as cars, buses, motorcycles, and trucks to travel on."
#   },
#   {
#     "Word": "sandwich",
#     "Hint": "A type of food made by placing ingredients such as meat, cheese, vegetables, or eggs between pieces of bread."
#   },
#   {
#     "Word": "seashell",
#     "Hint": "The hard outer shell of a sea animal that people often find washed up on beaches."
#   },
#   {
#     "Word": "shelter",
#     "Hint": "A place that provides protection from rain, wind, heat, cold, danger, or other difficult conditions."
#   },
#   {
#     "Word": "skating",
#     "Hint": "An activity where a person moves across a surface while wearing special shoes or equipment with wheels or blades."
#   },
#   {
#     "Word": "station",
#     "Hint": "A place where buses, trains, or other forms of transportation regularly arrive, stop, and leave with passengers."
#   },
#   {
#     "Word": "teacher",
#     "Hint": "A person who helps students understand lessons, learn new subjects, complete schoolwork, and develop useful skills."
#   },
#   {
#     "Word": "theater",
#     "Hint": "A building or place where people watch live performances, plays, shows, concerts, or other forms of entertainment."
#   },
#   {
#     "Word": "traffic",
#     "Hint": "The movement of cars, buses, motorcycles, trucks, and other vehicles along roads, especially when many vehicles are present."
#   },
#   {
#     "Word": "treasure",
#     "Hint": "A collection of valuable things such as gold, jewels, coins, or precious objects that people may hide or search for."
#   },
#   {
#     "Word": "uniform",
#     "Hint": "A special set of clothes that members of a school, team, company, police force, or other group wear to look similar."
#   },
#   {
#     "Word": "universe",
#     "Hint": "Everything that exists in space, including all galaxies, stars, planets, moons, matter, energy, and space itself."
#   },
#   {
#     "Word": "vehicle",
#     "Hint": "A machine used to transport people or things from one place to another, such as a car, bus, truck, or motorcycle."
#   },
#   {
#     "Word": "visitor",
#     "Hint": "A person who comes to a place for a short time, such as someone's home, a city, a museum, or another location."
#   },
#   {
#     "Word": "walking",
#     "Hint": "The activity of moving from one place to another by taking steps with your feet instead of running or using a vehicle."
#   },
#   {
#     "Word": "warning",
#     "Hint": "A message or sign that tells people about possible danger or a problem so they can be careful."
#   },
#   {
#     "Word": "whistle",
#     "Hint": "A small object or sound that produces a sharp high-pitched noise when air is blown through it."
#   },
#   {
#     "Word": "wildlife",
#     "Hint": "Animals and other living creatures that live naturally in forests, mountains, deserts, oceans, and other natural environments."
#   },
#   {
#     "Word": "windows",
#     "Hint": "Openings in the walls of buildings that usually contain glass and allow sunlight and fresh air to enter rooms."
#   },
#   {
#     "Word": "workout",
#     "Hint": "A period of physical exercise in which a person performs activities to improve strength, fitness, health, or endurance."
#   },
#   {
#     "Word": "yogurts",
#     "Hint": "Creamy foods made from fermented milk that can be eaten plain or mixed with fruit, sugar, honey, or other ingredients."
#   },
#   {
#     "Word": "zealous",
#     "Hint": "A word describing someone who is extremely enthusiastic, energetic, and strongly interested in supporting a person, activity, or cause."
#   },
#   {
#     "Word": "zombies",
#     "Hint": "Fictional creatures that are usually shown as dead people who have returned to life and walk around looking for living people."
#   },
#   {
#     "Word": "teacher",
#     "Hint": "A person who teaches students in a school and helps them understand subjects, complete lessons, and gain knowledge."
#   }
# ]



arrHardWords = [
  {
    "Word": "abalone",
    "Hint": "A sea animal that lives on rocks and has a hard shell with a shiny, colorful inside.",
    "UrduHint": "ایک سمندری جانور جو چٹانوں پر رہتا ہے اور اس کا سخت خول ہوتا ہے جس کا اندرونی حصہ چمکدار اور رنگین ہوتا ہے۔"
  },
  {
    "Word": "balloon",
    "Hint": "A light and colorful object filled with air or gas that is commonly used at parties and celebrations.",
    "UrduHint": "ایک ہلکی اور رنگین چیز جو ہوا یا گیس سے بھری ہوتی ہے اور عام طور پر تقریبات اور جشن میں استعمال ہوتی ہے۔"
  },
  {
    "Word": "biscuit",
    "Hint": "A small baked food that can be crunchy or soft and is often eaten with tea, milk, or another drink.",
    "UrduHint": "ایک چھوٹی بیک کی ہوئی غذا جو خستہ یا نرم ہو سکتی ہے اور اسے اکثر چائے، دودھ یا کسی دوسرے مشروب کے ساتھ کھایا جاتا ہے۔"
  },
  {
    "Word": "blanket",
    "Hint": "A large soft piece of cloth that you put over your body to keep yourself warm while sleeping.",
    "UrduHint": "کپڑے کا ایک بڑا نرم ٹکڑا جسے سوتے وقت جسم پر اوڑھا جاتا ہے تاکہ جسم گرم رہے۔"
  },
  {
    "Word": "cabinet",
    "Hint": "A piece of furniture with doors or shelves that is used to store dishes, clothes, books, or other things.",
    "UrduHint": "فرنیچر کا ایک حصہ جس میں دروازے یا شیلف ہوتے ہیں اور اسے برتن، کپڑے، کتابیں یا دوسری چیزیں رکھنے کے لیے استعمال کیا جاتا ہے۔"
  },
  {
    "Word": "coconut",
    "Hint": "A large tropical fruit with a hard brown shell, white flesh inside, and sweet water in the center.",
    "UrduHint": "ایک بڑا اشنکٹبندیی پھل جس کا سخت بھورا خول، اندر سفید گودا اور درمیان میں میٹھا پانی ہوتا ہے۔"
  },
  {
    "Word": "dolphin",
    "Hint": "A smart sea animal that swims quickly, lives in groups, and often jumps out of the water.",
    "UrduHint": "ایک ذہین سمندری جانور جو تیزی سے تیرتا ہے، گروہوں میں رہتا ہے اور اکثر پانی سے باہر چھلانگ لگاتا ہے۔"
  },
  {
    "Word": "giraffe",
    "Hint": "A very tall animal with a very long neck, long legs, and brown patches that eats leaves from trees.",
    "UrduHint": "ایک بہت لمبا جانور جس کی گردن اور ٹانگیں بہت لمبی ہوتی ہیں اور جسم پر بھورے دھبے ہوتے ہیں، یہ درختوں کے پتے کھاتا ہے۔"
  },
  {
    "Word": "glasses",
    "Hint": "An object with two lenses that people wear in front of their eyes to help them see more clearly.",
    "UrduHint": "دو عدسوں والی ایک چیز جو لوگ آنکھوں کے سامنے پہنتے ہیں تاکہ انہیں زیادہ واضح نظر آنے میں مدد ملے۔"
  },
  {
    "Word": "lantern",
    "Hint": "A portable light that can be carried or placed somewhere to help people see when it is dark.",
    "UrduHint": "ایک قابلِ نقل روشنی جسے اٹھا کر لے جایا یا کہیں رکھا جا سکتا ہے تاکہ اندھیرے میں دیکھنے میں مدد ملے۔"
  },
  {
    "Word": "lobster",
    "Hint": "A sea animal with a hard body, several legs, and two large claws that lives on the ocean floor.",
    "UrduHint": "ایک سمندری جانور جس کا جسم سخت، کئی ٹانگیں اور دو بڑے پنجے ہوتے ہیں اور یہ سمندر کی تہہ میں رہتا ہے۔"
  },
  {
    "Word": "monster",
    "Hint": "A frightening imaginary creature that is often seen in scary stories, movies, cartoons, and video games.",
    "UrduHint": "ایک خوفناک خیالی مخلوق جسے اکثر ڈراؤنی کہانیوں، فلموں، کارٹونز اور ویڈیو گیمز میں دکھایا جاتا ہے۔"
  },
  {
    "Word": "morning",
    "Hint": "The early part of the day when people usually wake up, eat breakfast, and prepare for school or work.",
    "UrduHint": "دن کا ابتدائی حصہ جب لوگ عام طور پر اٹھتے ہیں، ناشتہ کرتے ہیں اور اسکول یا کام کے لیے تیار ہوتے ہیں۔"
  },
  {
    "Word": "noodles",
    "Hint": "Long thin pieces of food that are usually boiled and served with soup, sauce, vegetables, or meat.",
    "UrduHint": "کھانے کے لمبے اور پتلے ٹکڑے جو عام طور پر ابال کر سوپ، چٹنی، سبزیوں یا گوشت کے ساتھ پیش کیے جاتے ہیں۔"
  },
  {
    "Word": "ostrich",
    "Hint": "A very large bird with a long neck and powerful legs that cannot fly but can run very fast.",
    "UrduHint": "ایک بہت بڑا پرندہ جس کی گردن لمبی اور ٹانگیں طاقتور ہوتی ہیں، یہ اڑ نہیں سکتا لیکن بہت تیزی سے دوڑ سکتا ہے۔"
  },
  {
    "Word": "penguin",
    "Hint": "A black-and-white bird that cannot fly but can swim very well and is commonly associated with cold places.",
    "UrduHint": "ایک سیاہ اور سفید پرندہ جو اڑ نہیں سکتا لیکن بہت اچھی طرح تیر سکتا ہے اور عام طور پر سرد علاقوں سے وابستہ ہے۔"
  },
  {
    "Word": "rainbow",
    "Hint": "A colorful curved shape that sometimes appears in the sky when sunlight shines through rain or water droplets.",
    "UrduHint": "ایک رنگین خم دار شکل جو کبھی کبھی آسمان پر اس وقت ظاہر ہوتی ہے جب سورج کی روشنی بارش یا پانی کے قطروں سے گزرتی ہے۔"
  },
  {
    "Word": "sandals",
    "Hint": "A type of open footwear that leaves much of the foot uncovered and is commonly worn in warm weather.",
    "UrduHint": "کھلے جوتوں کی ایک قسم جو پاؤں کے زیادہ تر حصے کو ڈھانپتی نہیں اور عام طور پر گرم موسم میں پہنی جاتی ہے۔"
  },
  {
    "Word": "seagull",
    "Hint": "A common bird that is often seen flying around beaches, oceans, lakes, and other areas near water.",
    "UrduHint": "ایک عام پرندہ جو اکثر ساحلوں، سمندروں، جھیلوں اور پانی کے قریب دوسرے علاقوں میں اڑتا ہوا نظر آتا ہے۔"
  },
  {
    "Word": "sunrise",
    "Hint": "The beautiful time in the morning when the sun begins appearing above the horizon and the sky becomes brighter.",
    "UrduHint": "صبح کا خوبصورت وقت جب سورج افق کے اوپر ظاہر ہونا شروع ہوتا ہے اور آسمان روشن ہونے لگتا ہے۔"
  },
  {
    "Word": "thunder",
    "Hint": "A loud booming sound heard during a storm, usually after lightning flashes across the sky.",
    "UrduHint": "طوفان کے دوران سنائی دینے والی ایک بلند گرج دار آواز جو عام طور پر آسمان پر بجلی چمکنے کے بعد سنائی دیتی ہے۔"
  },
  {
    "Word": "volcano",
    "Hint": "A mountain with an opening that can release hot lava, ash, smoke, and gases during an eruption.",
    "UrduHint": "ایک پہاڑ جس میں ایک سوراخ یا دہانہ ہوتا ہے جہاں سے پھٹنے کے دوران گرم لاوا، راکھ، دھواں اور گیسیں خارج ہو سکتی ہیں۔"
  },
  {
    "Word": "weather",
    "Hint": "The condition of the air outside, such as whether it is sunny, rainy, cloudy, windy, hot, or cold.",
    "UrduHint": "باہر کی ہوا اور ماحول کی حالت، جیسے دھوپ، بارش، بادل، ہوا، گرمی یا سردی کا ہونا۔"
  },
  {
    "Word": "airport",
    "Hint": "A large place where airplanes take off and land, with runways and buildings where passengers travel.",
    "UrduHint": "ایک بڑی جگہ جہاں ہوائی جہاز اڑان بھرتے اور اترتے ہیں، اور جہاں رن وے اور مسافروں کے لیے عمارتیں موجود ہوتی ہیں۔"
  },
  {
    "Word": "bedroom",
    "Hint": "A room in a house where people usually sleep and keep things such as beds, clothes, pillows, and blankets.",
    "UrduHint": "گھر کا ایک کمرہ جہاں لوگ عام طور پر سوتے ہیں اور بستر، کپڑے، تکیے اور کمبل جیسی چیزیں رکھتے ہیں۔"
  },
  {
    "Word": "dancing",
    "Hint": "An activity where a person moves their body in different ways, usually while following music or a rhythm.",
    "UrduHint": "ایک سرگرمی جس میں انسان عام طور پر موسیقی یا تال کے ساتھ اپنے جسم کو مختلف انداز میں حرکت دیتا ہے۔"
  },
  {
    "Word": "diamond",
    "Hint": "A very hard and valuable shiny stone that is often cut and polished and used to make beautiful jewelry.",
    "UrduHint": "ایک بہت سخت، قیمتی اور چمکدار پتھر جسے اکثر تراش کر پالش کیا جاتا ہے اور خوبصورت زیورات بنانے کے لیے استعمال کیا جاتا ہے۔"
  },
  {
    "Word": "firefly",
    "Hint": "A small flying insect that can produce a natural glowing light from its body, especially at night.",
    "UrduHint": "ایک چھوٹا اڑنے والا کیڑا جو اپنے جسم سے قدرتی روشنی پیدا کر سکتا ہے، خاص طور پر رات کے وقت۔"
  },
  {
    "Word": "jasmine",
    "Hint": "A flowering plant with small flowers that are famous for having a strong, sweet, and pleasant smell.",
    "UrduHint": "ایک پھولدار پودا جس کے چھوٹے پھول اپنی تیز، میٹھی اور خوشگوار خوشبو کے لیے مشہور ہیں۔"
  },
  {
    "Word": "kingdom",
    "Hint": "A country or territory ruled by a king or queen, often shown in stories with castles and royal families.",
    "UrduHint": "ایک ملک یا علاقہ جس پر بادشاہ یا ملکہ حکومت کرتے ہیں، اور کہانیوں میں اسے اکثر قلعوں اور شاہی خاندانوں کے ساتھ دکھایا جاتا ہے۔"
  },
  {
    "Word": "library",
    "Hint": "A quiet place where many books are kept and where people can read, study, or borrow books.",
    "UrduHint": "ایک پُرسکون جگہ جہاں بہت سی کتابیں رکھی جاتی ہیں اور لوگ پڑھ، مطالعہ یا کتابیں ادھار لے سکتے ہیں۔"
  },
  {
    "Word": "machine",
    "Hint": "A device made of different parts that uses energy to perform a job or make work easier for people.",
    "UrduHint": "مختلف حصوں سے بنا ہوا ایک آلہ جو توانائی استعمال کرکے کوئی کام انجام دیتا ہے یا لوگوں کے لیے کام آسان بناتا ہے۔"
  },
  {
    "Word": "pumpkin",
    "Hint": "A large round vegetable that is usually orange and is used in cooking, pies, soups, and Halloween decorations.",
    "UrduHint": "ایک بڑی گول سبزی جو عام طور پر نارنجی رنگ کی ہوتی ہے اور کھانا پکانے، پائی، سوپ اور ہالووین کی سجاوٹ میں استعمال ہوتی ہے۔"
  },
  {
    "Word": "teacher",
    "Hint": "A person whose job is to teach students different subjects and help them learn new knowledge and skills.",
    "UrduHint": "ایک شخص جس کا کام طلبہ کو مختلف مضامین پڑھانا اور انہیں نئی معلومات اور مہارتیں سیکھنے میں مدد دینا ہے۔"
  },
  {
    "Word": "tornado",
    "Hint": "A powerful spinning column of air that comes from a storm cloud and can cause serious damage when it reaches the ground.",
    "UrduHint": "ہوا کا ایک طاقتور گھومتا ہوا ستون جو طوفانی بادل سے بنتا ہے اور زمین تک پہنچنے پر شدید نقصان پہنچا سکتا ہے۔"
  },
  {
    "Word": "village",
    "Hint": "A small community where people live, usually with houses, roads, farms, shops, and other buildings.",
    "UrduHint": "ایک چھوٹی آبادی جہاں لوگ رہتے ہیں اور جہاں عام طور پر گھر، سڑکیں، کھیت، دکانیں اور دوسری عمارتیں ہوتی ہیں۔"
  },
  {
    "Word": "bicycle",
    "Hint": "A vehicle with two wheels that a person moves by pushing pedals with their feet.",
    "UrduHint": "دو پہیوں والی ایک سواری جسے انسان اپنے پاؤں سے پیڈل چلا کر حرکت دیتا ہے۔"
  },
  {
    "Word": "butterfly",
    "Hint": "A flying insect with colorful wings that begins life as a caterpillar before changing into its adult form.",
    "UrduHint": "ایک اڑنے والا کیڑا جس کے رنگین پر ہوتے ہیں اور جو بالغ شکل اختیار کرنے سے پہلے سنڈی کی صورت میں زندگی شروع کرتا ہے۔"
  },
  {
    "Word": "carrots",
    "Hint": "Orange vegetables that grow underground and have a long shape with green leaves growing from the top.",
    "UrduHint": "نارنجی رنگ کی سبزیاں جو زمین کے اندر اگتی ہیں اور لمبی شکل رکھتی ہیں جبکہ اوپر سبز پتے نکلتے ہیں۔"
  },
  {
    "Word": "chicken",
    "Hint": "A common farm bird that has feathers, two legs, and wings, and is also commonly raised for its meat and eggs.",
    "UrduHint": "ایک عام پالتو پرندہ جس کے پر، دو ٹانگیں اور پر ہوتے ہیں اور اسے عام طور پر گوشت اور انڈوں کے لیے بھی پالا جاتا ہے۔"
  },
  {
    "Word": "clothes",
    "Hint": "Things people wear on their bodies, such as shirts, trousers, jackets, dresses, and other pieces of clothing.",
    "UrduHint": "وہ چیزیں جو لوگ اپنے جسم پر پہنتے ہیں، جیسے قمیضیں، پتلون، جیکٹس، لباس اور دیگر کپڑے۔"
  },
  {
    "Word": "country",
    "Hint": "An area of land with its own government, borders, people, and usually its own national identity.",
    "UrduHint": "زمین کا ایک علاقہ جس کی اپنی حکومت، سرحدیں، لوگ اور عام طور پر اپنی قومی شناخت ہوتی ہے۔"
  },
  {
    "Word": "crystal",
    "Hint": "A hard solid material that naturally forms with a regular shape and can often look clear, shiny, or colorful.",
    "UrduHint": "ایک سخت ٹھوس مادہ جو قدرتی طور پر باقاعدہ شکل میں بنتا ہے اور اکثر شفاف، چمکدار یا رنگین دکھائی دے سکتا ہے۔"
  },
  {
    "Word": "curtain",
    "Hint": "A piece of cloth that hangs over a window or doorway and can be opened or closed to block light or provide privacy.",
    "UrduHint": "کپڑے کا ایک ٹکڑا جو کھڑکی یا دروازے کے سامنے لٹکتا ہے اور روشنی روکنے یا پردہ فراہم کرنے کے لیے کھولا یا بند کیا جا سکتا ہے۔"
  },
  {
    "Word": "dinosaur",
    "Hint": "An ancient animal that lived millions of years ago and is known from fossils found by scientists around the world.",
    "UrduHint": "ایک قدیم جانور جو لاکھوں سال پہلے زندہ تھا اور دنیا بھر میں سائنس دانوں کو ملنے والے فوسلز سے اس کے بارے میں معلومات حاصل ہوئی ہیں۔"
  },
  {
    "Word": "emerald",
    "Hint": "A valuable green gemstone that is often cut and polished and used in rings, necklaces, and other jewelry.",
    "UrduHint": "ایک قیمتی سبز جواہر جسے اکثر تراش کر پالش کیا جاتا ہے اور انگوٹھیوں، ہاروں اور دیگر زیورات میں استعمال کیا جاتا ہے۔"
  },
  {
    "Word": "evening",
    "Hint": "The part of the day that comes after the afternoon and before night, when the sun is going down.",
    "UrduHint": "دن کا وہ حصہ جو دوپہر کے بعد اور رات سے پہلے آتا ہے، جب سورج غروب ہونے لگتا ہے۔"
  },
  {
    "Word": "express",
    "Hint": "To show or communicate a feeling, thought, idea, or opinion using words, actions, writing, or another method.",
    "UrduHint": "الفاظ، اعمال، تحریر یا کسی دوسرے طریقے سے کسی احساس، خیال، تصور یا رائے کو ظاہر یا بیان کرنا۔"
  },
  {
    "Word": "factory",
    "Hint": "A large building where machines and workers are used to produce products such as cars, clothes, food, or electronics.",
    "UrduHint": "ایک بڑی عمارت جہاں مشینوں اور کارکنوں کی مدد سے کاریں، کپڑے، کھانے کی اشیاء یا برقی آلات جیسی مصنوعات تیار کی جاتی ہیں۔"
  },
  {
    "Word": "feather",
    "Hint": "A light structure that grows on the body of a bird and helps protect the bird and, in many birds, helps it fly.",
    "UrduHint": "ایک ہلکی ساخت جو پرندے کے جسم پر اگتی ہے اور پرندے کی حفاظت میں مدد دیتی ہے، جبکہ بہت سے پرندوں میں اڑنے میں بھی مدد کرتی ہے۔"
  },
  {
    "Word": "football",
    "Hint": "A popular team sport where players try to score by moving a ball toward the other team's goal.",
    "UrduHint": "ایک مشہور ٹیم کا کھیل جس میں کھلاڑی گیند کو مخالف ٹیم کے گول کی طرف لے جا کر گول کرنے کی کوشش کرتے ہیں۔"
  },
  {
    "Word": "freedom",
    "Hint": "The ability to make your own choices and act without being controlled or unfairly restricted by another person.",
    "UrduHint": "اپنے فیصلے خود کرنے اور کسی دوسرے شخص کے قابو یا غیر منصفانہ پابندی کے بغیر عمل کرنے کی صلاحیت۔"
  },
  {
    "Word": "garbage",
    "Hint": "Waste or unwanted things that people throw away after they are no longer useful.",
    "UrduHint": "وہ فضلہ یا غیر ضروری چیزیں جنہیں لوگ اس وقت پھینک دیتے ہیں جب وہ مزید استعمال کے قابل نہیں رہتیں۔"
  },
  {
    "Word": "gateway",
    "Hint": "An entrance or opening that allows people or vehicles to pass from one area into another.",
    "UrduHint": "ایک داخلی راستہ یا کھلا حصہ جو لوگوں یا گاڑیوں کو ایک علاقے سے دوسرے علاقے میں جانے کی اجازت دیتا ہے۔"
  },
  {
    "Word": "glacier",
    "Hint": "A huge and slowly moving mass of ice that forms on land in very cold regions.",
    "UrduHint": "برف کا ایک بہت بڑا اور آہستہ حرکت کرنے والا ذخیرہ جو انتہائی سرد علاقوں میں زمین پر بنتا ہے۔"
  },
  {
    "Word": "grocery",
    "Hint": "Food and household items that people buy from stores, such as vegetables, fruit, milk, bread, and cleaning products.",
    "UrduHint": "کھانے اور گھریلو استعمال کی وہ چیزیں جو لوگ دکانوں سے خریدتے ہیں، جیسے سبزیاں، پھل، دودھ، روٹی اور صفائی کی مصنوعات۔"
  },
  {
    "Word": "hammock",
    "Hint": "A piece of strong fabric or netting that hangs between two supports and is used for relaxing or sleeping.",
    "UrduHint": "مضبوط کپڑے یا جالی کا ایک ٹکڑا جو دو سہاروں کے درمیان لٹکا ہوتا ہے اور آرام کرنے یا سونے کے لیے استعمال کیا جاتا ہے۔"
  },
  {
    "Word": "holiday",
    "Hint": "A special day or period when people usually do not work or attend school and may relax, travel, or celebrate.",
    "UrduHint": "ایک خاص دن یا مدت جب لوگ عام طور پر کام یا اسکول نہیں جاتے اور آرام، سفر یا جشن منا سکتے ہیں۔"
  },
  {
    "Word": "hospital",
    "Hint": "A place where doctors and nurses treat sick or injured people and provide medical care.",
    "UrduHint": "ایک ایسی جگہ جہاں ڈاکٹر اور نرسیں بیمار یا زخمی لوگوں کا علاج کرتی ہیں اور طبی دیکھ بھال فراہم کرتی ہیں۔"
  },
  {
    "Word": "journey",
    "Hint": "A trip from one place to another, especially when traveling a long distance by car, train, plane, ship, or another vehicle.",
    "UrduHint": "ایک جگہ سے دوسری جگہ کا سفر، خاص طور پر جب کار، ٹرین، ہوائی جہاز، جہاز یا کسی دوسری سواری سے لمبا فاصلہ طے کیا جائے۔"
  },
  {
    "Word": "kitchen",
    "Hint": "A room in a house or building where people prepare, cook, and sometimes eat food.",
    "UrduHint": "گھر یا عمارت کا ایک کمرہ جہاں لوگ کھانا تیار اور پکاتے ہیں اور کبھی کبھی وہیں کھانا بھی کھاتے ہیں۔"
  },
  {
    "Word": "luggage",
    "Hint": "Bags, suitcases, and other containers that people take with them when traveling.",
    "UrduHint": "بیگ، سوٹ کیس اور دوسرے ڈبے یا سامان جو لوگ سفر کے دوران اپنے ساتھ لے جاتے ہیں۔"
  },
  {
    "Word": "morning",
    "Hint": "The first part of the day after the night, when people normally wake up and begin their daily activities.",
    "UrduHint": "رات کے بعد دن کا پہلا حصہ جب لوگ عام طور پر جاگتے ہیں اور اپنی روزمرہ کی سرگرمیاں شروع کرتے ہیں۔"
  },
  {
    "Word": "musical",
    "Hint": "Something related to music, songs, instruments, singing, or other forms of musical performance.",
    "UrduHint": "ایسی چیز جو موسیقی، گانوں، آلات، گانے یا موسیقی کی دوسری قسم کی پیشکش سے متعلق ہو۔"
  },
  {
    "Word": "natural",
    "Hint": "Something that comes from nature rather than being made or created by people.",
    "UrduHint": "ایسی چیز جو انسانوں کی بنائی یا تخلیق کردہ ہونے کے بجائے قدرت سے حاصل ہو۔"
  },
  {
    "Word": "newborn",
    "Hint": "A baby that has been born very recently and is usually only a few days or weeks old.",
    "UrduHint": "ایک بچہ جو بہت حال ہی میں پیدا ہوا ہو اور عام طور پر صرف چند دن یا ہفتے کا ہو۔"
  },
  {
    "Word": "notebook",
    "Hint": "A small book made of pages that people use for writing notes, homework, ideas, drawings, or important information.",
    "UrduHint": "صفحات سے بنی ایک چھوٹی کتاب جسے لوگ نوٹس، ہوم ورک، خیالات، ڈرائنگ یا اہم معلومات لکھنے کے لیے استعمال کرتے ہیں۔"
  },
  {
    "Word": "package",
    "Hint": "An object or collection of items wrapped or placed inside a box or other container so it can be stored or delivered.",
    "UrduHint": "ایک چیز یا اشیاء کا مجموعہ جسے لپیٹ کر یا ڈبے یا کسی دوسرے برتن میں رکھ کر محفوظ یا پہنچایا جاتا ہے۔"
  },
  {
    "Word": "painting",
    "Hint": "A picture created by putting paint on a surface such as paper, canvas, wood, or a wall.",
    "UrduHint": "ایک تصویر جو کاغذ، کینوس، لکڑی یا دیوار جیسی سطح پر رنگ لگا کر بنائی جاتی ہے۔"
  },
  {
    "Word": "pancake",
    "Hint": "A flat, round food made from a liquid batter and cooked in a pan, often served with syrup, fruit, or other toppings.",
    "UrduHint": "مائع آمیزے سے بنائی جانے والی ایک چپٹی اور گول غذا جو پین میں پکائی جاتی ہے اور اکثر شربت، پھل یا دیگر چیزوں کے ساتھ پیش کی جاتی ہے۔"
  },
  {
    "Word": "peacock",
    "Hint": "A large colorful bird known for the male's beautiful long tail feathers that can spread out like a large fan.",
    "UrduHint": "ایک بڑا رنگین پرندہ جو نر کے خوبصورت لمبے دُم کے پروں کے لیے مشہور ہے، جنہیں وہ بڑے پنکھے کی طرح پھیلا سکتا ہے۔"
  },
  {
    "Word": "picture",
    "Hint": "A visual image of a person, place, animal, or object that can be drawn, painted, printed, or shown on a screen.",
    "UrduHint": "کسی شخص، جگہ، جانور یا چیز کی بصری تصویر جسے بنایا، پینٹ، پرنٹ یا اسکرین پر دکھایا جا سکتا ہے۔"
  },
  {
    "Word": "rainbow",
    "Hint": "A curved display of many colors that can appear in the sky when sunlight passes through water droplets.",
    "UrduHint": "کئی رنگوں کا ایک خم دار منظر جو اس وقت آسمان پر ظاہر ہو سکتا ہے جب سورج کی روشنی پانی کے قطروں سے گزرتی ہے۔"
  },
  {
    "Word": "reading",
    "Hint": "The activity of looking at written words and understanding the information, story, or message they communicate.",
    "UrduHint": "لکھے ہوئے الفاظ کو دیکھنے اور ان سے حاصل ہونے والی معلومات، کہانی یا پیغام کو سمجھنے کی سرگرمی۔"
  },
  {
    "Word": "roadway",
    "Hint": "The part of a road designed for vehicles such as cars, buses, motorcycles, and trucks to travel on.",
    "UrduHint": "سڑک کا وہ حصہ جو کاروں، بسوں، موٹر سائیکلوں اور ٹرکوں جیسی گاڑیوں کے سفر کے لیے بنایا گیا ہوتا ہے۔"
  },
  {
    "Word": "sandwich",
    "Hint": "A type of food made by placing ingredients such as meat, cheese, vegetables, or eggs between pieces of bread.",
    "UrduHint": "ایک قسم کی غذا جس میں گوشت، پنیر، سبزیاں یا انڈے جیسی چیزیں روٹی کے ٹکڑوں کے درمیان رکھی جاتی ہیں۔"
  },
  {
    "Word": "seashell",
    "Hint": "The hard outer shell of a sea animal that people often find washed up on beaches.",
    "UrduHint": "سمندری جانور کا سخت بیرونی خول جو لوگوں کو اکثر ساحل پر پانی کے ساتھ بہہ کر آیا ہوا ملتا ہے۔"
  },
  {
    "Word": "shelter",
    "Hint": "A place that provides protection from rain, wind, heat, cold, danger, or other difficult conditions.",
    "UrduHint": "ایک ایسی جگہ جو بارش، ہوا، گرمی، سردی، خطرے یا دیگر مشکل حالات سے تحفظ فراہم کرتی ہے۔"
  },
  {
    "Word": "skating",
    "Hint": "An activity where a person moves across a surface while wearing special shoes or equipment with wheels or blades.",
    "UrduHint": "ایک سرگرمی جس میں انسان پہیوں یا بلیڈ والے خاص جوتے یا سامان پہن کر کسی سطح پر حرکت کرتا ہے۔"
  },
  {
    "Word": "station",
    "Hint": "A place where buses, trains, or other forms of transportation regularly arrive, stop, and leave with passengers.",
    "UrduHint": "ایک ایسی جگہ جہاں بسیں، ٹرینیں یا دوسری سواریوں کے ذرائع باقاعدگی سے آتے، رکتے اور مسافروں کو لے کر روانہ ہوتے ہیں۔"
  },
  {
    "Word": "teacher",
    "Hint": "A person who helps students understand lessons, learn new subjects, complete schoolwork, and develop useful skills.",
    "UrduHint": "ایک شخص جو طلبہ کو اسباق سمجھنے، نئے مضامین سیکھنے، اسکول کا کام مکمل کرنے اور مفید مہارتیں پیدا کرنے میں مدد دیتا ہے۔"
  },
  {
    "Word": "theater",
    "Hint": "A building or place where people watch live performances, plays, shows, concerts, or other forms of entertainment.",
    "UrduHint": "ایک عمارت یا جگہ جہاں لوگ براہ راست پرفارمنس، ڈرامے، شوز، کنسرٹس یا تفریح کی دوسری شکلیں دیکھتے ہیں۔"
  },
  {
    "Word": "traffic",
    "Hint": "The movement of cars, buses, motorcycles, trucks, and other vehicles along roads, especially when many vehicles are present.",
    "UrduHint": "سڑکوں پر کاروں، بسوں، موٹر سائیکلوں، ٹرکوں اور دوسری گاڑیوں کی نقل و حرکت، خاص طور پر جب بہت سی گاڑیاں موجود ہوں۔"
  },
  {
    "Word": "treasure",
    "Hint": "A collection of valuable things such as gold, jewels, coins, or precious objects that people may hide or search for.",
    "UrduHint": "قیمتی چیزوں کا مجموعہ جیسے سونا، زیورات، سکے یا قیمتی اشیاء جنہیں لوگ چھپا سکتے یا تلاش کر سکتے ہیں۔"
  },
  {
    "Word": "uniform",
    "Hint": "A special set of clothes that members of a school, team, company, police force, or other group wear to look similar.",
    "UrduHint": "کپڑوں کا ایک خاص لباس جو اسکول، ٹیم، کمپنی، پولیس یا کسی دوسرے گروپ کے ارکان ایک جیسا نظر آنے کے لیے پہنتے ہیں۔"
  },
  {
    "Word": "universe",
    "Hint": "Everything that exists in space, including all galaxies, stars, planets, moons, matter, energy, and space itself.",
    "UrduHint": "خلا میں موجود ہر چیز، جس میں تمام کہکشائیں، ستارے، سیارے، چاند، مادہ، توانائی اور خود خلا بھی شامل ہیں۔"
  },
  {
    "Word": "vehicle",
    "Hint": "A machine used to transport people or things from one place to another, such as a car, bus, truck, or motorcycle.",
    "UrduHint": "ایک مشین جو لوگوں یا چیزوں کو ایک جگہ سے دوسری جگہ لے جانے کے لیے استعمال ہوتی ہے، جیسے کار، بس، ٹرک یا موٹر سائیکل۔"
  },
  {
    "Word": "visitor",
    "Hint": "A person who comes to a place for a short time, such as someone's home, a city, a museum, or another location.",
    "UrduHint": "ایک شخص جو تھوڑی دیر کے لیے کسی جگہ آتا ہے، جیسے کسی کا گھر، شہر، عجائب گھر یا کوئی دوسری جگہ۔"
  },
  {
    "Word": "walking",
    "Hint": "The activity of moving from one place to another by taking steps with your feet instead of running or using a vehicle.",
    "UrduHint": "ایک جگہ سے دوسری جگہ پاؤں سے قدم اٹھا کر جانے کی سرگرمی، جس میں دوڑنے یا کسی گاڑی کے بجائے پیدل چلا جاتا ہے۔"
  },
  {
    "Word": "warning",
    "Hint": "A message or sign that tells people about possible danger or a problem so they can be careful.",
    "UrduHint": "ایک پیغام یا نشان جو لوگوں کو ممکنہ خطرے یا مسئلے کے بارے میں بتاتا ہے تاکہ وہ محتاط رہ سکیں۔"
  },
  {
    "Word": "whistle",
    "Hint": "A small object or sound that produces a sharp high-pitched noise when air is blown through it.",
    "UrduHint": "ایک چھوٹی چیز یا آواز جو اس میں سے ہوا گزرنے پر تیز اور اونچی آواز پیدا کرتی ہے۔"
  },
  {
    "Word": "wildlife",
    "Hint": "Animals and other living creatures that live naturally in forests, mountains, deserts, oceans, and other natural environments.",
    "UrduHint": "جانور اور دوسری جاندار مخلوقات جو قدرتی طور پر جنگلات، پہاڑوں، صحراؤں، سمندروں اور دیگر قدرتی ماحول میں رہتی ہیں۔"
  },
  {
    "Word": "windows",
    "Hint": "Openings in the walls of buildings that usually contain glass and allow sunlight and fresh air to enter rooms.",
    "UrduHint": "عمارتوں کی دیواروں میں موجود کھلے حصے جن میں عام طور پر شیشہ لگا ہوتا ہے اور جو سورج کی روشنی اور تازہ ہوا کو کمروں میں داخل ہونے دیتے ہیں۔"
  },
  {
    "Word": "workout",
    "Hint": "A period of physical exercise in which a person performs activities to improve strength, fitness, health, or endurance.",
    "UrduHint": "جسمانی ورزش کا ایک دورانیہ جس میں انسان طاقت، فٹنس، صحت یا برداشت بہتر بنانے کے لیے مختلف سرگرمیاں کرتا ہے۔"
  },
  {
    "Word": "yogurts",
    "Hint": "Creamy foods made from fermented milk that can be eaten plain or mixed with fruit, sugar, honey, or other ingredients.",
    "UrduHint": "خمیر شدہ دودھ سے بنی کریمی غذائیں جنہیں سادہ یا پھل، چینی، شہد یا دیگر اجزاء کے ساتھ ملا کر کھایا جا سکتا ہے۔"
  },
  {
    "Word": "zealous",
    "Hint": "A word describing someone who is extremely enthusiastic, energetic, and strongly interested in supporting a person, activity, or cause.",
    "UrduHint": "ایسا لفظ جو ایسے شخص کے لیے استعمال ہوتا ہے جو بہت زیادہ پُرجوش، سرگرم اور کسی شخص، سرگرمی یا مقصد کی حمایت میں گہری دلچسپی رکھتا ہو۔"
  },
  {
    "Word": "zombies",
    "Hint": "Fictional creatures that are usually shown as dead people who have returned to life and walk around looking for living people.",
    "UrduHint": "خیالی مخلوقات جنہیں عام طور پر ایسے مردہ لوگوں کے طور پر دکھایا جاتا ہے جو دوبارہ زندہ ہو گئے ہوں اور زندہ لوگوں کو تلاش کرتے پھرتے ہوں۔"
  },
  {
    "Word": "teacher",
    "Hint": "A person who teaches students in a school and helps them understand subjects, complete lessons, and gain knowledge.",
    "UrduHint": "ایک شخص جو اسکول میں طلبہ کو پڑھاتا ہے اور انہیں مضامین سمجھنے، اسباق مکمل کرنے اور علم حاصل کرنے میں مدد دیتا ہے۔"
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
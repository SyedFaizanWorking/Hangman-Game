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
    "Word": "apple",
    "Hint": "A round fruit that can be red, green, or yellow and grows on trees."
  },
  {
    "Word": "bread",
    "Hint": "A baked food made from flour that people commonly eat with meals."
  },
  {
    "Word": "chair",
    "Hint": "A piece of furniture made for one person to sit on."
  },
  {
    "Word": "table",
    "Hint": "A piece of furniture with a flat top and legs used for eating or working."
  },
  {
    "Word": "house",
    "Hint": "A building where people live, sleep, cook, and relax."
  },
  {
    "Word": "water",
    "Hint": "A clear liquid that people, animals, and plants need to survive."
  },
  {
    "Word": "earth",
    "Hint": "The planet where humans, animals, and plants live."
  },
  {
    "Word": "cloud",
    "Hint": "A white or gray mass in the sky made from tiny water droplets."
  },
  {
    "Word": "plant",
    "Hint": "A living thing that grows in soil and usually has roots, stems, and leaves."
  },
  {
    "Word": "grass",
    "Hint": "A green plant that commonly covers lawns, fields, and gardens."
  },
  {
    "Word": "green",
    "Hint": "The color commonly seen on leaves and grass."
  },
  {
    "Word": "black",
    "Hint": "A very dark color like the night sky."
  },
  {
    "Word": "white",
    "Hint": "A bright color like snow, milk, or a clean sheet of paper."
  },
  {
    "Word": "brown",
    "Hint": "An earthy color commonly seen in soil, wood, and tree trunks."
  },
  {
    "Word": "happy",
    "Hint": "A feeling you have when you are joyful, pleased, or having a good time."
  },
  {
    "Word": "angry",
    "Hint": "A strong feeling you may have when something upsetting happens."
  },
  {
    "Word": "smile",
    "Hint": "The happy expression you make by moving the corners of your mouth upward."
  },
  {
    "Word": "laugh",
    "Hint": "The sound or action people make when something is very funny."
  },
  {
    "Word": "heart",
    "Hint": "An organ that pumps blood around your body and is also a symbol of love."
  },
  {
    "Word": "brain",
    "Hint": "The organ inside your head that helps you think, learn, and remember."
  },
  {
    "Word": "blood",
    "Hint": "The red liquid that travels through your body and carries oxygen."
  },
  {
    "Word": "mouth",
    "Hint": "The part of your face used for eating, drinking, speaking, and smiling."
  },
  {
    "Word": "teeth",
    "Hint": "The hard white parts inside your mouth that help you bite and chew food."
  },
  {
    "Word": "child",
    "Hint": "A young human who is not yet an adult."
  },
  {
    "Word": "woman",
    "Hint": "An adult female human."
  },
  {
    "Word": "class",
    "Hint": "A group of students learning together or a lesson taught by a teacher."
  },
  {
    "Word": "teach",
    "Hint": "To help someone learn something by explaining or showing them."
  },
  {
    "Word": "study",
    "Hint": "To spend time learning about a subject by reading or practicing."
  },
  {
    "Word": "paper",
    "Hint": "A thin material commonly used for writing, drawing, and printing."
  },
  {
    "Word": "clock",
    "Hint": "A device that shows the current time."
  },
  {
    "Word": "watch",
    "Hint": "A small clock that is usually worn on the wrist."
  },
  {
    "Word": "phone",
    "Hint": "An electronic device used for calling, messaging, taking photos, and using apps."
  },
  {
    "Word": "mouse",
    "Hint": "A small computer device that you move with your hand to control the pointer."
  },
  {
    "Word": "music",
    "Hint": "Sounds arranged together that people enjoy listening to."
  },
  {
    "Word": "radio",
    "Hint": "A device or service used to listen to music, news, and broadcasts."
  },
  {
    "Word": "movie",
    "Hint": "A recorded story or show that you watch on a screen."
  },
  {
    "Word": "video",
    "Hint": "A recording of moving pictures that can be watched on a screen."
  },
  {
    "Word": "photo",
    "Hint": "A picture taken with a camera or phone."
  },
  {
    "Word": "sport",
    "Hint": "A physical game or activity played for exercise or competition."
  },
  {
    "Word": "beach",
    "Hint": "A sandy or rocky area beside the sea or ocean."
  },
  {
    "Word": "river",
    "Hint": "A natural stream of flowing water that usually moves toward a lake or sea."
  },
  {
    "Word": "ocean",
    "Hint": "A huge area of salty water that covers much of the Earth's surface."
  },
  {
    "Word": "islet",
    "Hint": "A very small island surrounded by water."
  },
  {
    "Word": "world",
    "Hint": "The Earth and everything that exists on it."
  },
  {
    "Word": "space",
    "Hint": "The vast area beyond Earth where stars, planets, and galaxies are found."
  },
  {
    "Word": "light",
    "Hint": "Something that allows you to see objects around you."
  },
  {
    "Word": "night",
    "Hint": "The dark part of the day when the sun is not visible."
  },
  {
    "Word": "sleep",
    "Hint": "The natural resting state when your body and brain recover."
  },
  {
    "Word": "dream",
    "Hint": "A series of images or thoughts that you may experience while sleeping."
  },
  {
    "Word": "roomy",
    "Hint": "A word describing a place that has plenty of space inside."
  },
  {
    "Word": "floor",
    "Hint": "The flat surface inside a building that you walk on."
  },
  {
    "Word": "spoon",
    "Hint": "A utensil with a rounded end used for eating or serving food."
  },
  {
    "Word": "plate",
    "Hint": "A flat dish used for serving and eating food."
  },
  {
    "Word": "glass",
    "Hint": "A container commonly used for drinking water or other liquids."
  },
  {
    "Word": "pizza",
    "Hint": "A round baked food usually covered with sauce, cheese, and toppings."
  },
  {
    "Word": "mango",
    "Hint": "A sweet tropical fruit with juicy flesh and one large seed."
  },
  {
    "Word": "grape",
    "Hint": "A small round fruit that grows in bunches and can be green, red, or purple."
  },
  {
    "Word": "lemon",
    "Hint": "A yellow citrus fruit with a very sour taste."
  },
  {
    "Word": "peach",
    "Hint": "A soft sweet fruit with fuzzy skin and a large seed inside."
  },
  {
    "Word": "guava",
    "Hint": "A tropical fruit that can have green skin and pink or white flesh."
  },
  {
    "Word": "melon",
    "Hint": "A large juicy fruit with sweet flesh and seeds inside."
  },
  {
    "Word": "olive",
    "Hint": "A small oval fruit that can be green or black and is also used to make oil."
  },
  {
    "Word": "onion",
    "Hint": "A vegetable with many layers that is commonly used to add flavor to food."
  },
  {
    "Word": "beans",
    "Hint": "Small edible seeds that are commonly cooked and used in many meals."
  },
  {
    "Word": "honey",
    "Hint": "A sweet golden food made by bees from flower nectar."
  },
  {
    "Word": "sugar",
    "Hint": "A sweet substance commonly added to tea, desserts, and other foods."
  },
  {
    "Word": "spice",
    "Hint": "An ingredient used in small amounts to add flavor to food."
  },
  {
    "Word": "horse",
    "Hint": "A large four-legged animal that people can ride."
  },
  {
    "Word": "tiger",
    "Hint": "A large wild cat with orange fur and black stripes."
  },
  {
    "Word": "zebra",
    "Hint": "A wild animal that looks like a horse and has black-and-white stripes."
  },
  {
    "Word": "sheep",
    "Hint": "A farm animal covered in wool that is often raised for wool and meat."
  },
  {
    "Word": "goose",
    "Hint": "A large bird with a long neck that can make a loud honking sound."
  },
  {
    "Word": "snake",
    "Hint": "A long animal with no legs that moves by sliding along the ground."
  },
  {
    "Word": "whale",
    "Hint": "A huge animal that lives in the ocean and breathes air through a blowhole."
  },
  {
    "Word": "shark",
    "Hint": "A large fish that lives in the ocean and has sharp teeth."
  },
  {
    "Word": "eagle",
    "Hint": "A large bird of prey with strong wings, sharp claws, and excellent eyesight."
  },
  {
    "Word": "meaty",
    "Hint": "A word describing food that contains a lot of meat."
  },
  {
    "Word": "spicy",
    "Hint": "A word describing food that has a hot or burning taste."
  },
  {
    "Word": "sweet",
    "Hint": "A word describing a sugary taste like candy, honey, or ripe fruit."
  },
  {
    "Word": "salty",
    "Hint": "A word describing food that tastes strongly of salt."
  },
  {
    "Word": "fresh",
    "Hint": "A word describing food that is new, recently prepared, or not spoiled."
  },
  {
    "Word": "clean",
    "Hint": "A word describing something without dirt, dust, or mess."
  },
  {
    "Word": "dirty",
    "Hint": "A word describing something covered with dirt or not clean."
  },
  {
    "Word": "small",
    "Hint": "A word describing something that is little in size."
  },
  {
    "Word": "large",
    "Hint": "A word describing something that is big in size."
  },
  {
    "Word": "quick",
    "Hint": "A word describing something that happens or moves fast."
  },
  {
    "Word": "quiet",
    "Hint": "A word describing a place or situation with very little noise."
  },
  {
    "Word": "funny",
    "Hint": "A word describing something that makes people laugh."
  },
  {
    "Word": "brave",
    "Hint": "A word describing someone who is willing to face danger without giving up."
  },
  {
    "Word": "smart",
    "Hint": "A word describing someone who is good at learning and understanding things."
  },
  {
    "Word": "young",
    "Hint": "A word describing someone or something that has lived for a short time."
  },
  {
    "Word": "older",
    "Hint": "A word used to describe someone or something with more age than another."
  },
  {
    "Word": "river",
    "Hint": "A natural flow of water that moves through land toward another body of water."
  },
  {
    "Word": "storm",
    "Hint": "A period of bad weather that can bring strong wind, rain, thunder, or lightning."
  },
  {
    "Word": "rainy",
    "Hint": "A word describing weather in which rain is falling or expected."
  },
  {
    "Word": "sunny",
    "Hint": "A word describing weather when the sun is shining brightly."
  },
  {
    "Word": "windy",
    "Hint": "A word describing weather with a lot of moving air."
  },
  {
    "Word": "frost",
    "Hint": "A thin layer of ice that forms on cold surfaces."
  },
  {
    "Word": "flame",
    "Hint": "The bright, hot part of a fire that you can see."
  },
  {
    "Word": "smoke",
    "Hint": "The gray or white cloud produced when something burns."
  },
  {
    "Word": "stone",
    "Hint": "A small piece of hard natural rock."
  },
  {
    "Word": "metal",
    "Hint": "A hard material such as iron, copper, or aluminum used to make many objects."
  },
  {
    "Word": "glass",
    "Hint": "A hard transparent material often used for windows and bottles."
  },
  {
    "Word": "wooden",
    "Hint": "Made from wood, such as a table, chair, or door."
  },
  {
    "Word": "truck",
    "Hint": "A large road vehicle used for carrying goods or heavy objects."
  },
  {
    "Word": "train",
    "Hint": "A long vehicle made of connected cars that travels on railway tracks."
  },
  {
    "Word": "plane",
    "Hint": "A flying vehicle with wings that carries people through the air."
  },
  {
    "Word": "bikes",
    "Hint": "Two-wheeled vehicles that people ride by turning pedals."
  },
  {
    "Word": "motor",
    "Hint": "A machine that uses energy to produce movement."
  },
  {
    "Word": "brass",
    "Hint": "A yellow-colored metal made mainly by mixing copper and zinc."
  },
  {
    "Word": "golds",
    "Hint": "A word referring to things made of or related to the valuable yellow metal."
  }
]


arrMediumWords = [
  {
    "Word": "animal",
    "Hint": "A living creature such as a dog, cat, horse, lion, or elephant that can move, eat, breathe, and respond to its surroundings."
  },
  {
    "Word": "banana",
    "Hint": "A long, soft fruit with yellow skin when ripe. It has a sweet taste and is easy to peel and eat as a snack."
  },
  {
    "Word": "bottle",
    "Hint": "A container with a narrow opening that is commonly used to hold water, juice, milk, oil, or other liquids."
  },
  {
    "Word": "bridge",
    "Hint": "A structure built over a river, road, railway, or other obstacle so that people and vehicles can safely travel from one side to the other."
  },
  {
    "Word": "castle",
    "Hint": "A large and strong building where kings, queens, or nobles lived in the past, often surrounded by thick walls and tall towers."
  },
  {
    "Word": "carpet",
    "Hint": "A thick piece of material that is placed on the floor of a room to make it softer, warmer, and more comfortable."
  },
  {
    "Word": "cloudy",
    "Hint": "A word used to describe weather when the sky is covered with many clouds and there is not much clear blue sky visible."
  },
  {
    "Word": "coffee",
    "Hint": "A popular hot drink made from roasted beans and hot water. Many people drink it in the morning to feel refreshed."
  },
  {
    "Word": "cookie",
    "Hint": "A small sweet baked food that can be soft or crunchy and may contain chocolate chips, nuts, raisins, or other ingredients."
  },
  {
    "Word": "donkey",
    "Hint": "A strong animal that looks similar to a small horse but has longer ears and is often used to carry people or heavy loads."
  },
  {
    "Word": "dragon",
    "Hint": "A large imaginary creature commonly shown with wings, scales, claws, and the ability to breathe fire in fantasy stories and movies."
  },
  {
    "Word": "flower",
    "Hint": "The colorful part of a plant that often has a pleasant smell and helps the plant produce seeds for creating new plants."
  },
  {
    "Word": "forest",
    "Hint": "A large area of land covered with many trees and plants where animals, birds, insects, and many other living things can live."
  },
  {
    "Word": "garden",
    "Hint": "An area around a home or building where people grow flowers, vegetables, herbs, trees, and other types of plants."
  },
  {
    "Word": "guitar",
    "Hint": "A musical instrument with a long neck and several strings that are played by strumming or picking them with your fingers."
  },
  {
    "Word": "hammer",
    "Hint": "A hand tool with a heavy head and a handle that is commonly used to hit nails into wood or other materials."
  },
  {
    "Word": "helmet",
    "Hint": "A hard protective covering worn on the head to help prevent injuries while riding a bicycle, playing sports, or doing dangerous work."
  },
  {
    "Word": "jacket",
    "Hint": "A piece of clothing worn over the upper body, usually over a shirt, to protect a person from cold weather, wind, or light rain."
  },
  {
    "Word": "jungle",
    "Hint": "A warm and wet natural area filled with thick trees, plants, vines, and many wild animals such as monkeys and big cats."
  },
  {
    "Word": "kitten",
    "Hint": "A very young cat that is usually small, soft, playful, curious, and full of energy."
  },
  {
    "Word": "ladder",
    "Hint": "A tool with two long sides connected by several steps that people climb when they need to reach something high."
  },
  {
    "Word": "lemons",
    "Hint": "Yellow citrus fruits that have a strong sour taste and are often used to make drinks, sauces, desserts, and other foods."
  },
  {
    "Word": "mirror",
    "Hint": "A smooth reflective surface that shows an image of a person or object standing in front of it."
  },
  {
    "Word": "monkey",
    "Hint": "An intelligent animal with arms, legs, and sometimes a long tail that can climb trees and is commonly found in forests."
  },
  {
    "Word": "orange",
    "Hint": "A round citrus fruit with orange-colored skin and juicy sections inside that have a sweet and slightly sour taste."
  },
  {
    "Word": "pencil",
    "Hint": "A common writing and drawing tool with a thin graphite center that leaves marks on paper and can usually be erased."
  },
  {
    "Word": "planet",
    "Hint": "A large round object in space that travels around a star. Earth is one example, and other examples include Mars and Jupiter."
  },
  {
    "Word": "rabbit",
    "Hint": "A small animal with long ears, soft fur, strong back legs, and a short tail that moves by hopping."
  },
  {
    "Word": "rocket",
    "Hint": "A powerful vehicle that uses strong engines to travel high into the sky and can continue traveling into outer space."
  },
  {
    "Word": "school",
    "Hint": "A place where students go to learn subjects such as mathematics, science, languages, computers, and many other useful skills."
  },
  {
    "Word": "shovel",
    "Hint": "A tool with a long handle and a wide blade that is used for digging and moving soil, sand, snow, or other loose material."
  },
  {
    "Word": "silver",
    "Hint": "A shiny gray-colored precious metal that is commonly used to make jewelry, coins, decorations, and other valuable objects."
  },
  {
    "Word": "spider",
    "Hint": "A small creature with eight legs that can produce silk and often uses that silk to build a web for catching insects."
  },
  {
    "Word": "spring",
    "Hint": "A season that comes after winter when temperatures become warmer and many plants begin growing new leaves and flowers."
  },
  {
    "Word": "street",
    "Hint": "A road in a town or city where cars, motorcycles, bicycles, and people travel, usually surrounded by buildings or houses."
  },
  {
    "Word": "summer",
    "Hint": "A warm season of the year when days are often longer, temperatures are higher, and people commonly enjoy outdoor activities."
  },
  {
    "Word": "tomato",
    "Hint": "A soft, round fruit that is usually red when ripe and is commonly used in salads, sauces, sandwiches, and cooked meals."
  },
  {
    "Word": "turtle",
    "Hint": "A slow-moving animal with a hard protective shell covering its body. Some types live on land while others live in water."
  },
  {
    "Word": "window",
    "Hint": "An opening in the wall of a building that usually has glass and allows sunlight and fresh air to enter a room."
  },
  {
    "Word": "winter",
    "Hint": "The cold season of the year when temperatures become low, and in some parts of the world, snow and ice can cover the ground."
  },
  {
    "Word": "button",
    "Hint": "A small round object attached to clothing that is pushed through a hole to close a shirt, jacket, coat, or other piece of clothing."
  },
  {
    "Word": "camera",
    "Hint": "A device used to take photographs or record videos by capturing images of people, places, objects, and events."
  },
  {
    "Word": "candle",
    "Hint": "A stick or block made from wax with a wick in the middle that produces light when the wick is lit."
  },
  {
    "Word": "carrot",
    "Hint": "A usually orange-colored vegetable that grows underground and has a long shape with green leaves growing from the top."
  },
  {
    "Word": "cheese",
    "Hint": "A food made from milk that can be soft, hard, creamy, or firm and is often added to pizza, sandwiches, burgers, and other meals."
  },
  {
    "Word": "cherry",
    "Hint": "A small round fruit that is usually red or dark red, has a sweet taste, and contains one hard seed in the center."
  },
  {
    "Word": "circle",
    "Hint": "A completely round shape in which every point around the outside is the same distance from the center."
  },
  {
    "Word": "closet",
    "Hint": "A small enclosed storage space in a home where people commonly keep clothes, shoes, bags, boxes, or other personal items."
  },
  {
    "Word": "cotton",
    "Hint": "A soft natural material that comes from a plant and is commonly used to make shirts, trousers, towels, bedsheets, and other fabrics."
  },
  {
    "Word": "desert",
    "Hint": "A very dry area of land that receives very little rainfall and may contain sand, rocks, and plants that can survive with little water."
  },
  {
    "Word": "dinner",
    "Hint": "A meal that people usually eat in the evening, often consisting of foods such as rice, meat, vegetables, bread, or other dishes."
  },
  {
    "Word": "doctor",
    "Hint": "A trained medical professional who examines sick or injured people, identifies health problems, and provides medical treatment or advice."
  },
  {
    "Word": "donuts",
    "Hint": "Sweet fried or baked rings of dough that are often covered with sugar, chocolate, icing, or colorful toppings."
  },
  {
    "Word": "engine",
    "Hint": "A machine that converts energy into movement and is commonly used to power cars, motorcycles, boats, airplanes, and other vehicles."
  },
  {
    "Word": "family",
    "Hint": "A group of people who are related to one another, such as parents, children, brothers, sisters, grandparents, or other relatives."
  },
  {
    "Word": "farmer",
    "Hint": "A person who grows crops or raises animals on land to produce food and other agricultural products."
  },
  {
    "Word": "finger",
    "Hint": "One of the small movable parts at the end of your hand that helps you hold, touch, point at, and move objects."
  },
  {
    "Word": "garlic",
    "Hint": "A small plant bulb made of several cloves that has a strong smell and taste and is commonly used to add flavor to food."
  },
  {
    "Word": "ginger",
    "Hint": "A root with a strong spicy flavor that is commonly used in cooking, tea, and traditional drinks."
  },
  {
    "Word": "island",
    "Hint": "A piece of land that is completely surrounded by water and can be small like a tiny island or large like a country."
  },
  {
    "Word": "kettle",
    "Hint": "A container with a handle and a spout that is designed to heat or boil water, often for making tea or coffee."
  },
  {
    "Word": "laptop",
    "Hint": "A portable computer with a screen, keyboard, and battery that can be folded closed and carried from one place to another."
  },
  {
    "Word": "market",
    "Hint": "A place where people buy and sell things such as fruits, vegetables, clothes, meat, household items, and many other products."
  },
  {
    "Word": "marble",
    "Hint": "A smooth hard stone that can be polished and is often used for floors, walls, countertops, statues, and decorative objects."
  },
  {
    "Word": "melons",
    "Hint": "Large juicy fruits with a thick outer skin and sweet flesh inside. Watermelons and cantaloupes are common examples."
  },
  {
    "Word": "mother",
    "Hint": "A female parent who gives birth to a child or raises and cares for a child as part of a family."
  },
  {
    "Word": "muffin",
    "Hint": "A small soft baked cake-like food that is often eaten for breakfast or as a snack and may contain fruit or chocolate."
  },
  {
    "Word": "nature",
    "Hint": "The natural world around us, including trees, plants, animals, rivers, mountains, oceans, weather, and other living and non-living things."
  },
  {
    "Word": "number",
    "Hint": "A mathematical value or symbol used for counting, measuring, ordering things, or performing calculations."
  },
  {
    "Word": "office",
    "Hint": "A place where people commonly work at desks, use computers, attend meetings, and perform professional or business tasks."
  },
  {
    "Word": "peanut",
    "Hint": "A small edible seed that grows underground inside a shell and is commonly eaten roasted or used to make peanut butter."
  },
  {
    "Word": "pillow",
    "Hint": "A soft object filled with material that you place under your head while sleeping to make your head and neck more comfortable."
  },
  {
    "Word": "potato",
    "Hint": "A round or oval vegetable that grows underground and can be boiled, fried, baked, mashed, or used in many different dishes."
  },
  {
    "Word": "purple",
    "Hint": "A color made by combining red and blue, often associated with flowers such as lavender and certain types of grapes."
  },
  {
    "Word": "singer",
    "Hint": "A person who uses their voice to perform songs, either alone or as part of a musical group."
  },
  {
    "Word": "soccer",
    "Hint": "A popular sport where two teams try to score goals by kicking a ball into the opposing team's goal."
  },
  {
    "Word": "square",
    "Hint": "A shape with four equal sides and four corners, where each corner forms a right angle."
  },
  {
    "Word": "statue",
    "Hint": "A three-dimensional object made to represent a person, animal, or other figure and is often displayed in public places or buildings."
  },
  {
    "Word": "subway",
    "Hint": "An underground railway system used to transport many passengers around a large city quickly and efficiently."
  },
  {
    "Word": "tablet",
    "Hint": "A portable electronic device with a flat touchscreen that can be used for watching videos, browsing the internet, reading, and using apps."
  },
  {
    "Word": "tennis",
    "Hint": "A sport played with rackets in which players hit a ball over a net and try to make it land inside the opponent's court."
  },
  {
    "Word": "travel",
    "Hint": "The activity of going from one place to another, often to visit different cities, countries, tourist attractions, or family members."
  },
  {
    "Word": "valley",
    "Hint": "A low area of land between hills or mountains that may contain a river, farms, forests, roads, or villages."
  },
  {
    "Word": "wallet",
    "Hint": "A small folding case that people carry in a pocket or bag to keep money, bank cards, identification cards, and other small items."
  },
  {
    "Word": "yellow",
    "Hint": "A bright color commonly seen in objects such as bananas, lemons, sunflowers, and some warning signs."
  },
  {
    "Word": "yogurt",
    "Hint": "A creamy food made from fermented milk that can be eaten plain or mixed with fruit, sugar, honey, or other ingredients."
  },
  {
    "Word": "bakery",
    "Hint": "A shop or place where bread, cakes, cookies, pastries, and other baked foods are prepared and sold."
  },
  {
    "Word": "basket",
    "Hint": "A container usually made from woven material or plastic that is used to carry, store, or organize different objects."
  },
  {
    "Word": "beaver",
    "Hint": "A large water-loving animal with strong teeth and a flat tail that is famous for building dams from wood and branches."
  },
  {
    "Word": "bucket",
    "Hint": "A round container with a handle that is commonly used to carry water, clean floors, store materials, or move liquids."
  },
  {
    "Word": "butter",
    "Hint": "A soft yellow dairy product made from cream that is commonly spread on bread or used while cooking and baking."
  },
  {
    "Word": "cactus",
    "Hint": "A plant that is adapted to dry environments and usually has a thick body that stores water and sharp spines for protection."
  },
  {
    "Word": "cruise",
    "Hint": "A vacation journey taken on a large passenger ship that travels between different coastal cities or countries."
  },
  {
    "Word": "dancer",
    "Hint": "A person who performs controlled body movements, often to music, either for entertainment, exercise, or professional performances."
  },
  {
    "Word": "danger",
    "Hint": "A situation or condition that could cause someone to be hurt, damaged, injured, or placed at risk."
  },
  {
    "Word": "galaxy",
    "Hint": "A huge collection of stars, planets, gas, dust, and other objects held together by gravity, with our solar system inside one."
  },
  {
    "Word": "garage",
    "Hint": "A building or enclosed space where people park cars and may also keep tools, bicycles, equipment, and other belongings."
  },
  {
    "Word": "grapes",
    "Hint": "Small round fruits that grow together in bunches on vines and can be green, red, purple, or almost black when ripe."
  },
  {
    "Word": "harbor",
    "Hint": "A sheltered area along a coast where boats and ships can safely stop, load goods, unload passengers, or wait during bad weather."
  },
  {
    "Word": "jaguar",
    "Hint": "A powerful wild cat with a spotted coat that lives mainly in forests and other parts of Central and South America."
  },
  {
    "Word": "magnet",
    "Hint": "An object that produces a magnetic force and can attract certain metals, especially iron and steel."
  },
  {
    "Word": "meadow",
    "Hint": "An open area of grassy land where wildflowers and plants grow and where animals may feed or move around."
  },
  {
    "Word": "museum",
    "Hint": "A public place where historical objects, artwork, scientific items, cultural artifacts, and other interesting things are collected and displayed."
  },
  {
    "Word": "napkin",
    "Hint": "A small piece of paper or cloth used while eating to clean your mouth, hands, or small spills from a table."
  },
  {
    "Word": "needle",
    "Hint": "A very thin sharp object with a pointed end and often a small hole that is used for sewing thread through cloth."
  },
  {
    "Word": "palace",
    "Hint": "A very large and impressive building where a king, queen, emperor, or other member of royalty may live."
  },
  {
    "Word": "parent",
    "Hint": "An adult who has a child and is responsible for caring for, protecting, supporting, and raising that child."
  },
  {
    "Word": "parrot",
    "Hint": "A colorful bird with a curved beak that can learn to copy sounds and, in some cases, imitate human speech."
  },
  {
    "Word": "picnic",
    "Hint": "A meal eaten outdoors, often in a park or natural area, where people bring food, drinks, blankets, and sometimes games."
  },
  {
    "Word": "pirate",
    "Hint": "A person who attacks or steals from ships at sea, often shown in stories wearing old-fashioned clothing and searching for treasure."
  },
  {
    "Word": "pocket",
    "Hint": "A small fabric compartment sewn into clothing or a bag where you can keep money, keys, a phone, or other small objects."
  },
  {
    "Word": "puzzle",
    "Hint": "A game or problem that requires you to think carefully and arrange, match, or solve different pieces to find the correct answer."
  },
  {
    "Word": "recipe",
    "Hint": "A set of instructions that tells you which ingredients to use and how to prepare and cook a particular food or dish."
  },
  {
    "Word": "remote",
    "Hint": "A small electronic device with buttons that allows you to control a television, air conditioner, or another device from a distance."
  },
  {
    "Word": "runner",
    "Hint": "A person who runs, especially someone who takes part in running for exercise, sport, competition, or fitness."
  },
  {
    "Word": "sailor",
    "Hint": "A person who works or travels on a ship and helps operate the vessel while it is traveling across the water."
  },
  {
    "Word": "salmon",
    "Hint": "A type of fish that lives in water and is commonly eaten as food. Some species are known for swimming upstream to lay eggs."
  },
  {
    "Word": "secret",
    "Hint": "Information that is kept hidden from other people because someone does not want them to know or discover it."
  },
  {
    "Word": "shadow",
    "Hint": "A dark shape that appears on the ground or another surface when an object blocks light from reaching that area."
  },
  {
    "Word": "smooth",
    "Hint": "A word used to describe a surface that feels even and soft without rough bumps, sharp edges, or an uneven texture."
  },
  {
    "Word": "stable",
    "Hint": "A building where horses are kept, fed, and cared for, usually with separate spaces for each animal."
  },
  {
    "Word": "stream",
    "Hint": "A small natural flow of water that moves across the land and may eventually join a larger river or body of water."
  }
]


arrHardWords = [
  {
    "Word": "abalone",
    "Hint": "A sea animal that lives on rocks and has a hard shell with a shiny, colorful inside."
  },
  {
    "Word": "balloon",
    "Hint": "A light and colorful object filled with air or gas that is commonly used at parties and celebrations."
  },
  {
    "Word": "biscuit",
    "Hint": "A small baked food that can be crunchy or soft and is often eaten with tea, milk, or another drink."
  },
  {
    "Word": "blanket",
    "Hint": "A large soft piece of cloth that you put over your body to keep yourself warm while sleeping."
  },
  {
    "Word": "cabinet",
    "Hint": "A piece of furniture with doors or shelves that is used to store dishes, clothes, books, or other things."
  },
  {
    "Word": "coconut",
    "Hint": "A large tropical fruit with a hard brown shell, white flesh inside, and sweet water in the center."
  },
  {
    "Word": "dolphin",
    "Hint": "A smart sea animal that swims quickly, lives in groups, and often jumps out of the water."
  },
  {
    "Word": "giraffe",
    "Hint": "A very tall animal with a very long neck, long legs, and brown patches that eats leaves from trees."
  },
  {
    "Word": "glasses",
    "Hint": "An object with two lenses that people wear in front of their eyes to help them see more clearly."
  },
  {
    "Word": "lantern",
    "Hint": "A portable light that can be carried or placed somewhere to help people see when it is dark."
  },
  {
    "Word": "lobster",
    "Hint": "A sea animal with a hard body, several legs, and two large claws that lives on the ocean floor."
  },
  {
    "Word": "monster",
    "Hint": "A frightening imaginary creature that is often seen in scary stories, movies, cartoons, and video games."
  },
  {
    "Word": "morning",
    "Hint": "The early part of the day when people usually wake up, eat breakfast, and prepare for school or work."
  },
  {
    "Word": "noodles",
    "Hint": "Long thin pieces of food that are usually boiled and served with soup, sauce, vegetables, or meat."
  },
  {
    "Word": "ostrich",
    "Hint": "A very large bird with a long neck and powerful legs that cannot fly but can run very fast."
  },
  {
    "Word": "penguin",
    "Hint": "A black-and-white bird that cannot fly but can swim very well and is commonly associated with cold places."
  },
  {
    "Word": "rainbow",
    "Hint": "A colorful curved shape that sometimes appears in the sky when sunlight shines through rain or water droplets."
  },
  {
    "Word": "sandals",
    "Hint": "A type of open footwear that leaves much of the foot uncovered and is commonly worn in warm weather."
  },
  {
    "Word": "seagull",
    "Hint": "A common bird that is often seen flying around beaches, oceans, lakes, and other areas near water."
  },
  {
    "Word": "sunrise",
    "Hint": "The beautiful time in the morning when the sun begins appearing above the horizon and the sky becomes brighter."
  },
  {
    "Word": "thunder",
    "Hint": "A loud booming sound heard during a storm, usually after lightning flashes across the sky."
  },
  {
    "Word": "volcano",
    "Hint": "A mountain with an opening that can release hot lava, ash, smoke, and gases during an eruption."
  },
  {
    "Word": "weather",
    "Hint": "The condition of the air outside, such as whether it is sunny, rainy, cloudy, windy, hot, or cold."
  },
  {
    "Word": "airport",
    "Hint": "A large place where airplanes take off and land, with runways and buildings where passengers travel."
  },
  {
    "Word": "bedroom",
    "Hint": "A room in a house where people usually sleep and keep things such as beds, clothes, pillows, and blankets."
  },
  {
    "Word": "dancing",
    "Hint": "An activity where a person moves their body in different ways, usually while following music or a rhythm."
  },
  {
    "Word": "diamond",
    "Hint": "A very hard and valuable shiny stone that is often cut and polished and used to make beautiful jewelry."
  },
  {
    "Word": "firefly",
    "Hint": "A small flying insect that can produce a natural glowing light from its body, especially at night."
  },
  {
    "Word": "jasmine",
    "Hint": "A flowering plant with small flowers that are famous for having a strong, sweet, and pleasant smell."
  },
  {
    "Word": "kingdom",
    "Hint": "A country or territory ruled by a king or queen, often shown in stories with castles and royal families."
  },
  {
    "Word": "library",
    "Hint": "A quiet place where many books are kept and where people can read, study, or borrow books."
  },
  {
    "Word": "machine",
    "Hint": "A device made of different parts that uses energy to perform a job or make work easier for people."
  },
  {
    "Word": "pumpkin",
    "Hint": "A large round vegetable that is usually orange and is used in cooking, pies, soups, and Halloween decorations."
  },
  {
    "Word": "teacher",
    "Hint": "A person whose job is to teach students different subjects and help them learn new knowledge and skills."
  },
  {
    "Word": "tornado",
    "Hint": "A powerful spinning column of air that comes from a storm cloud and can cause serious damage when it reaches the ground."
  },
  {
    "Word": "village",
    "Hint": "A small community where people live, usually with houses, roads, farms, shops, and other buildings."
  },
  {
    "Word": "bicycle",
    "Hint": "A vehicle with two wheels that a person moves by pushing pedals with their feet."
  },
  {
    "Word": "butterfly",
    "Hint": "A flying insect with colorful wings that begins life as a caterpillar before changing into its adult form."
  },
  {
    "Word": "carrots",
    "Hint": "Orange vegetables that grow underground and have a long shape with green leaves growing from the top."
  },
  {
    "Word": "chicken",
    "Hint": "A common farm bird that has feathers, two legs, and wings, and is also commonly raised for its meat and eggs."
  },
  {
    "Word": "clothes",
    "Hint": "Things people wear on their bodies, such as shirts, trousers, jackets, dresses, and other pieces of clothing."
  },
  {
    "Word": "country",
    "Hint": "An area of land with its own government, borders, people, and usually its own national identity."
  },
  {
    "Word": "crystal",
    "Hint": "A hard solid material that naturally forms with a regular shape and can often look clear, shiny, or colorful."
  },
  {
    "Word": "curtain",
    "Hint": "A piece of cloth that hangs over a window or doorway and can be opened or closed to block light or provide privacy."
  },
  {
    "Word": "dinosaur",
    "Hint": "An ancient animal that lived millions of years ago and is known from fossils found by scientists around the world."
  },
  {
    "Word": "emerald",
    "Hint": "A valuable green gemstone that is often cut and polished and used in rings, necklaces, and other jewelry."
  },
  {
    "Word": "evening",
    "Hint": "The part of the day that comes after the afternoon and before night, when the sun is going down."
  },
  {
    "Word": "express",
    "Hint": "To show or communicate a feeling, thought, idea, or opinion using words, actions, writing, or another method."
  },
  {
    "Word": "factory",
    "Hint": "A large building where machines and workers are used to produce products such as cars, clothes, food, or electronics."
  },
  {
    "Word": "feather",
    "Hint": "A light structure that grows on the body of a bird and helps protect the bird and, in many birds, helps it fly."
  },
  {
    "Word": "football",
    "Hint": "A popular team sport where players try to score by moving a ball toward the other team's goal."
  },
  {
    "Word": "freedom",
    "Hint": "The ability to make your own choices and act without being controlled or unfairly restricted by another person."
  },
  {
    "Word": "garbage",
    "Hint": "Waste or unwanted things that people throw away after they are no longer useful."
  },
  {
    "Word": "gateway",
    "Hint": "An entrance or opening that allows people or vehicles to pass from one area into another."
  },
  {
    "Word": "glacier",
    "Hint": "A huge and slowly moving mass of ice that forms on land in very cold regions."
  },
  {
    "Word": "grocery",
    "Hint": "Food and household items that people buy from stores, such as vegetables, fruit, milk, bread, and cleaning products."
  },
  {
    "Word": "hammock",
    "Hint": "A piece of strong fabric or netting that hangs between two supports and is used for relaxing or sleeping."
  },
  {
    "Word": "holiday",
    "Hint": "A special day or period when people usually do not work or attend school and may relax, travel, or celebrate."
  },
  {
    "Word": "hospital",
    "Hint": "A place where doctors and nurses treat sick or injured people and provide medical care."
  },
  {
    "Word": "journey",
    "Hint": "A trip from one place to another, especially when traveling a long distance by car, train, plane, ship, or another vehicle."
  },
  {
    "Word": "kitchen",
    "Hint": "A room in a house or building where people prepare, cook, and sometimes eat food."
  },
  {
    "Word": "luggage",
    "Hint": "Bags, suitcases, and other containers that people take with them when traveling."
  },
  {
    "Word": "morning",
    "Hint": "The first part of the day after the night, when people normally wake up and begin their daily activities."
  },
  {
    "Word": "musical",
    "Hint": "Something related to music, songs, instruments, singing, or other forms of musical performance."
  },
  {
    "Word": "natural",
    "Hint": "Something that comes from nature rather than being made or created by people."
  },
  {
    "Word": "newborn",
    "Hint": "A baby that has been born very recently and is usually only a few days or weeks old."
  },
  {
    "Word": "notebook",
    "Hint": "A small book made of pages that people use for writing notes, homework, ideas, drawings, or important information."
  },
  {
    "Word": "package",
    "Hint": "An object or collection of items wrapped or placed inside a box or other container so it can be stored or delivered."
  },
  {
    "Word": "painting",
    "Hint": "A picture created by putting paint on a surface such as paper, canvas, wood, or a wall."
  },
  {
    "Word": "pancake",
    "Hint": "A flat, round food made from a liquid batter and cooked in a pan, often served with syrup, fruit, or other toppings."
  },
  {
    "Word": "peacock",
    "Hint": "A large colorful bird known for the male's beautiful long tail feathers that can spread out like a large fan."
  },
  {
    "Word": "picture",
    "Hint": "A visual image of a person, place, animal, or object that can be drawn, painted, printed, or shown on a screen."
  },
  {
    "Word": "rainbow",
    "Hint": "A curved display of many colors that can appear in the sky when sunlight passes through water droplets."
  },
  {
    "Word": "reading",
    "Hint": "The activity of looking at written words and understanding the information, story, or message they communicate."
  },
  {
    "Word": "roadway",
    "Hint": "The part of a road designed for vehicles such as cars, buses, motorcycles, and trucks to travel on."
  },
  {
    "Word": "sandwich",
    "Hint": "A type of food made by placing ingredients such as meat, cheese, vegetables, or eggs between pieces of bread."
  },
  {
    "Word": "seashell",
    "Hint": "The hard outer shell of a sea animal that people often find washed up on beaches."
  },
  {
    "Word": "shelter",
    "Hint": "A place that provides protection from rain, wind, heat, cold, danger, or other difficult conditions."
  },
  {
    "Word": "skating",
    "Hint": "An activity where a person moves across a surface while wearing special shoes or equipment with wheels or blades."
  },
  {
    "Word": "station",
    "Hint": "A place where buses, trains, or other forms of transportation regularly arrive, stop, and leave with passengers."
  },
  {
    "Word": "teacher",
    "Hint": "A person who helps students understand lessons, learn new subjects, complete schoolwork, and develop useful skills."
  },
  {
    "Word": "theater",
    "Hint": "A building or place where people watch live performances, plays, shows, concerts, or other forms of entertainment."
  },
  {
    "Word": "traffic",
    "Hint": "The movement of cars, buses, motorcycles, trucks, and other vehicles along roads, especially when many vehicles are present."
  },
  {
    "Word": "treasure",
    "Hint": "A collection of valuable things such as gold, jewels, coins, or precious objects that people may hide or search for."
  },
  {
    "Word": "uniform",
    "Hint": "A special set of clothes that members of a school, team, company, police force, or other group wear to look similar."
  },
  {
    "Word": "universe",
    "Hint": "Everything that exists in space, including all galaxies, stars, planets, moons, matter, energy, and space itself."
  },
  {
    "Word": "vehicle",
    "Hint": "A machine used to transport people or things from one place to another, such as a car, bus, truck, or motorcycle."
  },
  {
    "Word": "visitor",
    "Hint": "A person who comes to a place for a short time, such as someone's home, a city, a museum, or another location."
  },
  {
    "Word": "walking",
    "Hint": "The activity of moving from one place to another by taking steps with your feet instead of running or using a vehicle."
  },
  {
    "Word": "warning",
    "Hint": "A message or sign that tells people about possible danger or a problem so they can be careful."
  },
  {
    "Word": "whistle",
    "Hint": "A small object or sound that produces a sharp high-pitched noise when air is blown through it."
  },
  {
    "Word": "wildlife",
    "Hint": "Animals and other living creatures that live naturally in forests, mountains, deserts, oceans, and other natural environments."
  },
  {
    "Word": "windows",
    "Hint": "Openings in the walls of buildings that usually contain glass and allow sunlight and fresh air to enter rooms."
  },
  {
    "Word": "workout",
    "Hint": "A period of physical exercise in which a person performs activities to improve strength, fitness, health, or endurance."
  },
  {
    "Word": "yogurts",
    "Hint": "Creamy foods made from fermented milk that can be eaten plain or mixed with fruit, sugar, honey, or other ingredients."
  },
  {
    "Word": "zealous",
    "Hint": "A word describing someone who is extremely enthusiastic, energetic, and strongly interested in supporting a person, activity, or cause."
  },
  {
    "Word": "zombies",
    "Hint": "Fictional creatures that are usually shown as dead people who have returned to life and walk around looking for living people."
  },
  {
    "Word": "teacher",
    "Hint": "A person who teaches students in a school and helps them understand subjects, complete lessons, and gain knowledge."
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
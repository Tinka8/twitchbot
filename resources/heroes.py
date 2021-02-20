structuredHeroes = {
    'pos1' : [
        # Strength
        "Chaos Knight",
        "Dragon Knight",
        "Lifestealer",
        "Sven",
        "Wraith King",

        # Agility
        "Anti-Mage",
        "Drow Ranger",
        "Faceless Void",
        "Gyrocopter",
        "Juggernaut",
        "Lone Druid",
        "Luna",
        "Morphling",
        "Naga Siren",
        "Phantom Assassin",
        "Phantom Lancer",
        "Riki",
        "Slark",
        "Spectre",
        "Terrorblade",
        "Troll Warlord",
        "Ursa",
        "Weaver",
    ],


    'pos2' : [
        # Strength
        "Huskar",
        "Kunkka",
        "Lycan",
        "Tiny",

        # Agility
        "Arc Warden",
        "Bloodseeker",
        "Broodmother",
        "Clinkz",
        "Ember Spirit",
        "Medusa",
        "Meepo",
        "Monkey King",
        "Razor",
        "Shadow Fiend",
        "Sniper",
        "Templar Assassin",
        "Viper",

        # Intelligence
        "Batrider",
        "Death Prophet",
        "Invoker",
        "Leshrac",
        "Lina",
        "Necrophos",
        "Outworld Devourer",
        "Puck",
        "Pugna",
        "Queen of Pain",
        "Storm Spirit",
        "Tinker",
        "Visage",
        "Zeus",
    ],


    'pos3' : [
        # Strength
        "Axe",
        "Beastmaster",
        "Brewmaster",
        "Bristleback",
        "Centaur Warrunner",
        "Doom",
        "Elder Titan",
        "Legion Commander",
        "Magnus",
        "Night Stalker",
        "Slardar",
        "Tidehunter",
        "Timbersaw",
        "Underlord",

        # Agility
        "Nyx Assassin",
        "Pangolier",

        # Intelligence
        "Dark Seer",
        "Nature’s Prophet",
        "Windranger",
    ],


    'pos4' : [
        # Strength
        "Clockwerk",
        "Earth Spirit",
        "Earthshaker",
        "Phoenix",
        "Pudge",
        "Sand King",
        "Spirit Breaker",
        "Tusk",
        "Undying",

        # Agility
        "Bounty Hunter",
        "Mirana",
        "Venomancer",

        # Intelligence
        "Dark Willow",
        "Dazzle",
        "Enigma",
        "Rubick",
        "Shadow Demon",
        "Silencer",
        "Skywrath Mage",
        "Techies",
    ],


    'pos5' : [
        # Strength
        "Abaddon",
        "Io",
        "Omniknight",
        "Treant Protector",

        # Agility
        "Vengeful Spirit",

        # Intelligence
        "Ancient Apparition",
        "Bane",
        "Chen",
        "Crystal Maiden",
        "Disruptor",
        "Enchantress",
        "Jakiro",
        "Keeper of the Light", 
        "Lich",
        "Lion",
        "Ogre Magi",
        "Oracle",
        "Shadow Shaman",
        "Warlock",
        "Winter Wyvern",
        "Witch Doctor",
    ]
}


# flatten dictionary
def flatten(structured):

    flat = []

    for key in structured.keys():
        flat = flat + structured[key]
    
    return flat

# flat list of all heroes
heroes = flatten(structuredHeroes)
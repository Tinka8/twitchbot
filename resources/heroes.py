structuredHeroes = {
    'pos1' : [
        # Strength
        'Alchemist',
        'Chaos Knight',
        'Dragon Knight',
        'Lifestealer',
        'Sven',
        'Wraith King',

        # Agility
        'Anti-Mage',
        'Bloodseeker',
        'Drow Ranger',
        'Faceless Void',
        'Gyrocopter',
        'Juggernaut',
        'Lone Druid',
        'Luna',
        'Medusa',
        'Monkey King',
        'Morphling',
        'Naga Siren',
        'Phantom Assassin',
        'Phantom Lancer',
        'Riki',
        'Slark',
        'Spectre',
        'Terrorblade',
        'Troll Warlord',
        'Ursa',
        'Weaver',
    ],


    'pos2' : [
        # Strength
        'Huskar',
        'Kunkka',
        'Lycan',
        'Tiny',

        # Agility
        'Arc Warden',
        'Broodmother',
        'Clinkz',
        'Ember Spirit',
        'Meepo',
        'Razor',
        'Shadow Fiend',
        'Sniper',
        'Templar Assassin',
        'Viper',

        # Intelligence
        'Batrider',
        'Death Prophet',
        'Invoker',
        'Leshrac',
        'Lina',
        'Necrophos',
        'Outworld Devourer',
        'Puck',
        'Pugna',
        'Queen of Pain',
        'Storm Spirit',
        'Tinker',
        'Visage',
        'Void Spirit',
        'Zeus',
    ],


    'pos3' : [
        # Strength
        'Axe',
        'Beastmaster',
        'Brewmaster',
        'Bristleback',
        'Centaur Warrunner',
        'Doom',
        'Legion Commander',
        'Magnus',
        'Mars',
        'Night Stalker',
        'Sand King',
        'Slardar',
        'Snapfire',
        'Tidehunter',
        'Timbersaw',
        'Underlord',

        # Agility
        'Hoodwink',
        'Pangolier',

        # Intelligence
        'Dark Seer',
        'Nature’s Prophet',
    ],


    'pos4' : [
        # Strength
        'Clockwerk',
        'Earth Spirit',
        'Earthshaker',
        'Elder Titan',
        'Phoenix',
        'Pudge',
        'Spirit Breaker',
        'Treant Protector',
        'Tusk',

        # Agility
        'Bounty Hunter',
        'Mirana',
        'Nyx Assassin',
        'Venomancer',

        # Intelligence
        'Dark Willow',
        'Enigma',
        'Grimstroke',
        'Jakiro',
        'Rubick',
        'Shadow Demon',
        'Silencer',
        'Skywrath Mage',
        'Techies',
        'Windranger',
        'Winter Wyvern',
    ],


    'pos5' : [
        # Strength
        'Abaddon',
        'Io',
        'Omniknight',
        'Undying',

        # Agility
        'Vengeful Spirit',

        # Intelligence
        'Ancient Apparition',
        'Bane',
        'Chen',
        'Crystal Maiden',
        'Dazzle',
        'Disruptor',
        'Enchantress',
        'Keeper of the Light', 
        'Lich',
        'Lion',
        'Ogre Magi',
        'Oracle',
        'Shadow Shaman',
        'Warlock',
        'Witch Doctor',
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

import twint

c = twint.Config()

depression_words = ["lonely", "anger", "abjection", "blahs", "bleakness", "bummer", "cheerlessness", "dejection",
                    "depressed", "desolation", "desperation", "despondency", "discouragement", "dispiritedness",
                    "distress", "dole", "dolefulness", "dolor", "downheartedness", "dreariness", "dullness", "dumps",
                    "ennui", "frustration", "gloom", "gloominess", "heavyheartedness", "hopelessness", "irritable",
                    "lowness", "melancholia", "melancholy", "misery", "mortification", "qualm", "sadness", "sorrow",
                    "stress", "trouble", "unhappiness", "vapors", "woefulness", "worry", "abjectness", "blue funk",
                    "disconsolation", "heaviness of heart", "lugubriosity", "blues", "dejection", "desolation",
                    "despond", "despondence", "disconsolateness", "dispiritedness", "doldrums", "dolefulness",
                    "downheartedness", "dreariness", "dumps", "forlornness", "gloom", "gloominess", "glumness",
                    "heartsickness", "joylessness", "melancholy", "miserableness", "mopes", "mournfulness",
                    "oppression", "sadness", "sorrowfulness", "unhappiness", "melancholia", "self-pity", "anguish",
                    "dolor", "grief, ", "mourning", "somberness", "sorrow", "woefulness", "agony", "distress", "pain",
                    "misery", "woe", "wretchedness", "discouragement", "disheartenment", "moodiness", "despair, ",
                    "esperation", "hopelessness", "self-despair", "boredom", "tedium", "dismalness", "drear",
                    "morbidness", "moroseness", "morosity", "regret"]

for keyword in depression_words:

    c.Search = keyword
    c.Limit = 10000
    c.Year = "2019"
    c.Output = "../Datasets/depression_2019.csv"
    c.Lang = "en"
    c.Hide_output = True
    c.Store_csv = True

    twint.run.Search(c)

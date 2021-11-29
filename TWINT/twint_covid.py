import twint

c = twint.Config()

covid_keywords = ["COVID-19", "Coronavirus", "COVID19", "covid", "Pandemic", "Community spread", "Quarantine", "isolation", "lockdown", "Social distancing"]

for keyword in covid_keywords:

    c.Search = keyword
    c.Limit = 1
    c.Output = "../Datasets/covid_keywords.csv"
    c.Lang = "en"
    c.Custom["tweet"] = ["tweet"]
    c.Hide_output = True
    c.Store_csv = True

    twint.run.Search(c)

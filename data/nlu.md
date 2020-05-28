## intent:greet
- hey
- hello
- hi
- good morning
- good evening
- hey there
- wazzup
- sup
- yo
- yow
- kumusta

## intent:goodbye
- bye
- goodbye
- see you around
- see you later
- seeyah
- babay
- paalam

## intent:thank
- thanks
- ty
- salamat
- arigatou
- agyamanak
- tnx
- tenks

## intent: affirm
- nice
- cool
- nice one
- good one
- good
- ayos

## intent: bot
- are you a bot?
- are you a human?
- am I talking to a bot?
- am I talking to a human?

## intent: show_tag
- Tagalog
- filipino

## intent: define_covid_tag
- anong [COVID-19](covid_names)?
- what is [SARS-CoV-2](covid_names)?
- covid
- what is [COVID](covid_names)?
- what [covid-19](covid_names)?
- tell me about [covid19](covid_names)?
- ano ba yang [coronavirus](covid_names)?
- bat may [ncov](covid_names)?
- Ano ang [covid](covid_names)?
- ano tong [CORONA](covid_names)?
- ano anong [virus](covid_names)?

## intent: prevent_covid_tag
- [Iwasan](prevent_names) ang [covid](covid_names)
- [iwas](prevent_names) sa [covid](covid_names)
- [iwasan](prevent_names) ang [covid](covid_names)
- iwas [covid](covid_names)
- paano [maiiwasan](prevent_names) ang [covid](covid_names)?
- mga paraan para [maiwasan](prevent_names) ang [covid](covid_names)
- mga [solusyon](prevent_names) sa [covid](covid_names)

## intent: list_covid_symptoms_tag
- [Sintomas](symptoms_names)
- anong mga [sintomas](symptoms_names) ng [covid](covid_names)?
- [covid](covid_names) [symptoms](symptoms_names)
- mga [simptoms](symptoms_names) nitong [covid](covid_names)
- [Sintomas](symptoms_names) ng [covid](covid_names)

## intent: cure_covid_tag
- anong [gamot](medicine_names)
- anong [cure](medicine_names) para sa [covid](covid_names)
- anong [solusyon](medicine_names) para sa [covid](covid_names) na to
- [medicine](medicine_names) para sa [covid](covid_names)
- pwedeng [medisina](medicine_names) para sa [covid](covid_names)
- [Gamot](medicine_names) para sa [covid](covid_names)
- may [bakuna](medicine_names) ba para sa [covid](covid_names)
- [vaccine](medicine_names) para sa [covid](covid_names)

## intent: corona_image
- [image](image_names) ng [covid](covid_names)
- anong [itsura](image_names) ng [covid](covid_names) to
- anong [itsura](image_names) nito
- [covid](covid_names) [picture](image_names)
- some [covid](covid_names) [pic](image_names)
- send [pix](image_names) of [covid](covid_names)
- sample [img](image_names) of [covid](covid_names)
- what [covid](covid_names) [look-like](image_names)
- magbigay ng [imahe](image_names) ng [covid](covid_names)
- tingin ng [picture](image_names) ng [covid](covid_names)

## intent: covid_origin_tag
- saan [nagmula](origin_names) ang [covid](covid_names)
- [pinagmulan](origin_names) nitong [covid](covid_names)
- [pinanggalingan](origin_names) ng [covid](covid_names)
- saan ba [nanggaling](origin_names) yang [covid](covid_names)
- [galing](origin_names) ang [covid](covid_names)
- [first case](origin_names) of [covid](covid_names)

## intent: curse
- [bobo](curse_words) ka
- ang [tanga](curse_words) mo
- [dambel](curse_words) ka ba?
- [ukkinam](curse_words) ket di
- [putang-ina](curse_words) ka
- [tangina](curse_words) ka
- [gago](curse_words) ka
- [ogag](curse_words) ka
- [fuck you](curse_words) ka
- [fuck](curse_words)
- [fu](curse_words)
- [yawa](curse_words)

## intent: respond_has_symptoms_none_tag
- Walang sintomas
- wala namang sintomas
- wala sintomas

## intent: respond_has_symptoms_all_tag
- Lahat ng sintomas
- lahat sintomas
- lahat ng sintomas

## intent: respond_has_symptoms_some_tag
- Ilan sa sintomas
- ilan sa sintomas
- ilan sa sintomas
- merong sintomas
- meron sintomas
- mayroong sintomas
- may sintomas

## intent: laugh
- hahaha
- haha
- HAHA
- wahaha
- hehe
- hehehe
- hihi

## lookup: prevent_names
data/lookups/prevent_names.txt

## synonym: Iwasan
- maiwasan
- iwasan
- mapigilan
- maprevent
- prevent
- solusyonan
- solusyon
- maiiwasan

## lookup: origin_names
data/lookups/origin_names.txt

## synonym: nagmula
- nanggaling
- galing
- pinanggalingan
- pinagmulan

## lookup: curse_words
data/lookups/curse_words.txt

## lookup: symptoms_names
- Sintomas

## synonym: Sintomas
- sintomas
- simptoms
- symptoms

## lookup: medicine_names
data/lookups/medicine_names.txt

## synonym: Gamot
- cure
- gamot
- medisina
- medicine

## synonym: Bakuna
- bakuna
- vaccine

## lookup: covid_names
data/lookups/covid_names.txt

## synonym:covid
- COVID-19
- COVID
- covid-19
- covid19
- coronavirus
- covid
- ncov
- CORONA
- virus
- SARS-CoV-2

## lookup: image_names
data/lookups/image_names.txt

## synonym:image
- itsura
- look-like
- imahe
- pix
- pic
- img
- picture
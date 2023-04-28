import datetime
from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel

CURRENT_YEAR = datetime.date.today().year

fake_employees_db = [
    {
        "id": 1,
        "first_name": "Torrin",
        "last_name": "Conibear",
        "email": "tconibear0@geocities.jp",
        "gender": "Male",
        "age": 47,
        "city": "São José dos Pinhais"
    }, {
        "id": 2,
        "first_name": "Shelbi",
        "last_name": "Risbridger",
        "email": "srisbridger1@globo.com",
        "gender": "Female",
        "age": 72,
        "city": "Tuxi"
    }, {
        "id": 3,
        "first_name": "Nikki",
        "last_name": "Chritchley",
        "email": "nchritchley2@multiply.com",
        "gender": "Female",
        "age": 89,
        "city": "Muqui"
    }, {
        "id": 4,
        "first_name": "Kendall",
        "last_name": "Kelson",
        "email": "kkelson3@jiathis.com",
        "gender": "Male",
        "age": 14,
        "city": "Rantau"
    }, {
        "id": 5,
        "first_name": "Daisey",
        "last_name": "Benns",
        "email": "dbenns4@about.me",
        "gender": "Female",
        "age": 20,
        "city": "Sheffield"
    }, {
        "id": 6,
        "first_name": "Glenn",
        "last_name": "Parkisson",
        "email": "gparkisson5@walmart.com",
        "gender": "Male",
        "age": 65,
        "city": "Meedhoo"
    }, {
        "id": 7,
        "first_name": "Marshall",
        "last_name": "Cicci",
        "email": "mcicci6@admin.ch",
        "gender": "Male",
        "age": 36,
        "city": "Añatuya"
    }, {
        "id": 8,
        "first_name": "Delmar",
        "last_name": "Heimann",
        "email": "dheimann7@jugem.jp",
        "gender": "Male",
        "age": 17,
        "city": "Noebesa"
    }, {
        "id": 9,
        "first_name": "Marika",
        "last_name": "Message",
        "email": "mmessage8@reuters.com",
        "gender": "Agender",
        "age": 54,
        "city": "Ambatolampy"
    }, {
        "id": 10,
        "first_name": "Juliet",
        "last_name": "Reitenbach",
        "email": "jreitenbach9@miitbeian.gov.cn",
        "gender": "Female",
        "age": 51,
        "city": "Masape"
    }, {
        "id": 11,
        "first_name": "Daryle",
        "last_name": "Dunn",
        "email": "ddunna@newyorker.com",
        "gender": "Male",
        "age": 62,
        "city": "Yanwang"
    }, {
        "id": 12,
        "first_name": "Jeni",
        "last_name": "Bernette",
        "email": "jbernetteb@va.gov",
        "gender": "Female",
        "age": 30,
        "city": "Lolayan"
    }, {
        "id": 13,
        "first_name": "Obed",
        "last_name": "Epperson",
        "email": "oeppersonc@google.ru",
        "gender": "Male",
        "age": 90,
        "city": "Sungaimaja"
    }, {
        "id": 14,
        "first_name": "Tades",
        "last_name": "Manley",
        "email": "tmanleyd@moonfruit.com",
        "gender": "Male",
        "age": 15,
        "city": "Cholpon-Ata"
    }, {
        "id": 15,
        "first_name": "Ody",
        "last_name": "Terrey",
        "email": "oterreye@hp.com",
        "gender": "Male",
        "age": 10,
        "city": "San Simon"
    }, {
        "id": 16,
        "first_name": "Irena",
        "last_name": "Alred",
        "email": "ialredf@vinaora.com",
        "gender": "Female",
        "age": 26,
        "city": "Bokaa"
    }, {
        "id": 17,
        "first_name": "Amby",
        "last_name": "Pauncefort",
        "email": "apauncefortg@whitehouse.gov",
        "gender": "Non-binary",
        "age": 87,
        "city": "Chiriguaná"
    }, {
        "id": 18,
        "first_name": "Jaquenetta",
        "last_name": "Damsell",
        "email": "jdamsellh@dagondesign.com",
        "gender": "Genderfluid",
        "age": 65,
        "city": "Tipo-Tipo"
    }, {
        "id": 19,
        "first_name": "Rudolfo",
        "last_name": "Mac Giany",
        "email": "rmacgianyi@aol.com",
        "gender": "Genderqueer",
        "age": 41,
        "city": "Pasarbaru"
    }, {
        "id": 20,
        "first_name": "Dudley",
        "last_name": "McCreedy",
        "email": "dmccreedyj@forbes.com",
        "gender": "Male",
        "age": 50,
        "city": "Phonphisai"
    }, {
        "id": 21,
        "first_name": "George",
        "last_name": "Rosoni",
        "email": "grosonik@yahoo.co.jp",
        "gender": "Female",
        "age": 45,
        "city": "Stockholm"
    }, {
        "id": 22,
        "first_name": "Wright",
        "last_name": "Lightning",
        "email": "wlightningl@shutterfly.com",
        "gender": "Male",
        "age": 84,
        "city": "Novyye Kuz’minki"
    }, {
        "id": 23,
        "first_name": "Ernestine",
        "last_name": "Stuchberry",
        "email": "estuchberrym@bloglines.com",
        "gender": "Female",
        "age": 28,
        "city": "Derviçian"
    }, {
        "id": 24,
        "first_name": "Ingeberg",
        "last_name": "Durling",
        "email": "idurlingn@japanpost.jp",
        "gender": "Female",
        "age": 21,
        "city": "Dongjiao"
    }, {
        "id": 25,
        "first_name": "Grantley",
        "last_name": "Lehrian",
        "email": "glehriano@etsy.com",
        "gender": "Male",
        "age": 81,
        "city": "Joal-Fadiout"
    }, {
        "id": 26,
        "first_name": "Reamonn",
        "last_name": "Esberger",
        "email": "resbergerp@senate.gov",
        "gender": "Male",
        "age": 38,
        "city": "San Quintin"
    }, {
        "id": 27,
        "first_name": "Zita",
        "last_name": "Cowope",
        "email": "zcowopeq@bizjournals.com",
        "gender": "Female",
        "age": 26,
        "city": "Gulbene"
    }, {
        "id": 28,
        "first_name": "Rosemary",
        "last_name": "Jouannisson",
        "email": "rjouannissonr@infoseek.co.jp",
        "gender": "Female",
        "age": 21,
        "city": "Bununu Kasa"
    }, {
        "id": 29,
        "first_name": "Konstantin",
        "last_name": "Nanson",
        "email": "knansons@sogou.com",
        "gender": "Male",
        "age": 49,
        "city": "Ośno Lubuskie"
    }, {
        "id": 30,
        "first_name": "Jonell",
        "last_name": "Byres",
        "email": "jbyrest@homestead.com",
        "gender": "Female",
        "age": 69,
        "city": "Cineumbeuy"
    }, {
        "id": 31,
        "first_name": "Antonietta",
        "last_name": "Mallord",
        "email": "amallordu@cafepress.com",
        "gender": "Polygender",
        "age": 78,
        "city": "Bílovice"
    }, {
        "id": 32,
        "first_name": "Hoebart",
        "last_name": "Shevelin",
        "email": "hshevelinv@storify.com",
        "gender": "Male",
        "age": 19,
        "city": "Rybí"
    }, {
        "id": 33,
        "first_name": "Birk",
        "last_name": "Alexandersson",
        "email": "balexanderssonw@wisc.edu",
        "gender": "Male",
        "age": 98,
        "city": "Santiago"
    }, {
        "id": 34,
        "first_name": "Yanaton",
        "last_name": "Rulf",
        "email": "yrulfx@hud.gov",
        "gender": "Non-binary",
        "age": 38,
        "city": "Al Mālikīyah"
    }, {
        "id": 35,
        "first_name": "Raoul",
        "last_name": "Brownsett",
        "email": "rbrownsetty@toplist.cz",
        "gender": "Male",
        "age": 30,
        "city": "Ugbokpo"
    }, {
        "id": 36,
        "first_name": "Westleigh",
        "last_name": "Walne",
        "email": "wwalnez@people.com.cn",
        "gender": "Male",
        "age": 54,
        "city": "Tebingtinggi"
    }, {
        "id": 37,
        "first_name": "Bernelle",
        "last_name": "Bumphries",
        "email": "bbumphries10@hhs.gov",
        "gender": "Female",
        "age": 65,
        "city": "Tobelo"
    }, {
        "id": 38,
        "first_name": "Chico",
        "last_name": "Habron",
        "email": "chabron11@t-online.de",
        "gender": "Bigender",
        "age": 32,
        "city": "Carregueira"
    }, {
        "id": 39,
        "first_name": "Kalila",
        "last_name": "Pingston",
        "email": "kpingston12@over-blog.com",
        "gender": "Female",
        "age": 61,
        "city": "Maniowy"
    }, {
        "id": 40,
        "first_name": "Spencer",
        "last_name": "Beamiss",
        "email": "sbeamiss13@howstuffworks.com",
        "gender": "Male",
        "age": 95,
        "city": "Pruszcz"
    }, {
        "id": 41,
        "first_name": "Angelika",
        "last_name": "Easthope",
        "email": "aeasthope14@ning.com",
        "gender": "Female",
        "age": 53,
        "city": "Palma Gil"
    }, {
        "id": 42,
        "first_name": "Stoddard",
        "last_name": "Callender",
        "email": "scallender15@is.gd",
        "gender": "Female",
        "age": 10,
        "city": "Cardal"
    }, {
        "id": 43,
        "first_name": "Gradeigh",
        "last_name": "Renbold",
        "email": "grenbold16@edublogs.org",
        "gender": "Male",
        "age": 42,
        "city": "Rączna"
    }, {
        "id": 44,
        "first_name": "Maxwell",
        "last_name": "Lovstrom",
        "email": "mlovstrom17@hao123.com",
        "gender": "Male",
        "age": 14,
        "city": "Stockholm"
    }, {
        "id": 45,
        "first_name": "Maureen",
        "last_name": "Peperell",
        "email": "mpeperell18@blog.com",
        "gender": "Female",
        "age": 89,
        "city": "Emmen"
    }, {
        "id": 46,
        "first_name": "Cate",
        "last_name": "Tort",
        "email": "ctort19@japanpost.jp",
        "gender": "Female",
        "age": 54,
        "city": "Terre Haute"
    }, {
        "id": 47,
        "first_name": "Addie",
        "last_name": "Flucks",
        "email": "aflucks1a@netscape.com",
        "gender": "Agender",
        "age": 97,
        "city": "Konyshevka"
    }, {
        "id": 48,
        "first_name": "Gaby",
        "last_name": "Rushton",
        "email": "grushton1b@redcross.org",
        "gender": "Non-binary",
        "age": 16,
        "city": "Phonphisai"
    }, {
        "id": 49,
        "first_name": "Lavinia",
        "last_name": "Skotcher",
        "email": "lskotcher1c@admin.ch",
        "gender": "Female",
        "age": 63,
        "city": "Älvsbyn"
    }, {
        "id": 50,
        "first_name": "Neil",
        "last_name": "Tatteshall",
        "email": "ntatteshall1d@yale.edu",
        "gender": "Male",
        "age": 46,
        "city": "Rohia"
    }, {
        "id": 51,
        "first_name": "Arney",
        "last_name": "Whilder",
        "email": "awhilder1e@dropbox.com",
        "gender": "Male",
        "age": 50,
        "city": "Xiangfeng"
    }, {
        "id": 52,
        "first_name": "Brittaney",
        "last_name": "Ferraretto",
        "email": "bferraretto1f@zimbio.com",
        "gender": "Female",
        "age": 65,
        "city": "Xinshi"
    }, {
        "id": 53,
        "first_name": "Mallissa",
        "last_name": "Barbisch",
        "email": "mbarbisch1g@java.com",
        "gender": "Female",
        "age": 88,
        "city": "Shuangxi"
    }, {
        "id": 54,
        "first_name": "Elmore",
        "last_name": "Edward",
        "email": "eedward1h@netscape.com",
        "gender": "Male",
        "age": 80,
        "city": "Fryčovice"
    }, {
        "id": 55,
        "first_name": "Haskel",
        "last_name": "Comrie",
        "email": "hcomrie1i@mozilla.com",
        "gender": "Male",
        "age": 27,
        "city": "Mosquera"
    }, {
        "id": 56,
        "first_name": "Jenna",
        "last_name": "Kubyszek",
        "email": "jkubyszek1j@princeton.edu",
        "gender": "Female",
        "age": 67,
        "city": "Hausjärvi"
    }, {
        "id": 57,
        "first_name": "Kittie",
        "last_name": "Bish",
        "email": "kbish1k@nhs.uk",
        "gender": "Agender",
        "age": 66,
        "city": "Cheongju-si"
    }, {
        "id": 58,
        "first_name": "Clevey",
        "last_name": "Colisbe",
        "email": "ccolisbe1l@facebook.com",
        "gender": "Male",
        "age": 36,
        "city": "Radocza"
    }, {
        "id": 59,
        "first_name": "Holt",
        "last_name": "Hannen",
        "email": "hhannen1m@miibeian.gov.cn",
        "gender": "Male",
        "age": 95,
        "city": "Arlington"
    }, {
        "id": 60,
        "first_name": "Lilyan",
        "last_name": "Luipold",
        "email": "lluipold1n@samsung.com",
        "gender": "Genderfluid",
        "age": 53,
        "city": "Villa Elisa"
    }, {
        "id": 61,
        "first_name": "Bridie",
        "last_name": "Ethersey",
        "email": "bethersey1o@webmd.com",
        "gender": "Female",
        "age": 28,
        "city": "Rosa Zarate"
    }, {
        "id": 62,
        "first_name": "Jarrid",
        "last_name": "Okenden",
        "email": "jokenden1p@patch.com",
        "gender": "Male",
        "age": 45,
        "city": "Ariquemes"
    }, {
        "id": 63,
        "first_name": "Giacobo",
        "last_name": "Inderwick",
        "email": "ginderwick1q@blogs.com",
        "gender": "Male",
        "age": 58,
        "city": "Amsterdam Westpoort"
    }, {
        "id": 64,
        "first_name": "Ewan",
        "last_name": "Gutsell",
        "email": "egutsell1r@ovh.net",
        "gender": "Male",
        "age": 56,
        "city": "Timon"
    }, {
        "id": 65,
        "first_name": "Gisella",
        "last_name": "Urwin",
        "email": "gurwin1s@dmoz.org",
        "gender": "Female",
        "age": 78,
        "city": "Ban Talat Yai"
    }, {
        "id": 66,
        "first_name": "Hartley",
        "last_name": "Druhan",
        "email": "hdruhan1t@bing.com",
        "gender": "Male",
        "age": 93,
        "city": "Toulouse"
    }, {
        "id": 67,
        "first_name": "Fraser",
        "last_name": "Bernardeschi",
        "email": "fbernardeschi1u@guardian.co.uk",
        "gender": "Male",
        "age": 48,
        "city": "Nedryhayliv"
    }, {
        "id": 68,
        "first_name": "Frankie",
        "last_name": "Ballinghall",
        "email": "fballinghall1v@va.gov",
        "gender": "Male",
        "age": 34,
        "city": "Alejo Ledesma"
    }, {
        "id": 69,
        "first_name": "Ignazio",
        "last_name": "Taffarello",
        "email": "itaffarello1w@bbc.co.uk",
        "gender": "Male",
        "age": 37,
        "city": "Sepekov"
    }, {
        "id": 70,
        "first_name": "Wilow",
        "last_name": "O'Lehane",
        "email": "wolehane1x@discuz.net",
        "gender": "Female",
        "age": 66,
        "city": "Besançon"
    }, {
        "id": 71,
        "first_name": "Patrizio",
        "last_name": "MacTague",
        "email": "pmactague1y@globo.com",
        "gender": "Male",
        "age": 40,
        "city": "Rio Largo"
    }, {
        "id": 72,
        "first_name": "Ilene",
        "last_name": "Lythgoe",
        "email": "ilythgoe1z@flickr.com",
        "gender": "Female",
        "age": 72,
        "city": "Taling Chan"
    }, {
        "id": 73,
        "first_name": "Sephira",
        "last_name": "Ducker",
        "email": "sducker20@engadget.com",
        "gender": "Female",
        "age": 61,
        "city": "Lindavista"
    }, {
        "id": 74,
        "first_name": "Karoly",
        "last_name": "Incogna",
        "email": "kincogna21@sina.com.cn",
        "gender": "Male",
        "age": 91,
        "city": "Kalety"
    }, {
        "id": 75,
        "first_name": "Terese",
        "last_name": "Collocott",
        "email": "tcollocott22@sbwire.com",
        "gender": "Female",
        "age": 17,
        "city": "Chortkiv"
    }, {
        "id": 76,
        "first_name": "Candide",
        "last_name": "Mourgue",
        "email": "cmourgue23@merriam-webster.com",
        "gender": "Female",
        "age": 20,
        "city": "Vilque Chico"
    }, {
        "id": 77,
        "first_name": "Randolf",
        "last_name": "Fayerbrother",
        "email": "rfayerbrother24@pbs.org",
        "gender": "Male",
        "age": 41,
        "city": "Mayapusi"
    }, {
        "id": 78,
        "first_name": "Fitzgerald",
        "last_name": "Chuney",
        "email": "fchuney25@google.com.br",
        "gender": "Male",
        "age": 58,
        "city": "Embalse"
    }, {
        "id": 79,
        "first_name": "Mendel",
        "last_name": "Syddall",
        "email": "msyddall26@yahoo.co.jp",
        "gender": "Male",
        "age": 57,
        "city": "San Pedro Ayampuc"
    }, {
        "id": 80,
        "first_name": "Jeni",
        "last_name": "Howard - Gater",
        "email": "jhowardgater27@google.com.au",
        "gender": "Female",
        "age": 10,
        "city": "Saint John’s"
    }, {
        "id": 81,
        "first_name": "Oralla",
        "last_name": "Kreber",
        "email": "okreber28@seattletimes.com",
        "gender": "Female",
        "age": 22,
        "city": "El Cantón de San Pablo"
    }, {
        "id": 82,
        "first_name": "Celie",
        "last_name": "Breckin",
        "email": "cbreckin29@hostgator.com",
        "gender": "Female",
        "age": 16,
        "city": "Campo"
    }, {
        "id": 83,
        "first_name": "Lissa",
        "last_name": "Sherborne",
        "email": "lsherborne2a@aol.com",
        "gender": "Female",
        "age": 50,
        "city": "Homagama"
    }, {
        "id": 84,
        "first_name": "Remington",
        "last_name": "Bonehill",
        "email": "rbonehill2b@storify.com",
        "gender": "Male",
        "age": 42,
        "city": "Perreng"
    }, {
        "id": 85,
        "first_name": "Lynnet",
        "last_name": "Rookwell",
        "email": "lrookwell2c@va.gov",
        "gender": "Female",
        "age": 46,
        "city": "Hamburg"
    }, {
        "id": 86,
        "first_name": "Corabelle",
        "last_name": "Steeden",
        "email": "csteeden2d@flavors.me",
        "gender": "Bigender",
        "age": 67,
        "city": "Victoria"
    }, {
        "id": 87,
        "first_name": "Tony",
        "last_name": "Stollenbecker",
        "email": "tstollenbecker2e@shareasale.com",
        "gender": "Male",
        "age": 19,
        "city": "Buffalo"
    }, {
        "id": 88,
        "first_name": "Oralla",
        "last_name": "Ibbetson",
        "email": "oibbetson2f@toplist.cz",
        "gender": "Female",
        "age": 76,
        "city": "Nirji"
    }, {
        "id": 89,
        "first_name": "Emmalynne",
        "last_name": "Jursch",
        "email": "ejursch2g@constantcontact.com",
        "gender": "Female",
        "age": 95,
        "city": "Saint-Quentin"
    }, {
        "id": 90,
        "first_name": "Tanhya",
        "last_name": "Surphliss",
        "email": "tsurphliss2h@ask.com",
        "gender": "Female",
        "age": 23,
        "city": "Turenki"
    }, {
        "id": 91,
        "first_name": "Florencia",
        "last_name": "Shooter",
        "email": "fshooter2i@php.net",
        "gender": "Female",
        "age": 27,
        "city": "Žemaičių Naumiestis"
    }, {
        "id": 92,
        "first_name": "Sissie",
        "last_name": "Sorsby",
        "email": "ssorsby2j@ft.com",
        "gender": "Female",
        "age": 63,
        "city": "Zhangatas"
    }, {
        "id": 93,
        "first_name": "Hillier",
        "last_name": "Cobon",
        "email": "hcobon2k@flickr.com",
        "gender": "Male",
        "age": 100,
        "city": "Mirsíni"
    }, {
        "id": 94,
        "first_name": "Rodolfo",
        "last_name": "Hurtado",
        "email": "rhurtado2l@answers.com",
        "gender": "Male",
        "age": 30,
        "city": "Pardesiyya"
    }, {
        "id": 95,
        "first_name": "Ewen",
        "last_name": "Tasseler",
        "email": "etasseler2m@upenn.edu",
        "gender": "Male",
        "age": 68,
        "city": "Tibigan"
    }, {
        "id": 96,
        "first_name": "Rodrick",
        "last_name": "Golds",
        "email": "rgolds2n@blogger.com",
        "gender": "Male",
        "age": 96,
        "city": "‘Arīqah"
    }, {
        "id": 97,
        "first_name": "Donnie",
        "last_name": "Morsey",
        "email": "dmorsey2o@nps.gov",
        "gender": "Female",
        "age": 85,
        "city": "Antsohimbondrona"
    }, {
        "id": 98,
        "first_name": "Gaylor",
        "last_name": "Jiggle",
        "email": "gjiggle2p@oakley.com",
        "gender": "Male",
        "age": 10,
        "city": "Suidong"
    }, {
        "id": 99,
        "first_name": "Dalenna",
        "last_name": "Totton",
        "email": "dtotton2q@cnet.com",
        "gender": "Female",
        "age": 32,
        "city": "Polevskoy"
    }, {
        "id": 100,
        "first_name": "Elie",
        "last_name": "Kingsland",
        "email": "ekingsland2r@digg.com",
        "gender": "Female",
        "age": 87,
        "city": "Huaizhong"
    }]


# Models

class Employee(BaseModel):
    id: int | None = None
    first_name: str
    last_name: str
    email: str | None = None
    gender: str | None = None
    age: int
    city: str


class Week(str, Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


app = FastAPI()

EMPLOYEES = []


@app.on_event("startup")
def load_database():
    for employee in fake_employees_db:
        EMPLOYEES.append(Employee.parse_obj(employee))


def filter_employees_by_city(employee, city):
    if employee.city == city:
        return True


def filter_employee_by_id(employee, id):
    if employee.id == id:
        return True


@app.get("/")
async def root():
    return {"message": "Hello World!!!"}


@app.get("/employees")
async def get_all_items(skip: int = 0, limit: int = 2, city: str | None = None, age: int | None = None):
    employees = EMPLOYEES[skip: skip + limit]
    if city:
        filtered_employees = filter(lambda employee: filter_employees_by_city(employee, city), employees)
        return list(filtered_employees)
    return employees


@app.get("/week-mapping/{day}")
async def get_week_mapping(day: Week):
    # this returns name/key of the enum
    # to access value, use .value instead .name
    return day.name


@app.post("/employees")
async def create_employee(employee: Employee):
    # birth_year = CURRENT_YEAR - employee_dict.get("age")
    # employee_dict.update({"birth_year": birth_year})
    employee.id = len(EMPLOYEES) + 1
    EMPLOYEES.append(employee)
    return {"message": "successful"}


@app.put("/employees/{employee_id}")
async def update_employee(employee: Employee, employee_id: int):
    employee_dict = employee.dict()
    print(employee_dict)
    filtered_employee = next(
        filter(lambda employee: filter_employee_by_id(employee, employee_id), EMPLOYEES))
    for key, value in employee_dict.items():
        print(key)
        print(value)
        filtered_employee[key] = value
    return {"message": "successful"}


if __name__ == '__main__':
    filtered = filter(lambda seq: filter_employees_by_city(seq, "Ventsy"), fake_employees_db)
    print(list(filtered))

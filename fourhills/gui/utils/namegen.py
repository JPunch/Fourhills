'''
This is a markov name generator based off the name generator from https://donjon.bin.sh/code/name/
and ported to python
'''

import math
import random


def generate_name(name_set):
    chain = markov_chain(name_set)
    if chain:
         return markov_name(chain)
    return ''


def name_list(name_set, n_of):
    return [generate_name(name_set) for _ in range(n_of)]


def markov_chain(name_set):
    ls = name_set
    chain = construct_chain(ls)
    if chain:
        return chain
    return False
    

def construct_chain(ls):
    chain = {}

    for i in range(len(ls)):
        names = ls[i].split()
        chain = incr_chain(chain, "parts", len(names))

        for name in names:
            chain = incr_chain(chain, "name_len", len(name))

            c =  name[0:1]
            chain = incr_chain(chain, "initial", c)

            string = name[1:]
            last_c = c

            while len(string) > 0:
                c = string[0:1]
                chain = incr_chain(chain, last_c,c)

                string = string[1:]
                last_c = c
    return scale_chain(chain)


def incr_chain(chain, key, token):
    if key in chain: 
        if token in chain[key]:
            chain[key][token] += 1
        else:
            chain[key][token] = 1
    else:
        chain[key] = {}
        chain[key][token] = 1
    return chain

    
def scale_chain(chain):
    table_len = {}
    for key in chain:
        table_len[key] = 0

        for token in chain[key]:
            count = chain[key][token]
            weighted = math.floor(math.pow(count, 1.3))

            chain[key][token] = weighted
            table_len[key] += weighted
            
    chain['table_len'] = table_len
    return chain


#construct name from markov chain

def markov_name(chain):                                                      
    parts = select_link(chain, "parts")
    names = []
    for i in range(parts):
        name_len = select_link(chain, "name_len")
        c = select_link(chain, "initial")
        name = c
        last_c = c

        while len(name) < name_len:
            c = select_link(chain, last_c)
            name += c
            last_c = c;
        names.append(name)

    return " ".join(names)


def select_link(chain, key):
    if key in chain["table_len"]:
        length = chain["table_len"][key]
    else:
        length = 1
    idx = math.floor(random.random() * length)
    t = 0
    for token in chain[key]:
        t += chain[key][token]
        if idx < t:
            return token

    return "-"

# def select_link(chain, key):
#     length = chain.table_len[key]
#     length = math.floor(random.random() * length)
#     d = 0
#     for token in chain[key]:
#         d += chain[key][token]
#         if length < d:
#             return token
#     return "-"


name_set = ['Aakheperkare', 'Addaya', 'Ahhotpe', 'Ahmes', 'Ahmose',
    'Ahmose-saneit', 'Ahmose-sipari', 'Akencheres', 'Akunosh',
    'Amenakht', 'Amenakhte', 'Amenemhat', 'Amenemheb', 'Amenemopet',
    'Amenhirkopshef', 'Amenhirwenemef', 'Amenhotpe', 'Amenmesse',
    'Amenmose', 'Amennestawy', 'Amenope', 'Amenophis', 'Amenwahsu',
    'Ameny', 'Amosis-ankh', 'Amoy', 'Amunemhat', 'Amunherpanesha',
    'Amunhotpe', 'Anen', 'Ankh-Psamtek', 'Ankhef', 'Ankhefenamun',
    'Ankhefenkhons', 'Ankhefenmut', 'Ankhsheshonq', 'Ankhtify',
    'Ankhtyfy', 'Ankhu', 'Ankhuemhesut', 'Any', 'Apophis', 'Baba',
    'Baenre', 'Bak', 'Bakenkhons', 'Bakenkhonsu', 'Bakenmut',
    'Bakennefi', 'Bakenptah', 'Baky', 'Bata', 'Bay', 'Bek', 'Bengay',
    'Besenmut', 'Butehamun', 'Denger', 'Deniuenkhons', 'Djadjaemankh',
    'Djau', 'Djedefhor', 'Djedhor', 'Djedhoriufankh', 'Djedi',
    'Djedkhonsiufankh', 'Djedkhonsuefankh', 'Djedptahefankh',
    'Djedptahiufankh', 'Djehutmose', 'Djehuty', 'Djehutymose',
    'Djenutymes', 'Djeserka', 'Djeserkare', 'Djeserkheprure',
    'Djesersukhons', 'Djethutmose', 'Djhutmose', 'Genubath', 'Gua',
    'Haankhef', 'Hapimen', 'Hapu', 'Hapuseneb', 'Hapymen',
    'Haremakhet', 'Haremsat', 'Harkhebi', 'Harkhuf', 'Harmhabi',
    'Harnakhte', 'Harsiese', 'Hay', 'Hemaka', 'Henenu', 'Henuka',
    'Heqaemeheh', 'Heqaib', 'Herenamenpenaef', 'Herihor', 'Hesire',
    'Hor', 'Horapollo', 'Hordedef', 'Horemheb', 'Hori', 'Hornedjitef',
    'Horpais', 'Horwebbefer', 'Hrihor', 'Hunefer', 'Huy', 'Huya',
    'Iawy', 'Ibana', 'Ibe', 'Idy', 'Ikeni', 'Ikui', 'Imhotep',
    'Inarus', 'Inebni', 'Ineni', 'Inyotef', 'Ipi', 'Ipuwer', 'Ipuy',
    'Ipy', 'Ishpi', 'Iu-Amun', 'Iufankh', 'Iufenamun', 'Iunmin',
    'Iuseneb', 'Iuwlot', 'Iyerniutef', 'Iyimennuef', 'Iymeru', 'Jarha',
    'Kadjadja', 'Kahma', 'Kaka', 'Kanakht', 'Karnefhere', 'Katenen',
    'Kawab', 'Kay', 'Kemuny', 'Kenamun', 'Kenefer', 'Kerasher', 'Kha',
    'Khaemhet', 'Khaemnetjeru', 'Khaemwaset', 'Khahor',
    'Khakheperraseneb', 'Khay', 'Khensthoth', 'Kheruef', 'Khety',
    'Khnemibre', 'Khnumhotep', 'Khnumhotpe', 'Khons', 'Khonsirdais',
    'Khonskhu', 'Khonsuemwaset', 'Khufukhaf', 'Khui', 'Kuenre',
    'Kysen', 'Maakha', 'Mahu', 'Mahuhy', 'Maiherpri', 'Manakhtuf',
    'Manetho', 'Masaharta', 'May', 'Maya', 'Mehy', 'Meketre', 'Mekhu',
    'Men', 'Menkheperraseneb', 'Menkheperre', 'Menmet-Ra', 'Menna',
    'Mentuemhat', 'Mentuherkhepshef', 'Meremptor', 'Merenamun',
    'Merenkhons', 'Merenptah', 'Mereruka', 'Merka', 'Mernebptah',
    'Mery', 'Meryamun', 'Meryatum', 'Meryawy', 'Merymose', 'Meryptah',
    'Meryrahashtef', 'Meryre', 'Mes', 'Min', 'Minkhat', 'Minmose',
    'Minnakht', 'Mokhtar', 'Montjuemhat', 'Montjuhirkopshef',
    'Montuemhet', 'Mose', 'Naga-ed-der', 'Nakhthorheb',
    'Nakhtimenwast', 'Nakhtmin', 'Nakhtnebef', 'Naneferkeptah',
    'Nebamun', 'Nebankh', 'Nebemakst', 'Nebhotep', 'Nebimes',
    'Nebitka', 'Nebmaetre', 'Nebnefer', 'Nebnetjeru', 'Nebseni',
    'Nebseny', 'Nebwennenef', 'Nechoutes', 'Neferhotep', 'Neferhotpe',
    'Neferkheperuhersekheper', 'Nefermaet', 'Nefermenu', 'Neferrenpet',
    'Neferti', 'Nehasy', 'Nehi', 'Nekau', 'Nekhwemmut',
    'Nendjbaendjed', 'Nenedjebaendjed', 'Neneferkaptah', 'Nenkhefta',
    'Nes', 'Nesamun', 'Neshi', 'Neshorpakhered', 'Neskhons', 'Nesmont',
    'Nespaherenhat', 'Nespakashuty', 'Nespatytawy', 'Nespherenhat',
    'Nessuimenopet', 'Nestanebetasheru', 'Nestefnut', 'Netihur',
    'Nigmed', 'Nimlot', 'Niumateped', 'Pa-Siamun', 'Pabasa',
    'Pabernefy', 'Padiamenet', 'Padiamenipet', 'Padiamun', 'Padineith',
    'Paheripedjet', 'Pairy', 'Pait', 'Pakharu', 'Pakhneter', 'Pamont',
    'Pamose', 'Pamu', 'Panas', 'Paneb', 'Paneferher', 'Panehesy',
    'Paperpa', 'Paramesse', 'Parennefer', 'Pasebakhaenniut',
    'Pasekhonsu', 'Paser', 'Pashedbast', 'Pashedu', 'Pasherdjehuty',
    'Pawiaeadja', 'Paynedjem', 'Payneferher', 'Pediamun', 'Pediese',
    'Pedihor', 'Penamun', 'Penbuy', 'Penmaat', 'Pennestawy',
    'Pentaweret', 'Pentu', 'Pepynakhte', 'Peraha', 'Pinhasy',
    'Pinotmou', 'Prahotpe', 'Pramessu', 'Preherwenemef',
    'Prehirwennef', 'Prepayit', 'Psamtek', 'Psenamy', 'Psenmin',
    'Ptahhemakhet', 'Ptahhemhat-Ty', 'Ptahhotep', 'Ptahhudjankhef',
    'Ptahmose', 'Ptahshepses', 'Qenymin', 'Rahotep', 'Rahotpe', 'Raia',
    'Ramessenakhte', 'Ramessu', 'Rekhmire', 'Reuser', 'Rewer',
    'Roma-Roy', 'Rudamun', 'Sabef', 'Sabni', 'Salatis', 'Samut',
    'Sanehet', 'Sasobek', 'Sawesit', 'Scepter', 'Sekhemkare',
    'Sekhmire', 'Seneb', 'Senebtyfy', 'Senemut', 'Senmen', 'Sennedjem',
    'Sennefer', 'Sennufer', 'Senui', 'Senwosret', 'Serapion', 'Sese',
    'Setau', 'Setep', 'Sethe', 'Sethherwenemef', 'Sethhirkopshef',
    'Sethnakhte', 'Sethnakte', 'Sethy', 'Setne', 'Setymerenptah',
    'Shedsunefertum', 'Shemay', 'Shepenwepet', 'Si-Mut', 'Siamun',
    'Siese', 'Sinuhe', 'Sipair', 'Sneferu', 'Somtutefnakhte', 'Surero',
    'Suty', 'Sutymose', 'Takairnayu', 'Takany', 'Tasetmerydjehuty',
    'Tayenimu', 'Tefibi', 'Tenermentu', 'Teti-en', 'Tetisheri',
    'Tjaenhebyu', 'Tjahapimu', 'Tjaroy', 'Tjauemdi', 'Tjenna', 'Tjety',
    'To', 'Tui', 'Tutu', 'Tymisba', 'Udjahorresne', 'Udjahorresneith',
    'Uni', 'Userhet', 'Usermontju', 'Wadjmose', 'Wahibre-Teni',
    'Wahka', 'Webaoner', 'Webensenu', 'Wedjakhons', 'Wenamun',
    'Wendjabaendjed', 'Wendjebaendjed', 'Weni', 'Wennefer', 'Wennufer',
    'Wepmose', 'Wepwawetmose', 'Werdiamenniut', 'Werirenptah',
    'Yanhamu', 'Yey', 'Yii', 'Yuya', 'Zazamoukh']

name_set1 = ["zacc", "ziam", "Lzc", "Gzzg", "Luzy", "Szacy"]
# for _ in range(10):
#     print(generate_name(name_set1))

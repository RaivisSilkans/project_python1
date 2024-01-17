import os # biblioteka, kas ir saistīta ar vis operetajsistemu, ar vinja palizdzibu es atrodu kur atrodas skirpts, kas atrodas vēl kopā ar skriptu, viss kas saistīts ar datoru
import shutil # sho biblioteku es izmantoju lai pārvietotu failus, jo mans skripts ir domats lai noskenetu mapi kur skripts atrodas, un izveidotu katram faila tipam atsevisku folderu
import time # vienkarsi prikola peec, lai izskatitos ka kkas notiek sarezhgiits.


def failusortings():
    
    scripta_loc = os.path.dirname(os.path.realpath(__file__)) # kur atrodas shis skripts
    faili_mape = os.listdir(scripta_loc) #nolasa kas atrodas šaja directorija
    dublikata_mapes = ["Folders", "csv", "png", "py", "pptx", "xlsx","doc","txt","webp","jpeg"]
    print("You mind if I scan and did sorting in this folder?")
    user_choice = input("Please, enter excactly 'Yeah' or 'Nope'").lower() # .lower() noziime Yes parveidot par yes, dēļ case sensetive, jeb dēļ  if user_choice == 'yes':

    if user_choice == 'yeah':
        time.sleep(1)
        print("Starting scnanning place...")
        folderi = []
        failu_tipi = {}# izveido listu un dict lai saglabatu failu tipus un mapes

        for item_nosaukums in faili_mape:
            item_vieta = os.path.join(scripta_loc, item_nosaukums)

            if item_nosaukums == os.path.basename(__file__):# šīs if ...... izdara lai šitais python fails nepārnestnos nekur, lai paliktu savā sākumpozīcijā
                continue

            if os.path.isfile(item_vieta): # shis isFile parbauda vai fails no nolasitas informacijas faili_mape, ir fails
                faila_tips = os.path.splitext(item_nosaukums)[1].lower()
                if faila_tips in failu_tipi:
                    failu_tipi[faila_tips].append(item_nosaukums) # shaja vieta, ja precizejas, ka tiesi shii nolaista vieniba ir fails, vins ievieto to dictionary, failu_tipi[file type].append(item_nosaukums)               
                else:
                    failu_tipi[faila_tips] = [item_nosaukums] # sheit vins panem no iepriekseja if.... faila tipu, piem, pirmais items bija png fails, pec ta kad bins vinu pievieno dict, vins iet uz else un izveido tiesi {<<<<png:>>>} sho png nodalijumu, kur veelak visas png bus pievienotas, un ja next fails nav png, vins atkal iet caur else un izveido jaunu nodalijumu dict
            elif os.path.isdir(item_vieta):
                folderi.append(item_nosaukums) # un sheit jau ir tas, ja tas item nav faila tips, tas nozime ka tas ir folder, un tapec izmantojas isdir, parbauda ja tas nav fails, tad tas ir folders, un pievieno vina parametrus folders lista


        print("Scan completed, setting up sorting. 50%...")
        time.sleep(1)

        for faila_tips, faili in failu_tipi.items(): #shis for cikls izveido katram failu tipam atsevisku folderi
            folderi_delj_tipiem = os.path.join(scripta_loc, f"{faila_tips[1:]}")# f"{faila_tips[1:*nogriezh punktu jeb pirmo elementu]}", un f ir tas pats kas format, lai formatetu apgriezto nosaukumu
            os.makedirs(folderi_delj_tipiem, exist_ok=True) #makedirs ir domats lai izvedidotu folderus, exist_ok=True ir domats ja folders ar tadu pasu nosaukumu jau ir, lai vins ignoretu to un nemestu erroru

            for faila_nosauk in faili:# sheit jau ir tas lai paarvietotu failus un folderus uz vinu folderiem izveidotajiem, seit izmantojas shutil biblioteka
                sakums = os.path.join(scripta_loc, faila_nosauk) # vins norada, ka saukuma ir scripta_loc kas ir skripta lokacijas folderis, un faila_nosaauk, kas ir for cikla pirmais parametrs, tas ir, ejot cauri for ciklam, seit un nakosaja rinda ierakstas katrs items kas ir faili iekshaa, un noradas, kur ir sakuma pozicijas, kur ir beigu destinacija)), un ar shutil.move norada no kurienes uz kurieni parnest
                beigu_pozicija = os.path.join(folderi_delj_tipiem, faila_nosauk)
                shutil.move(sakums, beigu_pozicija) 
        
        mape_del_mapem = os.path.join(scripta_loc, "Folders") # un shis ir gandriz tas pats kas ieprieks tikai shis izveido atseviski delj folderiem folderi_)
        os.makedirs(mape_del_mapem, exist_ok=True) # makedirs izveido folderi, exist_ok =true ir, lai, ja ir jau Folders folderis, lai nebutu errora.
        print("Sorting almost done, files sorted and moved, folders left. 80%...")
        
        for mapes_nosauk in folderi: # lai cik tas smiekligi neubtu, vins parvieto folderi uz Folders folderi__) iet cauri katram folderi[] listam un norada, ka vins sakuma ir seit, kur vinam jabut beigas, un jau ar sutil.move notiek kustiba
            sakums = os.path.join(scripta_loc, mapes_nosauk)
            beigu_pozicija = os.path.join(mape_del_mapem, mapes_nosauk)
            if mapes_nosauk in dublikata_mapes:
                continue
            shutil.move(sakums, beigu_pozicija)
        print("Sorting completed")
    elif user_choice == 'nope':
        print("Why not? Okay, maybe next time buddy_)")
    else:
        print("You typed wrong, dude. Run me again_))))")

if __name__ == "__main__":
    failusortings()

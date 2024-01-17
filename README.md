***SMF - Sort My Folder***
# Raivis Silkāns : 231RDB355
## 9. grupa
### 1. kurss

# Warning
***PIRMS IZMANTOT ŠO KODU MAPĒ. PĀRLIECINIETIES KA TUR NAV FAILU SAISTĪBĀ AR DATORU, OS u.c.***

# Kāpēc izmantot SMF?
SMF ir noderīga, piemēram, ja jums ir kāda mape, kur ir daudz vienību, jeb ***Item***, un ir ļoti liela gribēšana to visu atsortēt.
Piemēram, man ir mape ***Downloads***, kur man bija pāri 1000+ failu, kā arī tostarp bija vairakas mapes, un man gribējās ieviest
tur kārtību, tāpēc es izņēmu no arhīva SMF, nokopēju to, un vienkārši ***ctrl-v*** iemetu Downloads mapē. Pēc ***10 sekundēm***
Downloads mape bija ideāli atsortēta un viss bija nokoplektēts, kur ir png faili, bija atseviška mape ***png***, kur excel faili, ***xlsx*** mape, ***u.c.***

# Kādas bibliotēkas izmantojas SMF skripta rakstīšanā?
***SMF*** rakstīšanas procesā tika izmantotas kopumā ***3 bibliotēkas***, tās ir : ***OS***, ***shutil*** un ***time*** bibliotēkas.
No šīm bibliotēkām, tikai divas bija ***nopietni vajadzīgas***, tās ir **os** un **shutil**, tā kā viņas nodarbojās ar ***main*** darbībās,
tādāk kā : **mapes atrašanās vietas noteikšana**, **failu pārvietošana**, **failu skenēšana**, bet **time** bibliotēka ir izmantota tikai dēļ
tā lai nenotiktu viss par 2 sekundēm.

# Kā izmantot SMF?
***1.*** Nolādet arhīvu ar failu
***2.*** Izarhivēt failu **SMF**
***3.*** **CTRL-C** SMF failu
***4.*** **CTRL-V** jums izvēlētajā mapē
***5.*** palaist programmu 

# Kādas fukncijas no bibliotēkām ir main-orientated?
**os** : 

[***os.path.dirname()*** - Nolasa kāda ir programmas atrašanās vieta]

[***os.listdir()*** - Pēc tā kad nolasa kur atrodas programma, šis nolasa visu kas atrodas šajā mape] 

[***os.path.join()*** - Pievieno pie kādas esošās vietas izvēlēto lietu. Vienkāršāk,os.path.join("folder", "file.txt"), beigu beigās iznāks folder\filetxt] 

[***os.path.isfile()*** - Pārbauda, vai šajā atrašanās vietā nolasītie **items** it faili, vai kas cits]

[***os.path.splitext()*** - Šo izmantoju lai apgriezt .png un formatēt to, lai iznāktu ideāls nosaukums dēļ mapēm, t.i. .png --> png, .torrent --> torrent]

[***os.path.isdir()*** - Un šeit ir tas pats kas isFile, tikai šis pārbauda vai **item** ir mape jeb ***folder***]

[***os.makedirs()*** - Šis izmantojas lai izveidotu mapes jeb **folders**]

**shutil** :

[***shutil.move()*** - Tika izmantots lai pārvietotu failus un mapes uz citu lokāciju]

**time** : 

[***time.sleep()*** - Šo es ieliku lai vienkārši viss izskatītos estētiskāk]

# Programmatūras izmantošanmas metodes

***1.*** **Interface** pašlaik nebūs diez ko ideāla, bija doma ievietot pogas nevis vajadzību rakstīt tekstu, bet pašlaik tas ir viss uz ko esmu spējīgs.

***2.*** **Secība** šai programmai ir vienkāršāka par vienkāršo. No sākuma, kad viņu palaist, un ierakstīt 'Yeah', viņa sāk skenēt kur atrodas programma, t.i. kāda ir atrašanās vieta (C:\xxxx\xxxx\xxxx), un no tā seko, kad tā veica skenēšanu, un atrada lokāciju, viņa sāk skenēt kas vispār atrodas šajā mapē. Beidzoties skenēšanai, tā sāk savu darbību, sākot ar folderiem, SMF sāk nolasīt folderus, un ievietot informāciju par tiem jau nesen izveidotā listā **folders[]**. Pēc tā, kad noskenēja, un izveidoja jaunu mapi **Folders**, tā pārvieto visas iepriekš šajā mapē atrodošās mapes jaunajā mapē. Un ***identiska operācija*** notiek ar failiem. Bet arī kodā ir pierakstīts, ka paša programma paliks tur kur viņa bija, ***programma nekur netiks pārvietota***. Un tas ir viss, katram faila tipam, piemēram png, txt, xlsx, csv, jpeg u.c. būs savas mapes, un **png** mapē atradīsies visi png faili, utt. 

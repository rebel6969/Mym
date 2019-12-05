from telethon import events
import random, re
from uniborg.util import admin_cmd
import asyncio

METOOSTR = [
    "`Me too thanks`",
    "`Haha yes, me too`",
    "`Same lol`",
    "`Me irl`",
    "`HA me bhi bhai bsdk!`",
    "`Same here`",
    "`Haha yes`",
    "`Same pinch bsdk`",
]
NOOBSTR = [
    "`YOU PRO NIMBA DONT MESS WIDH MEH`",
    "`Haha yes`",
    "`NOOB NIMBA TRYING TO BE FAMOUS KEK`",
    "`Sometimes one middle finger isn’t enough to let someone know how you feel. That’s why you have two hands`",
    "`Some Nimbas need to open their small minds instead of their big mouths`",
    "`UH DONT KNOW MEH SO STAY AWAY LAWDE`",
    "`Kysa kysaaaa haaan? Phir MAAR nhi Khayega tu?`",
    "`Zikr Jinka hota hai galiyo meh woh bhosdika ajj paya gya naliyo me`",
]
RUNSREACTS = [
    "`Runs to Thanos`",
    "`Runs to Modiji For Achey Din`",
    "`Runs far, far away from earth`",
    "`Running faster than usian bolt coz I'mma Bot`",
    "`Runs to Marie`",
    "`This Group is too cancerous to deal with.`",
    "`Cya bois`",
    "`I am a mad person. Plox Ban me.`",
    "`I go away`",
    "`I am just walking off, coz me is too fat.`",
    "`I Fugged off!`",
]
RAPE_STRINGS = [
     "`Rape Done Drink The Cum`",
     "`EK baat yaad rkhio, Chut ka Chakkar matlab maut se takkar`",
     "`The user has been successfully raped`",
     "`Dekho Bhaiyya esa hai! Izzat bachailo apni warna Gaand maar lenge tumhari`",
     "`Relax your Rear, ders nothing to fear,The Rape train is finally here`",
     "`Rape coming... Raped! haha 😆`",
     "`Kitni baar Rape krvyega mujhse?`",
     "`Tu Randi hai Sabko pta hai😂`",
     "`Don't rape too much bossdk, else problem....`",
     "`Tu sasti rendi hai Sabko pta hai😂`",
     "`Lodu Andha hai kya Yaha tera rape ho raha hai aur tu abhi tak yahi gaand mara raha hai lulz`",
] 


ABUSEHARD_STRING = [
	"`Madarchod Randi ke bacche.Oye bosdike madarchod bhen ke lode tere gand me lohe ka danda garam karke dalu randwe tujhetho gali ke kutte gand pe chut rakh ke katenge me bata raha hu tere lode pe madhu makkhi Katelode ke ando pe Road roller chale tu kab bathroom me muthne Jaye tho Tera loda ghir Jaye fir tere ando me se lizard ke bacche nikle teko kidnap Kare aur childporn banaye maa ke chuttad ke lode tere saat Johnny sins rape Kare aur jab wo teko anal de tab loda andar fas Jaye bkl tere jhaat pe waxing karunga me dhek lio fir jab tu chillayega na tab tere muh me Mai gai ka gobar dalunga sale tere gand ke balo pe tel laga ke jala du me teko Anaconda leke gand me dalu tho muh se nikle maa ke lode hamesha chutiyo jaisa bartav kartha he tu maa ke Dai chawal drugs tere gand Me dalunga thi tatti nahi nikle maa darchod kabhi teko Marne ka mouka mil gaya na tho bas I'll do my best to get that tatti outof you aur tere jaise chutio ko is duniya me jagaha bhi nahi maa ke lode bandarchod tere gand me chitiya Kate wo bhi bullet ants maadarchod samj nahi aaraha tere baap NE teko kya khake paida kiya Tha kesa chutiya he tu rand ke bacche teko shadi me khana khane na mile teko gand pe 4 thappad mare sab log aur blade se likhe I want anal madarchod bosdike maccharki tatte ke baal chutiye maa ke chut pe ghode ka Lund tere gand me jaltha hu koila Dale bhen ke lode MAA KI CHUT MAI TALWAR DUNGA BC CHUT FAT JAEGI AUR USME SE ITNA KHOON NIKLEGA MZA AJAEGA DEKHNE KA SALE MAA KE BHOSDE SE BAHR AJA FIR BAAP SE ZUBAN DA TERI MAA KI CHUT CHOD CHOD KE BHOSDABNADU MADARCHOD AUR USKE UPAR CENENT LAGADU KI TERE JESA GANDU INSAAN KABHI BAHR NA A SKE ESI GANDI CHUT MAI SE LODA LASUN MADRCHOD TERI MAA KI CHUT GASTI AMA KA CHUTIA BACHA TERI MAA KO CHOD CHOD K PAGAL KAR DUNGA MAA K LODY KISI SASTIII RANDII K BACHY TERI MAA KI CHOOT MAIN TEER MAARUN GANDU HARAMI TERI COLLEGE JATI BAJI KA ROAD PEY RAPE KARONGANDU KI OLAAD HARAM KI NASAL PAPA HUN TERA BHEN PESH KAR AB PAPA KO TERI MAA KKALE KUSS MAIN KIS`",
	"`Main roz teri behno ki banjar chut me apna lawda daalke andar haryali lata tha magar aaj unke ke baare me sunke mujhe bhut afsos huwa..ki unko ab bada loudha chahye..ab mera balatkaaari lawda lagataar 4 ghante tk apne muh me kon rakhega..vo teri behne hi thi jo apni kaali magar rasilli chut mere saamne khol deti aur zameen pe naagin ki tarah rengne lgti thi jaise ki kisine unki chut pe naariyal tod diya ho vo b bada wala mumbai ka naariyal..apni chennal maa ko b nhi bhej rahe mere paas to main kaixe tum logo se vaada karu ki main teri maa chodd dungaw..ab agar tun sach me chahta hai ki main tum dono k mc ki chut me dhammal karu to mera lawda apne muh me rakho aur kaho Sameer hamare sage papa hain... Aur agar tb b the apni maa ki kaali chut mere saamne nahi rakhi to tumhare ghar me ghuske tumhari maa ka balatkaar kar dungaw jaixe delhi me huwa tha...ab teri chudi hui kuttiyo ki tarah apni gaand hilaate hue mere aage kalapna mt ni to tumhari fatti bhoxdi me 100 ched karunga`",
	"`Taare hai Asmaan me very very bright jaat na jla bskd dekh le apni hight.`",
        "`Zindagi ki na toote lari iski lulli hoti nhi khadi`",
        "`Kbhi kbhi meri dil me khyaal ata hai ayse chutiyo ko kon paida kr jata hai😂.`",
        "`Saawan ka mahina pawan kare shor jake gand mara bskd kahi aur.`", 
        "`Dil ke armaa ansuon me beh jaye tum bskd ke chutiye hi reh gye.`",
        "`Ishq Se Tabiyat Ne Zeest Ka Mazaa aya maine is lodu ko randi khane me paya.`",
        "`Mirza galib ki yeh khani hai tu bhosdika hai yeh sab ki jubani hai.`",
	"`Mashoor Rand, Ne Arz Kiya Hai. Aane Wale Aate Hai, Jaane Wale Jaate Hai. Yaade Bas Unki Reh Jaati Hai, Jo G**Nd Sujaa Ke Jaate Hai`",
        "`Pani kam hai matke me gand marlunga jhatke me.`",
        "`Aand kitne bhi bade ho, lund ke niche hi rehte hai`",
        "`Tum Ameer hum gareeb hum jhopdiwale Tum bhosiwale`",
        "`Sisi Bhari Gulab ki padi palang ke pass chodne wale chod gye ab q baitha udaas`",
        "`Phuloo Ka Raja Gulaab Kaato me Rehta hai Jeewan ka Nirmata jaato me rehta hai😂`",
        "`Chude hue maal ko yaad mt krna Jo Chut na de usse kabhi friyad mt karna jise chudna hai wo chud ke rhegi bekar me muth maar ke apni jindagi barbaad mt krna`",
        "`Gand mare gandu Chut mare Chutiya Sabse accha mutti 2 mint me chutti😛`",
        "`Marzi Ka Sex Pap Nahi Hota.. Piche Se Dalne Wala Kabhi Baap Nahi Hota.. Condom Zarur Lagana Mere Dost Qki.. Sex K Waqt Popat Ke Pass Dimag Nahi Hota.`",
        "`Uss Ne Hothon Se Chhu Kar Lowd* Pe Nasha Kar Diya; Lu*D Ki Baat To Aur Thi, Uss Ne To Jhato* Ko Bhi Khada Kar Diya!`",
]

ABUSE_STRINGS = [
       "`Madharchod`",
	   "`Gaandu`",
	   "`Chutiya he rah jaye ga`",
	   "`Ja be Gaandu`",
	   "`Ma ka Bharosa madharchod`",
	   "`mml`",
	   "`You MotherFeker`",
	   "`Muh Me Lega Bhosdike ?`"
	   "`Kro Gandu giri kam nhi toh Gand Maar lenge tumhari hum😂`",
           "`Suno Lodu Jyda muh na chalo be muh me lawda pel Diyaa jayega`",
           "`Sharam aagyi toh aakhe juka lijia land me dam nhi hai apke toh Shilajit kha lijia`",
           "`Kahe Rahiman Kaviraaj C**t Ki Mahima Aisi,L**d Murjha Jaaye Par Ch**t Waisi Ki Waisi`",
           "`Chudakkad Raand Ki Ch**T Mein Pele L*Nd Kabeer, Par Aisa Bhi Kya Choda Ki Ban Gaye Fakeer`",
]
GEY_STRINGS = [
          "`you gey bsdk`",
     "`you gey`",
     "`you gey in the house`",
     "`you chakka`",
     "`Bhago BC! Chakka aya`",
     "`you gey gey gey gey gey gey gey gey`",
     "`you gey go away`",
]
PRO_STRINGS = [
     "`This gey is pro as phack.`",
     "`Pros here -_- Time to Leave`",
     "`Proness Lebel: 6969696969`",
     "`Itna pro banda dekhlia bc, ab to marna hoga.`",
     "`U iz pro but i iz ur DAD, KeK`",
     "`What are you Bsdk? Human or Gawd(+_+)`",
     "`Aye pro,ek baat yaad rakhna, Agar Bharosa khud par ho to ksi ki chut tumhari kamzori nahi bnskti.`",

]
INSULT_STRINGS = [ 
    
     "`Owww ... Such a stupid idiot.`",
    "`Don't drink and type.`",
    "`Command not found. Just like your brain.`",
    "`Bot rule 420 section 69 prevents me from replying to stupid nubfuks like you.`",
    "`Sorry, we do not sell brains.`",
    "`Believe me you are not normal.`",
    "`I bet your brain feels as good as new, seeing that you never use it.`",
    "`If I wanted to kill myself I'd climb your ego and jump to your IQ.`",
    "`You didn't evolve from apes, they evolved from you.`",
    "`What language are you speaking? Cause it sounds like bullshit.`",
    "`You are proof that evolution CAN go in reverse.`",
    "`I would ask you how old you are but I know you can't count that high.`",
    "`As an outsider, what do you think of the human race?`",
    "`Ordinarily people live and learn. You just live.`",
    "`Keep talking, someday you'll say something intelligent!.......(I doubt it though)`",
    "`Everyone has the right to be stupid but you are abusing the privilege.`",
    "`I'm sorry I hurt your feelings when I called you stupid. I thought you already knew that.`",
    "`You should try tasting cyanide.`",
    "`You should try sleeping forever.`",
    "`Sharam kar bsdwale,kitni bkchodi deta.`",
    "`Chup Madarhox, bilkul chup..`",
    "`Me zindagi me chunotiyo se jyda inn jese Chutiyo se pareshaan hu.`",
    "`Pick up a gun and shoot yourself.`",
    "`Try bathing with Hydrochloric Acid instead of water.`",
    "`Go Green! Stop inhaling Oxygen.`",
    "`God was searching for you. You should leave to meet him.`",
    "`You should Volunteer for target in an firing range.`",
    "`Try playing catch and throw with RDX its fun.`",
    "`Jaana chodu chad jake land chaat`",
    "`Yaar ajab tere nkhare,gazab tera style hain, gand dhone ki tameez nahi, haath main mobile hai`",
    "`People like you are the reason we have middle fingers.`",
    "`When your mom dropped you off at the school, she got a ticket for littering.`",
    "`You’re so ugly that when you cry, the tears roll down the back of your head…just to avoid your face.`",
    "`If you’re talking behind my back then you’re in a perfect position to kiss my a**!.`",

]
# ===========================================
                          

@borg.on(admin_cmd("runs ?(.*)"))
async def _(event):
    if event.fwd_from:
         return
    bro = random.randint(0, len(RUNSREACTS) - 1)    
    input_str = event.pattern_match.group(1)
    reply_text = RUNSREACTS[bro]
    await event.edit(reply_text)


@borg.on(admin_cmd("metoo ?(.*)"))
async def _(event):
    if event.fwd_from:
         return
    bro = random.randint(0, len(METOOSTR) - 1)    
    input_str = event.pattern_match.group(1)
    reply_text = METOOSTR[bro]
    await event.edit(reply_text)


@borg.on(admin_cmd("rape ?(.*)"))
async def _(event):
    if event.fwd_from:
         return
    bro = random.randint(0, len(RAPE_STRINGS) - 1)    
    input_str = event.pattern_match.group(1)
    reply_text = RAPE_STRINGS[bro]
    await event.edit(reply_text)
			  
                          
@borg.on(admin_cmd("insult ?(.*)"))
async def _(event):
    if event.fwd_from:
         return
    bro = random.randint(0, len(INSULT_STRINGS) - 1)    
    input_str = event.pattern_match.group(1)
    reply_text = INSULT_STRINGS[bro]
    await event.edit(reply_text)
			  
			  
@borg.on(admin_cmd("pro ?(.*)"))
async def _(event):
    if event.fwd_from:
         return
    bro = random.randint(0, len(PRO_STRINGS) - 1)    
    input_str = event.pattern_match.group(1)
    reply_text = PRO_STRINGS[bro]
    await event.edit(reply_text)
			  
			  
@borg.on(admin_cmd("abuse ?(.*)"))
async def _(event):
    if event.fwd_from:
         return
    bro = random.randint(0, len(ABUSE_STRINGS) - 1)    
    input_str = event.pattern_match.group(1)
    reply_text = ABUSE_STRINGS[bro]
    await event.edit(reply_text)
			  
			  
@borg.on(admin_cmd("gey ?(.*)"))
async def _(event):
    if event.fwd_from:
         return
    bro = random.randint(0, len(GEY_STRINGS) - 1)    
    input_str = event.pattern_match.group(1)
    reply_text = GEY_STRINGS[bro]
    await event.edit(reply_text)       
	
	
	
@borg.on(admin_cmd("noob ?(.*)"))
async def _(event):
    if event.fwd_from:
         return
    bro = random.randint(0, len(NOOBSTR) - 1)    
    input_str = event.pattern_match.group(1)
    reply_text = NOOBSTR[bro]
    await event.edit(reply_text)
	

@borg.on(admin_cmd("abusehard ?(.*)"))
async def _(event):
    if event.fwd_from:
         return
    bro = random.randint(0, len(ABUSEHARD_STRING) - 1)    
    input_str = event.pattern_match.group(1)
    reply_text = ABUSEHARD_STRING[bro]
    await event.edit(reply_text)        
	


# Term segmentation analysis data

Annotated corpus data for checking correctness of the Chinese Notes tokenizer
with Buddhist texts.

## Koans from the Blue Cliff Record
Source (English): Cleary, T 1998, *The Blue Cliff Record*, Berkeley: Numata Center for Buddhist Translation and Research, https://www.bdkamerica.org/book/blue-cliff-record. 

Source (Chinese): Chong Xian and Ke Qin, 《佛果圜悟禪師碧巖錄》 'The Blue Cliff Record (Biyanlu),' in *Taishō shinshū Daizōkyō* 《大正新脩大藏經》, in Takakusu Junjiro, ed., (Tokyo: Taishō Shinshū Daizōkyō Kankōkai, 1988), Vol. 48, No. 2003, accessed 2020-01-26, http://ntireader.org/taisho/t2003_01.html.  

### Koan 1
Source: Cleary 1998, pp. 11-12

舉、梁武帝、問、 達磨、大師 
Translation: Story: The Emperor Wu of Liang asked the great teacher Bodhidharma 5
 (說、這、不、唧𠺕、漢) 
Translation: (Here’s someone talking such nonsense.) 5
如何、是、聖諦、第一義
Translation: “What is the ultimate meaning of the holy truths?” 4
 (是、甚、繫驢橛)
Translation: (What donkey-tethering stake is this?) 3
磨  云。
Translation: Bodhidharma said, 2
廓然無聖
Translation: “Empty, nothing holy.” 1
(將、謂、多少、奇特。
Translation: (One might have thought he’d say something extraordinary. 4
箭、過、新羅。
Translation: The point has already whizzed past. 3
可、殺、明白)
Translation: It’s quite clear.) 3
帝、曰。
Translation: The emperor said, 2
對、朕、者、誰
Translation: “Who is answering me?” 4
(滿面、慚惶。
Translation: (Filled with embarrassment, 2
強、惺惺  果然。
Translation: he tries to force himself to be astute. 3
摸索、不、着)
Translation: After all he gropes without finding.) 3
磨、云。
Translation: Bodhidharma said, 2
不識
Translation: “Don’t know.” 1
(咄。[(Tsk! 1] 再、來、不、直  半、文、錢)
Translation: A second try isn’t worth half a cent.) 7
帝、不、契
Translation: The emperor didn’t understand. 3
(可惜、許。
Translation: (Too bad. 2
却、較、些、子)
Translation: Still, this is getting somewhere.) 4
達磨、遂、渡江、至、魏( 
Translation: Bodhidharma subsequently crossed the Yangtse River into the kingdom of Wei. 5
(這、野狐精。
Translation: (Foxy devil! 2
不免、一、場、懡、㦬。
Translation: He can’t avoid embarrassment. 5
從、西、過、東。
Translation: He goes from west to east, 4
從、東、過、西) 
Translation: east to west.) 4

帝、後、舉、問、志、公
Translation: Later the emperor brought this up to Master Zhi and asked him about it. 6
(貧、兒、思、舊、債。
Translation: (A poor man remembers an old debt. 5
傍人、有、眼)
Translation: The bystander has eyes.) 3
志、公、云。
Translation: Master Zhi said, 3
陛下、還、識、此、人、否
Translation: “Did you recognize the man?” 6
(和、志、公、趕、出國、始、得。
Translation: (He should drive Master Zhi out of the country too. 7
好、與、三十、棒。
Translation: He deserves a beating. 4
達磨、來、也)
Translation: Bodhidharma is here.) 3
帝、云。
Translation: The emperor said 2
不識
Translation: he didn’t know him. 1
(却是、武帝、承當、得、達磨、公案)
Translation: (So after all the Emperor Wu has understood Bodhidharma’s case.) 6
志、公、云。
Translation: Master Zhi said, 3
此、是、觀音、大士。
Translation: “He is Mahasattva Avalokitesvara, 4
傳、佛心印 
Translation: transmitting the seal of the Buddha mind.” 2
(胡亂、指、注。
Translation: (An arbitrary explanation. 3
臂膊、不、向、外、曲) 
Translation: The elbow doesn’t bend outwards.) 5
帝、悔。
Translation: The emperor, regretful, 2
遂、遣使、去、請
Translation: sent an emissary to invite Bodhidharma back. 4
(果然、把、不住。
Translation: (After all Wu can’t hold Bodhidharma back; 3
向、道、不唧、𠺕)
Translation: I told you he was a dunce.) 4
志、公、云。
Translation: Master Zhi said, 3
莫道、陛下、發、使、去、取
Translation: “Don’t tell me you’re going to send an emissary to get him!” 6
(東家、人、死。
Translation: (When someone in the house to the east dies, 3
西家、人、助、哀。
Translation: someone from the house to the west helps in the mourning. 4
Error: 西家 (false negative, missing term)
也好、一時  趕、出國)
Translation: Better they should all be driven out of the country at once.) 4
闔、國人、去。
Translation: “Even if everyone in the country went, 4
他、亦、不、回
Translation: he wouldn’t return.” 4
(志、公、也好、與、三十、棒。
Translation: (Master Zhi again deserves a beating. 6
不知、脚跟、下放、大、光明)。
Translation: He doesn’t know the great illumination shines forth right where one is.) 5
Error: 下放 (false positive)

Note: total 199 segments, 2 errors (1 false negative, 1 false positive)


### Koan 2
Source: Cleary 1998, pp. 19-20

舉、趙州、示眾、云
Translation: Story: Zhaozhou said to the assembly, 4
(這、老漢、作、什麼。
Translation: (What is this old guy doing? 4
莫、打、這、葛藤)
Translation: Don’t make such complications.)  4
至道無難
Translation:  “The ultimate Way is without difficulty;” ( 1
(非難、非、易)
Translation: (It is neither difficult nor easy.) 3
唯嫌揀擇
Translation: “just avoid discrimination.” 1
(眼前、是、什麼。
Translation: (What is in front of your eyes?  3
三、祖、猶在)。
Translation: The third patriarch is still alive.) 3
Error: 猶在 (false negative, missing term)
纔、有、語言。
Translation: “As soon as there are words, 3
是、揀擇、是、明白
Translation: ‘this is discrimination,’ ‘this is clarity,’” 4
(兩頭三面。
Translation: (Two heads, three faces. 1
少、賣弄。
Translation: Don’t brag so much. 2
魚、行、水、濁。
Translation: When a fish swims through, the water is turbulent; 4
鳥、飛、落、毛)
Translation: when a bird flies by, feathers fall.) 4
老僧、不在、明白、裏
Translation: I am not within clarity. ” 4
Error: 不在 (false negative, missing term)
(賊、身、已、露。
Translation: (The thief is already revealed. 4
這、老漢、向、什麼、處、去)
Translation: Where’s the old fellow going?) 6
是、汝、還、護、惜、也、無
Translation: “Do you preserve anything or not?” 7
(敗、也。
Translation: (He’s lost. 2
也、有、一、箇、半、箇)
Translation: There’s one or a half.) 6

 時、有、僧、問。
Translation: At that time a monk asked, 4
既、不在、明白、裏。
Translation: “Since you are not within clarity, 4
護、惜、箇、什麼
Translation: what do you preserve?” 5
(也好、與、一、拶。
Translation: (He gives him a good rejoinder; 4
舌、拄、上、齶)
Translation: that ought to shut him up.) 4

州、云。
Translation: Zhaozhou said, 2
我、亦、不知
Translation: “Even I don’t know.” 3
(拶、殺、這、老漢。
Translation: (At this deadly rejoinder, 4
倒退、三千)
Translation: the old fellow has fallen back three thousand miles.) 2

僧、云。
Translation: The monk said, 2
和尚、既、不知。
Translation: “Since you don’t know, 4
為什麼、却、道、不在、明白、裏
Translation: why then do you say you are not in clarity?” 6
(看、走向、什麼、處、去。
Translation: ” (Watch and see where he’ll run; 5
逐、教、上、樹、去)
Translation: the monk’s chased him up a tree.) 5

州、云。
Translation: Zhaozhou said, 2
問事、即、得。
Translation: “You have managed to ask about the matter; 3
禮拜、了、退
Translation: you can go now.” 3
(賴、有、這、一着。
Translation: (Lucky he has this move. 4
Error: 一着 (false negative, missing term)
這、老賊)。
Translation: The old bandit!) 2
Error: 老賊 (false negative, missing term)

Note: total 138 segments, 4 errors (4 false negative, 0 false positive)

### Koan 3

Source: Cleary, p. 25

舉、馬大師不安
Translation: Story: Great Master Ma was unwell. 2
(這、漢、漏逗、不少。
Translation: (This guy has broken down quite a bit. 4
帶累、別人、去、也)
Translation: He’s dragging in other people.) 4
院主、問。
Translation: The temple superintendent asked him, 4
和尚、近日。尊、候、如何
Translation: “Teacher, how are you these days?” 5
(四百、四、病、一時、發。
Translation: (Four hundred four diseases break out all at once. 5
三、日後、不、送、亡、僧。
Translation: They’ll be lucky if they’re not seeing off a dead monk in three days. 6
Error: 日後 (false positive)
是、好手。仁義、道中)
Translation: This is in the course of human duty.) 4
大師、云。
Translation: The great master said, 4
日面佛月面佛
Translation:  “Sun Face Buddha, Moon Face Buddha.” 1
(可、殺、新鮮。
Translation: (How fresh and new!  3
養子、之、緣)
Translation: Sustenance for his fledgling.) 3

Note: total 45 segments, 1 error (1 false positive)

### Koan 4

Source: Cleary, pp. 28-29

舉、德山、到、溈山
Translation: Story: When Deshan arrived at Guishan 4
(擔板漢。
Translation: He’s being one-sided, 1
野狐精) 
Translation: the foxy devil.) 1
挾、複、子、於、法堂、上
Translation: he carried his bundle with him into the teaching hall, 6
(不妨、令人、疑、着。
Translation: (Un­avoidably he causes people to doubt. 4
納敗缺)
Translation: He’s suffered defeat already.) 1
Error: 敗缺 (false negative, missing term)
從、東、過、西。
Translation: where he crossed from east to west 4
從西過東
Translation: where he crossed from east to west 4
從、西、過、東
Translation: and from west to east. 4
(可、殺、有、禪、作、什麼) 
Translation: (He has a lot of Chan, but what for?) 6
顧、視、云、無、無。
Translation: He looked around and said, “None, none.” 5
便、出
Translation: Then he went out. 2
(好、與、三十、棒。
Translation: (He deserves a beating. 4
可殺氣、衝、天。
Translation: He’s extremely high-spirited. 3
真、師子、兒。
Translation: A real lion cub 3
善、師子吼)
Translation: can roar the lion’s roar.) 2

雪竇、著語、云。
Translation: Xuedou added the comment, 3
勘破、了、也
Translation: “Completely exposed.” 3
(錯。
Translation: (Wrong. 1
果然。
Translation: After all. 1
點) 
Translation: Check!) 1

德山、至、門首、却、云。
Translation: But when Deshan got to the monastery gate, he said, 5
也、不得、草草
Translation: “Still, I shouldn’t be careless.” 3
(放、去、收、來。
Translation: (Letting go, gathering in.
頭上、太、高、生。
Translation: At first too high; 4
Error: 頭上 (false positive)
末後、太、低、生。
Translation: in the end too low. 4
知過必改。
Translation: When one realizes one’s fault one should reform, 1
能、有、幾、人)
Translation: but how many people can?) 4
便、具、威儀。再、入、相見
Translation: So he went back to meet Guishan for­mally. 6
(依、前、作、這、去、就。
Translation: (As before, he acts like this. 6
已、是、第二、重、敗缺。
Translation: It’s already his second defeat. 5
Error: 敗缺 (false negative, missing term)
嶮)
Translation: Danger!) 1
溈山、坐、次
Translation: As Guishan sat there, 3
(冷眼、看、這、老漢。
Translation: (He watches this fellow with cold eyes. 4
捋虎鬚。也、須是、這、般、人、始、得)
Translation: It takes this kind of man to grab a tiger’s whiskers.) 8
Error: 捋虎鬚 (false negative, missing term)
Error:須是 (false negative, missing term)
德山提起坐具云。
Translation: Deshan held up his mat and said, 4
和尚
Translation: “Teacher!” 1] (改頭換面。
Translation: (He changes heads, switches faces; 1
無風起浪) 
Translation: he stirs up waves where there’s no wind.) 1
溈山、擬、取、拂子
Translation: Guishan reached for his whisk, 4
(須是、那、漢、始、得。
Translation: (Only he could do this; 5
Error: 須是 (false negative, missing term)
運籌、帷幄、之中。
Translation: he sets his strategy in motion from within his tent. 3
不妨、坐斷、天下、人、舌頭)
Translation: Surely he silences everyone in the world.) 5
德山、便、喝。拂袖、而、出
Translation: whereupon Deshan shouted and left. 6
Error: 拂袖 (false negative, missing term)
(野狐精、見解。
Translation: (This is the understanding of a wild fox spirit. 2
這、一喝。
Translation: This one shout 2
也、有、權。
Translation: contains both the provisional 3
也、有、實。
Translation: and the real, 3
也、有、照。
Translation: both illumination 3
也、有用。
Translation: and function. 3
Error: 有用 (false positive)
一等、是、拏、雲、攫、霧、者。
Translation: He’s one of those who can grab the clouds and grasp the fog, 7
就中、奇特)
Translation: and he is outstanding among them.) 2
Error: 就中 (false negative, missing term)

雪竇、著語、云。
Translation: Xuedou added the comment, 3
勘破、了、也
Translation: “Completely exposed.” 3
(錯。果然。點) 
Translation: (Wrong. After all. Check!) 3

德山、背、却、法堂。
Translation: Deshan turned his back on the teaching hall, 4
著、草鞋、便、行
Translation: put on his san­dals, and left. 4
(風光可愛。
Translation: The scenery is lovely, 1
公案、未、圓。
Translation: but the case is not yet com­pleted. 3
贏得、項、上、笠。
Translation: He won the hat on his head 4
失却、脚下、鞋。
Translation: but lost the shoes on his feet. 3
Error: 失却 (false negative, missing term)
Error: 脚下 (false negative, missing term)
已、是、喪身、失、命、了、也) 
Translation: He’s already lost his life.) 7
溈山、至、晚、問、首座。
Translation: That evening Guishan asked the head monk, 5
適來、新、到、在、什麼、處
Translation: “Where is that newcomer? ” 6
Error: 適來 (false negative, missing term)
(東邊、落、節。
Translation: (He lost his interest in the east 3
西邊、拔、本。
Translation: and loses his principle in the west. 3
眼、觀、東南。
Translation: His eyes look southeast, 3
意、在、西北)
Translation: but his mind is in the northwest.) 3
首座、云。
Translation: The monk answered, 2
當時、背、却、法堂。
Translation: “At that time he turned his back on the teaching hall, 4
著、草鞋、出去、也
Translation: put on his sandals, 4
(靈、龜、曳、尾。
Translation: (The sacred tortoise drags his tail; 4
好、與、三十、棒。
Translation: he deserves a beating. 4
這、般、漢、腦後、合、喫、多少) 
Translation: How many blows to the back of the head would this kind of person need?) 7
溈山、云。
Translation: Guishan said, 2
此、子、已、後。
Translation: “Hereafter that lad 4
向、孤、峯、頂上。
Translation: will go to the summit of a soli­tary peak, 4
盤、結草、庵。
Translation: build himself a grass hut, 3
Error: 結草 (false negative, missing term)
呵佛罵祖、去、在
Translation: and scold the Buddhas and revile the patriarchs.” 3
(賊、過後、張弓。
Translation: (He draws his bow after the thief is gone. 3
天下、衲僧、跳、不出) 
Translation: No one in the world can leap out of this.) 4

雪竇、著語、云。
Translation: Xuedou added the comment, 3
雪上加霜
Translation: “ This is adding frost to snow.” 1
(錯。
Translation: (Wrong. 1
果然。
Translation: After all. 1
點)。
Translation: Check!) 1

Note: total 285 segments, 13 errors (11 false negative, 2 false positive)

### Koan 5

English from Cleary, p. 36

舉、雪峯、示眾、云
Translation: Story: Xuefeng said to his group, 4
(一、盲引眾盲。
Translation: (One blind man leading a crowd of the blind. 2
不為、分外) 
Translation: It’s not beyond him.) 2 
盡、大地、撮、來、如、粟米、粒、大 
Translation: “Pick up the whole world, and it’s as big as a grain of rice.” 8
Error: 粟米 (false negative, missing term)
(是、什麼、手段。
Translation: (What technique is this? 3
 山僧、從來、不、弄、鬼、眼睛) 
Translation: I myself have never sported devil eyes.) 6
拋、向、面前 
Translation: “ Throw it down before you.”  3
(只、恐、拋、不、下、有、什麼、伎倆) 
Translation:  (I’m afraid it can’t be thrown down. What ability do you have?) 8
漆、桶、不、會 
Translation: “If you’re in the dark and don’t understand,”4
(倚勢、欺、人。
Translation: (Xuefeng relies on his power to deceive people. 3
Error: 倚勢 (false negative, missing term)
自領、出、去。
Translation: Take what’s coming to you and get out. 3
莫、謾、大眾、好) 
Translation: Better not slight the people.) 4
打鼓、普請、看 
Translation: “I’ll beat the drum to call everyone to look.” 3
(瞎。
Translation: Blind! 1
打鼓、為、三軍)。
Translation: The beat of the drum is for the three armies.) 3

Note: Total 56 segments,  0 errors (2 false negative, 0 false positive)

### Koan 6

Source:  Cleary, p. 40

舉、雲門、垂語、云。
Translation: Story Yunmen said, 4 
十五、日、已、前、不問、汝 
Translation: “I don’t ask about before the fifteenth day;” 5
(半、河南。
Translation: (Half south of the river, 2
 半、河北。
Translation: half north of the river. 
這、裏、不、收、舊曆、日) 
Translation: We don’t keep old calen­dar dates here.) 6
 十五、日、已、後、道、將、一句、來 
Translation: “try to say something about after the fifteenth day.” 8
(不免、從、朝、至、暮。
Translation: (Inevitably it will go from dawn to sunset; 5
 切忌、道、著。
Translation: just don’t say 3
 來日、是、十六。
Translation: that the next day is the sixteenth. 3
 日月如流) 
Translation: The days and months seem to flow by.) 1
Error: 日月如流 (false negative, missing term)
自、代、云。
Translation: He answered himself, 3
日日是好日 1
Translation:  “Every day is a good day.” 
(收。
Translation: (He’s gathered it in. 1
鰕、跳、不出、斗。
Translation: Though the frog jumps, it can’t get out of the bas­ket. 4
誰、家、無明、月、清風。
Translation: Whose house has no bright moon and clear breeze? 5
Error: 無明 (false positive)
Error: 明月 (false negative)
還、知、麼。
Translation: But do you know it? 3
 海神、知、貴、不知、價)。
Translation: The sea god knows its value but not its price.) 5

Note: total 43 segments,  3 errors (2 false negative, 2 false positive)

### Koan 7

Source: Cleary, p. 48

舉、僧、問、法眼 
Translation: Story: Huichao asked Fayan, 
(道、什麼。
Translation: (What does he say? 2
檐、枷、過、狀) 
Translation: Wearing handcuffs, he hands over his own indictment.) 4
慧超、咨、和尚。
Translation: “Huichao asks the teacher, 3
如何、是、佛 
Translation: what is the Buddha?” 3
(道、什麼。
Translation: (What’s he saying? 2
眼睛、突出) 
Translation: His eyeballs pop out.) 2
法眼、云。Fayan said, 2
汝、是、慧超 
Translation: “You are Huichao.” 3
(依、模、脫、出。
Translation: (He comes out according to the pattern. 4
鐵餕饀。
Translation: Iron scrap stuffing. 1
就、身、打劫)。
Translation: He fends him off with a counterattack.) 3

Note: total 25 segments,  0 errors

### Koan 8

Source: Cleary, p. 53

舉、翠嵒、夏、末、示眾、云。
Translation: Story: At the end of a summer retreat Cuiyan said to the group, 6
一、夏、以來。
Translation: “All summer 3
為、兄弟、說話 
Translation: I’ve been talking to you;” 3
(開口、焉知、恁麼) 
Translation: (If you open your mouth, how can you know it to be so?) 3
看、翠嵒、眉毛、在、麼 
Translation: “see if my eyebrows are still there.” 5
(只贏得眼睛也落地。
Translation: (All he’s achieved is that his eyes have fallen out too, 1
和、鼻孔、也、失、了。
Translation: along with his nostrils, which he’s already lost. 5
入、地 獄、如、箭、射) 
Translation: He enters hell like an arrow shot.)  5
保福、云。Baofu said, 2
作賊、人、心虛 
Translation: “ The thief’s heart is cowardly.” 3
(灼然、是、賊、識、賊) 
Translation: (Obviously. This is a thief recognizing a thief.) 5
長慶、云。
Translation: Changqing said, 2
生、也 
Translation: “Grown.” 2
 (舌頭、落地。
Translation: (His tongue falls to the ground; 2
將錯就錯。
Translation: he meets error with error. 1
Error: 將錯就錯 (false negative, missing term)
 果然) 
Translation: After all.) 1
 雲門、云。
Translation: Yunmen said, 2
 關 
Translation: “ Barrier.” 1
(走、在、什麼、處、去。
Translation: (Where is there to run to? 5
天下、衲僧、跳、不出。
Translation: No one in the world can leap out. 4
 敗、也)。
Translation: Overcome.) 2

Note: total 63 segments, 1 error (false negative)

### Koan 9

Source: Cleary, p. 58

舉、僧、問、趙州。
Translation: Story: A monk asked Zhaozhou, 4
如何、是、趙州 
Translation: “What is Zhaozhou? ” 3
(河北、河南。
Translation: (North of the river, south of the river, 2
 總、說、不著。
Translation: no one can say. 3
Error: 不著 (false negative, missing term)
 爛泥、裏、有、刺。
Translation: There are thorns in the soft mud. 4
 不在、河南。
Translation: If it’s not south of the river, 2
 正在河北) 
Translation: then it’s north of the river.) 2
州、云。
Translation: Zhaozhou replied, 2
東門、西門、南門、北門 
Translation:  “East gate, west gate, south gate, north gate.” 4
 (開、也。
Translation: (Open. 2
相罵、饒、爾、接嘴。
Translation: “When we’re reviling each other, you may lock jaws with me; 4
相、唾、饒、爾、潑水。
Translation: when w e’re spitting at each other, you may spew me with slobber.” 5
 見成、公案。
Translation: It’s the issue at hand; 2
Error: 見成 (false negative, missing term)
 還見麼。
Translation: but do you see? 3
 便、打)。 
Translation: I strike!) 2

Note: total 42 segments, 2 errors (2 false negative)

### Koan 10

Source: Cleary, p. 63

舉、睦州、問、僧、近、離、甚、處 
Translation: Story: Muzhou asked a monk, “Where have you just come from? ” 8
(探竿影草) 
Translation: (This is a probe, for observation.) 1
僧、便、喝 The monk immediately shouted. 3
(作家、禪客。
Translation: (An adept Chan student, 2
Error: 禪客 (false negative, missing term)
且、莫、詐、明、頭、也、解、恁麼、去) 
Translation: but don’t pretend to be enlightened. Still he does know how to act like this.) 9
 州、云。
Translation: Muzhou said, 2
老僧、被、汝、一喝 
Translation: “ I’ve been shouted at by you once.”  4
(陷、虎、之、機。
Translation: (A trap to fell a tiger. 4
猱、人、作、麼) 
Translation: Why make a monkey of the man?)  4
僧、又、喝 
Translation: Again the monk shouted. 3
(看、取、頭角。
Translation: (Look at the horns on his head. 3
Error: 頭角 (false positive)
似、則、似。
Translation: He seems to be right  3
是、則、未、是。
Translation: but actually isn’t. 4
只、恐、龍頭蛇尾) 
Translation: I’m afraid he has a dragon’s head but a snake’s tail.) 3
Error: 恐龍 (false positive)
Error: 龍頭蛇尾 (false negative, not detected)
州、云。
Translation: Muzhou said, 2
三、喝、四、喝、後、作麼生 
Translation: “After three or four shouts, then what?” 6
Error: 作麼生 (false negative, missing term)
(逆水、之、波。
Translation: (A wave against the current. 3
未曾、有、一、人、出、得、頭。 
Translation: There’s never been any­ one who could come forth. 7
Error: 未曾有 (false positive)
 入、那裏、去) 
Translation: Where to go?) 3
 僧、無語 
Translation: The monk was speech­less. 2
Error: 無語 (false negative, missing term)
 (果然、摸索、不著) 
Translation: (After all he searched without finding.) 3
州、便、打、云 
Translation: Muzhou hit him and said, 4
(若、使、睦州、盡、令、而、行。
Translation: (If we let Muzhou carry out his mandate to the full, 7
盡、大地、草木。
Translation: all the plants and trees on earth 3
悉、斬、為、三、段) 
Translation: would be cut into three pieces.) 5
這掠虛頭漢 
Translation: “You phony! ” 2
(放過、一、著。
Translation:  (If he let the first move go, 3
落、在、第二)。
Translation: he’d fall back into the secondary.) 3

Note: total 105 segments,  3 errors (5 false negative, 3 false positive)

## Koan 11

Source: Cleary, p. 69

舉、黃檗、示眾、云
Translation: Story: Huangbo said to his group,
(打水、礙、盆。
Translation: (Drawing water, one is limited by the size of the container.
一口吞盡。
Translation: He swallows all in one gulp.
天下、衲僧、跳、不出)
Translation: No one in the world can leap clear.)
汝等諸人。
Translation: “All of you 
盡、是、噇、酒、糟、漢。
Translation: are gobblers of dregs;
恁麼、行脚
Translation: if you go on traveling around this way,”
(道、着。
Translation: (You said it!
踏、破、草鞋。
Translation: You’ll wear out your shoes.
掀天、搖、地)
Translation: He overturns the heaven and shakes the earth.)

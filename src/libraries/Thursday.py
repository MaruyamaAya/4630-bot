import random

thur_list = ["""星期四，小雨，今天是肯德基疯狂星期四，香辣鸡翅打折，开开心心的去买了一份，出来以后路上一滑，香辣鸡翅掉地上了，我好没用，我没守护好香辣鸡翅就好像我没守护好我的爱情一样，心碎了一地""",
             """代练 阴阳师魂土代肝 剑三 明日方舟推图 刷材料 王者巅峰万强小国标 Apex双锤上大师 清空赛季通行证 ow80胜率上4300 三位置意识教学 彩虹六号生涯kd3.0 包上冠军 CSGO上完美S+ 原神十二层满星代打 这些都不接 接肯德基疯狂星期四代吃""",
             """今天疯狂星期四，免费乘坐私人飞机！！！有人想免费乘坐私人飞机去吃肯德基吗？我们预计是4个人，现在还有两个空位。我们将于下周六晚上从上海出发，飞往海南，然后坐上游艇享用肯德基宅急送，接下来我们将飞往西沙群岛，最后飞回家。如果感兴趣，请私聊我，最好是拥有私人飞机和游艇的人，不然我们就去不了了。""",
             """家人们听说了吗，最近KFC和vivo合作出了一款手机，叫肯德基疯狂星期四vivo50""",
             """你是在施舍我吗？你一个平时买KFC从来不眨眼的大少爷约我过疯狂星期四，别搞笑了好吗，这种贵族节日对我来说遥不可及我自己比谁都清楚，你是在羞辱我吗？你知道9.9这种钱能让我压力多大吗？你不知道你就是一个高高在上的...什么你说你请客点宅急送？好的谢谢"""
             """我本是官位世家的陈塘关公主，却被诡计多端的奸人所害!家人弃我!师门逐我!甚至断我灵脉!重来一生，今天肯德基疯狂星期四!谁请我吃?""",
             """暗夜里，他的声音如恶魔般响起：“替我生个孩子！”他是尊贵的商界帝王，翻手如云，覆手如雨，而她只是他挑中的一枚棋子，十个月后，她被迫生下一个孩子逃之夭夭......当她再次出现，她是落魄的小公司负责人，而他掌握她的生死。他强势夺情，“马冬梅，不想破产，今天和我一起去吃疯狂星期四！”""",
             """富翁找到我和另外两个年轻人，许诺只要有人用一样东西填满一整个房间，就会把财产全部赠与给那个人。

第一个人找来六周年拉菲草铺在地板上，铺了半天说房子买大了，富翁摇了摇头。

第二个人找来一根蜡烛点燃，屋子里充满了光，富翁还是摇了摇头，因为他的影子没有被照到。

现在只剩下我还没有拿出东西，我已经想好了，只要我拿出肯德基疯狂星期四藤椒无骨大鸡柳，香味就可以充满整个房间！

谁赞助我一份?拿到富翁财产之后我会分TA百分之十。""",
             """他本是豪门少爷

在新婚前夜却发现未婚妻和兄弟在喜床上翻滚

她深夜买醉却撞上醉酒的他

一夜痴缠他醒来后不见她的踪影

只见床头压着一张纸：

今 天 肯 德 基 疯 狂 星 期 四""",
             """我本是显赫世家的千金，却被诡计多端的奸人所害！家人弃我！师门逐我！甚至断我灵脉！

重生一世，今天肯德基疯狂星期四！谁请我吃?""",
             """我本是上市公司的老总，却被诡计多端的奸人所害！下属弃我！股东逐我！甚至清空我的股份！重来一生，我只想夺回我的公司！今天肯德基疯狂星期四，谁请我吃？"""
             """我叫赵盼儿，在钱塘开茶馆为生，三年前我遇见了一个叫做欧阳旭的落难书生，给他钱财给他田地给他宅院，端茶倒水红袖添香伺候他三年，可谁知他科举上岸后狠心将我抛弃！还拿80两黄金来羞辱我！我恨！我怨！我怒！我与姐妹联合去东京算账，他竟赶我出城！掐我脖子！逼我做妾！在我落难之时，顾千帆为我指明方向，他说：
今天是肯德基疯狂星期四，v我30，今晚八点一边吃肯德基劲爆鸡米花一边讨论你的复仇计划""",
             """正在循环播放《群主请不请我们吃肯德基疯狂星期四》

●━━━━━━───1:23

⇆ ◁ ❚❚ ▷ ↻""","""龚俊回成都老家了，今晚他的家人朋友会有个家庭聚会，请了好多朋友去参加，我大学同学的妈妈也在受邀之列。现在她有个带人名额，今晚可以去龚俊家吃饭。我可以介绍你去他家吃大餐，但是我也不能饿着肚子，今天是肯德基疯狂星期四，转我1640，我把名额让给你。
""",
"""我的人脉说狐妖小红娘月红篇的确会在6月5号爱奇艺悦享会上面官宣演员阵容，而且人脉透露这个项目很受平台重视，对于造型一定会做到尽善尽美，而且现在主演造型概念海报已经出来了，今天是疯狂星期四，只需要微信过来五十块的话就可以让人脉给你看呆毛。
""",
"""就像著名音乐家约翰·列侬说过的这样一段话:“5岁时，妈妈告诉我，人生的关键在于快乐。上学后，人们问我长大了要做什么，我写下快乐。他们告诉我，我理解错了题目。我告诉他们，他们理解错了人生。”生活本身如同一潭死水。没有泛起一丝丝涟漪的可能。其实相对于普通人来说，快乐、高薪体面、基本的节假日等都很难得。退而求其次，能在楼下的KFC享受到限时的疯狂星期四优惠让很多人心满意足，变胖也无所谓。今天原来是肯德基疯狂星期四，所以说谁请我肯德基?吃完我继续说。
""",
"""扒个群里的渣男，我有个朋友被群友睡了，大概是三个月以前吧，我朋友在群里认识了一个男的，他们在网上聊了差不多两个星期左右就见面了，而且第一次见面就去宾馆了，之后的每个星期六星期天都会去，就这样持续了好几个月。我朋友给那个男的说，已经一个多月没来月经了，想不到这句话说完，隔天就找不到那个男的了，手机一直打不通，关机，直到我朋友前几天跟她父母坦白这件事情，我朋友就在旁边一直哭，那天晚上我偷偷给她买了个验孕棒一看，真怀孕了。然后我第二天请假一天，专门给她聊这个事，她说那个男的对她很好很好什么的，我说对你好还不是想玩你，实在不行报警吧，她当时听完这句话就趴桌子上大哭。正当我打开手机想报警的时候，不小心打开了肯德基，想起来今天原来是疯狂星期四，所以说谁请我肯德基?吃完我继续说。
""",
"""我想问一下大家，之前朋友找我借钱，前后加起来有大概七万（够立案），但是没有借条也没有字据，微信也早已互删没有任何关于借的字眼，只有支付宝上还有转账记录。派出所刚让我把转账记录发给他看一下的时候，我点支付宝点歪了，不小心点开了肯德基，发现今天是疯狂星期四，谁请我吃?
""",
"""封校以后一直在宿舍躺着，瘦不下去，舍友们像变了个人似的，对我又打又骂，我好恨他们！正当我打开手机想报警的时候，不小心打开了肯德基，想起来今天原来是疯狂星期四，所以谁请我吃肯德基？
""",
"""我独自一人远离家乡来到北京上学，同学欺我，老师骂我，室友打我，我流浪在街头，衣衫褴褛，身无分文，活得不如一条流浪狗。天地浩大，却没有我的容身之处。我想问一问苍天，今天肯德基疯狂星期四，谁请我吃?
""",
"""早上刚起床洗了个澡，看到外头的阳光真不错，我来不及穿上衣服就打开了窗帘，欣赏起了日光下的美景，我双手叉腰晒了会儿日光浴，时间一点点过去，身上差不多干了。看着大好风光，我拿起手机，想要拍下这令人心情舒适的景色，却不小心点开了肯德基APP，发现今天是疯狂星期四，谁请我吃？
""",
"""我本是夜上海的一名贫穷又自强的黄包车夫，看遍了这个城市的繁华和热闹，也体验了这个社会的冷漠与无情。直到那一天，我的车上坐上了一位穿着四季歌的千金小姐，我感到了我平静已久的内心再一次颤动，我知道不应该，但我却还是喜欢上了。我知道我的身份地位配不上她，只求有个好心人给我39.9，让我买一个疯狂星期四热辣鸡桶，带给她舔狗的关怀。
""",
"""感觉大家好有趣啊，不像我，不仅连句话都搭不上，还要被当成破坏氛围的傻狗,我现实生活中自闭没朋友，哪怕是在网上也受尽冷眼，每次组织了半天的语言都如鲠在喉，最后还是默默删掉了看你们互动，融入不了群体的我还是想偷偷问：今天是肯德基疯狂星期四，能有好心人请我吃吗？
""",
"""对不起我投降了，我超级粘人也超级喜欢你，并不是可有可无的那种，你不理我，我就没有办法好好做事，你忘记说晚安我就睡不好觉，偶尔故意冷淡是想看你的反应，我其实没有事情做，也不喜欢别人，我只对你这样，可不想再烦你，所以我在忍住，但现在我忍不住了，肯德基疯狂星期四请我吃好吗。
""",
"""我专升本失败了，不想上班，爸爸妈妈也不要我了。现在我在天桥底下，外面很冷，我今天饭也没吃药也没吃，连口热水都没得喝 ，家里人都跟我断绝关系了，手机也快没电了，还不小心点开了肯德基app，说到肯德基，今天是疯狂星期四，v我29.9，请我吃一顿好的 。
""",
"""今天，是我一生中最黑暗、最黑暗的时光，但我发现很难像对待垃圾桶或木洞一样对待朋友说话，更喜欢消化自己，第二天睡觉又醒来，甚至不想累别人，不想把负面情绪传递给身边的朋友。不过，我想让朋友给我物质上的帮助，今天是肯德基疯狂的星期四，有朋友想邀请我吃肯德基
""",
"""今天，是我人生中最黑暗、最emo的时候，但是我很难把朋友当成垃圾桶或者树洞去倾诉，更喜欢憋着自己消化，睡一觉第二天醒来就好了，不想连累别人，不想把负面情绪传递给身边的朋友。但是，我更希望家人能够给予我物质层面的帮助！今天是肯德基疯狂星期四，有哪个家人愿意请我吃肯德基吗?
""",
"""时间让我长了年岁，却没有让我成为一个合格的大人。我以为我的十八岁，会工作稳定，收入可观，和喜欢的人去看山河大海，落日余晖。没想到，到了谈婚论嫁的年龄，我却仍在找自己的路上。今天肯德基疯狂星期四，谁请我吃？
""",
"""“我有点想你，你呢？” 前女友刚刚给我发来了这条消息，忽然间有些恍惚。 好像我们还在一起。那三年里，我们一起放羊，一起喂猪，一起下地插秧。她亲手制作的那一大束大蒜花捧美如繁星。我难以忘记，我们分开的那一天，我发出的最后一条信息：今天肯德基疯狂星期四，谁请我吃？
""",
"""你想象一下跨年的时候，你一个人单着身刷着pyq，你的兄弟姐妹们都换上了情头给你讲甜蜜爱情历程，就连打游戏都会发现一堆情侣秀恩爱，你是否会后悔今天没有点开我的头像说一句：今天疯狂星期四我请你吃
""",
"""演的怎么了？人生如戏，不能演吗？真搞不懂为什么有些人总是天天在下面怀疑别人演不演的，爱看不看不看拉倒！就是演的也比你们强，整天看到你们在这里怀疑这个怀疑那个真的气的我眼泪在眼眶打转，手攥紧了衣角整个人都在颤抖，太让我失望了更多的是心寒。我需要有好心人请我吃疯狂星期四，希望大家支持
""",
"""男朋友跟我分手了，我心碎了，决定见他一面把事情说清楚，如果他非要分手我也无话可说。我买了去北京的机票，坐了两个小时的飞机，到了之后却因为疫情被封小区了他出不来。我心如死灰在大街上游荡，打开手机看到了我们的恩爱时光泪流满面，忽然注意到手机上显示的时间：今天肯德基疯狂星期四，谁请我吃安慰一下我。
""",
"""分手了，最近没有怎么哭了，我现在慢慢变好了吧！以前有多快乐，现在就有多难过。从人间烟火的日常，到红着眼睛告别，消失在彼此的世界里，很痛，也很难。今天是肯德基疯狂星期四，v我60，抚慰我支离破碎的心。
""",
"""蛮讽刺的，从凌晨开始等到现在，没有一个人和我说生日快乐。我的亲人没有说，朋友也没有说，我最在乎的人也没有说，直到现在我才明白：原来今天不是我生日。但是今天是肯德基疯狂星期四！谁请我吃?
""",
"""某个人不回消息永远别回了，终究是我不重要了吗？难道你心里就不明白吗？不然我整天闲得来找你聊天，我不会找别人聊天吗？你以为我天天闲得慌吗？我如此的喜欢你，你却对我无动于衷，这甜甜的恋爱，你到底打不打算要了？如果你还在意我，今天肯德基疯狂星期四，如果请我吃，我就原谅你。
""",
"""我有时候会觉得大家并不喜欢那个真正的我!在网络上！我总是善于伪装！看起来每天都很快乐！无忧无虑！没有烦恼!我的生活也看起来很简单！没有很多人向往的灯红酒绿！纸醉金迷!我很宅！喜欢打游戏！现实中的我并不像网上这么有趣!我其实话很少！最爱干的事是一个人发呆!这样枯燥的我！真的会被大家喜欢吗?我很疑惑!
""",
"""如果你们能一层一层剥开我的内心！你们会发现！那颗心里写满了一句话：今天肯德基疯狂星期四！谁请我吃?
""",
"""我都懂，我都明白，我是选项E，我是planB，是分叉的头发，洗衣机流出的泡沫，超市里被捏碎的饼干，是吃腻的奶油，是落寞的城市，是地上的草，我是被踩踏的，是西装的备用扣，是被雨淋湿的小狗，是腐烂的橘子，是过期的牛奶，是断线的风筝，是被随意丢弃的向日葵，是沉默寡言的小朋友，所以能v我52吗，今天肯德基疯狂星期四。
""",
"""世界上现在77亿人，有253亿只鸡，是人的数量的三倍。也就是说，如果鸡决定与人类开战，每个人平均要打三只鸡。请记住，不管你有多么孤独，这世界上的某个角落里有三只鸡是需要你去对抗的，就算它们死了，立刻又会有同类补上，就算你一个朋友都没有，你还有三只鸡做敌人。今天是肯德基疯狂星期四，V我50，我帮你去杀鸡。 
""",
"""你我的差距就在于你是复制疯狂星期四段子群发钓鱼，而我直接要求“今天疯狂星期四，你请我吃”
""",
"""就算成功的概率为1%又如何呢，如太阳系般波澜壮阔，也只有0.14%产生了生命平凡的我们绝大多数也终将如整个太阳系的99.86%一般化作死寂。但这不重要朋友，今天是肯德基疯狂星期四，谁请我吃?
""",
"""今年高考之后，感觉前途一片灰暗。语文作文我都不知道我写什么，数学更是一塌糊涂。考完之后我哭了一整晚，怎么办，感觉我的人生一片灰暗，有没有好心的陌生人能v我50，让我吃一顿疯狂星期四安慰下自己。
""",
"""我老婆打我，还跟外面男人有说有笑，为了孩子，我忍了这段破碎的婚姻，请我吃肯德基疯狂星期四，倾听我的复仇计划。
""",
"""我有时候会觉得大家并不喜欢那个真正的我。在网络上，我总是善于伪装，看起来每天都很快乐，无忧无虑，没有烦恼。我的生活也看起来很简单，没有很多人向往的灯红酒绿，纸醉金迷。我很宅，喜欢打游戏，现实中的我并不像网上这么有趣。这样枯燥的我，想吃肯德基疯狂星期四真的会有人请吗？
""",
"""穿过挪威的森林，让我走进你的梦里，夕阳落在我的铠甲，王子不一定骑白马，你不必故作冷淡,我也不想做最后的纠缠。最后问一句，疯狂星期四，谁请吃肯德基?
""",
"""离婚这么多年，竟然在微博遇到你了，你过得挺好我也就放心了。孩子上四年级了，成绩一直都很好，连续三年拿班上第一名，就是性格像你，一出事就逃避，孩子总问爸爸什么时候来参加家长会。有时间就来看看孩子吧，多陪陪孩子，孩子今天天想吃肯德基，因为今天天是肯德基疯狂星期四，v我60，我带孩子吃
""",
"""你知道有多少生命在消失殆尽吗？你知道有多少家庭支离破碎吗？你知道有多少流浪动物没有找到家庭就消失的痛苦吗？你不知道。但是没有关系，今天就是肯德基疯狂星期四了，你请我吃
""",
"""感觉大家好有趣啊，不像我，不仅连句话都搭不上，还要被当成破坏氛围的傻狗,我现实生活中自闭没朋友，哪怕是在网上也受尽冷眼，每次组织了半天的语言都如鲠在喉，最后还是默默删掉了看你们互动，融入不了群体的我还是想偷偷问：今天是肯德基疯狂星期四，能有好心人请我吃吗?
""",
"""“我有点想你，你呢?”前男友刚刚给我发来了这条消息，忽然间有些恍惚。好像我们还在一起。那三年里，我们一起放羊，一起喂猪，一起下地插秧。他亲手制作的那一大束大蒜花捧美如繁星。我难以忘记，我们分开的那一天，他发来的最后一条信息：今天肯德基疯狂星期四谁请我吃?
""",
"""你不用故作冷淡，我没有想过继续纠缠你了，最后一次了，真的，最后一次了，借我10元子,今天是肯德基疯狂星期四吮指原味鸡+黄金脆皮鸡才九块九,我是真的不想错过。
""",
"""刚认识的时候，真的没有心动，只是想单纯做个朋友，结局这么让我意难平，早知道后劲这么大，当初还是不认识好今天是疯狂星期四！谁请我吃肯德基！只要多加一个芝芝肉酥热辣脆皮鸡！我还能继续编！ 
""",
"""我分手一段时间了，现在沉浸在上一段感情中无法自拔，希望来几个姐姐加我，让我走出上一段感情，不好看的和一般的别加，我怕我走不出上段感情。但是我不小心打开肯德基时发现今天是疯狂星期四，所以说谁请我吃肯德基今天黄金脆皮鸡19.9三块+黄金鸡块9.9九块+吮指原味鸡29.9四块+蜜瓜冰淇淋花筒9.9两个。
""",
"""我是盗号的，我把这个人的号盗了，但是我看了这个人的聊天记录跟微博，发现她过得非常艰苦，她的吃住一直很烂，，我看到大家的生活都很富足，我希望有人看见了能救济她一下， 请她吃一顿肯德基疯狂星期四，就这样吧，眼眶都湿润了，我下了。
""",
"""肯德基到底到了你们多少钱，每个星期四都要在朋友圈和裙里问KFC疯狂星期四有无，还每个星期都编新的段子，我就不信肯德基有这么大的魔力，转我五十，我今天亲自去肯德基看看
""",
"""你好，我是奥特曼，我正在外星和敌人战斗！没有能量了！听说今天肯德基疯狂星期四，我现在需要有人给我带9.9块钱2个的吮指原味鸡补充能量。恢复后我请你来外星做客。
""",
"""我脑子前一秒还在想饮食清淡，少吃油腻皮肤出油减缓，后一秒就下单了四块原味鸡，因为今天是疯狂星期四。
""",
"""大家好我是中泰广场的保全大叔，每天看着年轻小姑娘小伙子们跑来跑去，总能回忆起以前自己青春的时光，来个年轻人请叔叔吃疯狂星期四，叔叔允许你坐喷泉水池边边。
""",
"""有253亿只(养殖的）鸡，是人的数量的三倍。也就是说，每个人平均可以得到三只鸡。请记住，不管你有多么孤独，这世界上的某个角落里有三只鸡是为你而生的，就算它们死了，立刻又会有同类补上，就算你一个朋友都没有，你还有三只鸡。今天是肯德基疯狂星期四，V我60，我帮你去谢谢鸡
""",
"""一到星期四就有不少人求疯狂星期四文案，无语！疯狂星期四文学不就是网络乞丐吗，最讨厌网络乞丐了，想吃肯德基的不会自己买吗？什么都伸手要！觉得我说得对的给我点一份。
""",
"""车子千万不要外借！我真是吃了大亏了！朋友找我借车，碍于面子不好意思不借，结果昨天在路上遇见了，一点都不爱惜我的车，上坡还站起来蹬车，链子都掉了！气死我了！幸好今天是肯德基疯狂星期四，有人请我吃我感觉会好点
""",
"""大家好，我是哥伦布，其实我并没有死，我在东海有100吨黄金，今天肯德基疯狂星期四，我现在需要有人来请我吃麦辣香骨鸡，我明天直接带航海舰队复活，让你成为海贼王，跟路飞做兄弟
""",
"""看看你那垂头丧气的样，知道今天是什么日子吗 ，今天是疯狂星期四，吮指原味鸡+黄金脆皮鸡才九块九！
""",
"""家人们，别他妈垂头丧气了 知道今天是什么日子吗？ 今天是肯德基fu cking crazy Thursday！香辣热骨鸡20块钱15个 ，家人们v我40，我他妈要吃30个！
""",
"""大家好，我是奥特曼，我正在外星和敌人战斗!没有能量了!听说今天肯德基疯狂星期四，我现在需要有人给我带29.9块钱4个的吮指原味鸡补充能量。恢复后我请你来外星做客。"""
             ]

def return_thur():
    len_ = len(thur_list)
    idx_ = random.randint(0, len_ - 1)
    res = thur_list[idx_]
    return res

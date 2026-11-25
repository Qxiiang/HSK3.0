// Bài 10: 你明天再把书还给我 (New HSK Course 3 Workbook - Lesson 10)
const hsk3Lesson10 = {
  lesson: 10,
  title: "你明天再把书还给我",
  englishTitle: "You can return the book to me tomorrow",

  // 一、汉字 (Chinese Characters)
  chineseCharacters: {
    similarCharacters: [
      {
        characters: ["炼", "练"],
        details: [
          { char: "炼", pinyin: "liàn", meaning: "rèn luyện", examples: ["锻炼", "他每天早上都锻炼身体。"] },
          { char: "练", pinyin: "liàn", meaning: "luyện tập", examples: ["练习", "这本书上还有几个练习。"] }
        ]
      }
    ],
    polyphonicCharacters: [
      {
        char: "要",
        variants: [
          { word: "要求", pinyin: "yāoqiú", example: "老师要求我们明天把作业做完。" },
          { word: "需要", pinyin: "xūyào", example: "我们需要把这些句子写在本子上。" }
        ]
      }
    ]
  },

  // 二、词语汇聚 Word Bank
  wordBank: {
    vocabulary: {
      learningScenarios: ["课本", "课文", "笔记", "铅笔", "纸", "页", "作业", "句子", "黑板", "办公室", "年级"],
      coursesAndSubjects: ["历史", "数学", "外语", "中文", "体育", "音乐"],
      learningBehaviors: ["认真", "努力", "差", "清楚", "难", "明白", "考试", "成绩", "提高", "要求", "复习", "讲", "读", "遍"]
    },
    keyWords: [
      {
        word: "课本",
        pinyin: "kèběn",
        pos: "n.",
        meaning: "textbook",
        collocation: "历史课本",
        example: "请同学们打开课本，看第15页。",
        dialogue: ["A: 你的历史课本在哪儿？", "B: 我把它放在书包里了。"]
      },
      {
        word: "课文",
        pinyin: "kèwén",
        pos: "n.",
        meaning: "text",
        collocation: "读课文",
        example: "老师让我们读一遍课文。",
        dialogue: ["A: 写作业以前，你先复习一遍课文。", "B: 我已经复习完了。"]
      },
      {
        word: "铅笔",
        pinyin: "qiānbǐ",
        pos: "n.",
        meaning: "pencil",
        collocation: "黑色铅笔",
        example: "考试结束我就把铅笔还给你。",
        dialogue: ["A: 我的铅笔找不到了，你还有铅笔吗？", "B: 有，你用我的吧。"]
      }
    ],
    collocations: [
      "记笔记", "写作业", "看黑板", "讲课",
      "一页纸/第十页", "一年级", "一个句子", "读两遍",
      "努力学习", "认真复习", "提高成绩", "考得很差"
    ],
    fillInTheBlanks: [
      { id: 1, question: "我女儿七岁，今年上小学二（   ）。", answer: "年级" },
      { id: 2, question: "你把名字写在历史（   ）上吧。", answer: "课本" },
      { id: 3, question: "明天考试，一定要带护照和笔，还可以带几张（   ）。", answer: "纸" },
      { id: 4, question: "这几个月他的学习（   ）提高了很多。", answer: "成绩" },
      { id: 5, question: "这本书太好看了，我想再读一（   ）。", answer: "遍" }
    ]
  },

  // 模拟测练 (Simulated Practice)
  simulatedPractice: {
    // 一、听力 (Listening)
    listening: {
      part1: {
        instruction: "第1~3题：听对话，选择最匹配的图片。每题听两次。",
        listeningPart1Image: "images/hsk3_bai10_nghe_1_3.png",
        example: {
          dialogue: "男：喂，请问张经理在吗？ / 女：他正在开会，您半个小时以后再打，好吗？",
          answer: "D"
        },
        options: ["A", "B", "C", "D"],
        questions: [
          { id: 1, answer: null },
          { id: 2, answer: null },
          { id: 3, answer: null }
        ]
      },
      part2: {
        instruction: "第4~6题：听对话，选择正确答案。每题听两次。",
        example: {
          dialogue: "女：我需要搬一些椅子到楼上办公室，你能来帮忙吗？ / 男：没问题，我再叫几个人来帮你。",
          question: "问：他们要把椅子搬到哪儿？",
          options: { A: "教室", B: "办公室", C: "体育馆" },
          answer: "B"
        },
        questions: [
          { id: 4, options: { A: "每天读历史书", B: "上课认真听课", C: "看同学的笔记" }, answer: null },
          { id: 5, options: { A: "老师没讲过", B: "女的做对了", C: "男的觉得不太难" }, answer: null },
          { id: 6, options: { A: "考得不好", B: "没准备考试", C: "每天都复习" }, answer: null }
        ]
      },
      part3: {
        instruction: "第7~10题：听一段话，选择正确答案。每题听两次。",
        example: {
          passage: "那个年轻人刚来公司不久，很有工作热情，人也很聪明。",
          question: "问：关于那个年轻人，可以知道什么？",
          options: { A: "很聪明", B: "是留学生", C: "爱踢足球" },
          answer: "A"
        },
        questions: [
          { id: 7, options: { A: "学习很认真", B: "不常写作业", C: "让妈妈检查作业" }, answer: null },
          { id: 8, options: { A: "画画", B: "中文歌", C: "中国电影" }, answer: null },
          { id: 9, options: { A: "不爱看书", B: "学习认真", C: "每天很早回家" }, answer: null },
          { id: 10, options: { A: "快要考试了", B: "姐姐影响了他", C: "考试成绩不好" }, answer: null }
        ]
      }
    },

    // 二、阅读 (Reading)
    reading: {
      part1: {
        instruction: "第11~15题：匹配句子。",
        choices: {
          A: "我想在出国前提高我的水平。",
          B: "好主意。在数学上我帮你，历史上你多帮帮我。",
          C: "你把它写在本子上，每天写几遍就记住了。",
          D: "他现在就在办公室，咱们一起去吧。",
          E: "当然。我们先坐公交车，然后换地铁。",
          F: "对。我读三年级，她读二年级。"
        },
        example: { question: "你知道怎么去国家图书馆吗？", answer: "E" },
        questions: [
          { id: 11, question: "我有几个问题想问李老师，不知道什么时间合适。", answer: "D" },
          { id: 12, question: "你为什么每天用这么多时间学外语？", answer: "A" },
          { id: 13, question: "你和妹妹在一个学校读书吗？", answer: "F" },
          { id: 14, question: "我总是忘了这个字怎么写。", answer: "C" },
          { id: 15, question: "马上就要考试了，咱们一起复习吧。", answer: "B" }
        ]
      },
      part2: {
        instruction: "第16~20题：选词填空。",
        wordChoices: {
          A: "差",
          B: "要求",
          C: "当然",
          D: "遇到",
          E: "鞋",
          F: "清楚"
        },
        example: { question: "中间那双（   ）是谁的？", answer: "E" },
        questions: [
          { id: 16, question: "我昨天在学校门口（   ）了以前的体育老师。", answer: "D" },
          { id: 17, question: "他这次考试考得很（   ），因为没认真复习。", answer: "A" },
          { id: 18, question: "我在教室外面，听不（   ）老师说什么。", answer: "F" },
          { id: 19, question: "A: 你能帮我把这本书还给李老师吗？ / B: （   ）可以。", answer: "C" },
          { id: 20, question: "A: 老师（   ）我们明天把错题本拿给他。 / B: 我的错题太多了，今天晚上一定写不完。", answer: "B" }
        ]
      },
      part3: {
        instruction: "第21~24题：选择正确答案。",
        example: {
          passage: "您是来参加今天会议的吗？您来早了一点儿，现在才八点半。您先进来坐吧。",
          question: "会议最可能几点开始？",
          options: { A: "8:00", B: "8:30", C: "9:00" },
          answer: "C"
        },
        questions: [
          {
            id: 21,
            passage: "张老师教我们外语。他上课讲得很清楚，还常在休息的时候让我们听音乐，同学们都很喜欢他。",
            question: "关于张老师，可以知道什么？",
            options: { A: "他教音乐", B: "他上课听音乐", C: "学生都很喜欢他" },
            answer: "C"
          },
          {
            id: 22,
            passage: "今天有历史课，但是我忘了带历史课本。上课时，我和同学一起看书、做练习，有点儿不方便。下次我一定会记得带。",
            question: "他今天怎么了？",
            options: { A: "没带课本", B: "没做练习", C: "没上历史课" },
            answer: "A"
          },
          {
            id: 23,
            sharedPassage: "昨天作业里的几个错题我不太明白，想问问李老师。进办公室的时候，李老师正在给别的同学讲题，我站在旁边听了一会儿，发现我想问的句子跟这几个同学一样。李老师讲得很清楚，听完我们都明白了。我把作业本放进书包里，高高兴兴地走出了办公室。",
            question: "他为什么去找李老师？",
            options: { A: "他想找作业本", B: "他有不明白的题", C: "李老师要给他讲题" },
            answer: "B"
          },
          {
            id: 24,
            sharedPassage: "昨天作业里的几个错题我不太明白，想问问李老师。进办公室的时候，李老师正在给别的同学讲题，我站在旁边听了一会儿，发现我想问的句子跟这几个同学一样。李老师讲得很清楚，听完我们都明白了。我把作业本放进书包里，高高兴兴地走出了办公室。",
            question: "关于李老师，可以知道什么？",
            options: { A: "在上课", B: "在教室里等他", C: "在给学生讲题" },
            answer: "C"
          }
        ]
      }
    },

    // 三、书写 (Writing)
    writing: {
      part1: {
        instruction: "第25~27题：根据拼音写汉字。",
        example: { sentence: "咱们一会儿（   ）车回家吧。", pinyin: "dǎ", answer: "打" },
        questions: [
          { id: 25, sentence: "她一般（   ）这些东西放在桌子上。", pinyin: "bǎ", answer: "把" },
          { id: 26, sentence: "老师要求我们这个星期就开始（   ）习。", pinyin: "fù", answer: "复" },
          { id: 27, sentence: "这（   ）话我没听懂，请你再说一遍。", pinyin: "jù", answer: "句" }
        ]
      },
      part2: {
        instruction: "第28~30题：看图，用词造句。",
        example: { keyword: "开心", sampleAnswer: "他开心得跳起来了。" },
        questions: [
          {
            id: 28,
            img: "images/hsk3_bai10_viet_28.png",
            keyword: "努力",
            imageDescription: "Các học sinh đang giơ tay phát biểu rất hăng hái và chăm chỉ trong lớp học",
            sampleAnswer: "同学们在课堂上学习很努力。"
          },
          {
            id: 29,
            img: "images/hsk3_bai10_viet_29.png",
            keyword: "后年",
            imageDescription: "Bốn sinh viên đeo ba lô đang bước lên bậc thang trước tòa nhà trường đại học",
            sampleAnswer: "他们后年就要大学毕业了。"
          },
          {
            id: 30,
            img: "images/hsk3_bai10_viet_30.png",
            keyword: "对话",
            imageDescription: "Hai cô gái ngồi trên ghế sofa trò chuyện vui vẻ với nhau",
            sampleAnswer: "她们正在用中文练习对话。"
          }
        ]
      }
    }
  }
};

export default hsk3Lesson10;
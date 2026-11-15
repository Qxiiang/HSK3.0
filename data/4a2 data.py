# -*- coding: utf-8 -*-

lesson_data = {
    "lesson_title": "Bài 2: 租到了合适的房子 (Đã thuê được căn nhà phù hợp)",
    "blocks": [
        # ==================== TRANG BÌA ====================
        {
            "type": "title_slide",
            "data": {
                "title_zh": "租到了合适的房子",
                "lesson_number": "2",
                "bg_image": "assets/hinhnen.png",
                "show_number": True
            }
        },

        # ==================== MỤC TIÊU ====================
        {
            "type": "objectives",
            "data": {
                "items": [
                    {"zh": "能够听懂并交流关于租房的话题。", "vi": "Có thể nghe hiểu và giao tiếp về chủ đề thuê nhà."},
                    {"zh": "能够口头或书面表达租房意愿、要求等。", "vi": "Có thể trình bày bằng lời nói hoặc văn bản nguyện vọng, yêu cầu thuê nhà, v.v."},
                    {"zh": "了解中国人的住房观念。", "vi": "Hiểu biết về quan niệm nhà ở của người Trung Quốc."}
                ]
            }
        },

        # ==================== KHỞI ĐỘNG ====================
        {
            "type": "warmup",
            "data": {
                "title": "Khởi động",
                "instruction": "Chọn từ ngữ phù hợp với hình ảnh tương ứng.",
                "raw_options": [
                    {"zh": "客厅", "pinyin": "kètīng", "img": "assets/warmup_1.png", "answer": "A"},
                    {"zh": "种", "pinyin": "zhòng", "img": "assets/warmup_2.png", "answer": "B"},
                    {"zh": "收拾", "pinyin": "shōushi", "img": "assets/warmup_3.png", "answer": "C"},
                    {"zh": "毕业", "pinyin": "bìyè", "img": "assets/warmup_4.png", "answer": "D"},
                    {"zh": "厨房", "pinyin": "chúfáng", "img": "assets/warmup_5.png", "answer": "E"},
                    {"zh": "价格", "pinyin": "jiàgé", "img": "assets/warmup_6.png", "answer": "F"}
                ]
            }
        },
        {
            "type": "qa_slide",
            "data": {
                "title": "Khởi động",
                "instruction": "Hai người một nhóm, dựa vào tình huống thực tế để hỏi đáp.",
                "questions": [
                    "你觉得租房子好，还是买房子好？为什么？",
                    "如果租房子，你喜欢租什么样的房子？"
                ]
            }
        },

        # ==================== BÀI KHÓA 1 ====================
        {
            "type": "title_slide",
            "data": {
                "title_zh": "课文 1",
                "lesson_number": "2",
                "bg_image": "assets/hinhnen.png",
                "show_number": False
            }
        },
        {
            "type": "vocabulary_table",
            "data": {
                "lesson_num": "2",
                "level": "4",
                "audio_index": "2",
                "words": [
                    {"stt": 1, "zh": "房东", "pinyin": "fángdōng", "type": "danh", "hanviet": "Phòng đông", "vi": "chủ nhà"},
                    {"stt": 2, "zh": "出租", "pinyin": "chūzū", "type": "động", "hanviet": "Xuất tô", "vi": "cho thuê"},
                    {"stt": 3, "zh": "房租", "pinyin": "fángzū", "type": "danh", "hanviet": "Phòng tô", "vi": "tiền thuê nhà"},
                    {"stt": 4, "zh": "收拾", "pinyin": "shōushi", "type": "động", "hanviet": "Thu thập", "vi": "dọn dẹp, thu xếp"},
                    {"stt": 5, "zh": "租", "pinyin": "zū", "type": "động", "hanviet": "Tô", "vi": "thuê"},
                    {"stt": 6, "zh": "嗯", "pinyin": "ǹg", "type": "thán", "hanviet": "Ân", "vi": "ừ, ừm"},
                    {"stt": 7, "zh": "亮", "pinyin": "liàng", "type": "tính/động", "hanviet": "Lượng", "vi": "sáng sủa; chiếu sáng"},
                    {"stt": 8, "zh": "就是", "pinyin": "jiùshì", "type": "trợ", "hanviet": "Tựu thị", "vi": "cứ (dùng để nhấn mạnh)"}
                ]
            }
        },
        {
            "type": "listening_abcd",
            "data": {
                "title": "Nghe và chọn đáp án đúng",
                "context_zh": "白家月想租房，李文陪白家月去看房。",
                "context_vi": "Bạch Giai Nguyệt muốn thuê nhà, Lý Văn đi cùng cô ấy đi xem nhà.",
                "lesson_num": "2",
                "level": "4",
                "audio_index": "1",
                "questions": [
                    {
                        "q_zh": "白家月在看的房子每个月房租是多少？",
                        "options": ["A. 3500元", "B. 5000元", "C. 5500元", "D. 6500元"]
                    },
                    {
                        "q_zh": "白家月在看的房子离哪里近？",
                        "options": ["A. 公司", "B. 地铁站", "C. 公交站", "D. 大超市"]
                    }
                ]
            }
        },
        {
            "type": "text_hsk3",
            "data": {
                "title": "课文\n1",
                "context_zh": "白家月想租房，李文陪白家月去看房。",
                "context_vi": "Bạch Giai Nguyệt muốn thuê nhà, Lý Văn đi cùng cô ấy đi xem nhà.",
                "lesson_num": "2",
                "level": "4",
                "audio_index": "1",
                "lines": [
                    {"speaker": "房东:", "text": "请进！我给你们介绍一下，这个房子有两个房间，那个大房间出租，房租每月5500元。现在已经收拾好了，想租的话，今天就可以搬进来。"},
                    {"speaker": "白家月:", "text": "嗯，这个房间真不小，还挺亮。小区离我们学校也不远。"},
                    {"speaker": "房东:", "text": "是的，我们小区离地铁站也很近，生活上很方便。如果决定租了，告诉我就是了。"},
                    {"speaker": "白家月:", "text": "好的，我们再去看看外面的环境。"}
                ]
            }
        },
        {
            "type": "qa_slide",
            "data": {
                "title": "Đọc phân vai và trả lời câu hỏi",
                "questions": [
                    "房东要出租哪个房间？那个房间怎么样？",
                    "房东为什么说住在那个小区生活上很方便？"
                ]
            }
        },
        {
            "type": "retell_hsk4",
            "data": {
                "title": "根据给出的提示复述课文",
                "text": "李文和白家月到房东家看房子。房东要出租的是________，房租________。房东告诉白家月，要出租的房间现在________，想租的话，今天________。这个房间________，还________。小区离白家月的________不远，离地铁站________，生活上________。白家月比较满意，他们决定再________。"
            }
        },
        {
            "type": "grammar",
            "data": {
                "title_vi": "1. Cấu trúc cố định “×就是了”",
                "description_zh": "固定格式“×就是了”用于口语中，在句子末尾表示肯定。例如：",
                "formula": "动词短语 + 就是了",
                "explanation_vi": "Cấu trúc cố định “×就是了” dùng trong khẩu ngữ, đặt ở cuối câu để biểu thị sự khẳng định.",
                "examples": [
                    "(1) 如果决定租了，告诉我就是了。",
                    "(2) 我一定能办到，您放心就是了。",
                    "(3) 这次考得不好没关系，下次努力就是了。"
                ]
            }
        },
        {
            "type": "open_cloze",
            "data": {
                "title": "完成对话",
                "questions": [
                    "A: 这个房子很干净，小区也安静，我租不租呢？\nB: ______",
                    "A: 这里离地铁站比较远，我怎么去好呢？\nB: ______",
                    "A: 你觉得这件衣服怎么样？我要不要买？\nB: 我觉得很漂亮，______"
                ]
            }
        },

        # ==================== BÀI KHÓA 2 ====================
        {
            "type": "title_slide",
            "data": {
                "title_zh": "课文 2",
                "lesson_number": "2",
                "bg_image": "assets/hinhnen.png",
                "show_number": False
            }
        },
        {
            "type": "vocabulary_table",
            "data": {
                "lesson_num": "2",
                "level": "4",
                "audio_index": "4",
                "words": [
                    {"stt": 9, "zh": "种", "pinyin": "zhòng", "type": "động", "hanviet": "Chủng", "vi": "trồng"},
                    {"stt": 10, "zh": "周围", "pinyin": "zhōuwéi", "type": "danh", "hanviet": "Chu vi", "vi": "xung quanh"},
                    {"stt": 11, "zh": "不过", "pinyin": "búguò", "type": "liên", "hanviet": "Bất quá", "vi": "nhưng, tuy nhiên"},
                    {"stt": 12, "zh": "毕业", "pinyin": "bìyè", "type": "động", "hanviet": "Tất nghiệp", "vi": "tốt nghiệp"},
                    {"stt": 13, "zh": "恐怕", "pinyin": "kǒngpà", "type": "phó", "hanviet": "Khủng phạ", "vi": "e rằng, có lẽ"},
                    {"stt": 14, "zh": "热闹", "pinyin": "rènao", "type": "tính/động", "hanviet": "Nhiệt nháo", "vi": "náo nhiệt; vui vẻ"},
                    {"stt": 15, "zh": "入住", "pinyin": "rùzhù", "type": "động", "hanviet": "Nhập trú", "vi": "dọn vào ở, nhận phòng"}
                ]
            }
        },
        {
            "type": "listening_abcd",
            "data": {
                "title": "Nghe và chọn đáp án đúng",
                "context_zh": "在小区里，白家月和李文继续查看周围环境。",
                "context_vi": "Trong khu dân cư, Bạch Giai Nguyệt và Lý Văn tiếp tục xem xét môi trường xung quanh.",
                "lesson_num": "2",
                "level": "4",
                "audio_index": "3",
                "questions": [
                    {
                        "q_zh": "白家月觉得小区的环境怎么样？",
    			"options": ["A. 树不多", "B. 不太好", "C. 很安静", "D. 很干净"]
                    },
                    {
                        "q_zh": "白家月想什么时候搬进新房子？",
                        "options": ["A. 今天", "B. 明天", "C. 后天下午", "D. 后天晚上"]
                    }
                ]
            }
        },
        {
            "type": "text_hsk3",
            "data": {
                "title": "课文\n2",
                "context_zh": "在小区里，白家月和李文继续查看周围环境。",
                "context_vi": "Trong khu dân cư, Bạch Giai Nguyệt và Lý Văn tiếp tục xem xét môi trường xung quanh.",
                "lesson_num": "2",
                "level": "4",
                "audio_index": "3",
                "lines": [
                    {"speaker": "李文:", "text": "家月，你看，那边还有个小花园。"},
                    {"speaker": "白家月:", "text": "嗯，这个小区到处是花，还种了不少树，周围也很安静。"},
                    {"speaker": "李文:", "text": "是啊！这个小区的环境真不错，不过我听说，附近有十几家公司，很多刚毕业的学生都租住在这里。周末他们可能会玩到很晚，恐怕会影响你休息。"},
                    {"speaker": "白家月:", "text": "没关系，我还想多认识一些朋友，和他们一起玩呢。"},
                    {"speaker": "李文:", "text": "是呢，大家可以一起热闹热闹。"},
                    {"speaker": "白家月:", "text": "这里房租合适，环境很好，而且房东也热情，所以我决定租这个房子了，明天就入住新家。"}
                ]
            }
        },
        {
            "type": "qa_slide",
            "data": {
                "title": "Đọc phân vai và trả lời câu hỏi",
                "questions": [
                    "李文为什么担心周末白家月休息不好？",
                    "白家月为什么决定租那个房子？"
                ]
            }
        },
        {
            "type": "grammar",
            "data": {
                "title_vi": "2. Câu phức chuyển ngoặt “……，不过……”",
                "description_zh": "连词“不过”用在两个分句中后一个分句的开头，表示转折。例如：",
                "formula": "分句1 + ，不过 + 分句2",
                "explanation_vi": "Liên từ “不过” dùng ở đầu phân câu thứ hai trong hai phân câu, biểu thị sự chuyển ngoặt.",
                "examples": [
                    "(1) 这个小区的环境真不错，不过我听说，附近有十几家公司，很多刚毕业的学生都租住在这里。",
                    "(2) 我们在动物园看见了很多动物，不过没看见大熊猫。",
                    "(3) 我刚来北京时还不太习惯这里的天气，不过很快就适应了。"
                ]
            }
        },
        {
            "type": "open_cloze",
            "data": {
                "title": "完成对话",
                "questions": [
                    "A: 你觉得这个手机怎么样？\nB: 还可以，不过______",
                    "A: 你生病了？\nB: 没有，______",
                    "A: 我们可以走着去那里吗？\nB: 可以，______"
                ]
            }
        },

        # ==================== BÀI KHÓA 3 ====================
        {
            "type": "title_slide",
            "data": {
                "title_zh": "课文 3",
                "lesson_number": "2",
                "bg_image": "assets/hinhnen.png",
                "show_number": False
            }
        },
        {
            "type": "vocabulary_table",
            "data": {
                "lesson_num": "2",
                "level": "4",
                "audio_index": "6",
                "words": [
                    {"stt": 16, "zh": "日记", "pinyin": "rìjì", "type": "danh", "hanviet": "Nhật ký", "vi": "nhật ký"},
                    {"stt": 17, "zh": "顺利", "pinyin": "shùnlì", "type": "tính", "hanviet": "Thuận lợi", "vi": "thuận lợi, suôn sẻ"},
                    {"stt": 18, "zh": "并", "pinyin": "bìng", "type": "liên/phó", "hanviet": "Tịnh", "vi": "và, hơn nữa; hoàn toàn (không)"},
                    {"stt": 19, "zh": "客厅", "pinyin": "kètīng", "type": "danh", "hanviet": "Khách sảnh", "vi": "phòng khách"},
                    {"stt": 20, "zh": "台", "pinyin": "tái", "type": "lượng", "hanviet": "Đài", "vi": "cái, chiếc (máy móc, thiết bị)"},
                    {"stt": 21, "zh": "厨房", "pinyin": "chúfáng", "type": "danh", "hanviet": "Trù phòng", "vi": "nhà bếp"},
                    {"stt": 22, "zh": "平常", "pinyin": "píngcháng", "type": "danh/tính", "hanviet": "Bình thường", "vi": "ngày thường, bình thường"},
                    {"stt": 23, "zh": "基本上", "pinyin": "jīběnshàng", "type": "phó", "hanviet": "Cơ bản thượng", "vi": "cơ bản là, về cơ bản"},
                    {"stt": 24, "zh": "整个", "pinyin": "zhěnggè", "type": "tính", "hanviet": "Chỉnh cá", "vi": "toàn bộ, cả"},
                    {"stt": 25, "zh": "毛巾", "pinyin": "máojīn", "type": "danh", "hanviet": "Mao cân", "vi": "khăn mặt"}
                ]
            }
        },
        {
            "type": "listening_abcd",
            "data": {
                "title": "Nghe và chọn đáp án đúng",
                "context_zh": "搬进新家后，白家月很开心，写了一篇日记。",
                "context_vi": "Sau khi chuyển vào nhà mới, Bạch Giai Nguyệt rất vui và viết một bài nhật ký.",
                "lesson_num": "2",
                "level": "4",
                "audio_index": "5",
                "questions": [
                    {
                        "q_zh": "白家月租的房子，客厅里都有什么？",
                        "options": ["A. 椅子、沙发和电视", "B. 椅子、空调和书桌", "C. 冰箱、电视和空调", "D. 书桌、椅子和沙发"]
                    },
                    {
                        "q_zh": "白家月平常主要在哪儿吃饭？",
                        "options": ["A. 家里", "B. 饭馆", "C. 邻居家", "D. 学校食堂"]
                    }
                ]
            }
        },
        {
            "type": "text_hsk3",
            "data": {
                "title": "课文\n3",
                "context_zh": "搬进新家后，白家月很开心，写了一篇日记。",
                "context_vi": "Sau khi chuyển vào nhà mới, Bạch Giai Nguyệt rất vui và viết một bài nhật ký.",
                "lesson_num": "2",
                "level": "4",
                "audio_index": "5",
                "lines": [
                    {"speaker": "白家月:", "text": "8月25日，晴。昨天我顺利租到了合适的房子，今天李文帮我搬家。搬进去的时候，房东又向我介绍了一下房子里的东西，并告诉我这些东西怎么用。"},
                    {"speaker": "白家月:", "text": "我看了一下，客厅里有椅子、沙发，还有一台大电视；厨房里有冰箱和一些做饭用的东西，不过，我平常主要在学校食堂吃，基本上不做饭。我租的房间里，除了一张床以外，还有一台空调、一张书桌和一把椅子。"},
                    {"speaker": "白家月:", "text": "看完整个房子后，我准备再去买几条毛巾，其他东西还不需要。"}
                ]
            }
        },
        {
            "type": "qa_slide",
            "data": {
                "title": "Đọc bài khóa và trả lời câu hỏi",
                "questions": [
                    "白家月租的房间里都有什么？",
                    "白家月准备去买什么？"
                ]
            }
        },
        {
            "type": "retell_hsk4",
            "data": {
                "title": "根据给出的提示复述课文",
                "text": "昨天白家月顺利________，今天李文帮她________。搬进去的时候，房东又向白家月________，并告诉她________。白家月看到，客厅里有________，还有________；厨房里有冰箱和________，不过，白家月平常________，基本上________。白家月租的房间里，除了________以外，还有一台空调、________。看完整个房子后，她觉得再去________就行了。"
            }
        },
        {
            "type": "grammar",
            "data": {
                "title_vi": "3. Liên từ / Phó từ “并” (Phần 1: Liên từ)",
                "description_zh": "“并”作连词，连接并列的双音节动词、短语或小句，表示并列关系，有更进一层的意思。例如：",
                "formula": "动词1 + 并 + 动词2",
                "explanation_vi": "“并” làm liên từ, nối các động từ song âm tiết, cụm từ hoặc mệnh đề song song, biểu thị quan hệ song song, mang ý nghĩa tiến thêm một bước.",
                "examples": [
                    "(1) 房东又向我介绍了一下房子里的东西，并告诉我这些东西怎么用。",
                    "(2) 她考上了北京大学并申请到了奖学金。"
                ]
            }
        },
        {
            "type": "grammar",
            "data": {
                "title_vi": "3. Liên từ / Phó từ “并” (Phần 2: Phó từ)",
                "description_zh": "“并”作副词，用在否定词前，加强否定语气，说明事实并非如此。例如：",
                "formula": "并 + 不/没 + 动词",
                "explanation_vi": "“并” làm phó từ, dùng trước từ phủ định để tăng cường ngữ khí phủ định, giải thích sự thật không phải như vậy.",
                "examples": [
                    "(1) 我并没有答应你就租这个房子，我还要再想想。"
                ]
            }
        },
        {
            "type": "open_cloze",
            "data": {
                "title": "完成句子",
                "questions": [
                    "他毕业后来到北京工作，______(租)",
                    "我吃完饭______后，才去公园跑步。(收拾)",
                    "她______这个小区，这里人太多，她不喜欢。(入住)"
                ]
            }
        },

        # ==================== BÀI KHÓA 4 ====================
        {
            "type": "title_slide",
            "data": {
                "title_zh": "课文 4",
                "lesson_number": "2",
                "bg_image": "assets/hinhnen.png",
                "show_number": False
            }
        },
        {
            "type": "vocabulary_table",
            "data": {
                "lesson_num": "2",
                "level": "4",
                "audio_index": "8",
                "words": [
                    {"stt": 26, "zh": "建议", "pinyin": "jiànyì", "type": "danh/động", "hanviet": "Kiến nghị", "vi": "lời đề nghị; đề nghị"},
                    {"stt": 27, "zh": "查看", "pinyin": "chákàn", "type": "động", "hanviet": "Tra khán", "vi": "kiểm tra, xem xét"},
                    {"stt": 28, "zh": "信息", "pinyin": "xìnxī", "type": "danh", "hanviet": "Tín tức", "vi": "thông tin"},
                    {"stt": 29, "zh": "查找", "pinyin": "cházhǎo", "type": "động", "hanviet": "Tra tìm", "vi": "tìm kiếm"},
                    {"stt": 30, "zh": "接着", "pinyin": "jiēzhe", "type": "phó/động", "hanviet": "Tiếp trứ", "vi": "tiếp theo, sau đó"},
                    {"stt": 31, "zh": "同时", "pinyin": "tóngshí", "type": "liên/danh", "hanviet": "Đồng thời", "vi": "đồng thời, cùng lúc"},
                    {"stt": 32, "zh": "位置", "pinyin": "wèizhì", "type": "danh", "hanviet": "Vị trí", "vi": "vị trí"},
                    {"stt": 33, "zh": "价格", "pinyin": "jiàgé", "type": "danh", "hanviet": "Giá cách", "vi": "giá cả"},
                    {"stt": 34, "zh": "理想", "pinyin": "lǐxiǎng", "type": "tính/danh", "hanviet": "Lý tưởng", "vi": "lý tưởng"},
                    {"stt": 35, "zh": "由于", "pinyin": "yóuyú", "type": "liên/giới", "hanviet": "Do vu", "vi": "do, bởi vì"},
                    {"stt": 36, "zh": "工资", "pinyin": "gōngzī", "type": "danh", "hanviet": "Công tư", "vi": "tiền lương"},
                    {"stt": 37, "zh": "感", "pinyin": "gǎn", "type": "hậu tố", "hanviet": "Cảm", "vi": "cảm giác (hậu tố)"}
                ]
            }
        },
        {
            "type": "listening_abcd",
            "data": {
                "title": "Đọc bài khóa và chọn đáp án đúng",
                "context_zh": "怎样租到合适的房子",
                "context_vi": "Làm thế nào để thuê được căn nhà phù hợp.",
                "lesson_num": "2",
                "level": "4",
                "audio_index": "7",
                "questions": [
                    {
                        "q_zh": "白家月觉得这次租房怎么样？",
                        "options": ["A. 很简单", "B. 不容易", "C. 不理想", "D. 有意思"]
                    },
                    {
                        "q_zh": "根据课文，很多刚工作的年轻人为什么选择租房？",
                        "options": ["A. 更有安全感", "B. 不喜欢买房", "C. 喜欢租房子住", "D. 工资还不太高"]
                    }
                ]
            }
        },
        {
            "type": "text_hsk3",
            "data": {
                "title": "课文\n4",
                "context_zh": "怎样租到合适的房子",
                "context_vi": "Làm thế nào để thuê được căn nhà phù hợp.",
                "lesson_num": "2",
                "level": "4",
                "audio_index": "7",
                "lines": [
                    {"speaker": "旁白:", "text": "在李文的帮助下，白家月租到了合适的房子。对白家月来说，这次租房并不容易。根据李文的建议，她先在租房网站和App上查看有关信息，查找合适的房子，接着又去看了看房子，同时了解房子周围的环境。她看了好几个房子，才找到一个位置、环境和价格都合适的，最后顺利租到了理想的房子。"},
                    {"speaker": "旁白:", "text": "租房的时候，李文告诉白家月，在中国，由于很多刚工作的年轻人工资还不太高，所以他们一开始也不买房，都选择租房。工作几年后，不少人就会买房，因为大家一直觉得，有房才有家，有自己的房子会更有安全感。"}
                ]
            }
        },
        {
            "type": "qa_slide",
            "data": {
                "title": "Đọc bài khóa và trả lời câu hỏi",
                "questions": [
                    "白家月是怎么租到合适的房子的？",
                    "在中国，为什么不少人工作几年后会买房？"
                ]
            }
        },
        {
            "type": "grammar",
            "data": {
                "title_vi": "4. Liên từ / Giới từ “由于” (Phần 1: Liên từ)",
                "description_zh": "“由于”作连词，用在复句中前一分句的开头，表示原因，后一分句开头一般有“所以、因此”等词语。例如：",
                "formula": "由于 + 原因 + ，所以/因此 + 结果",
                "explanation_vi": "“由于” làm liên từ, dùng ở đầu phân câu trước trong câu phức để biểu thị nguyên nhân, đầu phân câu sau thường có các từ như “所以, 因此”.",
                "examples": [
                    "(1) 在中国，由于很多刚工作的年轻人工资还不太高，所以他们一开始也不买房，都选择租房。",
                    "(2) 由于一直下大雨，所以我们决定不爬山了。",
                    "(3) 由于大家的努力，这次运动会我们班获得了第一名。"
                ]
            }
        },
        {
            "type": "grammar",
            "data": {
                "title_vi": "4. Liên từ / Giới từ “由于” (Phần 2: Giới từ)",
                "description_zh": "“由于”作介词，表示原因或理由，后面常接名词或名词性短语。例如：",
                "formula": "由于 + 名词/名词短语",
                "explanation_vi": "“由于” làm giới từ, biểu thị nguyên nhân hoặc lý do, phía sau thường là danh từ hoặc cụm danh từ.",
                "examples": [
                    "(1) 由于天气原因，飞机晚点了。",
                    "(2) 他由于身体不舒服，今天没来上课。"
                ]
            }
        },
        {
            "type": "open_cloze",
            "data": {
                "title": "完成句子",
                "questions": [
                    "由于手机没电了，______",
                    "由于这个小区很安静，房子价格也不高，因此，______",
                    "______，我们很快就完成了这个工作。"
                ]
            }
        },

        # ==================== LUYỆN TẬP TỔNG HỢP ====================
        {
            "type": "title_slide",
            "data": {
                "title_zh": "综合练习",
                "lesson_number": "2",
                "bg_image": "assets/hinhnen.png",
                "show_number": False
            }
        },
        {
            "type": "fill_in_blanks",
            "data": {
                "title": "选词填空",
                "questions": [
                    "(1) 这个小区环境好，______也不高，一个月才5000元。",
                    "(2) 要______一个好房子也不容易，需要多多比较。",
                    "(3) 我女儿每天都把房间______得干干净净的。",
                    "(4) 这次比赛的通知已经发到大家的邮箱了，请注意______",
                    "(5) ______后我发现，宾馆房间的灯是坏的。"
                ],
                "options": ["A 收拾", "B 房租", "C 入住", "D 租", "E 查看"]
            }
        },
        {
            "type": "fill_in_blanks",
            "data": {
                "title": "选词填空",
                "questions": [
                    "(6) A: 我最近打算在公司附近租个房子。\nB: 那你上网______租房信息时，一定要小心，不要只看价格。",
                    "(7) A: 你假期打算做什么？\nB: 我要先回家住几天，______跟朋友去上海玩。",
                    "(8) A: 听说小区______有很多公司，很多年轻人都租住在附近。\nB: 是的，所以周末时特别热闹。"
                ],
                "options": ["A 周围", "B 建议", "C 查找", "D 客厅", "E 接着"]
            }
        },
        {
            "type": "fill_in_blanks",
            "data": {
                "title": "选词填空",
                "questions": [
                    "(9) A: 这个房子怎么样？\nB: 很大，______也大，里边除了沙发以外，还有一台大电视。",
                    "(10) A: 关于租什么样的房子合适，你还有什么好______？\nB: 除了离公司近以外，我觉得生活上方便也很重要。"
                ],
                "options": ["A 周围", "B 建议", "C 查找", "D 客厅", "E 接着"]
            }
        },
        {
            "type": "complete_passage_abcd",
            "data": {
                "title": "选择合适的内容完成短文",
                "context_text": "小张最近换了一个比较理想的工作。由于新公司离她现在住的地方比较远，________。她在网上查找到一条出租信息，________。房东说，小张要租的房子不太大，________，房租不高，位置也比较好。接着，房东又建议小张过去看看。小张看了以后，________，就租了下来。",
                "options": [
                    "A. 就给房东打了电话",
                    "B. 觉得房子很不错",
                    "C. 她决定在公司附近租个房子",
                    "D. 但是很干净"
                ]
            }
        },
        # ==================== MIÊU TẢ TRANH (HSK4) ====================
        {
            "type": "slide_describe_picture_hsk4",
            "data": {
                "title": "看图，用词语造句",
                "quyen": "4",
                "bai": "2",
                "items": [
                    {"word": "房东"},
                    {"word": "毛巾"},
                    {"word": "理想"}
                ]
            }
        },

        # ==================== VIẾT ====================
        {
            "type": "slide_writing_hsk4",
            "data": {
                "title": "写作",
                "instruction_zh": "假如你是一个刚毕业的大学生，想要租房子。请你写一段租房需求信息，不少于120字。",
                "instruction_vi": "Giả sử bạn là một sinh viên đại học vừa tốt nghiệp, muốn thuê nhà. Hãy viết một đoạn thông tin nhu cầu thuê nhà, không ít hơn 120 chữ.",
                "image": "writting.png"
            }
        },

        # ==================== TỔNG KẾT ====================
        # ==================== TỔNG KẾT ====================
        {
            "type": "summary",
            "data": {
                "title": "学习小结",
                "table_header": "Nội dung tự đánh giá",
                "row1_title_vi": "Có thể sử dụng các từ ngữ như “房东, 出租, 房租, 收拾, 租, 入住” trong bài để thảo luận về chủ đề thuê nhà.",
                "row2_title_vi": "Có thể hiểu và vận dụng các điểm ngữ pháp như “×就是了”, “……，不过……”, “并”, “由于”.",
                "row3_title_vi": "Có thể bày tỏ quan điểm thuê nhà hay mua nhà."
            }
        },

        # ==================== TRANG CẢM ƠN ====================
        {
            "type": "title_slide",
            "data": {
                "title_zh": "谢谢！",
                "lesson_number": "2",
                "bg_image": "assets/hinhnen.png",
                "show_number": False
            }
        }
    ]
}
# -*- coding: utf-8 -*-

lesson_data = {
    "lesson_title": "Bài 3: 手机扫一下 (Quét mã điện thoại một chút)",
    "blocks": [
        # ==================== TRANG BÌA ====================
        {
            "type": "title_slide",
            "data": {
                "title_zh": "手机扫一下",
                "lesson_number": "3",
                "bg_image": "assets/hinhnen.png",
                "show_number": True
            }
        },

        # ==================== MỤC TIÊU ====================
        {
            "type": "objectives",
            "data": {
                "items": [
                    {"zh": "能够听懂并交流下载App、网购、手机支付等话题。", "vi": "Có thể nghe hiểu và giao tiếp về các chủ đề như tải App, mua sắm trực tuyến, thanh toán bằng điện thoại."},
                    {"zh": "能够口头或书面表达手机的各种用处。", "vi": "Có thể trình bày bằng lời nói hoặc văn bản các công dụng khác nhau của điện thoại di động."},
                    {"zh": "了解网络时代保护个人信息的做法。", "vi": "Hiểu biết về các biện pháp bảo vệ thông tin cá nhân trong thời đại mạng internet."}
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
                    {"zh": "法律", "pinyin": "fǎlǜ", "img": "assets/warmup_1.png", "answer": "A"},
                    {"zh": "扫码支付", "pinyin": "sǎomǎ zhīfù", "img": "assets/warmup_2.png", "answer": "B"},
                    {"zh": "网购", "pinyin": "wǎnggòu", "img": "assets/warmup_3.png", "answer": "C"},
                    {"zh": "快递员", "pinyin": "kuàidìyuán", "img": "assets/warmup_4.png", "answer": "D"},
                    {"zh": "管", "pinyin": "guǎn", "img": "assets/warmup_5.png", "answer": "E"},
                    {"zh": "保护", "pinyin": "bǎohù", "img": "assets/warmup_6.png", "answer": "F"}
                ]
            }
        },
        {
            "type": "qa_slide",
            "data": {
                "title": "Khởi động",
                "instruction": "Hai người một nhóm, dựa vào tình huống thực tế để hỏi đáp.",
                "questions": [
                    "你在网上购物吗？如果你网购，说说你是怎么进行网购的；如果你不网购，为什么？",
                    "用手机时，你会怎样保护自己的信息？"
                ]
            }
        },

        # ==================== BÀI KHÓA 1 ====================
        {
            "type": "title_slide",
            "data": {
                "title_zh": "课文 1",
                "lesson_number": "3",
                "bg_image": "assets/hinhnen.png",
                "show_number": False
            }
        },
        {
            "type": "vocabulary_table",
            "data": {
                "lesson_num": "3",
                "level": "4",
                "audio_index": "2",
                "words": [
                    {"stt": 1, "zh": "十字路口", "pinyin": "shízì lùkǒu", "type": "danh", "hanviet": "Thập tự lộ khẩu", "vi": "ngã tư"},
                    {"stt": 2, "zh": "直接", "pinyin": "zhíjiē", "type": "tính", "hanviet": "Trực tiếp", "vi": "trực tiếp"},
                    {"stt": 3, "zh": "转", "pinyin": "zhuǎn", "type": "động", "hanviet": "Chuyển", "vi": "quay, rẽ, chuyển"},
                    {"stt": 4, "zh": "正好", "pinyin": "zhènghǎo", "type": "phó/tính", "hanviet": "Chính hảo", "vi": "vừa đúng, vừa khéo"},
                    {"stt": 5, "zh": "熟悉", "pinyin": "shúxī", "type": "động", "hanviet": "Thục tất", "vi": "quen thuộc, thông thạo"},
                    {"stt": 6, "zh": "正", "pinyin": "zhèng", "type": "tính", "hanviet": "Chính", "vi": "ngay thẳng, chính"},
                    {"stt": 7, "zh": "目的地", "pinyin": "mùdìdì", "type": "danh", "hanviet": "Mục đích địa", "vi": "điểm đến"}
                ]
            }
        },
        {
            "type": "listening_abcd",
            "data": {
                "title": "Nghe và chọn đáp án đúng",
                "context_zh": "一天，陈天中从学校出来迷路了，就向一位同学问路。",
                "context_vi": "Một ngày nọ, Trần Thiên Trung đi ra từ trường học bị lạc đường, bèn hỏi đường một bạn học.",
                "lesson_num": "3",
                "level": "4",
                "audio_index": "1",
                "questions": [
                    {
                        "q_zh": "陈天中到十字路口后，应该怎么走？",
                        "options": ["A. 向前走", "B. 向右转", "C. 向左转", "D. 向南走"]
                    },
                    {
                        "q_zh": "为了找到目的地，同学建议陈天中：",
                        "options": ["A. 坐地铁", "B. 买张地图", "C. 用手机地图", "D. 问出租车司机"]
                    }
                ]
            }
        },
        {
            "type": "text_hsk3",
            "data": {
                "title": "课文\n1",
                "context_zh": "一天，陈天中从学校出来迷路了，就向一位同学问路。",
                "context_vi": "Một ngày nọ, Trần Thiên Trung đi ra từ trường học bị lạc đường, bèn hỏi đường một bạn học.",
                "lesson_num": "3",
                "level": "4",
                "audio_index": "1",
                "lines": [
                    {"speaker": "陈天中:", "text": "请问，花园小区怎么走？"},
                    {"speaker": "同学:", "text": "你往前走，到十字路口不要过马路，直接右转就到小区门口了。正好我也去那边，一起走吧。"},
                    {"speaker": "陈天中:", "text": "好的。我刚来中国，不熟悉路。北京真是太大了。"},
                    {"speaker": "同学:", "text": "北京大是大，不过这边的路基本上都是正南正北、正东正西的，很好找。你也可以用手机地图，很容易就能找到目的地。"},
                    {"speaker": "陈天中:", "text": "嗯，不过很多中文地名我还不认识。"},
                    {"speaker": "同学:", "text": "没关系，你很快就会熟悉的。"}
                ]
            }
        },
        {
            "type": "qa_slide",
            "data": {
                "title": "Đọc phân vai và trả lời câu hỏi",
                "questions": [
                    "陈天中为什么找不到花园小区了？",
                    "陈天中为什么没用手机地图？"
                ]
            }
        },
        {
            "type": "retell_hsk4",
            "data": {
                "title": "根据给出的提示复述课文",
                "text": "陈天中从学校出来，不知道怎么去________，就向一位同学问路。同学告诉他，先往前走，到十字路口________，直接右转就到________。正好同学________，就和他________。陈天中说________，还________。同学告诉他，北京的路基本上都是________，很好找。他也可以用________，很容易就能________。不过，很多________陈天中还________。同学说，他很快就会________。"
            }
        },
        {
            "type": "grammar",
            "data": {
                "title_vi": "1. Câu phức chuyển ngoặt “……×是×，就是/不过……”",
                "description_zh": "该复句里的“×是×”是固定格式，表示肯定某种情况或属性，后边用“就是、不过”等词语表示转折或补充说明，指出前一小句的内容有局限性。例如：",
                "formula": "A + 是 + A，就是/不过 + ……",
                "explanation_vi": "Trong câu phức này, “×是×” là cấu trúc cố định, biểu thị sự khẳng định một tình huống hoặc thuộc tính nào đó, phía sau dùng các từ như “就是, 不过” để biểu thị sự chuyển ngoặt hoặc bổ sung giải thích, chỉ ra nội dung của phân câu trước có tính hạn chế.",
                "examples": [
                    "(1) 北京大是大，不过这边的路基本上都是正南正北、正东正西的，很好找。",
                    "(2) 这个房子便宜是便宜，就是离我的公司太远了。",
                    "(3) 我们想是想了，就是没想出更好的办法。"
                ]
            }
        },
        {
            "type": "open_cloze",
            "data": {
                "title": "完成对话",
                "questions": [
                    "A: 你们那里凉快了吧？\nB: ______，不过夏天还没结束，过几天又会热起来了。",
                    "A: 网购真是太方便了！\nB: 方便是方便，______",
                    "A: 你们的作业写完了吗？\nB: ______"
                ]
            }
        },

        # ==================== BÀI KHÓA 2 ====================
        {
            "type": "title_slide",
            "data": {
                "title_zh": "课文 2",
                "lesson_number": "3",
                "bg_image": "assets/hinhnen.png",
                "show_number": False
            }
        },
        {
            "type": "vocabulary_table",
            "data": {
                "lesson_num": "3",
                "level": "4",
                "audio_index": "4",
                "words": [
                    {"stt": 8, "zh": "下载", "pinyin": "xiàzài", "type": "động", "hanviet": "Hạ tải", "vi": "tải xuống"},
                    {"stt": 9, "zh": "进行", "pinyin": "jìnxíng", "type": "động", "hanviet": "Tiến hành", "vi": "tiến hành"},
                    {"stt": 10, "zh": "支付", "pinyin": "zhīfù", "type": "động", "hanviet": "Chi phó", "vi": "thanh toán"},
                    {"stt": 11, "zh": "软件", "pinyin": "ruǎnjiàn", "type": "danh", "hanviet": "Nhuyễn kiện", "vi": "phần mềm"},
                    {"stt": 12, "zh": "不仅", "pinyin": "bùjǐn", "type": "liên", "hanviet": "Bất cẩn", "vi": "không những"},
                    {"stt": 13, "zh": "扫码", "pinyin": "sǎomǎ", "type": "động", "hanviet": "Tảo mã", "vi": "quét mã"},
                    {"stt": 14, "zh": "结账", "pinyin": "jiézhàng", "type": "động", "hanviet": "Kết trướng", "vi": "thanh toán, tính tiền"},
                    {"stt": 15, "zh": "购物", "pinyin": "gòuwù", "type": "động", "hanviet": "Cấu vật", "vi": "mua sắm"},
                    {"stt": 16, "zh": "订", "pinyin": "dìng", "type": "động", "hanviet": "Đính", "vi": "đặt, đặt mua"},
                    {"stt": 17, "zh": "快递", "pinyin": "kuàidì", "type": "danh", "hanviet": "Khoái đệ", "vi": "chuyển phát nhanh"}
                ]
            }
        },
        {
            "type": "vocabulary_table",
            "data": {
                "lesson_num": "3",
                "level": "4",
                "audio_index": "4",
                "words": [
                    {"stt": 18, "zh": "微信", "pinyin": "Wēixìn", "type": "danh từ riêng", "hanviet": "Vi Tín", "vi": "WeChat"},
                    {"stt": 19, "zh": "支付宝", "pinyin": "Zhīfùbǎo", "type": "danh từ riêng", "hanviet": "Chi phó bảo", "vi": "Alipay"}
                ]
            }
        },
        {
            "type": "listening_abcd",
            "data": {
                "title": "Nghe và chọn đáp án đúng",
                "context_zh": "中午下课后，白家月和陈天中在学校食堂相遇，两人边吃饭边聊天儿。",
                "context_vi": "Sau giờ học buổi trưa, Bạch Giai Nguyệt và Trần Thiên Trung gặp nhau ở căng tin trường, hai người vừa ăn vừa trò chuyện.",
                "lesson_num": "3",
                "level": "4",
                "audio_index": "3",
                "questions": [
                    {
                        "q_zh": "李文帮陈天中下载了什么软件？",
                        "options": ["A. 快递软件", "B. 网购软件", "C. 中国银行软件", "D. 微信和支付宝"]
                    },
                    {
                        "q_zh": "陈天中为什么着急回去？",
                        "options": ["A. 要上课了", "B. 李文找他", "C. 快递员快到了", "D. 网购的手机到了"]
                    }
                ]
            }
        },
        {
            "type": "text_hsk3",
            "data": {
                "title": "课文\n2",
                "context_zh": "中午下课后，白家月和陈天中在学校食堂相遇，两人边吃饭边聊天儿。",
                "context_vi": "Sau giờ học buổi trưa, Bạch Giai Nguyệt và Trần Thiên Trung gặp nhau ở căng tin trường, hai người vừa ăn vừa trò chuyện.",
                "lesson_num": "3",
                "level": "4",
                "audio_index": "3",
                "lines": [
                    {"speaker": "陈天中:", "text": "前两天和李文喝咖啡时，他帮我下载了微信和支付宝，教我认识里边的汉字，还教我用手机进行支付。"},
                    {"speaker": "白家月:", "text": "他也教了我怎么用这两个软件。"},
                    {"speaker": "陈天中:", "text": "现在我不仅会扫码结账，还会用手机在网上购物了。昨天我就在网上订了一台电脑，今天下午一点送到。"},
                    {"speaker": "白家月:", "text": "学会了这些，我们在中国生活真是方便了不少。"},
                    {"speaker": "陈天中:", "text": "对。快递员要到了，我得马上回去！家月，明天见！"},
                    {"speaker": "白家月:", "text": "好的，天中，再见。"}
                ]
            }
        },
        {
            "type": "qa_slide",
            "data": {
                "title": "Đọc phân vai và trả lời câu hỏi",
                "questions": [
                    "前几天李文帮陈天中做什么了？",
                    "陈天中现在会用手机做什么了？"
                ]
            }
        },
        {
            "type": "grammar",
            "data": {
                "title_vi": "2. Câu phức tiến bộ “不仅/不光……，还/而且……”",
                "description_zh": "“不仅/不光……，还/而且……”表示递进关系。后一分句是前一分句的延伸或补充，表示语意更进一步。本课学习的是由一个主语构成的复句，结构为：主语+不仅/不光……，还/而且……。例如：",
                "formula": "主语 + 不仅/不光 + ……，还/而且 + ……",
                "explanation_vi": "“不仅/不光……，还/而且……” biểu thị quan hệ tiến bộ. Phân câu sau là sự mở rộng hoặc bổ sung cho phân câu trước, biểu thị ý nghĩa tiến thêm một bước. Bài này học câu phức do một chủ ngữ cấu thành, cấu trúc là: Chủ ngữ + 不仅/不光……，还/而且…….",
                "examples": [
                    "(1) 现在我不仅会扫码结账，还会用手机在网上购物了。",
                    "(2) 王老师不光教我们说中文，而且带我们了解中国文化。",
                    "(3) 现在很多书店不仅卖书，还卖咖啡和奶茶。"
                ]
            }
        },
        {
            "type": "open_cloze",
            "data": {
                "title": "完成对话",
                "questions": [
                    "A: 她中文怎么说得这么好了？\nB: 她不仅每天认真听课，______",
                    "A: 你妹妹一年前就开始学唱中文歌，现在已经会唱了吧？\nB: 她______，而且唱得很好。",
                    "A: 你们都去看了这个电影，觉得怎么样？\nB: ______"
                ]
            }
        },

        # ==================== BÀI KHÓA 3 ====================
        {
            "type": "title_slide",
            "data": {
                "title_zh": "课文 3",
                "lesson_number": "3",
                "bg_image": "assets/hinhnen.png",
                "show_number": False
            }
        },
        {
            "type": "vocabulary_table",
            "data": {
                "lesson_num": "3",
                "level": "4",
                "audio_index": "6",
                "words": [
                    {"stt": 20, "zh": "现金", "pinyin": "xiànjīn", "type": "danh", "hanviet": "Hiện kim", "vi": "tiền mặt"},
                    {"stt": 21, "zh": "网购", "pinyin": "wǎnggòu", "type": "động", "hanviet": "Võng cấu", "vi": "mua sắm trực tuyến"},
                    {"stt": 22, "zh": "寄", "pinyin": "jì", "type": "động", "hanviet": "Ký", "vi": "gửi"},
                    {"stt": 23, "zh": "等", "pinyin": "děng", "type": "trợ", "hanviet": "Đẳng", "vi": "vân vân"},
                    {"stt": 24, "zh": "货", "pinyin": "huò", "type": "danh", "hanviet": "Hóa", "vi": "hàng hóa"},
                    {"stt": 25, "zh": "甚至", "pinyin": "shènzhì", "type": "liên", "hanviet": "Thậm chí", "vi": "thậm chí"},
                    {"stt": 26, "zh": "改变", "pinyin": "gǎibiàn", "type": "động", "hanviet": "Cải biến", "vi": "thay đổi"},
                    {"stt": 27, "zh": "手指", "pinyin": "shǒuzhǐ", "type": "danh", "hanviet": "Thủ chỉ", "vi": "ngón tay"},
                    {"stt": 28, "zh": "乱", "pinyin": "luàn", "type": "phó/tính", "hanviet": "Loạn", "vi": "bừa bãi, lung tung; tùy tiện"},
                    {"stt": 29, "zh": "管", "pinyin": "guǎn", "type": "động", "hanviet": "Quản", "vi": "quản lý, kiểm soát"}
                ]
            }
        },
        {
            "type": "listening_abcd",
            "data": {
                "title": "Nghe và chọn đáp án đúng",
                "context_zh": "生活新体验",
                "context_vi": "Trải nghiệm cuộc sống mới",
                "lesson_num": "3",
                "level": "4",
                "audio_index": "5",
                "questions": [
                    {
                        "q_zh": "白家月和陈天中发现中国人在饭馆吃饭有什么习惯？",
                        "options": ["A. 用现金结账", "B. 用手机支付", "C. 喜欢用筷子", "D. 吃完饭再结账"]
                    },
                    {
                        "q_zh": "根据课文，留学生网购时会担心什么？",
                        "options": ["A. 乱花钱", "B. 价格高", "C. 送货太慢", "D. 银行卡会丢"]
                    }
                ]
            }
        },
        {
            "type": "text_hsk3",
            "data": {
                "title": "课文\n3",
                "context_zh": "生活新体验",
                "context_vi": "Trải nghiệm cuộc sống mới",
                "lesson_num": "3",
                "level": "4",
                "audio_index": "5",
                "lines": [
                    {"speaker": "旁白:", "text": "白家月和陈天中刚到北京时就发现，中国人在饭馆或超市结账时，几乎都用手机支付，只有他们用现金结账。"},
                    {"speaker": "旁白:", "text": "在李文的帮助下，白家月和陈天中也都学会了用手机支付、网购、寄快递等等。在中国网购，不仅选择多、价格不高，而且送货很快，很多留学生甚至改变了自己的购物习惯。不过，由于网购太方便了，动动手指就能买到想要的东西，他们也开始担心自己在网购时会乱花钱。怎么才能管住自己不乱花钱呢？"}
                ]
            }
        },
        {
            "type": "xiaoyu_tip",
            "data": {
                "tips": "“等”也可以叠用，即“等等”.",
                "img_path": "assets/tip.png"
            }
        },
        {
            "type": "qa_slide",
            "data": {
                "title": "Đọc bài khóa và trả lời câu hỏi",
                "questions": [
                    "白家月和陈天中学会用手机做什么了？",
                    "留学生为什么也喜欢网购？"
                ]
            }
        },
        {
            "type": "retell_hsk4",
            "data": {
                "title": "根据给出的提示复述课文",
                "text": "白家月和陈天中________就发现，中国人在________结账时，几乎都________，只有他们________。后来，在________下，他们也都学会了________、网购、寄快递等等。在中国网购，不仅________、价格不高，而且________，很多留学生甚至改变了________。不过，由于网购________，动动手指就能________，他们也开始担心自己在网购时________。怎么才能________？"
            }
        },
        {
            "type": "grammar",
            "data": {
                "title_vi": "3. Liên từ “甚至”",
                "description_zh": "连词“甚至”强调某种情况更突出，超出常规预期。例如：",
                "formula": "甚至 + 突出情况/极端例子",
                "explanation_vi": "Liên từ “甚至” nhấn mạnh một tình huống nào đó nổi bật hơn, vượt quá dự kiến thông thường.",
                "examples": [
                    "(1) 在中国网购，不仅选择多、价格不高，而且送货很快，很多留学生甚至改变了自己的购物习惯。",
                    "(2) 高铁速度真快，甚至还没看清楚，它就已经开过去了。",
                    "(3) 这个小区真不错，有小花园、球场，甚至还有一个超市。"
                ]
            }
        },
        {
            "type": "open_cloze",
            "data": {
                "title": "完成句子",
                "questions": [
                    "______，上午寄出下午就收到了。（快递）",
                    "这家咖啡店很有名，______。（名人）",
                    "他太了解我了，______，他就知道我想做什么。（说话）"
                ]
            }
        },

        # ==================== BÀI KHÓA 4 ====================
        {
            "type": "title_slide",
            "data": {
                "title_zh": "课文 4",
                "lesson_number": "3",
                "bg_image": "assets/hinhnen.png",
                "show_number": False
            }
        },
        {
            "type": "vocabulary_table",
            "data": {
                "lesson_num": "3",
                "level": "4",
                "audio_index": "8",
                "words": [
                    {"stt": 30, "zh": "提供", "pinyin": "tígōng", "type": "động", "hanviet": "Đề cung", "vi": "cung cấp"},
                    {"stt": 31, "zh": "身份证", "pinyin": "shēnfènzhèng", "type": "danh", "hanviet": "Thân phận chứng", "vi": "chứng minh thư, thẻ căn cước"},
                    {"stt": 32, "zh": "个人", "pinyin": "gèrén", "type": "danh", "hanviet": "Cá nhân", "vi": "cá nhân"},
                    {"stt": 33, "zh": "能否", "pinyin": "néngfǒu", "type": "động", "hanviet": "Năng phủ", "vi": "có thể hay không"},
                    {"stt": 34, "zh": "保护", "pinyin": "bǎohù", "type": "động", "hanviet": "Bảo hộ", "vi": "bảo vệ"},
                    {"stt": 35, "zh": "于是", "pinyin": "yúshì", "type": "liên", "hanviet": "Ư thị", "vi": "thế là, vì vậy"},
                    {"stt": 36, "zh": "密码", "pinyin": "mìmǎ", "type": "danh", "hanviet": "Mật mã", "vi": "mật khẩu"},
                    {"stt": 37, "zh": "随便", "pinyin": "suíbiàn", "type": "tính/phó/liên", "hanviet": "Tùy tiện", "vi": "tùy tiện; tùy ý"},
                    {"stt": 38, "zh": "技术", "pinyin": "jìshù", "type": "danh", "hanviet": "Kỹ thuật", "vi": "kỹ thuật"},
                    {"stt": 39, "zh": "法律", "pinyin": "fǎlǜ", "type": "danh", "hanviet": "Pháp luật", "vi": "pháp luật"},
                    {"stt": 40, "zh": "手段", "pinyin": "shǒuduàn", "type": "danh", "hanviet": "Thủ đoạn", "vi": "thủ đoạn, phương thức"},
                    {"stt": 41, "zh": "保证", "pinyin": "bǎozhèng", "type": "động/danh", "hanviet": "Bảo chứng", "vi": "bảo đảm"},
                    {"stt": 42, "zh": "网络", "pinyin": "wǎngluò", "type": "danh", "hanviet": "Võng lạc", "vi": "mạng lưới, internet"}
                ]
            }
        },
        {
            "type": "listening_abcd",
            "data": {
                "title": "Đọc bài khóa và chọn đáp án đúng",
                "context_zh": "用手机时如何保护个人信息",
                "context_vi": "Làm thế nào để bảo vệ thông tin cá nhân khi sử dụng điện thoại di động.",
                "lesson_num": "3",
                "level": "4",
                "audio_index": "7",
                "questions": [
                    {
                        "q_zh": "网上购物或者订票时，经常需要提供哪些信息？",
                        "options": ["A. 身份证号", "B. 个人姓名", "C. 手机号码", "D. 以上都需要"]
                    },
                    {
                        "q_zh": "下列哪项不是课文中的建议？",
                        "options": ["A. 不发自己的车票信息", "B. 不随便告诉别人密码", "C. 不在咖啡馆收发邮件", "D. 不发自己的机票信息"]
                    }
                ]
            }
        },
        {
            "type": "text_hsk3",
            "data": {
                "title": "课文\n4",
                "context_zh": "用手机时如何保护个人信息",
                "context_vi": "Làm thế nào để bảo vệ thông tin cá nhân khi sử dụng điện thoại di động.",
                "lesson_num": "3",
                "level": "4",
                "audio_index": "7",
                "lines": [
                    {"speaker": "旁白:", "text": "网上购物或者订票时，我们经常需要提供姓名、手机号、身份证号等个人信息。在提供这些信息时，我们也会担心：我的个人信息能否得到保护？于是，有人在网上说出了自己的担心，很快就有人给出了一些建议。比如，别把密码随便告诉别人，不在网上发自己的车票、机票信息……"},
                    {"speaker": "旁白:", "text": "现在，很多国家也通过技术、法律等手段来保证个人信息安全。比如中国的网络安全法、个人信息保护法等就很好地保护了人们的个人信息。"}
                ]
            }
        },
        {
            "type": "qa_slide",
            "data": {
                "title": "Đọc bài khóa và trả lời câu hỏi",
                "questions": [
                    "人们为什么会担心个人信息安全问题？",
                    "国家会通过什么手段来保证个人信息安全？"
                ]
            }
        },
        {
            "type": "grammar",
            "data": {
                "title_vi": "4. Câu phức tiếp nối “……，于是……”",
                "description_zh": "两个分句按顺序描述连续动作或事件，“于是”用在后一分句的开头。两个分句之间存在先后关系，逻辑上有承接关系。例如：",
                "formula": "分句1 + ，于是 + 分句2",
                "explanation_vi": "Hai phân câu miêu tả hành động hoặc sự việc liên tiếp theo thứ tự, “于是” dùng ở đầu phân câu sau. Giữa hai phân câu có quan hệ trước sau, về mặt logic có quan hệ tiếp nối.",
                "examples": [
                    "(1) 在提供这些信息时，我们也会担心：我的个人信息能否得到保护？于是，有人在网上说出了自己的担心。",
                    "(2) 她从小就想要医生，于是上大学时就选择了学医。",
                    "(3) 最近总感冒，于是他决定病好后就开始锻炼身体。"
                ]
            }
        },
        {
            "type": "open_cloze",
            "data": {
                "title": "完成句子",
                "questions": [
                    "弟弟找到了一个新工作，但离家远，______",
                    "我昨天一天都在看书，很累，______",
                    "大家都不说话，______"
                ]
            }
        },

        # ==================== LUYỆN TẬP TỔNG HỢP ====================
        {
            "type": "title_slide",
            "data": {
                "title_zh": "综合练习",
                "lesson_number": "3",
                "bg_image": "assets/hinhnen.png",
                "show_number": False
            }
        },
        {
            "type": "fill_in_blanks",
            "data": {
                "title": "选词填空",
                "questions": [
                    "(1) 丽丽去快递站拿快递时，又______了一个快递。",
                    "(2) 从这儿走到十字路口，再向左______，就是超市了。",
                    "(3) 在十字路口等了半个小时，他们也没来，______我就一个人去图书馆了。",
                    "(4) 在商场购物的时候，我喜欢用信用卡______。",
                    "(5) 我们到电影院的时候，电影______开始了。"
                ],
                "options": ["A 结账", "B 于是", "C 转", "D 寄", "E 正好"]
            }
        },
        {
            "type": "fill_in_blanks",
            "data": {
                "title": "选词填空",
                "questions": [
                    "(6) A: 我用______结账可以吗？\nB: 当然，这些一共125块。",
                    "(7) A: 这个工作要求对网络______很了解，你可以吗？\nB: 没问题，我做这方面的工作已经有五年了。",
                    "(8) A: 你们能______这些货下午就送到吗？\nB: 您放心，我们有“闪送”服务，下午两点前就能送到。"
                ],
                "options": ["A 保证", "B 现金", "C 购物", "D 提供", "E 技术"]
            }
        },
        {
            "type": "fill_in_blanks",
            "data": {
                "title": "选词填空",
                "questions": [
                    "(9) A: 这个商场特别漂亮，在这里______很舒服。\nB: 是啊，周末过来走走、看看，累了还可以坐下来喝喝咖啡或者茶。",
                    "(10) A: 您好，办入住需要您______身份证和手机号后四位。\nB: 好的，这是我的身份证，手机号后四位是5063。"
                ],
                "options": ["A 保证", "B 现金", "C 购物", "D 提供", "E 技术"]
            }
        },
        {
            "type": "complete_passage_abcd",
            "data": {
                "title": "选择合适的内容完成短文",
                "context_text": "在中国，用手机支付、网购和寄快递都很方便，所以很多人觉得自己快要离不开手机了。________，还不会用中国人常用的手机App，她很着急。她的中国朋友知道后，________，教她怎么用，她很快就学会用手机支付和网购了。________，不到40分钟，外卖员就把饭送来了，________。现在，她几乎每天都用手机，点外卖或网购。",
                "options": [
                    "A. 马上给她提供帮助",
                    "B. 爱丽觉得太方便了",
                    "C. 第一次点外卖时",
                    "D. 爱丽刚来北京留学时"
                ]
            }
        },

        # ==================== MIÊU TẢ TRANH (HSK4) ====================
        {
            "type": "slide_describe_picture_hsk4",
            "data": {
                "title": "看图，用词语造句",
                "quyen": "4",
                "bai": "3",
                "items": [
                    {"word": "结账"},
                    {"word": "密码"},
                    {"word": "身份证"}
                ]
            }
        },

        # ==================== HOẠT ĐỘNG NHÓM ====================
        {
            "type": "class_activity_pair_work_2",
            "data": {
                "title": "小组辩论",
                "instruction": "Cả lớp chia thành hai nhóm, tranh luận với chủ đề “Điện thoại di động mang lại nhiều lợi ích hay nhiều vấn đề hơn”. Mỗi nhóm chuẩn bị quan điểm và lý do của mình trước, sau đó tiến hành tranh luận, bày tỏ quan điểm. Một bạn học chủ trì cuộc tranh luận và công bố kết quả.",
                "dialogue": "正方：手机带来的好处多，因为用手机可以购物，可以结账……\n反方：手机带来的问题多，因为手机上的信息太多，看多了，很浪费时间……"
            }
        },

        # ==================== VIẾT ====================
        {
            "type": "slide_writing_hsk4",
            "data": {
                "title": "写作",
                "instruction_zh": "生活中手机有很多用处。比如，在中国，可以用手机扫码支付，还可以点外卖、网购等。请写一篇短文，介绍一下你会用手机做什么，不少于120字。",
                "instruction_vi": "Trong cuộc sống, điện thoại di động có rất nhiều công dụng. Ví dụ, ở Trung Quốc, có thể dùng điện thoại quét mã thanh toán, còn có thể gọi đồ ăn ngoài, mua sắm trực tuyến, v.v. Hãy viết một đoạn văn ngắn giới thiệu bạn sẽ dùng điện thoại di động để làm gì, không ít hơn 120 chữ.",
                "image": "writting.png"
            }
        },

        # ==================== TỔNG KẾT ====================
        {
            "type": "summary",
            "data": {
                "title": "Tình hình học tập của tôi",
                "table_header": "Nội dung tự đánh giá",
                "row1_title_vi": "Có thể sử dụng các từ ngữ như “支付, 扫码, 结账, 订, 快递, 网购” trong bài để thảo luận về chủ đề thanh toán bằng điện thoại, mua sắm trực tuyến, v.v.",
                "row2_title_vi": "Có thể hiểu và vận dụng các điểm ngữ pháp như “……×是×，就是/不过……”, “不仅/不光……，还/而且……”, “甚至”, “……，于是……”.",
                "row3_title_vi": "Có thể bày tỏ suy nghĩ về cách bảo vệ thông tin cá nhân khi sử dụng điện thoại di động."
            }
        },

        # ==================== TRANG CẢM ƠN ====================
        {
            "type": "title_slide",
            "data": {
                "title_zh": "谢谢！",
                "lesson_number": "3",
                "bg_image": "assets/hinhnen.png",
                "show_number": False
            }
        }
    ]
}
# -*- coding: utf-8 -*-

lesson_data = {
    "lesson_title": "Bài 5: “不怕辣”和“怕不辣” (“Không sợ cay” và “Sợ không cay”)",
    "blocks": [
        # ==================== TRANG BÌA ====================
        {
            "type": "title_slide",
            "data": {
                "title_zh": "“不怕辣”和“怕不辣”",
                "lesson_number": "5",
                "bg_image": "assets/hinhnen.png",
                "show_number": True
            }
        },

        # ==================== MỤC TIÊU ====================
        {
            "type": "objectives",
            "data": {
                "items": [
                    {"zh": "能够听懂并交流饮食习惯和聚餐的话题。", "vi": "Có thể nghe hiểu và giao tiếp về chủ đề thói quen ăn uống và tụ tập ăn uống."},
                    {"zh": "能够口头或书面表达个人的饮食偏好和用餐体验。", "vi": "Có thể trình bày bằng lời nói hoặc văn bản sở thích ăn uống và trải nghiệm dùng bữa của cá nhân."},
                    {"zh": "了解中国人的饮食习惯和正式宴请中的座次礼仪。", "vi": "Hiểu biết về thói quen ăn uống của người Trung Quốc và nghi thức sắp xếp chỗ ngồi trong các bữa tiệc chính thức."}
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
                    {"zh": "辣子鸡", "pinyin": "Làzǐjī", "img": "assets/warmup_1.png", "answer": "A"},
                    {"zh": "红烧羊肉", "pinyin": "Hóngshāo Yángròu", "img": "assets/warmup_2.png", "answer": "B"},
                    {"zh": "松鼠鳜鱼", "pinyin": "Sōngshǔ Guìyú", "img": "assets/warmup_3.png", "answer": "C"},
                    {"zh": "酸汤米线", "pinyin": "Suāntāng Mǐxiàn", "img": "assets/warmup_4.png", "answer": "D"},
                    {"zh": "酸", "pinyin": "suān", "img": "assets/warmup_5.png", "answer": "E"},
                    {"zh": "甜", "pinyin": "tián", "img": "assets/warmup_6.png", "answer": "F"},
                    {"zh": "咸", "pinyin": "xián", "img": "assets/warmup_7.png", "answer": "G"},
                    {"zh": "辣", "pinyin": "là", "img": "assets/warmup_8.png", "answer": "H"}
                ]
            }
        },
        {
            "type": "qa_slide",
            "data": {
                "title": "Khởi động",
                "instruction": "Hai người một nhóm, dựa vào tình huống thực tế để hỏi đáp.",
                "questions": [
                    "你吃过哪些中国菜？觉得怎么样？",
                    "你喜欢什么味道的菜？"
                ]
            }
        },
        {
            "type": "xiaoyu_tip",
            "data": {
                "tips": "松鼠鳜鱼 là một trong những món ăn đại diện nổi tiếng của ẩm thực Tô Bang (Suzhou). Món này được làm từ cá quế (mandarin fish). Thành phẩm có hình dáng giống một con sóc lông xù, vị chua ngọt vừa phải, rất ngon miệng.",
                "img_path": "assets/tip.png"
            }
        },
        # ==================== BÀI KHÓA 1 ====================
        {
            "type": "title_slide",
            "data": {
                "title_zh": "课文 1",
                "lesson_number": "5",
                "bg_image": "assets/hinhnen.png",
                "show_number": False
            }
        },
        {
            "type": "vocabulary_table",
            "data": {
                "lesson_num": "5",
                "level": "4",
                "audio_index": "2",
                "words": [
                    {"stt": 1, "zh": "至少", "pinyin": "zhìshǎo", "type": "phó", "hanviet": "Chí thiểu", "vi": "ít nhất"},
                    {"stt": 2, "zh": "中餐", "pinyin": "zhōngcān", "type": "danh", "hanviet": "Trung xan", "vi": "món ăn Trung Quốc, cơm Trung"},
                    {"stt": 3, "zh": "专门", "pinyin": "zhuānmén", "type": "phó/tính", "hanviet": "Chuyên môn", "vi": "chuyên môn, đặc biệt"},
                    {"stt": 4, "zh": "煮", "pinyin": "zhǔ", "type": "động", "hanviet": "Chử", "vi": "luộc, nấu"},
                    {"stt": 5, "zh": "油", "pinyin": "yóu", "type": "danh", "hanviet": "Du", "vi": "dầu ăn"},
                    {"stt": 6, "zh": "道", "pinyin": "dào", "type": "lượng", "hanviet": "Đạo", "vi": "món (lượng từ đếm món ăn)"},
                    {"stt": 7, "zh": "熟", "pinyin": "shú/shóu", "type": "tính", "hanviet": "Thục", "vi": "chín; quen thuộc"},
                    {"stt": 8, "zh": "倒", "pinyin": "dào", "type": "động", "hanviet": "Đảo", "vi": "đổ, rót"},
                    {"stt": 9, "zh": "辣椒", "pinyin": "làjiāo", "type": "danh", "hanviet": "Lạt tiêu", "vi": "ớt"},
                    {"stt": 10, "zh": "辣", "pinyin": "là", "type": "tính", "hanviet": "Lạt", "vi": "cay"}
                ]
            }
        },
        {
            "type": "vocabulary_table",
            "data": {
                "lesson_num": "5",
                "level": "4",
                "audio_index": "2",
                "words": [
                    {"stt": 11, "zh": "水煮鱼", "pinyin": "Shuǐzhǔyú", "type": "danh từ riêng", "hanviet": "Thủy chử ngư", "vi": "Cá nấu nước (món Tứ Xuyên)"}
                ]
            }
        },
        {
            "type": "listening_abcd",
            "data": {
                "title": "Nghe và chọn đáp án đúng",
                "context_zh": "在刘明和王一雪家，夫妻两人请白家月和李文吃饭。",
                "context_vi": "Tại nhà Lưu Minh và Vương Nhất Tuyết, hai vợ chồng mời Bạch Giai Nguyệt và Lý Văn ăn cơm.",
                "lesson_num": "5",
                "level": "4",
                "audio_index": "1",
                "questions": [
                    {
                        "q_zh": "白家月来中国多久了？",
                        "options": ["A. 不到两个月", "B. 两个月", "C. 两个多月", "D. 两年多"]
                    },
                    {
                        "q_zh": "白家月觉得水煮鱼怎么样？",
                        "options": ["A. 不好吃", "B. 没做熟", "C. 不太辣", "D. 比较辣"]
                    }
                ]
            }
        },
        {
            "type": "text_hsk3",
            "data": {
                "title": "课文\n1",
                "context_zh": "在刘明和王一雪家，夫妻两人请白家月和李文吃饭。",
                "context_vi": "Tại nhà Lưu Minh và Vương Nhất Tuyết, hai vợ chồng mời Bạch Giai Nguyệt và Lý Văn ăn cơm.",
                "lesson_num": "5",
                "level": "4",
                "audio_index": "1",
                "lines": [
                    {"speaker": "刘明:", "text": "家月，你来中国至少两个月了，习惯吃中餐了吗？"},
                    {"speaker": "白家月:", "text": "习惯了，而且我很喜欢吃中国菜。"},
                    {"speaker": "王一雪:", "text": "你还没吃过水煮鱼吧？这是我专门为你做的。"},
                    {"speaker": "白家月:", "text": "看起来不像水煮鱼，更像“油煮鱼”。"},
                    {"speaker": "王一雪:", "text": "这道菜是先用水把鱼煮熟，最后再倒上辣椒油，其实只有最上面那一层是油。你尝尝，对你来说辣不辣？"},
                    {"speaker": "白家月:", "text": "辣是辣，但是非常好吃！"},
                    {"speaker": "王一雪:", "text": "那你多吃点儿，不要客气。"}
                ]
            }
        },
        {
            "type": "xiaoyu_tip",
            "data": {
                "tips": "“熟”字有两个发音：口语里常读作“shóu”，比如“菜熟了”；在书面语和双音节词中常读作“shú”，比如“熟悉”。",
                "img_path": "assets/tip.png"
            }
        },
        {
            "type": "qa_slide",
            "data": {
                "title": "Đọc phân vai và trả lời câu hỏi",
                "questions": [
                    "白家月习惯吃中餐了吗？",
                    "水煮鱼是怎么做的？"
                ]
            }
        },
        {
            "type": "retell_hsk4",
            "data": {
                "title": "根据给出的提示复述课文",
                "text": "白家月________，她习惯________，而且________。王一雪让她尝尝________。白家月觉得这道菜看起来________，更________。王一雪告诉她，这道菜是先________，最后再________，其实只有________。白家月尝了以后，觉得________，不过________。王一雪让她________，不要________。"
            }
        },
        {
            "type": "grammar",
            "data": {
                "title_vi": "1. Phó từ phạm vi “至少”",
                "description_zh": "范围副词“至少”表示时间、数量、程度等不低于某个最低限度。例如：",
                "formula": "至少 + 数量/时间/程度",
                "explanation_vi": "Phó từ phạm vi “至少” biểu thị thời gian, số lượng, mức độ... không thấp hơn một giới hạn tối thiểu nào đó.",
                "examples": [
                    "(1) 家月，你来中国至少两个月了，习惯吃中餐了吗？",
                    "(2) 每年至少有两百名留学生来我校学习中文专业。",
                    "(3) 我们虽然没有见过面，但至少在网上聊过很多次，也算比较熟悉了。"
                ]
            }
        },
        {
            "type": "open_cloze",
            "data": {
                "title": "完成对话",
                "questions": [
                    "A: 这个房子是不是有点儿旧？\nB: 旧是旧，不过______",
                    "A: 老师，我刚入学，不知道应该选几门课。\nB: 研究生一年级的时候，______",
                    "A: 你现在怎么不坐公交车，每天骑电动车了？\nB: 骑电动车______，我早上就不用太早出发了。"
                ]
            }
        },

        # ==================== BÀI KHÓA 2 ====================
        {
            "type": "title_slide",
            "data": {
                "title_zh": "课文 2",
                "lesson_number": "5",
                "bg_image": "assets/hinhnen.png",
                "show_number": False
            }
        },
        {
            "type": "vocabulary_table",
            "data": {
                "lesson_num": "5",
                "level": "4",
                "audio_index": "4",
                "words": [
                    {"stt": 12, "zh": "敢", "pinyin": "gǎn", "type": "động", "hanviet": "Cảm", "vi": "dám"},
                    {"stt": 13, "zh": "肚子", "pinyin": "dùzi", "type": "danh", "hanviet": "Đỗ tử", "vi": "bụng"},
                    {"stt": 14, "zh": "相同", "pinyin": "xiāngtóng", "type": "tính", "hanviet": "Tương đồng", "vi": "giống nhau"},
                    {"stt": 15, "zh": "顺序", "pinyin": "shùnxù", "type": "danh", "hanviet": "Thuận tự", "vi": "thứ tự"},
                    {"stt": 16, "zh": "够", "pinyin": "gòu", "type": "phó/động", "hanviet": "Cấu", "vi": "đủ; rất, thật là"},
                    {"stt": 17, "zh": "不够", "pinyin": "búgòu", "type": "phó/động", "hanviet": "Bất cấu", "vi": "không đủ"},
                    {"stt": 18, "zh": "达到", "pinyin": "dádào", "type": "động", "hanviet": "Đạt đáo", "vi": "đạt tới"}
                ]
            }
        },
        {
            "type": "listening_abcd",
            "data": {
                "title": "Nghe và chọn đáp án đúng",
                "context_zh": "在刘明和王一雪家，夫妻两人和白家月、李文边吃边聊。",
                "context_vi": "Tại nhà Lưu Minh và Vương Nhất Tuyết, hai vợ chồng và Bạch Giai Nguyệt, Lý Văn vừa ăn vừa trò chuyện.",
                "lesson_num": "5",
                "level": "4",
                "audio_index": "3",
                "questions": [
                    {
                        "q_zh": "关于王一雪一家，可以知道什么？",
                        "options": ["A. 现在不吃辣", "B. 现在能吃辣", "C. 以前敢吃辣", "D. 以前爱吃辣"]
                    },
                    {
                        "q_zh": "白家月现在的口味是什么？",
                        "options": ["A. 不吃辣", "B. 爱吃辣", "C. 不怕辣", "D. 怕不辣"]
                    }
                ]
            }
        },
        {
            "type": "text_hsk3",
            "data": {
                "title": "课文\n2",
                "context_zh": "在刘明和王一雪家，夫妻两人和白家月、李文边吃边聊。",
                "context_vi": "Tại nhà Lưu Minh và Vương Nhất Tuyết, hai vợ chồng và Bạch Giai Nguyệt, Lý Văn vừa ăn vừa trò chuyện.",
                "lesson_num": "5",
                "level": "4",
                "audio_index": "3",
                "lines": [
                    {"speaker": "王一雪:", "text": "我听李文说，你现在也爱吃辣了？"},
                    {"speaker": "白家月:", "text": "是的，来中国以后，我越来越喜欢吃辣了。"},
                    {"speaker": "王一雪:", "text": "我们以前不太敢吃辣，吃完可能会肚子不舒服，不过现在也慢慢适应了。"},
                    {"speaker": "刘明:", "text": "对，我们现在都不怕辣了。家月，你是“不怕辣”还是“怕不辣”？"},
                    {"speaker": "白家月:", "text": "中文真有意思，相同的字，顺序一换，意思就变了。"},
                    {"speaker": "李文:", "text": "你的中文水平够高的，这都听懂了！你说得对，“不怕辣”是说不怕吃辣的菜，“怕不辣”是担心菜还不够辣呢。"},
                    {"speaker": "白家月:", "text": "我还达不到“怕不辣”的水平，甚至也不能算“不怕辣”，只是喜欢吃辣。"}
                ]
            }
        },
        {
            "type": "qa_slide",
            "data": {
                "title": "Đọc phân vai và trả lời câu hỏi",
                "questions": [
                    "王一雪一家以前敢不敢吃辣？为什么？",
                    "“不怕辣”“怕不辣”都是什么意思？"
                ]
            }
        },
        {
            "type": "grammar",
            "data": {
                "title_vi": "2. Phó từ / Động từ “够” (Phần 1: Phó từ)",
                "description_zh": "“够”作副词，表示程度高，常用在固定格式“够……的”中。例如：",
                "formula": "够 + 形容词 + 的",
                "explanation_vi": "“够” làm phó từ, biểu thị mức độ cao, thường dùng trong cấu trúc cố định “够……的”.",
                "examples": [
                    "(1) 你的中文水平够高的，这都听懂了！"
                ]
            }
        },
        {
            "type": "grammar",
            "data": {
                "title_vi": "2. Phó từ / Động từ “够” (Phần 2: Động từ)",
                "description_zh": "“够”作动词，表示数量上满足需要或者达到某个标准或程度。例如：",
                "formula": "够 + 名词/数量 (hoặc 够 + 动词)",
                "explanation_vi": "“够” làm động từ, biểu thị về mặt số lượng đáp ứng nhu cầu hoặc đạt tới một tiêu chuẩn hay mức độ nào đó.",
                "examples": [
                    "(1) 明天请家月和李文来家里吃饭，四个菜够不够？",
                    "(2) 我尝了一下，还不够甜，再加一点儿糖吧。"
                ]
            }
        },
        {
            "type": "open_cloze",
            "data": {
                "title": "完成对话",
                "questions": [
                    "A: 这个箱子______，放不下这么多东西。\nB: 那我再看看有没有别的箱子。",
                    "A: 你家房子______，不仅有上下两层，还有一个小花园。\nB: 我买房的时候就想着要能住下一家五口人。",
                    "A: 完成这个工作需要三天，现在只有两天，时间______\nB: 那我再去跟经理说一下。"
                ]
            }
        },

        # ==================== BÀI KHÓA 3 ====================
        {
            "type": "title_slide",
            "data": {
                "title_zh": "课文 3",
                "lesson_number": "5",
                "bg_image": "assets/hinhnen.png",
                "show_number": False
            }
        },
        {
            "type": "vocabulary_table",
            "data": {
                "lesson_num": "5",
                "level": "4",
                "audio_index": "6",
                "words": [
                    {"stt": 19, "zh": "聚", "pinyin": "jù", "type": "động", "hanviet": "Tụ", "vi": "tụ tập"},
                    {"stt": 20, "zh": "午餐", "pinyin": "wǔcān", "type": "danh", "hanviet": "Ngọ xan", "vi": "bữa trưa"},
                    {"stt": 21, "zh": "咸", "pinyin": "xián", "type": "tính", "hanviet": "Hàm", "vi": "mặn"},
                    {"stt": 22, "zh": "凉", "pinyin": "liáng", "type": "tính", "hanviet": "Lương", "vi": "mát, nguội, lạnh"},
                    {"stt": 23, "zh": "酸", "pinyin": "suān", "type": "tính", "hanviet": "Toan", "vi": "chua"},
                    {"stt": 24, "zh": "汤", "pinyin": "tāng", "type": "danh", "hanviet": "Thang", "vi": "canh, súp"},
                    {"stt": 25, "zh": "各", "pinyin": "gè", "type": "phó/đại", "hanviet": "Các", "vi": "mỗi, các"},
                    {"stt": 26, "zh": "付", "pinyin": "fù", "type": "động", "hanviet": "Phó", "vi": "trả (tiền)"},
                    {"stt": 27, "zh": "聚餐", "pinyin": "jùcān", "type": "động", "hanviet": "Tụ xan", "vi": "ăn cơm tụ tập"}
                ]
            }
        },
        {
            "type": "vocabulary_table",
            "data": {
                "lesson_num": "5",
                "level": "4",
                "audio_index": "6",
                "words": [
                    {"stt": 28, "zh": "辣子鸡", "pinyin": "Làzǐjī", "type": "danh từ riêng", "hanviet": "Lạt tử kê", "vi": "Gà cay Tứ Xuyên"},
                    {"stt": 29, "zh": "松鼠鳜鱼", "pinyin": "Sōngshǔ Guìyú", "type": "danh từ riêng", "hanviet": "Tùng thử quế ngư", "vi": "Cá quế sóc"},
                    {"stt": 30, "zh": "红烧羊肉", "pinyin": "Hóngshāo Yángròu", "type": "danh từ riêng", "hanviet": "Hồng thiêu dương nhục", "vi": "Thịt cừu kho tàu"},
                    {"stt": 31, "zh": "贵州", "pinyin": "Guìzhōu", "type": "danh từ riêng", "hanviet": "Quý Châu", "vi": "Quý Châu (tỉnh)"},
                    {"stt": 32, "zh": "酸汤米线", "pinyin": "Suāntāng Mǐxiàn", "type": "danh từ riêng", "hanviet": "Toan thang mễ tuyến", "vi": "Bún canh chua"}
                ]
            }
        },
        {
            "type": "listening_abcd",
            "data": {
                "title": "Nghe và chọn đáp án đúng",
                "context_zh": "在餐厅里，白家月、陈天中、李文和安妮聚餐。",
                "context_vi": "Tại nhà hàng, Bạch Giai Nguyệt, Trần Thiên Trung, Lý Văn và Annie tụ tập ăn trưa.",
                "lesson_num": "5",
                "level": "4",
                "audio_index": "5",
                "questions": [
                    {
                        "q_zh": "陈天中点了什么菜？",
                        "options": ["A. 辣子鸡", "B. 松鼠鳜鱼", "C. 红烧羊肉", "D. 酸汤米线"]
                    },
                    {
                        "q_zh": "李文喜欢吃什么口味的菜？",
                        "options": ["A. 辣的", "B. 甜的", "C. 咸的", "D. 酸的"]
                    }
                ]
            }
        },
        {
            "type": "text_hsk3",
            "data": {
                "title": "课文\n3",
                "context_zh": "在餐厅里，白家月、陈天中、李文和安妮聚餐。",
                "context_vi": "Tại nhà hàng, Bạch Giai Nguyệt, Trần Thiên Trung, Lý Văn và Annie tụ tập ăn trưa.",
                "lesson_num": "5",
                "level": "4",
                "audio_index": "5",
                "lines": [
                    {"speaker": "旁白:", "text": "周末，白家月、陈天中、李文和安妮聚在一起吃午餐。白家月想吃辣的，要了辣子鸡；陈天中爱吃甜的，想尝尝松鼠鳜鱼；李文更喜欢吃咸的，选了红烧羊肉和一道凉菜；安妮听说贵州酸汤很有名，点了酸汤米线。他们边吃边聊，非常愉快。"},
                    {"speaker": "旁白:", "text": "结账时，李文想请客，但大家觉得还是各付各的更合适。于是，李文付完钱后，大家把钱转给了他，还笑着说下次再一起聚餐。"}
                ]
            }
        },
        {
            "type": "xiaoyu_tip",
            "data": {
                "tips": "“转”还可以表示把一方的物品、意见等传到另一方。这里的意思是用手机转账。",
                "img_path": "assets/tip.png"
            }
        },
        {
            "type": "qa_slide",
            "data": {
                "title": "Đọc bài khóa và trả lời câu hỏi",
                "questions": [
                    "白家月点了什么菜？为什么？",
                    "他们是怎么结账的？"
                ]
            }
        },
        {
            "type": "retell_hsk4",
            "data": {
                "title": "根据给出的提示复述课文",
                "text": "周末，白家月、陈天中、李文和安妮________吃午餐。白家月________，要了辣子鸡；陈天中________，想尝尝松鼠鳜鱼；李文更喜欢________，选了红烧羊肉和________；安妮听说贵州酸汤________，点了酸汤米线。他们________，非常愉快。结账时，李文________，但大家觉得还是________更合适。于是，李文________，大家________，还笑着说________。"
            }
        },
        {
            "type": "grammar",
            "data": {
                "title_vi": "3. Cấu trúc cố định “各x各的”",
                "description_zh": "固定格式“各x各的”表示每个人独立进行同一类动作，互不影响。例如：",
                "formula": "各 + 动词 + 各的",
                "explanation_vi": "Cấu trúc cố định “各x各的” biểu thị mỗi người độc lập tiến hành cùng một loại hành động, không ảnh hưởng lẫn nhau.",
                "examples": [
                    "(1) 大家觉得还是各付各的更合适。",
                    "(2) 到了办公室，大家就开始各忙各的了。",
                    "(3) 在图书馆里，大家都很安静，各看各的书。"
                ]
            }
        },
        {
            "type": "open_cloze",
            "data": {
                "title": "完成句子",
                "questions": [
                    "他们想买的东西不一样，到了商场以后就______",
                    "他们虽然住在一起，但是口味不同，______",
                    "老师说完作业怎么做以后，大家就______，不再说话了。"
                ]
            }
        },

        # ==================== BÀI KHÓA 4 ====================
        {
            "type": "title_slide",
            "data": {
                "title_zh": "课文 4",
                "lesson_number": "5",
                "bg_image": "assets/hinhnen.png",
                "show_number": False
            }
        },
        {
            "type": "vocabulary_table",
            "data": {
                "lesson_num": "5",
                "level": "4",
                "audio_index": "8",
                "words": [
                    {"stt": 33, "zh": "随意", "pinyin": "suíyì", "type": "tính", "hanviet": "Tùy ý", "vi": "tùy ý, thoải mái"},
                    {"stt": 34, "zh": "正式", "pinyin": "zhèngshì", "type": "tính", "hanviet": "Chính thức", "vi": "chính thức"},
                    {"stt": 35, "zh": "普通", "pinyin": "pǔtōng", "type": "tính", "hanviet": "Phổ thông", "vi": "bình thường, phổ thông"},
                    {"stt": 36, "zh": "重视", "pinyin": "zhòngshì", "type": "động", "hanviet": "Trọng thị", "vi": "coi trọng"},
                    {"stt": 37, "zh": "座位", "pinyin": "zuòwèi", "type": "danh", "hanviet": "Tọa vị", "vi": "chỗ ngồi"},
                    {"stt": 38, "zh": "安排", "pinyin": "ānpái", "type": "động", "hanviet": "An bài", "vi": "sắp xếp"},
                    {"stt": 39, "zh": "按照", "pinyin": "ànzhào", "type": "giới", "hanviet": "Án chiếu", "vi": "dựa theo, theo"},
                    {"stt": 40, "zh": "年龄", "pinyin": "niánlíng", "type": "danh", "hanviet": "Niên linh", "vi": "tuổi tác"},
                    {"stt": 41, "zh": "面对", "pinyin": "miànduì", "type": "động", "hanviet": "Diện đối", "vi": "đối mặt, hướng về"},
                    {"stt": 42, "zh": "主人", "pinyin": "zhǔrén", "type": "danh", "hanviet": "Chủ nhân", "vi": "chủ nhà, chủ tiệc"},
                    {"stt": 43, "zh": "等", "pinyin": "děng", "type": "giới", "hanviet": "Đẳng", "vi": "đợi đến khi"},
                    {"stt": 44, "zh": "尊重", "pinyin": "zūnzhòng", "type": "động", "hanviet": "Tôn trọng", "vi": "tôn trọng"}
                ]
            }
        },
        {
            "type": "listening_abcd",
            "data": {
                "title": "Đọc bài khóa và chọn đáp án đúng",
                "context_zh": "中国餐桌上的座位安排",
                "context_vi": "Cách sắp xếp chỗ ngồi trên bàn ăn của người Trung Quốc.",
                "lesson_num": "5",
                "level": "4",
                "audio_index": "7",
                "questions": [
                    {
                        "q_zh": "一般来说，什么人会坐面对门口的座位？",
                        "options": ["A. 主人", "B. 主人的家人", "C. 年龄小的客人", "D. 年龄大的客人"]
                    },
                    {
                        "q_zh": "一般来说，正式聚餐时，谁先坐下？",
                        "options": ["A. 主人", "B. 老人", "C. 小孩子", "D. 年轻人"]
                    }
                ]
            }
        },
        {
            "type": "text_hsk3",
            "data": {
                "title": "课文\n4",
                "context_zh": "中国餐桌上的座位安排",
                "context_vi": "Cách sắp xếp chỗ ngồi trên bàn ăn của người Trung Quốc.",
                "lesson_num": "5",
                "level": "4",
                "audio_index": "7",
                "lines": [
                    {"speaker": "旁白:", "text": "今天吃饭的时候，大家坐得比较随意。李文告诉白家月，在中国，正式聚餐和普通聚餐不同，正式聚餐时人们比较重视座位的安排，比如可以按照年龄大小来安排，年龄比较大的客人往往会坐在中间或者面对门口的座位。大家坐下时，主人会请客人先坐。如果聚餐时有老人，年轻人要等老人坐下后再坐。"},
                    {"speaker": "旁白:", "text": "白家月听后觉得很有意思，她认为这么做是照顾客人、尊重老人的表现。"}
                ]
            }
        },
        {
            "type": "qa_slide",
            "data": {
                "title": "Đọc bài khóa và trả lời câu hỏi",
                "questions": [
                    "正式聚餐时，可以怎么安排座位？",
                    "白家月怎么看这种座位安排方式？"
                ]
            }
        },
        {
            "type": "grammar",
            "data": {
                "title_vi": "4. Giới từ “等”",
                "description_zh": "本课中“等”是介词，表示“等到”，用于引出时间、条件。例如：",
                "formula": "等 + 动作/时间 + (再) + 动词",
                "explanation_vi": "Trong bài này, “等” là giới từ, có nghĩa là “đợi đến khi”, dùng để đưa ra thời gian, điều kiện.",
                "examples": [
                    "(1) 如果聚餐时有老人，年轻人要等老人坐下后再坐。",
                    "(2) 等我写完作业，再跟你出去玩。",
                    "(3) 等我们到火车站的时候，火车已经开走了。"
                ]
            }
        },
        {
            "type": "open_cloze",
            "data": {
                "title": "完成句子",
                "questions": [
                    "别着急，______就去找你。",
                    "______，你就能先花钱再还钱了。",
                    "______，走路十分钟就到公司了。"
                ]
            }
        },

        # ==================== LUYỆN TẬP TỔNG HỢP ====================
        {
            "type": "title_slide",
            "data": {
                "title_zh": "综合练习",
                "lesson_number": "5",
                "bg_image": "assets/hinhnen.png",
                "show_number": False
            }
        },
        {
            "type": "fill_in_blanks",
            "data": {
                "title": "选词填空",
                "questions": [
                    "(1) 家里没______了，你去超市买一瓶吧。",
                    "(2) 这道菜看起来太辣了，我不______吃。",
                    "(3) 我______有点儿不舒服，想休息一下。",
                    "(4) 已经煮了十多分钟了，饺子______了吧？",
                    "(5) 这是我______为你准备的礼物，希望你喜欢。"
                ],
                "options": ["A 熟", "B 敢", "C 油", "D 专门", "E 肚子"]
            }
        },
        {
            "type": "fill_in_blanks",
            "data": {
                "title": "选词填空",
                "questions": [
                    "(6) A: 请问，这个______有人吗？\nB: 没有人，您坐吧。",
                    "(7) A: 你尝尝，这道菜是不是做得太______了？\nB: 嗯，是的，我跟服务员说一下。",
                    "(8) A: 你们怎么还不吃？一会儿菜都______了。\nB: 我们在等你呢，一起吃更热闹。"
                ],
                "options": ["A 凉", "B 咸", "C 付", "D 重视", "E 座位"]
            }
        },
        {
            "type": "fill_in_blanks",
            "data": {
                "title": "选词填空",
                "questions": [
                    "(9) A: 我发现早上出来跑步的人变多了。\nB: 是啊，因为人们越来越______身体健康了。",
                    "(10) A: 这是我去超市帮你带的东西。\nB: 谢谢！多少钱？我把钱______给你。"
                ],
                "options": ["A 凉", "B 咸", "C 付", "D 重视", "E 座位"]
            }
        },
        {
            "type": "complete_passage_abcd",
            "data": {
                "title": "选择合适的内容完成短文",
                "context_text": "周末，白家月请大家一起吃饭，________。点菜时，白家月让大家想吃什么就点什么，并说自己很喜欢这家饭店的菜，味道特别好。王一雪建议每个人先点一个自己喜欢的菜，________。王一雪要了一个汤，李文选了一道凉菜，________。白家月最后点了一道肉菜。________，边吃边聊，非常开心。",
                "options": [
                    "A. 不够再加",
                    "B. 刘明和两个孩子也各点了一道菜",
                    "C. 大家聚在一起",
                    "D. 感谢他们这段时间对自己的照顾"
                ]
            }
        },

        # ==================== MIÊU TẢ TRANH (HSK4) ====================
        {
            "type": "slide_describe_picture_hsk4",
            "data": {
                "title": "看图，用词语造句",
                "quyen": "4",
                "bai": "5",
                "items": [
                    {"word": "午餐"},
                    {"word": "辣"},
                    {"word": "汤"}
                ]
            }
        },

        # ==================== HOẠT ĐỘNG NHÓM ====================
        {
            "type": "class_activity_pair_work_2",
            "data": {
                "title": "角色扮演",
                "instruction": "Bạn mời những người bạn Trung Quốc đến nhà làm khách, vừa ăn vừa trò chuyện về văn hóa ẩm thực của mỗi quốc gia, bao gồm các loại món ăn và khẩu vị, cảm nhận khi dùng bữa, phép tắc trên bàn ăn, v.v.",
                "dialogue": "A: 今天请你们来我家吃饭，尝尝我们国家的菜。\nB: 太好了，这些菜看起来真好吃！"
            }
        },

        # ==================== VIẾT ====================
        {
            "type": "slide_writing_hsk4",
            "data": {
                "title": "写作",
                "instruction_zh": "校园美食节就要到了。为了让大家更好地了解你们国家的饮食文化，请根据上面谈论的内容，写一篇短文进行介绍，不少于120字。",
                "instruction_vi": "Lễ hội ẩm thực của trường sắp đến. Để mọi người hiểu rõ hơn về văn hóa ẩm thực của đất nước bạn, vui lòng viết một đoạn văn ngắn giới thiệu dựa trên nội dung đã thảo luận ở trên, không ít hơn 120 chữ.",
                "image": "writting.png"
            }
        },

        # ==================== TỔNG KẾT ====================
        {
            "type": "summary",
            "data": {
                "title": "Tình hình học tập của tôi",
                "table_header": "Nội dung tự đánh giá",
                "row1_title_vi": "Có thể sử dụng các từ ngữ như “油, 熟, 辣, 咸, 凉, 酸, 汤” trong bài để thảo luận về chủ đề ăn uống.",
                "row2_title_vi": "Có thể hiểu và vận dụng các điểm ngữ pháp như “至少”, “够”, “各x各的”, “等”.",
                "row3_title_vi": "Có thể thảo luận về chủ đề thói quen ăn uống và tụ tập ăn uống.",
                "row4_title_vi": "Có thể bày tỏ sở thích ăn uống và trải nghiệm dùng bữa của cá nhân."
            }
        },

        # ==================== TRANG CẢM ƠN ====================
        {
            "type": "title_slide",
            "data": {
                "title_zh": "谢谢！",
                "lesson_number": "5",
                "bg_image": "assets/hinhnen.png",
                "show_number": False
            }
        }
    ]
}
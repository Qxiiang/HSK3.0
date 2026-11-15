# -*- coding: utf-8 -*-

lesson_data = {
    "lesson_title": "Bài 6: 我陪你去看病 (Tôi đi cùng bạn đến khám bệnh)",
    "quyen": "4",
    "phan": "a",
    "bai": "6",
    "blocks": [
        # ==================== TRANG BÌA ====================
        {
            "type": "title_slide",
            "data": {
                "title_zh": "我陪你去看病",
                "lesson_number": "6",
                "bg_image": "assets/hinhnen.png",
                "show_number": True
            }
        },

        # ==================== MỤC TIÊU ====================
        {
            "type": "objectives",
            "data": {
                "items": [
                    {"zh": "能够听懂并交流身体状况和治疗方案等信息。", "vi": "Có thể nghe hiểu và giao tiếp về các thông tin như tình trạng sức khỏe và phương án điều trị."},
                    {"zh": "能够口头或书面表达就医过程。", "vi": "Có thể trình bày quá trình đi khám bệnh bằng lời nói hoặc văn bản."},
                    {"zh": "了解在中国看病的基本流程。", "vi": "Hiểu biết về quy trình cơ bản khi đi khám bệnh tại Trung Quốc."}
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
                    {"zh": "护士", "pinyin": "hùshi", "img": "assets/warmup_1.png", "answer": "A"},
                    {"zh": "大厅", "pinyin": "dàtīng", "img": "assets/warmup_2.png", "answer": "B"},
                    {"zh": "汗", "pinyin": "hàn", "img": "assets/warmup_3.png", "answer": "C"},
                    {"zh": "醒", "pinyin": "xǐng", "img": "assets/warmup_4.png", "answer": "D"},
                    {"zh": "打针", "pinyin": "dǎzhēn", "img": "assets/warmup_5.png", "answer": "E"},
                    {"zh": "咳嗽", "pinyin": "késòu", "img": "assets/warmup_6.png", "answer": "F"}
                ]
            }
        },
        {
            "type": "qa_slide",
            "data": {
                "title": "Khởi động",
                "instruction": "Hai người một nhóm, dựa vào tình huống thực tế để hỏi đáp.",
                "questions": [
                    "你在中国生过病吗？生病后，你是怎么做的？",
                    "你在中国的医院看过病吗？看病的过程中有没有遇到什么问题？"
                ]
            }
        },

        # ==================== BÀI KHÓA 1 ====================
        {
            "type": "title_slide",
            "data": {
                "title_zh": "课文 1",
                "lesson_number": "6",
                "bg_image": "assets/hinhnen.png",
                "show_number": False
            }
        },
        {
            "type": "vocabulary_table",
            "data": {
                "lesson_num": "6",
                "level": "4",
                "audio_index": "2",
                "words": [
                    {"stt": 1, "zh": "咳嗽", "pinyin": "késòu", "type": "động", "hanviet": "Khái thấu", "vi": "ho"},
                    {"stt": 2, "zh": "咳", "pinyin": "ké", "type": "động", "hanviet": "Khái", "vi": "ho (ho khan)"},
                    {"stt": 3, "zh": "厉害", "pinyin": "lìhai", "type": "tính", "hanviet": "Lợi hại", "vi": "dữ dội, nghiêm trọng, ghê gớm"},
                    {"stt": 4, "zh": "严重", "pinyin": "yánzhòng", "type": "tính", "hanviet": "Nghiêm trọng", "vi": "nghiêm trọng"},
                    {"stt": 5, "zh": "赶快", "pinyin": "gǎnkuài", "type": "phó", "hanviet": "Cản khoái", "vi": "mau lên, nhanh lên"},
                    {"stt": 6, "zh": "陪", "pinyin": "péi", "type": "động", "hanviet": "Bồi", "vi": "đi cùng, tháp tùng"},
                    {"stt": 7, "zh": "翻译", "pinyin": "fānyì", "type": "động/danh", "hanviet": "Phiên dịch", "vi": "phiên dịch, biên dịch; phiên dịch viên"}
                ]
            }
        },
        {
            "type": "listening_abcd",
            "data": {
                "title": "Nghe và chọn đáp án đúng",
                "context_zh": "在家里，白家月躺在床上给李文打电话。",
                "context_vi": "Tại nhà, Bạch Giai Nguyệt nằm trên giường gọi điện cho Lý Văn.",
                "lesson_num": "6",
                "level": "4",
                "audio_index": "1",
                "questions": [
                    {
                        "q_zh": "李文让白家月做什么？",
                        "options": ["A. 在家休息", "B. 陪他去医院", "C. 去医院检查", "D. 给他当翻译"]
                    },
                    {
                        "q_zh": "白家月担心什么？",
                        "options": ["A. 不知道吃什么药", "B. 不知道怎么看病", "C. 不知道哪家医院好", "D. 身体越来越不舒服"]
                    }
                ]
            }
        },
        {
            "type": "text_hsk3",
            "data": {
                "title": "课文\n1",
                "context_zh": "在家里，白家月躺在床上给李文打电话。",
                "context_vi": "Tại nhà, Bạch Giai Nguyệt nằm trên giường gọi điện cho Lý Văn.",
                "lesson_num": "6",
                "level": "4",
                "audio_index": "1",
                "lines": [
                    {"speaker": "白家月:", "text": "喂，李文，我身体不舒服。"},
                    {"speaker": "李文:", "text": "你怎么了？听你的声音，好像感冒了。"},
                    {"speaker": "白家月:", "text": "对，我还发烧，一直咳嗽，咳得很厉害。"},
                    {"speaker": "李文:", "text": "那挺严重的，最好赶快去医院检查一下。"},
                    {"speaker": "白家月:", "text": "我也这么想，不过我来中国后还没去过医院，不知道怎么在中国的医院看病。"},
                    {"speaker": "李文:", "text": "没关系，我陪你一起去，还能帮你翻译。你在家等一下，我现在就去接你。"},
                    {"speaker": "白家月:", "text": "太好了！有你陪着，我就放心多了。"}
                ]
            }
        },
        {
            "type": "qa_slide",
            "data": {
                "title": "Đọc phân vai và trả lời câu hỏi",
                "questions": [
                    "白家月怎么了？",
                    "李文为什么要陪白家月去医院？"
                ]
            }
        },
        {
            "type": "retell_hsk4",
            "data": {
                "title": "根据给出的提示复述课文",
                "text": "白家月给李文打电话，告诉他自己________，发烧，一直________，还________。李文觉得她病得________，建议她________。不过，白家月来中国后________，不知道________。李文让她在家________，说马上去________，________去医院，还能帮她________。白家月觉得，有________，她就________。"
            }
        },
        {
            "type": "grammar",
            "data": {
                "title_vi": "1. Tính từ “厉害”",
                "description_zh": "形容词“厉害”可以放在动词或形容词的后面，表示程度很高，结构是“动词+得+（副词）+厉害”“形容词+得+厉害”。例如：",
                "formula": "Động từ/Tính từ + 得 + (Phó từ) + 厉害",
                "explanation_vi": "Tính từ “厉害” có thể đặt sau động từ hoặc tính từ, biểu thị mức độ rất cao. Cấu trúc là “Động từ + 得 + (Phó từ) + 厉害” hoặc “Tính từ + 得 + 厉害”.",
                "examples": [
                    "(1) 我还发烧，一直咳嗽，咳得很厉害。",
                    "(2) 我昨天跑步跑多了，今天腿疼得厉害。",
                    "(3) 这道菜辣得厉害，我吃了一口就不敢再吃了。"
                ]
            }
        },
        {
            "type": "open_cloze",
            "data": {
                "title": "完成对话",
                "questions": [
                    "A: 外面刮风了，咱们是现在走还是过一会儿再走？\nB: 我看________，咱们等会儿再走吧。",
                    "A: 我已经咳嗽好几天了，今天还有点儿发烧。\nB: 我看你________，快去医院看看吧。",
                    "A: 你怎么了？哪儿不舒服吗？\nB: 我刚吃完冰激凌，现在________。"
                ]
            }
        },

        # ==================== BÀI KHÓA 2 ====================
        {
            "type": "title_slide",
            "data": {
                "title_zh": "课文 2",
                "lesson_number": "6",
                "bg_image": "assets/hinhnen.png",
                "show_number": False
            }
        },
        {
            "type": "vocabulary_table",
            "data": {
                "lesson_num": "6",
                "level": "4",
                "audio_index": "4",
                "words": [
                    {"stt": 8, "zh": "护士", "pinyin": "hùshi", "type": "danh", "hanviet": "Hộ sĩ", "vi": "y tá"},
                    {"stt": 9, "zh": "表", "pinyin": "biǎo", "type": "danh", "hanviet": "Biểu", "vi": "bảng, biểu mẫu"},
                    {"stt": 10, "zh": "性别", "pinyin": "xìngbié", "type": "danh", "hanviet": "Tính biệt", "vi": "giới tính"},
                    {"stt": 11, "zh": "国籍", "pinyin": "guójí", "type": "danh", "hanviet": "Quốc tịch", "vi": "quốc tịch"},
                    {"stt": 12, "zh": "家庭", "pinyin": "jiātíng", "type": "danh", "hanviet": "Gia đình", "vi": "gia đình"},
                    {"stt": 13, "zh": "地址", "pinyin": "dìzhǐ", "type": "danh", "hanviet": "Địa chỉ", "vi": "địa chỉ"},
                    {"stt": 14, "zh": "挂号", "pinyin": "guàhào", "type": "động", "hanviet": "Quải hiệu", "vi": "đăng ký khám bệnh"},
                    {"stt": 15, "zh": "排队", "pinyin": "páiduì", "type": "động", "hanviet": "Bài đội", "vi": "xếp hàng"},
                    {"stt": 16, "zh": "大厅", "pinyin": "dàtīng", "type": "danh", "hanviet": "Đại sảnh", "vi": "sảnh lớn"}
                ]
            }
        },
        {
            "type": "listening_abcd",
            "data": {
                "title": "Nghe và chọn đáp án đúng",
                "context_zh": "在医院大厅，李文帮白家月办理看病手续。",
                "context_vi": "Tại sảnh bệnh viện, Lý Văn giúp Bạch Giai Nguyệt làm thủ tục khám bệnh.",
                "lesson_num": "6",
                "level": "4",
                "audio_index": "3",
                "questions": [
                    {
                        "q_zh": "护士让李文做什么？",
                        "options": ["A. 排队等医生", "B. 在大厅休息", "C. 把护照交给她", "D. 在表上写病人的信息"]
                    },
                    {
                        "q_zh": "李文要去做什么？",
                        "options": ["A. 挂号", "B. 买药", "C. 办护照", "D. 找医生"]
                    }
                ]
            }
        },
        {
            "type": "text_hsk3",
            "data": {
                "title": "课文\n2",
                "context_zh": "在医院大厅，李文帮白家月办理看病手续。",
                "context_vi": "Tại sảnh bệnh viện, Lý Văn giúp Bạch Giai Nguyệt làm thủ tục khám bệnh.",
                "lesson_num": "6",
                "level": "4",
                "audio_index": "3",
                "lines": [
                    {"speaker": "李文:", "text": "护士，您好，我的这位外国朋友生病了，第一次来这里看病，需要怎么做？"},
                    {"speaker": "护士:", "text": "请在这张表上写上病人的姓名、性别、国籍、年龄、电话号码和家庭地址。"},
                    {"speaker": "李文:", "text": "我写好了，您看看，这样可以吗？"},
                    {"speaker": "护士:", "text": "没问题，您拿着病人的护照去挂号吧。"},
                    {"speaker": "李文:", "text": "家月，我去排队挂号，你先在大厅休息，别着急。"},
                    {"speaker": "白家月:", "text": "好的，真是太谢谢你了！"},
                    {"speaker": "李文:", "text": "你跟我有什么好客气的。"}
                ]
            }
        },
        {
            "type": "qa_slide",
            "data": {
                "title": "Đọc phân vai và trả lời câu hỏi",
                "questions": [
                    "李文要在表上写什么？",
                    "李文让白家月做什么？"
                ]
            }
        },
        {
            "type": "grammar",
            "data": {
                "title_vi": "2. Cấu trúc cố định “（没）有什么（好）x的”",
                "description_zh": "固定格式“（没）有什么（好）x的”表示没有必要做某件事或者有某种感受或状态。例如：",
                "formula": "(没)有什么(好) + Động từ + 的",
                "explanation_vi": "Cấu trúc cố định “（没）有什么（好）x的” biểu thị không cần thiết phải làm việc gì đó hoặc có cảm giác/trạng thái nào đó.",
                "examples": [
                    "(1) 你跟我有什么好客气的。",
                    "(2) 这种事在网上有很多，没有什么奇怪的。",
                    "(3) 我觉得这家商场里的东西都很一般，没有什么好买的。"
                ]
            }
        },
        {
            "type": "open_cloze",
            "data": {
                "title": "完成对话",
                "questions": [
                    "A: 你怎么这么快就打扫完房间了？\nB: 前天刚打扫过，还很干净，________",
                    "A: 你的病严重吗？我特别担心。\nB: 放心吧，我得的只是小感冒，________",
                    "A: 你敢一个人看这个电影吗？我陪你一起看吧。\nB: 谢谢你，________"
                ]
            }
        },

        # ==================== BÀI KHÓA 3 ====================
        {
            "type": "title_slide",
            "data": {
                "title_zh": "课文 3",
                "lesson_number": "6",
                "bg_image": "assets/hinhnen.png",
                "show_number": False
            }
        },
        {
            "type": "vocabulary_table",
            "data": {
                "lesson_num": "6",
                "level": "4",
                "audio_index": "6",
                "words": [
                    {"stt": 17, "zh": "偶尔", "pinyin": "ǒu'ěr", "type": "phó/tính", "hanviet": "Ngẫu nhĩ", "vi": "thỉnh thoảng, đôi khi"},
                    {"stt": 18, "zh": "身", "pinyin": "shēn", "type": "danh/lượng", "hanviet": "Thân", "vi": "thân thể, người"},
                    {"stt": 19, "zh": "结果", "pinyin": "jiéguǒ", "type": "danh/liên", "hanviet": "Kết quả", "vi": "kết quả; kết quả là"},
                    {"stt": 20, "zh": "性", "pinyin": "xìng", "type": "hậu tố", "hanviet": "Tính", "vi": "tính (hậu tố tạo tính từ)"},
                    {"stt": 21, "zh": "体温", "pinyin": "tǐwēn", "type": "danh", "hanviet": "Thể ôn", "vi": "nhiệt độ cơ thể"},
                    {"stt": 22, "zh": "降", "pinyin": "jiàng", "type": "động", "hanviet": "Giáng", "vi": "giảm, hạ"},
                    {"stt": 23, "zh": "光", "pinyin": "guāng", "type": "phó", "hanviet": "Quang", "vi": "chỉ, không (phó từ)"},
                    {"stt": 24, "zh": "打针", "pinyin": "dǎzhēn", "type": "động", "hanviet": "Đả châm", "vi": "tiêm"},
                    {"stt": 25, "zh": "有效", "pinyin": "yǒuxiào", "type": "tính", "hanviet": "Hữu hiệu", "vi": "hiệu quả"},
                    {"stt": 26, "zh": "按时", "pinyin": "ànshí", "type": "phó", "hanviet": "Án thời", "vi": "đúng giờ"},
                    {"stt": 27, "zh": "汗", "pinyin": "hàn", "type": "danh", "hanviet": "Hãn", "vi": "mồ hôi"},
                    {"stt": 28, "zh": "醒", "pinyin": "xǐng", "type": "động", "hanviet": "Tỉnh", "vi": "tỉnh dậy"},
                    {"stt": 29, "zh": "感觉", "pinyin": "gǎnjué", "type": "động/danh", "hanviet": "Cảm giác", "vi": "cảm thấy; cảm giác"},
                    {"stt": 30, "zh": "低", "pinyin": "dī", "type": "tính", "hanviet": "Đê", "vi": "thấp"},
                    {"stt": 31, "zh": "难受", "pinyin": "nánshòu", "type": "tính", "hanviet": "Nan thụ", "vi": "khó chịu"}
                ]
            }
        },
        {
            "type": "listening_abcd",
            "data": {
                "title": "Nghe và chọn đáp án đúng",
                "context_zh": "一次看病的经历",
                "context_vi": "Một lần đi khám bệnh.",
                "lesson_num": "6",
                "level": "4",
                "audio_index": "5",
                "questions": [
                    {
                        "q_zh": "白家月告诉医生什么了？",
                        "options": ["A. 她总出汗", "B. 她吃过药了", "C. 她体温很低", "D. 她一直头疼"]
                    },
                    {
                        "q_zh": "第二天，白家月怎么样了？",
                        "options": ["A. 头更疼了", "B. 更不舒服了", "C. 体温变高了", "D. 不那么难受了"]
                    }
                ]
            }
        },
        {
            "type": "text_hsk3",
            "data": {
                "title": "课文\n3",
                "context_zh": "一次看病的经历",
                "context_vi": "Một lần đi khám bệnh.",
                "lesson_num": "6",
                "level": "4",
                "audio_index": "5",
                "lines": [
                    {"speaker": "旁白:", "text": "下午白家月去看病了，她告诉医生，自己平时身体不错，偶尔才会生一次病。这次她病得很厉害，头也一直疼，身上一点儿力气都没有。医生给她做了检查，检查结果出来后，发现她得了比较严重的流行性感冒。"},
                    {"speaker": "旁白:", "text": "医生告诉她，现在需要把体温降下来，光吃药恐怕不够，打针会更有效。医生还让她回家以后按时吃药，多喝水，多休息。"},
                    {"speaker": "旁白:", "text": "晚上，白家月睡觉时出了一身汗。第二天醒来时，她感觉头不那么疼了，体温也低了一些，身体不那么难受了。"}
                ]
            }
        },
        {
            "type": "qa_slide",
            "data": {
                "title": "Đọc bài khóa và trả lời câu hỏi",
                "questions": [
                    "白家月得了什么病？",
                    "医生让白家月做什么？"
                ]
            }
        },
        {
            "type": "retell_hsk4",
            "data": {
                "title": "根据给出的提示复述课文",
                "text": "下午白家月去看病了，她告诉医生，自己________，偶尔________。这次她________，头也________，身上________。医生给她________，检查结果________，发现她得了________。医生建议她________，因为那样________。医生还让她回家以后________，多________，多________。晚上，白家月睡觉时________。第二天醒来时，她感觉头________，体温________，身体________。"
            }
        },
        {
            "type": "grammar",
            "data": {
                "title_vi": "3. Phó từ tần suất “偶尔”",
                "description_zh": "频率副词“偶尔”表示动作或情况发生的次数很少。例如：",
                "formula": "偶尔 + Động từ/Cụm động từ",
                "explanation_vi": "Phó từ tần suất “偶尔” biểu thị số lần hành động hoặc tình huống xảy ra rất ít.",
                "examples": [
                    "(1) 她告诉医生，自己平时身体不错，偶尔才会生一次病。",
                    "(2) 他经常在家看电影，偶尔才去电影院看。",
                    "(3) 我一般都在学校食堂吃饭，偶尔会跟朋友一起出去吃。"
                ]
            }
        },
        {
            "type": "open_cloze",
            "data": {
                "title": "完成句子",
                "questions": [
                    "我一般坐公交车，________来学校。（自行车）",
                    "我喜欢吃辣的菜，不过________。（甜）",
                    "我一般在网上买东西，________。（商场）"
                ]
            }
        },

        # ==================== BÀI KHÓA 4 ====================
        {
            "type": "title_slide",
            "data": {
                "title_zh": "课文 4",
                "lesson_number": "6",
                "bg_image": "assets/hinhnen.png",
                "show_number": False
            }
        },
        {
            "type": "vocabulary_table",
            "data": {
                "lesson_num": "6",
                "level": "4",
                "audio_index": "8",
                "words": [
                    {"stt": 32, "zh": "通", "pinyin": "tōng", "type": "động", "hanviet": "Thông", "vi": "hiểu, thông"},
                    {"stt": 33, "zh": "过程", "pinyin": "guòchéng", "type": "danh", "hanviet": "Quá trình", "vi": "quá trình"},
                    {"stt": 34, "zh": "部", "pinyin": "bù", "type": "danh", "hanviet": "Bộ", "vi": "bộ phận, khoa"},
                    {"stt": 35, "zh": "收费", "pinyin": "shōufèi", "type": "động", "hanviet": "Thu phí", "vi": "thu phí"},
                    {"stt": 36, "zh": "情况", "pinyin": "qíngkuàng", "type": "danh", "hanviet": "Tình huống", "vi": "tình hình, tình trạng"},
                    {"stt": 37, "zh": "好", "pinyin": "hǎo", "type": "động", "hanviet": "Hảo", "vi": "để (mục đích)"},
                    {"stt": 38, "zh": "治疗", "pinyin": "zhìliáo", "type": "động", "hanviet": "Trị liệu", "vi": "điều trị"},
                    {"stt": 39, "zh": "步", "pinyin": "bù", "type": "danh", "hanviet": "Bộ", "vi": "bước"}
                ]
            }
        },
        {
            "type": "listening_abcd",
            "data": {
                "title": "Đọc bài khóa và chọn đáp án đúng",
                "context_zh": "怎么在中国看病",
                "context_vi": "Làm thế nào để khám bệnh tại Trung Quốc.",
                "lesson_num": "6",
                "level": "4",
                "audio_index": "7",
                "questions": [
                    {
                        "q_zh": "关于国际部里的医生，下列哪项正确？",
                        "options": ["A. 更专业", "B. 是外国医生", "C. 年龄比较大", "D. 一般会说英文"]
                    },
                    {
                        "q_zh": "根据课文，在中国看病，怎么做能顺利得到治疗？",
                        "options": ["A. 找一个翻译", "B. 去国际部看病", "C. 按照医生说的做", "D. 跟中国朋友一起去"]
                    }
                ]
            }
        },
        {
            "type": "text_hsk3",
            "data": {
                "title": "课文\n4",
                "context_zh": "怎么在中国看病",
                "context_vi": "Làm thế nào để khám bệnh tại Trung Quốc.",
                "lesson_num": "6",
                "level": "4",
                "audio_index": "7",
                "lines": [
                    {"speaker": "旁白:", "text": "外国人第一次在中国看病，可能会担心语言不通，或者觉得看病的过程和自己的国家不同。其实，这些问题都有办法解决。"},
                    {"speaker": "旁白:", "text": "有的医院有国际部，那里的医生一般会说英文，交流比较方便，但是国际部的收费比较高。如果没有特别需要，可以选择普通部，用简单的中文和医生交流。"},
                    {"speaker": "旁白:", "text": "在中国看病要先挂号，然后再去找医生。医生会问病人的情况，有时还会做一些检查，好给出合适的治疗方法。只要按照医生说的一步一步来，一般都可以顺利得到治疗。"}
                ]
            }
        },
        {
            "type": "qa_slide",
            "data": {
                "title": "Đọc bài khóa và trả lời câu hỏi",
                "questions": [
                    "外国人第一次在中国看病，可能会担心什么问题？",
                    "在中国的医院，看病的过程是怎样的？"
                ]
            }
        },
        {
            "type": "grammar",
            "data": {
                "title_vi": "4. Câu mục đích “……，好……”",
                "description_zh": "前一分句说明某个动作或情况，后一分句说明其目的。例如：",
                "formula": "Hành động/Tình huống, 好 + Mục đích",
                "explanation_vi": "Mệnh đề trước giải thích một hành động hoặc tình huống, mệnh đề sau giải thích mục đích của nó.",
                "examples": [
                    "(1) 医生有时还会做一些检查，好给出合适的治疗方法。",
                    "(2) 你们先了解一下情况，好做出决定。",
                    "(3) 我把电话号码告诉你，以后有什么事好联系我。"
                ]
            }
        },
        {
            "type": "open_cloze",
            "data": {
                "title": "完成句子",
                "questions": [
                    "我每天都给家人打电话，________。",
                    "你要早点儿准备好材料，________。",
                    "我今天就把工作做完，明天________。"
                ]
            }
        },

        # ==================== LUYỆN TẬP TỔNG HỢP ====================
        {
            "type": "title_slide",
            "data": {
                "title_zh": "综合练习",
                "lesson_number": "6",
                "bg_image": "assets/hinhnen.png",
                "show_number": False
            }
        },
        {
            "type": "fill_in_blanks",
            "data": {
                "title": "选词填空",
                "questions": [
                    "(1) 咱们过去问问______，看牙应该去几楼。",
                    "(2) 我这两天有点儿______，不知道是不是感冒了。",
                    "(3) 把你的______给我吧，我给你寄点儿东西。",
                    "(4) 这个问题很______，我们必须马上想办法解决。",
                    "(5) 你都发烧好几天了，______去医院检查一下吧。"
                ],
                "options": ["A 地址", "B 咳嗽", "C 赶快", "D 护士", "E 严重"]
            }
        },
        {
            "type": "fill_in_blanks",
            "data": {
                "title": "选词填空",
                "questions": [
                    "(6) A: 这道菜是怎么做的？\nB: 下次我把做菜的______拍下来发给你。",
                    "(7) A: 你今天怎么这么饿？\nB: 白天太忙了，______喝了点儿水，一口饭都没吃。",
                    "(8) A: 经理叫你过去，要了解一下最近的工作______。\nB: 好的，我现在就去他的办公室。"
                ],
                "options": ["A 光", "B 醒", "C 有效", "D 过程", "E 情况"]
            }
        },
        {
            "type": "fill_in_blanks",
            "data": {
                "title": "选词填空",
                "questions": [
                    "(9) A: 我早上给你打电话，你怎么没接啊？\nB: 昨天睡得太晚了，今天10点才______。",
                    "(10) A: 你觉得看电影学中文怎么样？\nB: 我觉得这种方法很______，不但能学语言，还能了解中国文化。"
                ],
                "options": ["A 光", "B 醒", "C 有效", "D 过程", "E 情况"]
            }
        },
        {
            "type": "complete_passage_abcd",
            "data": {
                "title": "选择合适的内容完成短文",
                "context_text": "________，最好赶快去医院看看。第一次在中国的医院看病，可以先问护士应该怎么做。一般来说，顺序是先挂号，然后去找医生看病。要是怕听不懂医生说的话，可以找个中国朋友陪你一起去医院，________。看病时，医生会先问你哪儿不舒服，然后给你做一些检查。________，医生会给出治疗的方法。按照医生说的做，________，多休息，病就会好得更快。",
                "options": [
                    "A. 按时吃药",
                    "B. 帮你翻译",
                    "C. 如果感觉身体不舒服",
                    "D. 检查结果出来以后"
                ]
            }
        },

        # ==================== MIÊU TẢ TRANH (HSK4) ====================
        {
            "type": "describe_picture_hsk4",
            "data": {
                "title": "看图，用词语造句",
                "quyen": "4",
                "bai": "6",
                "items": [
                    {"word": "排队"},
                    {"word": "体温"},
                    {"word": "难受"}
                ]
            }
        },

        # ==================== HOẠT ĐỘNG NHÓM ====================
        # ==================== HOẠT ĐỘNG NHÓM ====================
        # ==================== HOẠT ĐỘNG NHÓM ====================
        {
            "type": "class_activity_pair_work_2", # Không có bảng -> dùng class_activity
            "data": {
                "title": "小组讨论 (Thảo luận nhóm)",
                "instruction": "四人一组，讨论各自国家的医疗情况，比如医疗体系、看病流程以及常见病的处理方式等，并向全班简单介绍讨论结果。 (Chia thành nhóm 4 người, thảo luận về tình hình y tế của mỗi quốc gia, ví dụ như hệ thống y tế, quy trình khám bệnh và cách xử lý các bệnh thông thường, sau đó giới thiệu tóm tắt kết quả thảo luận trước lớp.)",
                "dialogue": "A: 在你们国家，看病需要先挂号吗？\nB: 是的，一般需要先预约或者挂号。"
            }
        },
        # ==================== VIẾT ====================
        {
            "type": "writing_hsk4",
            "data": {
                "title": "写作",
                "instruction_zh": "你的一个中国朋友正在你的国家旅行。他/她最近生病了，给你发微信，询问如何在医院看病。请你根据上面讨论的内容，给他/她写回复，不少于120字。",
                "instruction_vi": "Một người bạn Trung Quốc của bạn đang du lịch tại đất nước bạn. Gần đây bạn ấy bị ốm và gửi tin nhắn WeChat hỏi bạn cách đi khám bệnh tại bệnh viện. Vui lòng viết thư trả lời dựa trên nội dung đã thảo luận ở trên, không ít hơn 120 chữ.",
                "image": "writting.png"
            }
        },

        # ==================== TỔNG KẾT ====================
        {
            "type": "summary",
            "data": {
                "title": "Tình hình học tập của tôi",
                "table_header": "Nội dung tự đánh giá",
                "row1_title_vi": "Có thể sử dụng các từ ngữ như “严重, 结果, 体温, 打针, 感觉, 情况” trong bài để thảo luận về chủ đề y tế.",
                "row2_title_vi": "Có thể hiểu và vận dụng các điểm ngữ pháp như “厉害”, “（没）有什么（好）x的”, “偶尔”, “……，好……”.",
                "row3_title_vi": "Có thể giao tiếp về chủ đề tình trạng sức khỏe và điều trị bệnh.",
                "row4_title_vi": "Có thể trình bày quá trình đi khám bệnh của cá nhân."
            }
        },

        # ==================== TRANG CẢM ƠN ====================
        {
            "type": "title_slide",
            "data": {
                "title_zh": "谢谢！",
                "lesson_number": "6",
                "bg_image": "assets/hinhnen.png",
                "show_number": False
            }
        }
    ]
}
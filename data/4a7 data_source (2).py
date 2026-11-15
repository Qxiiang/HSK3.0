# -*- coding: utf-8 -*-

lesson_data = {
    "lesson_title": "Bài 7: 在工作中学习 (Học hỏi trong công việc)",
    "quyen": "4",
    "phan": "a",
    "bai": "7",
    "blocks": [
        # ==================== TRANG BÌA ====================
        {
            "type": "title_slide",
            "data": {
                "title_zh": "在工作中学习",
                "lesson_number": "7",
                "bg_image": "assets/hinhnen.png",
                "show_number": True
            }
        },

        # ==================== MỤC TIÊU ====================
        {
            "type": "objectives",
            "data": {
                "items": [
                    {"zh": "能够听懂并交流工作任务和安排等内容。", "vi": "Có thể nghe hiểu và giao tiếp về các nội dung như nhiệm vụ và sắp xếp công việc."},
                    {"zh": "能够口头或书面表达工作经验和职业发展建议。", "vi": "Có thể trình bày bằng lời nói hoặc văn bản kinh nghiệm làm việc và lời khuyên phát triển nghề nghiệp."},
                    {"zh": "了解职场中重视学习和积累经验的做法。", "vi": "Hiểu biết về cách làm coi trọng việc học hỏi và tích lũy kinh nghiệm trong môi trường công sở."}
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
                    {"zh": "市场", "pinyin": "shìchǎng", "img": "assets/warmup_1.png", "answer": "A"},
                    {"zh": "想法", "pinyin": "xiǎngfǎ", "img": "assets/warmup_2.png", "answer": "B"},
                    {"zh": "打扰", "pinyin": "dǎrǎo", "img": "assets/warmup_3.png", "answer": "C"},
                    {"zh": "谈", "pinyin": "tán", "img": "assets/warmup_4.png", "answer": "D"},
                    {"zh": "计划", "pinyin": "jìhuà", "img": "assets/warmup_5.png", "answer": "E"},
                    {"zh": "出差", "pinyin": "chūchāi", "img": "assets/warmup_6.png", "answer": "F"}
                ]
            }
        },
        {
            "type": "qa_slide",
            "data": {
                "title": "Khởi động",
                "instruction": "Hai người một nhóm, dựa vào tình huống thực tế để hỏi đáp.",
                "questions": [
                    "你最想做什么工作？为什么？",
                    "你觉得刚开始工作时，要注意什么？"
                ]
            }
        },

        # ==================== BÀI KHÓA 1 ====================
        {
            "type": "title_slide",
            "data": {
                "title_zh": "课文 1",
                "lesson_number": "7",
                "bg_image": "assets/hinhnen.png",
                "show_number": False
            }
        },
        {
            "type": "vocabulary_table",
            "data": {
                "lesson_num": "7",
                "level": "4",
                "audio_index": "2",
                "words": [
                    {"stt": 1, "zh": "打扰", "pinyin": "dǎrǎo", "type": "động", "hanviet": "Đả nhiễu", "vi": "làm phiền, quấy rầy"},
                    {"stt": 2, "zh": "市场", "pinyin": "shìchǎng", "type": "danh", "hanviet": "Thị trường", "vi": "thị trường"},
                    {"stt": 3, "zh": "调查", "pinyin": "diàochá", "type": "động", "hanviet": "Điều tra", "vi": "điều tra, khảo sát"},
                    {"stt": 4, "zh": "计划", "pinyin": "jìhuà", "type": "danh/động", "hanviet": "Kế hoạch", "vi": "kế hoạch; lên kế hoạch"},
                    {"stt": 5, "zh": "内容", "pinyin": "nèiróng", "type": "danh", "hanviet": "Nội dung", "vi": "nội dung"},
                    {"stt": 6, "zh": "改", "pinyin": "gǎi", "type": "động", "hanviet": "Cải", "vi": "sửa, thay đổi"},
                    {"stt": 7, "zh": "细心", "pinyin": "xìxīn", "type": "tính", "hanviet": "Tế tâm", "vi": "tỉ mỉ, cẩn thận"},
                    {"stt": 8, "zh": "客户", "pinyin": "kèhù", "type": "danh", "hanviet": "Khách hộ", "vi": "khách hàng"},
                    {"stt": 9, "zh": "真正", "pinyin": "zhēnzhèng", "type": "tính/phó", "hanviet": "Chân chính", "vi": "chân chính, thực sự"},
                    {"stt": 10, "zh": "想法", "pinyin": "xiǎngfǎ", "type": "danh", "hanviet": "Tưởng pháp", "vi": "ý nghĩ, suy nghĩ"},
                    {"stt": 11, "zh": "任务", "pinyin": "rènwù", "type": "danh", "hanviet": "Nhiệm vụ", "vi": "nhiệm vụ"},
                    {"stt": 12, "zh": "及时", "pinyin": "jíshí", "type": "phó/tính", "hanviet": "Cập thời", "vi": "kịp thời"}
                ]
            }
        },
        {
            "type": "listening_abcd",
            "data": {
                "title": "Nghe và chọn đáp án đúng",
                "context_zh": "在王一雪办公室，同事向她汇报工作。",
                "context_vi": "Tại văn phòng của Vương Nhất Tuyết, đồng nghiệp báo cáo công việc với cô ấy.",
                "lesson_num": "7",
                "level": "4",
                "audio_index": "1",
                "questions": [
                    {
                        "q_zh": "同事把什么发到王一雪的邮箱了？",
                        "options": ["A. 网店的名字", "B. 客户的信息", "C. 要买的东西", "D. 调查的计划"]
                    },
                    {
                        "q_zh": "除了超市，同事还打算在哪儿进行调查？",
                        "options": ["A. 网店", "B. 大学", "C. 菜市场", "D. 国际公司"]
                    }
                ]
            }
        },
        {
            "type": "text_hsk3",
            "data": {
                "title": "课文\n1",
                "context_zh": "在王一雪办公室，同事向她汇报工作。",
                "context_vi": "Tại văn phòng của Vương Nhất Tuyết, đồng nghiệp báo cáo công việc với cô ấy.",
                "lesson_num": "7",
                "level": "4",
                "audio_index": "1",
                "lines": [
                    {"speaker": "同事:", "text": "经理，打扰您一下。市场调查的计划书我昨天发到您邮箱了。在内容方面，您觉得有需要改的吗？"},
                    {"speaker": "王一雪:", "text": "我看过了，写得不错，就是调查的地点只有超市，不太够。"},
                    {"speaker": "同事:", "text": "好的，那我再加一些网店。"},
                    {"speaker": "王一雪:", "text": "行。做调查的时候要细心，注意了解客户真正的想法。"},
                    {"speaker": "同事:", "text": "明白了，我会认真准备，按时完成任务。"},
                    {"speaker": "王一雪:", "text": "嗯，如果遇到什么问题，及时跟我联系。"}
                ]
            }
        },
        {
            "type": "qa_slide",
            "data": {
                "title": "Đọc phân vai và trả lời câu hỏi",
                "questions": [
                    "同事交的计划书有什么问题？",
                    "王一雪建议调查的时候要怎么做？"
                ]
            }
        },
        {
            "type": "retell_hsk4",
            "data": {
                "title": "根据给出的提示复述课文",
                "text": "昨天同事把________发到________，并请她看看________。王一雪觉得________，就是________。同事说她会再加________，并认真准备，按时________。王一雪建议她做调查的时候要________，注意了解________，如果遇到什么问题，________。"
            }
        },
        {
            "type": "grammar",
            "data": {
                "title_vi": "1. Cấu trúc cố định “在……方面”",
                "description_zh": "固定格式“在……方面”用于限定讨论的范围或领域。例如：",
                "formula": "在 + Lĩnh vực/Phương diện + 方面",
                "explanation_vi": "Cấu trúc cố định “在……方面” được dùng để giới hạn phạm vi hoặc lĩnh vực thảo luận.",
                "examples": [
                    "(1) 在内容方面，您觉得有需要改的吗？",
                    "(2) 在时间安排方面，你可以再想一想。",
                    "(3) 他才来中国两个月，在生活方面，还不太习惯。"
                ]
            }
        },
        {
            "type": "open_cloze",
            "data": {
                "title": "完成对话",
                "questions": [
                    "A: 你建议我去医院的国际部看病吗？\nB: ________",
                    "A: 为什么现在很多人都喜欢骑电动车？\nB: ________",
                    "A: 老师，我儿子最近在学校的表现怎么样？\nB: ________"
                ]
            }
        },
        {
            "type": "xiaoyu_tip",
            "data": {
                "tips": "Trong môi trường công sở Trung Quốc, đồng nghiệp thường dựa vào tuổi tác, mối quan hệ và môi trường làm việc để sử dụng các cách xưng hô mang tính thân thiết, ví dụ như dùng “×哥” (anh ×) “×姐” (chị ×) để gọi những đồng nghiệp lớn tuổi hơn một chút và có quan hệ khá thân thiết. Tuy nhiên, trong các dịp trang trọng, người ta vẫn sẽ sử dụng chức danh như “经理” (giám đốc).",
                "img_path": "assets/tip.png"
            }
        },

        # ==================== BÀI KHÓA 2 ====================
        {
            "type": "title_slide",
            "data": {
                "title_zh": "课文 2",
                "lesson_number": "7",
                "bg_image": "assets/hinhnen.png",
                "show_number": False
            }
        },
        {
            "type": "vocabulary_table",
            "data": {
                "lesson_num": "7",
                "level": "4",
                "audio_index": "4",
                "words": [
                    {"stt": 13, "zh": "出差", "pinyin": "chūchāi", "type": "động", "hanviet": "Xuất sai", "vi": "đi công tác"},
                    {"stt": 14, "zh": "经验", "pinyin": "jīngyàn", "type": "danh", "hanviet": "Kinh nghiệm", "vi": "kinh nghiệm"},
                    {"stt": 15, "zh": "采访", "pinyin": "cǎifǎng", "type": "động", "hanviet": "Thái phỏng", "vi": "phỏng vấn"},
                    {"stt": 16, "zh": "产品", "pinyin": "chǎnpǐn", "type": "danh", "hanviet": "Sản phẩm", "vi": "sản phẩm"},
                    {"stt": 17, "zh": "看法", "pinyin": "kànfǎ", "type": "danh", "hanviet": "Khán pháp", "vi": "cách nhìn, quan điểm"},
                    {"stt": 18, "zh": "提前", "pinyin": "tíqián", "type": "động", "hanviet": "Đề tiền", "vi": "làm trước, đẩy sớm lên"},
                    {"stt": 19, "zh": "便于", "pinyin": "biànyú", "type": "động", "hanviet": "Tiện vu", "vi": "thuận tiện cho"},
                    {"stt": 20, "zh": "既然", "pinyin": "jìrán", "type": "liên", "hanviet": "Ký nhiên", "vi": "đã... thì..."}
                ]
            }
        },
        {
            "type": "listening_abcd",
            "data": {
                "title": "Nghe và chọn đáp án đúng",
                "context_zh": "在公司，同事向杨同乐征求建议。",
                "context_vi": "Tại công ty, đồng nghiệp xin ý kiến của Dương Đồng Lạc.",
                "lesson_num": "7",
                "level": "4",
                "audio_index": "3",
                "questions": [
                    {
                        "q_zh": "同事要去上海做什么？",
                        "options": ["A. 出差", "B. 旅游", "C. 购物", "D. 看朋友"]
                    },
                    {
                        "q_zh": "同事已经准备好什么了？",
                        "options": ["A. 行李", "B. 新产品", "C. 要问的问题", "D. 给客户的礼物"]
                    }
                ]
            }
        },
        {
            "type": "text_hsk3",
            "data": {
                "title": "课文\n2",
                "context_zh": "在公司，同事向杨同乐征求建议。",
                "context_vi": "Tại công ty, đồng nghiệp xin ý kiến của Dương Đồng Lạc.",
                "lesson_num": "7",
                "level": "4",
                "audio_index": "3",
                "lines": [
                    {"speaker": "同事:", "text": "杨哥，经理让我下周去上海出差，做市场调查，你有这方面的经验吗？"},
                    {"speaker": "杨同乐:", "text": "你要去几天？主要调查什么内容？"},
                    {"speaker": "同事:", "text": "去四天，打算采访一些客户，了解他们对新产品的看法。"},
                    {"speaker": "杨同乐:", "text": "那你要提前准备好问题，便于和客户交流。"},
                    {"speaker": "同事:", "text": "好的，我已经准备了一些问题。"},
                    {"speaker": "杨同乐:", "text": "很好。既然出差时间不长，就要安排好时间，多获得有用的信息。"}
                ]
            }
        },
        {
            "type": "qa_slide",
            "data": {
                "title": "Đọc phân vai và trả lời câu hỏi",
                "questions": [
                    "同事要调查什么内容？",
                    "杨同乐提了什么建议？"
                ]
            }
        },
        {
            "type": "grammar",
            "data": {
                "title_vi": "2. Câu phức nhân quả “既然……，就……”",
                "description_zh": "前一分句说明前提，后一分句说明根据这个前提推出的结论。例如：",
                "formula": "既然 + Tiền đề, 就 + Kết luận",
                "explanation_vi": "Mệnh đề trước giải thích tiền đề, mệnh đề sau giải thích kết luận được suy ra từ tiền đề đó.",
                "examples": [
                    "(1) 既然出差时间不长，就要安排好时间，多获得有用的信息。",
                    "(2) 既然大家都同意，我们就这么做吧。",
                    "(3) 既然你们已经决定了，就不要再改了。"
                ]
            }
        },
        {
            "type": "open_cloze",
            "data": {
                "title": "完成对话",
                "questions": [
                    "A: 老师，我有点儿不舒服。\nB: ________",
                    "A: 外面下雨了，咱们还出去吗？\nB: ________",
                    "A: 我觉得这个工作没什么发展机会。\nB: ________"
                ]
            }
        },
        {
            "type": "xiaoyu_tip",
            "data": {
                "tips": "这里“提”的意思是“提出”。(Ở đây “提” có nghĩa là “đưa ra, đề xuất”.)",
                "img_path": "assets/tip.png"
            }
        },

        # ==================== BÀI KHÓA 3 ====================
        {
            "type": "title_slide",
            "data": {
                "title_zh": "课文 3",
                "lesson_number": "7",
                "bg_image": "assets/hinhnen.png",
                "show_number": False
            }
        },
        {
            "type": "vocabulary_table",
            "data": {
                "lesson_num": "7",
                "level": "4",
                "audio_index": "6",
                "words": [
                    {"stt": 21, "zh": "谈", "pinyin": "tán", "type": "động", "hanviet": "Đàm", "vi": "nói chuyện, đàm phán"},
                    {"stt": 22, "zh": "笔", "pinyin": "bǐ", "type": "lượng", "hanviet": "Bút", "vi": "khoản, món (lượng từ chỉ tiền)"},
                    {"stt": 23, "zh": "生意", "pinyin": "shēngyì", "type": "danh", "hanviet": "Sinh ý", "vi": "việc kinh doanh, buôn bán"},
                    {"stt": 24, "zh": "困难", "pinyin": "kùnnan", "type": "danh/tính", "hanviet": "Khốn nạn", "vi": "khó khăn"},
                    {"stt": 25, "zh": "优点", "pinyin": "yōudiǎn", "type": "danh", "hanviet": "Ưu điểm", "vi": "ưu điểm"},
                    {"stt": 26, "zh": "缺点", "pinyin": "quēdiǎn", "type": "danh", "hanviet": "Khuyết điểm", "vi": "khuyết điểm, nhược điểm"},
                    {"stt": 27, "zh": "实际", "pinyin": "shíjì", "type": "tính/danh", "hanviet": "Thực tế", "vi": "thực tế"},
                    {"stt": 28, "zh": "效果", "pinyin": "xiàoguǒ", "type": "danh", "hanviet": "Hiệu quả", "vi": "hiệu quả"},
                    {"stt": 29, "zh": "点", "pinyin": "diǎn", "type": "danh", "hanviet": "Điểm", "vi": "điểm, phương diện"},
                    {"stt": 30, "zh": "一下", "pinyin": "yíxià", "type": "phó", "hanviet": "Nhất hạ", "vi": "ngay lập tức, một cái (bổ ngữ thời gian ngắn)"}
                ]
            }
        },
        {
            "type": "listening_abcd",
            "data": {
                "title": "Nghe và chọn đáp án đúng",
                "context_zh": "不同客户，不同方法",
                "context_vi": "Khách hàng khác nhau, phương pháp khác nhau.",
                "lesson_num": "7",
                "level": "4",
                "audio_index": "5",
                "questions": [
                    {
                        "q_zh": "前段时间，杨同乐的同事怎么了？",
                        "options": ["A. 生病了", "B. 休假了", "C. 当上了经理", "D. 谈成了生意"]
                    },
                    {
                        "q_zh": "同事是通过什么办法解决问题的？",
                        "options": ["A. 找经理帮忙", "B. 做市场调查", "C. 请客户吃饭", "D. 提前准备问题"]
                    }
                ]
            }
        },
        {
            "type": "text_hsk3",
            "data": {
                "title": "课文\n3",
                "context_zh": "不同客户，不同方法",
                "context_vi": "Khách hàng khác nhau, phương pháp khác nhau.",
                "lesson_num": "7",
                "level": "4",
                "audio_index": "5",
                "lines": [
                    {"speaker": "旁白:", "text": "前段时间，杨同乐的同事谈成了一笔不错的生意。刚开始，这位同事也遇到了一些困难。拿和客户交流来说，虽然她能把产品的优缺点说得很清楚，但实际效果并不理想。杨同乐告诉她，这是因为她介绍的方式都一样。其实，不同年龄、不同性别的客户对产品的关注点是不一样的。"},
                    {"speaker": "旁白:", "text": "于是，这位同事又认真地进行了几次市场调查，了解不同客户的想法。后来她在面对不同客户时，能根据他们的情况介绍产品，效果一下就好了很多。"}
                ]
            }
        },
        {
            "type": "qa_slide",
            "data": {
                "title": "Đọc bài khóa và trả lời câu hỏi",
                "questions": [
                    "刚开始的时候，同事遇到了什么困难？",
                    "后来同事是怎么做的？"
                ]
            }
        },
        {
            "type": "retell_hsk4",
            "data": {
                "title": "根据给出的提示复述课文",
                "text": "前段时间，杨同乐的同事________。刚开始，这位同事________。拿________来说，虽然她能________，但实际效果________。杨同乐告诉她，这是因为________。其实，不同年龄、不同性别的客户________。于是，这位同事________，了解________。后来她在面对不同客户时，能________，效果________。"
            }
        },
        {
            "type": "grammar",
            "data": {
                "title_vi": "3. Cấu trúc cố định “拿……来说”",
                "description_zh": "固定格式“拿……来说”用于引出具体方面或例子。例如：",
                "formula": "拿 + Ví dụ/Phương diện cụ thể + 来说",
                "explanation_vi": "Cấu trúc cố định “拿……来说” được dùng để đưa ra một phương diện hoặc ví dụ cụ thể.",
                "examples": [
                    "(1) 拿和客户交流来说，虽然她能把产品的优缺点说得很清楚，但实际效果并不理想。",
                    "(2) 现在的生活很方便。拿购物来说，人们不出门就能买到想要的东西。",
                    "(3) 在中国，南北方的生活习惯不同。拿吃饭来说，一般南方人更爱吃米饭。"
                ]
            }
        },
        {
            "type": "open_cloze",
            "data": {
                "title": "完成句子",
                "questions": [
                    "我很喜欢这个小区。________（环境）",
                    "现在快递的速度很快。________（网购）",
                    "我们班同学之间经常互相帮助。________（学习）"
                ]
            }
        },
        {
            "type": "xiaoyu_tip",
            "data": {
                "tips": "“优缺点”是“优点和缺点”的缩略形式。(“优缺点” là hình thức viết tắt của “优点和缺点” - ưu điểm và khuyết điểm.)",
                "img_path": "assets/tip.png"
            }
        },
        # ==================== BÀI KHÓA 4 ====================
        {
            "type": "title_slide",
            "data": {
                "title_zh": "课文 4",
                "lesson_number": "7",
                "bg_image": "assets/hinhnen.png",
                "show_number": False
            }
        },
        {
            "type": "vocabulary_table",
            "data": {
                "lesson_num": "7",
                "level": "4",
                "audio_index": "8",
                "words": [
                    {"stt": 31, "zh": "份", "pinyin": "fèn", "type": "lượng", "hanviet": "Phần", "vi": "phần, bản (lượng từ)"},
                    {"stt": 32, "zh": "积累", "pinyin": "jīlěi", "type": "động", "hanviet": "Tích lũy", "vi": "tích lũy"},
                    {"stt": 33, "zh": "使", "pinyin": "shǐ", "type": "động", "hanviet": "Sử", "vi": "khiến, làm cho"},
                    {"stt": 34, "zh": "进入", "pinyin": "jìnrù", "type": "động", "hanviet": "Tiến nhập", "vi": "bước vào, gia nhập"},
                    {"stt": 35, "zh": "社会", "pinyin": "shèhuì", "type": "danh", "hanviet": "Xã hội", "vi": "xã hội"},
                    {"stt": 36, "zh": "管理", "pinyin": "guǎnlǐ", "type": "động", "hanviet": "Quản lý", "vi": "quản lý"},
                    {"stt": 37, "zh": "基础", "pinyin": "jīchǔ", "type": "danh", "hanviet": "Cơ sở", "vi": "cơ sở, nền tảng"},
                    {"stt": 38, "zh": "能力", "pinyin": "nénglì", "type": "danh", "hanviet": "Năng lực", "vi": "năng lực"},
                    {"stt": 39, "zh": "今后", "pinyin": "jīnhòu", "type": "danh", "hanviet": "Kim hậu", "vi": "sau này, từ nay về sau"}
                ]
            }
        },
        {
            "type": "listening_abcd",
            "data": {
                "title": "Đọc bài khóa và chọn đáp án đúng",
                "context_zh": "工作的选择与发展",
                "context_vi": "Lựa chọn và phát triển công việc.",
                "lesson_num": "7",
                "level": "4",
                "audio_index": "7",
                "questions": [
                    {
                        "q_zh": "根据课文，为什么有的年轻人经常换工作？",
                        "options": ["A. 工资太低", "B. 工作没意思", "C. 对自己要求高", "D. 觉得下一份工作会更好"]
                    },
                    {
                        "q_zh": "他认为，年轻人刚进入社会时，应该更重视什么？",
                        "options": ["A. 工资", "B. 学习", "C. 休息", "D. 心情"]
                    }
                ]
            }
        },
        {
            "type": "text_hsk3",
            "data": {
                "title": "课文\n4",
                "context_zh": "工作的选择与发展",
                "context_vi": "Lựa chọn và phát triển công việc.",
                "lesson_num": "7",
                "level": "4",
                "audio_index": "7",
                "lines": [
                    {"speaker": "旁白:", "text": "有的年轻人经常换工作，总觉得下一份工作会更好。但是，适应新工作往往需要比较长的时间。如果总是换工作，不但很难积累经验，还可能会使自己的发展受到影响。\n\u3000\u3000我认为，年轻人刚进入社会时，不能只关心工资的高低，更要重视学习。比如，学习课本中没有的专业知识，了解公司的管理方式，学会和同事有效交流，等等。只有把这些基础打好，提高工作能力，今后才会有更好的发展机会。"}
                ]
            }
        },
        {
            "type": "qa_slide",
            "data": {
                "title": "Đọc bài khóa và trả lời câu hỏi",
                "questions": [
                    "为什么不建议年轻人总换工作？",
                    "年轻人怎样才能获得更好的发展机会？"
                ]
            }
        },
        {
            "type": "grammar",
            "data": {
                "title_vi": "4. Câu kiêm ngữ “主语 + 使 + 宾语 + 动词短语”",
                "description_zh": "兼语句“主语+使+宾语+动词短语”表示某种情况或原因致使人或事物发生变化或产生结果。例如：",
                "formula": "Chủ ngữ + 使 + Tân ngữ + Cụm động từ",
                "explanation_vi": "Câu kiêm ngữ “Chủ ngữ + 使 + Tân ngữ + Cụm động từ” biểu thị một tình huống hoặc nguyên nhân nào đó khiến người hoặc vật thay đổi hoặc tạo ra kết quả.",
                "examples": [
                    "(1) 如果总是换工作，可能会使自己的发展受到影响。",
                    "(2) 这个新方法使工作变得更加简单了。",
                    "(3) 参加这些交流活动使留学生更快适应了大学生活。"
                ]
            }
        },
        {
            "type": "open_cloze",
            "data": {
                "title": "完成句子",
                "questions": [
                    "和同事多交流________",
                    "长时间不休息________",
                    "这次市场调查________"
                ]
            }
        },

        # ==================== LUYỆN TẬP TỔNG HỢP ====================
        {
            "type": "title_slide",
            "data": {
                "title_zh": "综合练习",
                "lesson_number": "7",
                "bg_image": "assets/hinhnen.png",
                "show_number": False
            }
        },
        {
            "type": "fill_in_blanks",
            "data": {
                "title": "选词填空",
                "questions": [
                    "(1) 发现问题以后，我们要______解决。",
                    "(2) 不好意思，这么晚还来______您休息。",
                    "(3) 我刚才把家庭地址写错了，可以______一下吗？",
                    "(4) 他和同事交流了一下，了解了大家的______。",
                    "(5) 老师把学习材料放到了网上，______学生们复习。"
                ],
                "options": ["A 改", "B 想法", "C 便于", "D 打扰", "E 及时"]
            }
        },
        {
            "type": "fill_in_blanks",
            "data": {
                "title": "选词填空",
                "questions": [
                    "(6) A: 听说你最近一直坚持跑步。\nB: 是的，我觉得______很好，身体比以前好多了。",
                    "(7) A: 经理为什么让小王去做市场调查？\nB: 经理说他的______是很会和别人交流。",
                    "(8) A: 我想学好中文，有什么建议吗？\nB: 刚开始的时候别太着急，先把______打好。"
                ],
                "options": ["A 一下", "B 基础", "C 优点", "D 效果", "E 管理"]
            }
        },
        {
            "type": "fill_in_blanks",
            "data": {
                "title": "选词填空",
                "questions": [
                    "(9) A: 你在大学学的是什么专业？\nB: 我学的是酒店______专业，现在在一家酒店工作。",
                    "(10) A: 您讲得真好，讲完我______就明白了。谢谢您！\nB: 别客气，还有不懂的就来问我。"
                ],
                "options": ["A 一下", "B 基础", "C 优点", "D 效果", "E 管理"]
            }
        },
        {
            "type": "complete_passage_abcd",
            "data": {
                "title": "选择合适的内容完成短文",
                "context_text": "上周，小张接到经理的任务，________。她和一些客户交流了一下，________。有的客户觉得价格有点儿高，有的客户更关心产品好用不好用。昨天，小张按照客户的年龄和性别，写好了调查结果，并交给了经理，________，________。",
                "options": [
                    "A. 按时完成了任务",
                    "B. 也积累了不少经验",
                    "C. 去几家公司做市场调查了",
                    "D. 了解他们对新产品的看法"
                ]
            }
        },

        # ==================== MIÊU TẢ TRANH (HSK4) ====================
        {
            "type": "describe_picture_hsk4",
            "data": {
                "title": "看图，用词语造句",
                "quyen": "4",
                "bai": "7",
                "items": [
                    {"word": "调查"},
                    {"word": "能力"},
                    {"word": "细心"}
                ]
            }
        },

        # ==================== HOẠT ĐỘNG NHÓM ====================
        # ==================== HOẠT ĐỘNG NHÓM ====================
        {
            "type": "group_game",
            "data": {
                "title": "Tranh luận nhóm",
                "rule_title": "Quy tắc",
                "rule_text": "Cả lớp chia thành hai nhóm, tranh luận với chủ đề: “换工作还是继续做” (Thay đổi công việc hay tiếp tục làm). Mỗi nhóm chuẩn bị quan điểm và lý do của mình trước, sau đó tranh luận để bày tỏ quan điểm.",
                "example_title": "Quan điểm",
                "examples": [
                    "正方：年轻人应该多换几份工作，找到最适合自己的。",
                    "反方：年轻人应该坚持一份工作，积累更多工作经验。"
                ],
                "img_path": "assets/Group Game.png"
            }
        },
        # ==================== VIẾT ====================
        {
            "type": "writing_hsk4", # Đã sửa chuẩn key
            "data": {
                "title": "写作",
                "instruction_zh": "你的一个朋友最近很苦恼，他/她不喜欢现在的工作，觉得没有发展机会。请你根据上面辩论的内容，给他/她写一封邮件，谈谈你的看法，不少于120字。",
                "instruction_vi": "Một người bạn của bạn dạo này rất phiền lòng, bạn ấy không thích công việc hiện tại và cảm thấy không có cơ hội phát triển. Vui lòng viết một bức email cho bạn ấy dựa trên nội dung cuộc tranh luận ở trên, nói về quan điểm của bạn, không ít hơn 120 chữ.",
                "image": "writting.png"
            }
        },

        # ==================== TỔNG KẾT ====================
        {
            "type": "summary",
            "data": {
                "title": "Tình hình học tập của tôi",
                "table_header": "Nội dung tự đánh giá",
                "row1_title_vi": "Có thể sử dụng các từ ngữ như “市场, 调查, 任务, 出差, 经验, 管理” trong bài để thảo luận về chủ đề công sở.",
                "row2_title_vi": "Có thể hiểu và vận dụng các điểm ngữ pháp như “在……方面”, “既然……，就……”, “拿……来说”, “主语+使+宾语+动词短语”.",
                "row3_title_vi": "Có thể giao tiếp về nhiệm vụ và sắp xếp công việc.",
                "row4_title_vi": "Có thể trình bày kinh nghiệm làm việc của cá nhân."
            }
        },

        # ==================== TRANG CẢM ƠN ====================
        {
            "type": "title_slide",
            "data": {
                "title_zh": "谢谢！",
                "lesson_number": "7",
                "bg_image": "assets/hinhnen.png",
                "show_number": False
            }
        }
    ]
}
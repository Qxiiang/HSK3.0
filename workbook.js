// =========================================================================
// MODULE XỬ LÝ TAB 6: SÁCH BÀI TẬP (WORKBOOK)
// =========================================================================

function openCharStrokeByChar(ch, py, meaning) {
    currentStrokeWord = { hz: ch, py: py, pos: "Chữ Hán", vi: meaning, memo: "" };
    document.getElementById('stroke-word-hz').textContent = ch;
    document.getElementById('stroke-word-py').textContent = py;
    document.getElementById('stroke-word-vi').textContent = meaning;
    document.getElementById('stroke-memo-tip').innerHTML = `💡 Bấm <strong>Xem nét</strong> để xem thứ tự nét hoặc <strong>Tập viết</strong> để tự tô theo nét.`;

    const container = document.getElementById('stroke-characters-container');
    container.className = "grid grid-cols-1 gap-6 justify-items-center";
    container.innerHTML = `
        <div class="bg-slate-50 border border-slate-200 rounded-2xl p-4 flex flex-col items-center space-y-3 w-full max-w-[230px]">
            <div class="flex items-center justify-between w-full text-xs text-slate-500">
                <span class="font-bold text-slate-700">Chữ Hán: <span class="zh-font text-base text-rose-800">${ch}</span></span>
                <span id="stroke-status-0" class="text-[11px] font-medium text-slate-400">Thứ tự nét</span>
            </div>
            <div id="hanzi-target-0" class="hanzi-grid-bg w-[170px] h-[170px] rounded-xl border-2 border-slate-300 shadow-2xs flex items-center justify-center overflow-hidden"></div>
            <div class="flex gap-2 w-full">
                <button onclick="animateSingleWriter(0)" class="flex-1 py-1.5 rounded-lg bg-white border border-slate-200 hover:bg-rose-50 hover:text-rose-800 text-xs font-semibold text-slate-700">▶ Xem nét</button>
                <button onclick="quizSingleWriter(0)" class="flex-1 py-1.5 rounded-lg bg-amber-50 border border-amber-200 hover:bg-amber-100 text-xs font-semibold text-amber-900">✍️ Tập viết</button>
            </div>
        </div>
    `;
    toggleModal('stroke-modal', true);
    strokeWriterInstances = [];
    if (typeof HanziWriter !== 'undefined') {
        const writer = HanziWriter.create('hanzi-target-0', ch, {
            width: 170,
            height: 170,
            padding: 12,
            showOutline: true,
            strokeAnimationSpeed: 1.1,
            delayBetweenStrokes: 180,
            strokeColor: '#991b1b',
            radicalColor: '#b45309',
            outlineColor: '#cbd5e1',
            drawingColor: '#1e293b',
            drawingWidth: 18
        });
        strokeWriterInstances.push(writer);
        setTimeout(() => writer.animateCharacter(), 200);
    }
}

function renderWorkbookSection() {
    const container = document.getElementById('workbook-container');
    if (!container) return;

    const wb = (window.HSK_WORKBOOKS || {})[currentLessonKey];

    if (!wb) {
        container.innerHTML = `<div class="bg-white p-6 rounded-2xl border border-slate-200 text-sm text-slate-500">Chưa có dữ liệu Sách bài tập cho bài học này.</div>`;
        return;
    }

    const xy = wb.xiaoyuClassroom || {};
    const pr = wb.practice || {};

    let html = `
        <!-- PHẦN A: TIỂU NGỮ GIẢNG ĐƯỜNG -->
        <div class="bg-white p-6 sm:p-8 rounded-2xl border border-slate-200 shadow-xs space-y-6">
            <div class="border-b border-slate-100 pb-4">
                <span class="text-xs font-bold uppercase tracking-wider text-amber-900 bg-amber-50 px-3 py-1 rounded-full border border-amber-200">📘 Sách bài tập HSK 3.0</span>
                <h2 class="text-xl sm:text-2xl font-bold text-slate-900 mt-2">Phần I: Tiểu Ngữ Giảng Đường (小语讲堂)</h2>
                <p class="text-xs text-slate-500 mt-1">Phân biệt chữ hình gần giống, chữ đa âm và luyện tập mở rộng cụm từ.</p>
            </div>

            ${xy.similarChars ? `
            <div class="space-y-3">
                <h3 class="text-base font-bold text-rose-900">1. Chữ hình gần giống (形近字)</h3>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    ${xy.similarChars.map(sc => `
                        <div class="p-4 rounded-xl bg-slate-50 border border-slate-200 space-y-2.5">
                            <div class="flex items-center justify-between">
                                <div class="flex items-center gap-3">
                                    <span class="zh-font text-4xl font-bold text-rose-900 bg-white w-14 h-14 rounded-xl border border-slate-200 flex items-center justify-center shadow-2xs">${sc.char}</span>
                                    <div>
                                        <p class="text-sm font-bold text-rose-800">${sc.py}</p>
                                        <p class="text-xs text-slate-600 font-medium">Nghĩa: ${sc.meaning}</p>
                                    </div>
                                </div>
                                <div class="flex gap-1.5">
                                    <button onclick="speakText('${escapeJsSingleQuote(sc.char)}')" class="px-2.5 py-1.5 rounded-lg bg-white border border-slate-200 text-xs font-semibold text-rose-700 hover:bg-rose-50">🔊 Nghe</button>
                                    <button onclick="openCharStrokeByChar('${escapeJsSingleQuote(sc.char)}', '${escapeJsSingleQuote(sc.py)}', '${escapeJsSingleQuote(sc.meaning)}')" class="px-2.5 py-1.5 rounded-lg bg-amber-50 border border-amber-200 text-xs font-semibold text-amber-900 hover:bg-amber-100">✍️ Tập viết</button>
                                </div>
                            </div>
                            <p class="text-xs text-slate-600 bg-white p-2.5 rounded-lg border border-slate-200/80">💡 <strong>Điểm khác biệt:</strong> ${sc.diff}</p>
                            <div class="flex flex-wrap items-center gap-2 text-xs">
                                <span class="font-semibold text-slate-500">Từ ghép:</span>
                                ${sc.words.map(w => `<span onclick="speakText('${escapeJsSingleQuote(w)}')" class="zh-font bg-rose-50 text-rose-900 px-2.5 py-0.5 rounded-md border border-rose-200 cursor-pointer hover:bg-rose-100">🔊 ${w}</span>`).join('')}
                            </div>
                            <div class="text-xs text-slate-800 zh-font flex items-center justify-between bg-white px-3 py-2 rounded-lg border border-slate-200/80">
                                <span><strong>Câu mẫu:</strong> ${sc.sentence}</span>
                                <button onclick="speakText('${escapeJsSingleQuote(sc.sentence)}')" class="text-rose-700">🔊</button>
                            </div>
                        </div>
                    `).join('')}
                </div>
            </div>` : ''}

            ${xy.polyphonic ? `
            <div class="space-y-3 pt-2">
                <h3 class="text-base font-bold text-rose-900">2. Chữ đa âm (多音字): 「<span class="zh-font">${xy.polyphonic.char}</span>」</h3>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    ${xy.polyphonic.items.map(item => `
                        <div class="p-4 rounded-xl bg-slate-50 border border-slate-200 space-y-2">
                            <div class="flex items-center justify-between">
                                <div>
                                    <span class="zh-font text-xl font-bold text-slate-900">${item.word}</span>
                                    <span class="ml-2 text-sm font-bold text-rose-800">${item.py}</span>
                                </div>
                                <button onclick="speakText('${escapeJsSingleQuote(item.sentence)}')" class="px-3 py-1 rounded-lg bg-white border border-slate-200 text-xs font-semibold text-rose-700 hover:bg-rose-50">🔊 Nghe câu</button>
                            </div>
                            <p class="text-xs text-slate-600">${item.meaning}</p>
                            <p class="zh-font text-sm text-slate-900 bg-white p-2.5 rounded-lg border border-slate-200/80">${item.sentence}</p>
                        </div>
                    `).join('')}
                </div>
            </div>` : ''}

            ${xy.wordFill ? `
            <div class="space-y-4 pt-2">
                <h3 class="text-base font-bold text-rose-900">3. Kho từ & Cụm từ thường gặp (词语汇聚)</h3>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
                    ${(xy.wordThemes || []).map(th => `
                        <div class="p-3.5 rounded-xl bg-amber-50/50 border border-amber-200/80 space-y-2">
                            <p class="text-xs font-bold text-amber-950">${th.theme}</p>
                            <div class="flex flex-wrap gap-1.5">
                                ${th.words.map(w => `<span onclick="speakText('${escapeJsSingleQuote(w)}')" class="zh-font text-xs bg-white hover:bg-rose-50 text-slate-800 px-2.5 py-1 rounded-lg border border-amber-200/80 cursor-pointer">${w}</span>`).join('')}
                            </div>
                        </div>
                    `).join('')}
                </div>

                <div class="p-4 rounded-xl bg-slate-50 border border-slate-200 space-y-3">
                    <p class="text-xs font-bold text-slate-800">Bài tập điền từ vào chỗ trống (Chọn từ trong kho từ phía trên để điền):</p>
                    <div class="space-y-2.5">
                        ${xy.wordFill.map((wf, idx) => `
                            <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 bg-white p-3 rounded-xl border border-slate-200">
                                <span class="zh-font text-sm text-slate-900">${wf.q}</span>
                                <div class="flex items-center gap-2 shrink-0">
                                    <input type="text" id="wb-wf-${idx}" placeholder="Nhập từ..." class="w-28 px-2.5 py-1 text-sm border border-slate-300 rounded-lg zh-font text-center focus:outline-none focus:border-rose-700">
                                    <span id="wb-wf-fb-${idx}" class="text-xs font-bold hidden"></span>
                                </div>
                            </div>
                        `).join('')}
                    </div>
                    <button onclick="checkWbWordFill()" class="px-4 py-2 rounded-xl bg-rose-800 hover:bg-rose-900 text-white text-xs font-semibold">Kiểm tra bài điền từ</button>
                </div>
            </div>` : ''}
        </div>

        <!-- PHẦN B: MÔ PHỎNG LUYỆN ĐỀ (NGHE - ĐỌC - VIẾT) -->
        <div class="bg-white p-6 sm:p-8 rounded-2xl border border-slate-200 shadow-xs space-y-8">
            <div class="border-b border-slate-100 pb-4">
                <h2 class="text-xl sm:text-2xl font-bold text-slate-900">Phần II: Mô phỏng luyện đề (模拟测练)</h2>
                <p class="text-xs text-slate-500 mt-1">Đầy đủ 3 kỹ năng Nghe hiểu (Câu 1–10), Đọc hiểu (Câu 11–24) và Viết (Câu 25–30).</p>
            </div>

            <!-- I. NGHE HIỂU -->
            <div class="space-y-5">
                <h3 class="text-lg font-bold text-rose-900 flex items-center gap-2"><span>🎧</span> 一、听力 (Nghe hiểu — Câu 1~10)</h3>
                
                <div class="p-4 rounded-xl bg-slate-50 border border-slate-200 space-y-4">
                    <p class="text-xs font-bold text-slate-800">Phần 1 (Câu 1~3): Nghe hội thoại và chọn bức tranh phù hợp (A, B, C, D)</p>
                    ${pr.listeningPart1Image ? `<div class="flex justify-center bg-white p-3 rounded-xl border border-slate-200"><img src="${pr.listeningPart1Image}" alt="Tranh A-D" class="max-h-64 object-contain"></div>` : ''}
                    <div class="grid grid-cols-1 md:grid-cols-3 gap-3">
                        ${(pr.listeningPart1 || []).map((q, idx) => `
                            <div class="bg-white p-3.5 rounded-xl border border-slate-200 space-y-2.5">
                                <div class="flex items-center justify-between">
                                    <span class="font-bold text-xs text-slate-900">Câu ${q.num}</span>
                                    <select id="wb-l1-${idx}" class="px-2.5 py-1 text-xs font-bold border border-slate-300 rounded-lg bg-slate-50">
                                        <option value="">-- Chọn --</option>
                                        <option value="A">A</option>
                                        <option value="B">B</option>
                                        <option value="C">C</option>
                                        <option value="D">D</option>
                                    </select>
                                </div>
                                <button onclick="speakText('${escapeJsSingleQuote(q.dialogue)}')" class="w-full py-1.5 rounded-lg bg-rose-50 hover:bg-rose-100 text-rose-800 text-xs font-semibold">🔊 Nghe câu ${q.num}</button>
                                <div id="wb-l1-fb-${idx}" class="hidden text-xs p-2 rounded-lg"></div>
                            </div>
                        `).join('')}
                    </div>
                </div>

                <div class="p-4 rounded-xl bg-slate-50 border border-slate-200 space-y-4">
                    <p class="text-xs font-bold text-slate-800">Phần 2 & 3 (Câu 4~10): Nghe hội thoại / đoạn văn và chọn đáp án đúng</p>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
                        ${[...(pr.listeningPart2 || []), ...(pr.listeningPart3 || [])].map((q, idx) => `
                            <div class="bg-white p-3.5 rounded-xl border border-slate-200 space-y-2.5">
                                <div class="flex items-center justify-between">
                                    <span class="font-bold text-xs text-slate-900">Câu ${q.num}</span>
                                    <button onclick="speakText('${escapeJsSingleQuote(q.dialogue)}')" class="px-3 py-1 rounded-lg bg-rose-50 hover:bg-rose-100 text-rose-800 text-xs font-semibold">🔊 Nghe</button>
                                </div>
                                <div class="space-y-1.5">
                                    ${q.options.map(opt => {
                                        const letter = opt.trim().charAt(0);
                                        return `
                                            <label class="flex items-center gap-2 p-2 rounded-lg bg-slate-50 hover:bg-rose-50/50 border border-slate-200 cursor-pointer text-xs zh-font">
                                                <input type="radio" name="wb-l23-${idx}" value="${letter}" class="accent-rose-800">
                                                <span>${opt}</span>
                                            </label>
                                        `;
                                    }).join('')}
                                </div>
                                <div id="wb-l23-fb-${idx}" class="hidden text-xs p-2 rounded-lg"></div>
                            </div>
                        `).join('')}
                    </div>
                </div>
                <button onclick="checkWbListening()" class="px-5 py-2.5 rounded-xl bg-rose-800 hover:bg-rose-900 text-white text-xs font-semibold">Chấm điểm phần Nghe (Câu 1~10)</button>
            </div>

            <!-- II. ĐỌC HIỂU -->
            <div class="space-y-5 pt-4 border-t border-slate-100">
                <h3 class="text-lg font-bold text-rose-900 flex items-center gap-2"><span>📖</span> 二、阅读 (Đọc hiểu — Câu 11~24)</h3>

                <div class="p-4 rounded-xl bg-slate-50 border border-slate-200 space-y-3">
                    <p class="text-xs font-bold text-slate-800">Phần 1 (Câu 11~15): Ghép câu đối đáp phù hợp</p>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-2 bg-amber-50/70 p-3 rounded-xl border border-amber-200 text-xs zh-font">
                        ${(pr.readingPart1Options || []).map(opt => `<div class="bg-white px-2.5 py-1.5 rounded-lg border border-amber-200/80">${opt}</div>`).join('')}
                    </div>
                    <div class="space-y-2">
                        ${(pr.readingPart1 || []).map((q, idx) => `
                            <div class="bg-white p-3 rounded-xl border border-slate-200 space-y-1.5">
                                <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
                                    <span class="zh-font text-sm text-slate-900">${q.q}</span>
                                    <select id="wb-r1-${idx}" class="px-2.5 py-1 text-xs font-bold border border-slate-300 rounded-lg bg-slate-50 shrink-0">
                                        <option value="">-- Chọn A-F --</option>
                                        ${['A','B','C','D','E','F'].map(l => `<option value="${l}">${l}</option>`).join('')}
                                    </select>
                                </div>
                                <div id="wb-r1-fb-${idx}" class="hidden text-xs p-2 rounded-lg"></div>
                            </div>
                        `).join('')}
                    </div>
                </div>

                <div class="p-4 rounded-xl bg-slate-50 border border-slate-200 space-y-3">
                    <p class="text-xs font-bold text-slate-800">Phần 2 (Câu 16~20): Chọn từ thích hợp điền vào chỗ trống</p>
                    <div class="flex flex-wrap gap-2 bg-amber-50/70 p-3 rounded-xl border border-amber-200 text-xs zh-font font-bold">
                        ${(pr.readingPart2Options || []).map(opt => `<span class="bg-white px-3 py-1 rounded-lg border border-amber-200">${opt}</span>`).join('')}
                    </div>
                    <div class="space-y-2">
                        ${(pr.readingPart2 || []).map((q, idx) => `
                            <div class="bg-white p-3 rounded-xl border border-slate-200 space-y-1.5">
                                <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
                                    <span class="zh-font text-sm text-slate-900 whitespace-pre-line">${q.q}</span>
                                    <select id="wb-r2-${idx}" class="px-2.5 py-1 text-xs font-bold border border-slate-300 rounded-lg bg-slate-50 shrink-0">
                                        <option value="">-- Chọn A-F --</option>
                                        ${['A','B','C','D','E','F'].map(l => `<option value="${l}">${l}</option>`).join('')}
                                    </select>
                                </div>
                                <div id="wb-r2-fb-${idx}" class="hidden text-xs p-2 rounded-lg"></div>
                            </div>
                        `).join('')}
                    </div>
                </div>

                <div class="p-4 rounded-xl bg-slate-50 border border-slate-200 space-y-3">
                    <p class="text-xs font-bold text-slate-800">Phần 3 (Câu 21~24): Đọc đoạn văn và chọn đáp án đúng</p>
                    <div class="space-y-3">
                        ${(pr.readingPart3 || []).map((q, idx) => `
                            <div class="bg-white p-4 rounded-xl border border-slate-200 space-y-2.5">
                                <p class="zh-font text-sm text-slate-800 leading-relaxed bg-slate-50 p-3 rounded-lg border border-slate-200/80">${q.passage}</p>
                                <p class="zh-font text-sm font-bold text-rose-900">${q.question}</p>
                                <div class="grid grid-cols-1 sm:grid-cols-3 gap-2">
                                    ${q.options.map(opt => {
                                        const letter = opt.trim().charAt(0);
                                        return `
                                            <label class="flex items-center gap-2 p-2 rounded-lg bg-slate-50 hover:bg-rose-50/50 border border-slate-200 cursor-pointer text-xs zh-font">
                                                <input type="radio" name="wb-r3-${idx}" value="${letter}" class="accent-rose-800">
                                                <span>${opt}</span>
                                            </label>
                                        `;
                                    }).join('')}
                                </div>
                                <div id="wb-r3-fb-${idx}" class="hidden text-xs p-2 rounded-lg"></div>
                            </div>
                        `).join('')}
                    </div>
                </div>
                <button onclick="checkWbReading()" class="px-5 py-2.5 rounded-xl bg-rose-800 hover:bg-rose-900 text-white text-xs font-semibold">Chấm điểm phần Đọc hiểu (Câu 11~24)</button>
            </div>

            <!-- III. VIẾT -->
            <div class="space-y-5 pt-4 border-t border-slate-100">
                <h3 class="text-lg font-bold text-rose-900 flex items-center gap-2"><span>✍️</span> 三、书写 (Viết — Câu 25~30)</h3>

                <div class="p-4 rounded-xl bg-slate-50 border border-slate-200 space-y-3">
                    <p class="text-xs font-bold text-slate-800">Phần 1 (Câu 25~27): Nhìn Pinyin viết chữ Hán tương ứng</p>
                    <div class="grid grid-cols-1 md:grid-cols-3 gap-3">
                        ${(pr.writingPart1 || []).map((q, idx) => `
                            <div class="bg-white p-3.5 rounded-xl border border-slate-200 space-y-2">
                                <p class="zh-font text-sm font-medium text-slate-900">${q.q}</p>
                                <div class="flex items-center gap-2">
                                    <input type="text" id="wb-w1-${idx}" maxlength="2" placeholder="Gõ 1 chữ Hán..." class="w-full px-3 py-1.5 text-base font-bold text-center border border-slate-300 rounded-lg zh-font focus:outline-none focus:border-rose-700">
                                </div>
                                <div id="wb-w1-fb-${idx}" class="hidden text-xs p-2 rounded-lg"></div>
                            </div>
                        `).join('')}
                    </div>
                    <button onclick="checkWbWriting1()" class="px-4 py-2 rounded-xl bg-rose-800 hover:bg-rose-900 text-white text-xs font-semibold">Kiểm tra Câu 25~27</button>
                </div>

                <div class="p-4 rounded-xl bg-slate-50 border border-slate-200 space-y-4">
                    <div class="flex flex-wrap items-center justify-between gap-2">
                        <p class="text-xs font-bold text-slate-800">Phần 2 (Câu 28~30): Nhìn hình và dùng từ cho sẵn để đặt câu (Hỗ trợ ✨ AI Sửa câu)</p>
                        <button onclick="toggleModal('ai-key-modal', true)" class="text-xs text-amber-800 bg-amber-100/70 px-3 py-1 rounded-lg font-semibold hover:bg-amber-100">🔑 Cài đặt AI Key</button>
                    </div>
                    <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                        ${(pr.writingPart2 || []).map((q, idx) => `
                            <div class="bg-white p-4 rounded-xl border border-slate-200 space-y-3 flex flex-col justify-between">
                                <div class="space-y-2.5">
                                    <div class="flex items-center justify-between">
                                        <span class="text-xs font-bold text-slate-500">Câu ${q.num}</span>
                                        <span class="zh-font text-lg font-bold text-rose-900 bg-rose-50 px-3 py-0.5 rounded-lg border border-rose-200">${q.word}</span>
                                    </div>
                                    ${q.img ? `<div class="flex justify-center bg-slate-50 p-2 rounded-xl border border-slate-100"><img src="${q.img}" alt="Hình câu ${q.num}" class="h-36 object-contain rounded-lg"></div>` : ''}
                                    <textarea id="wb-w2-input-${idx}" rows="2" placeholder="Đặt câu với từ「${q.word}」theo hình trên..." class="w-full p-2.5 text-sm border border-slate-300 rounded-xl zh-font focus:outline-none focus:border-rose-700"></textarea>
                                </div>
                                <div class="space-y-2">
                                    <div class="flex gap-2">
                                        <button onclick="document.getElementById('wb-w2-sample-${idx}').classList.toggle('hidden')" class="flex-1 py-1.5 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-700 text-xs font-semibold">👁️ Câu mẫu</button>
                                        <button id="wb-w2-btn-${idx}" onclick="gradeWbPictureSentence(${idx})" class="flex-1 py-1.5 rounded-lg bg-rose-800 hover:bg-rose-900 text-white text-xs font-semibold">✨ AI Sửa câu</button>
                                    </div>
                                    <div id="wb-w2-sample-${idx}" class="hidden text-xs p-2.5 rounded-lg bg-emerald-50 text-emerald-950 border border-emerald-200">
                                        <strong>Gợi ý chuẩn:</strong> <span class="zh-font font-bold">${q.sample}</span>
                                    </div>
                                    <div id="wb-w2-fb-${idx}" class="hidden"></div>
                                </div>
                            </div>
                        `).join('')}
                    </div>
                </div>
            </div>
        </div>
    `;

    container.innerHTML = html;
}

function checkWbWordFill() {
    const wb = (window.HSK_WORKBOOKS || {})[currentLessonKey];
    if (!wb || !wb.xiaoyuClassroom) return;
    wb.xiaoyuClassroom.wordFill.forEach((wf, idx) => {
        const val = document.getElementById(`wb-wf-${idx}`).value.trim();
        const fb = document.getElementById(`wb-wf-fb-${idx}`);
        fb.classList.remove('hidden');
        const validAnswers = wf.answer.split('/').map(s => s.trim());
        if (validAnswers.includes(val)) {
            fb.textContent = "✅ Đúng";
            fb.className = "text-xs font-bold text-emerald-700";
        } else {
            fb.textContent = `❌ Đáp án: ${wf.answer}`;
            fb.className = "text-xs font-bold text-rose-700";
        }
    });
}

function checkWbListening() {
    const wb = (window.HSK_WORKBOOKS || {})[currentLessonKey];
    if (!wb || !wb.practice) return;
    const pr = wb.practice;

    (pr.listeningPart1 || []).forEach((q, idx) => {
        const val = document.getElementById(`wb-l1-${idx}`).value;
        const fb = document.getElementById(`wb-l1-fb-${idx}`);
        fb.classList.remove('hidden');
        if (val === q.answer) {
            fb.innerHTML = `✅ <strong>Đúng!</strong> ${q.explain}`;
            fb.className = "text-xs p-2 rounded-lg bg-emerald-50 text-emerald-800 border border-emerald-200";
        } else {
            fb.innerHTML = `❌ <strong>Sai.</strong> Đáp án: <strong>${q.answer}</strong>. ${q.explain}`;
            fb.className = "text-xs p-2 rounded-lg bg-rose-50 text-rose-800 border border-rose-200";
        }
    });

    const l23 = [...(pr.listeningPart2 || []), ...(pr.listeningPart3 || [])];
    l23.forEach((q, idx) => {
        const sel = document.querySelector(`input[name="wb-l23-${idx}"]:checked`);
        const fb = document.getElementById(`wb-l23-fb-${idx}`);
        fb.classList.remove('hidden');
        if (sel && sel.value === q.answer) {
            fb.innerHTML = `✅ <strong>Đúng!</strong> ${q.explain}`;
            fb.className = "text-xs p-2 rounded-lg bg-emerald-50 text-emerald-800 border border-emerald-200";
        } else {
            fb.innerHTML = `❌ <strong>Sai.</strong> Đáp án: <strong>${q.answer}</strong>. ${q.explain}`;
            fb.className = "text-xs p-2 rounded-lg bg-rose-50 text-rose-800 border border-rose-200";
        }
    });
}

function checkWbReading() {
    const wb = (window.HSK_WORKBOOKS || {})[currentLessonKey];
    if (!wb || !wb.practice) return;
    const pr = wb.practice;

    (pr.readingPart1 || []).forEach((q, idx) => {
        const val = document.getElementById(`wb-r1-${idx}`).value;
        const fb = document.getElementById(`wb-r1-fb-${idx}`);
        fb.classList.remove('hidden');
        if (val === q.answer) {
            fb.innerHTML = `✅ <strong>Đúng!</strong> ${q.explain}`;
            fb.className = "text-xs p-2 rounded-lg bg-emerald-50 text-emerald-800 border border-emerald-200";
        } else {
            fb.innerHTML = `❌ <strong>Sai.</strong> Đáp án: <strong>${q.answer}</strong>. ${q.explain}`;
            fb.className = "text-xs p-2 rounded-lg bg-rose-50 text-rose-800 border border-rose-200";
        }
    });

    (pr.readingPart2 || []).forEach((q, idx) => {
        const val = document.getElementById(`wb-r2-${idx}`).value;
        const fb = document.getElementById(`wb-r2-fb-${idx}`);
        fb.classList.remove('hidden');
        if (val === q.answer) {
            fb.innerHTML = `✅ <strong>Đúng!</strong> ${q.explain}`;
            fb.className = "text-xs p-2 rounded-lg bg-emerald-50 text-emerald-800 border border-emerald-200";
        } else {
            fb.innerHTML = `❌ <strong>Sai.</strong> Đáp án: <strong>${q.answer}</strong>. ${q.explain}`;
            fb.className = "text-xs p-2 rounded-lg bg-rose-50 text-rose-800 border border-rose-200";
        }
    });

    (pr.readingPart3 || []).forEach((q, idx) => {
        const sel = document.querySelector(`input[name="wb-r3-${idx}"]:checked`);
        const fb = document.getElementById(`wb-r3-fb-${idx}`);
        fb.classList.remove('hidden');
        if (sel && sel.value === q.answer) {
            fb.innerHTML = `✅ <strong>Đúng!</strong> ${q.explain}`;
            fb.className = "text-xs p-2 rounded-lg bg-emerald-50 text-emerald-800 border border-emerald-200";
        } else {
            fb.innerHTML = `❌ <strong>Sai.</strong> Đáp án: <strong>${q.answer}</strong>. ${q.explain}`;
            fb.className = "text-xs p-2 rounded-lg bg-rose-50 text-rose-800 border border-rose-200";
        }
    });
}

function checkWbWriting1() {
    const wb = (window.HSK_WORKBOOKS || {})[currentLessonKey];
    if (!wb || !wb.practice) return;
    (wb.practice.writingPart1 || []).forEach((q, idx) => {
        const val = document.getElementById(`wb-w1-${idx}`).value.trim();
        const fb = document.getElementById(`wb-w1-fb-${idx}`);
        fb.classList.remove('hidden');
        if (val === q.answer) {
            fb.innerHTML = `✅ <strong>Chính xác!</strong> (${q.pinyin}: ${q.meaning})`;
            fb.className = "text-xs p-2 rounded-lg bg-emerald-50 text-emerald-800 border border-emerald-200";
        } else {
            fb.innerHTML = `❌ <strong>Chưa đúng.</strong> Chữ chuẩn là: <strong class="zh-font text-base">${q.answer}</strong> (${q.pinyin}: ${q.meaning})`;
            fb.className = "text-xs p-2 rounded-lg bg-rose-50 text-rose-800 border border-rose-200";
        }
    });
}

function gradeWbPictureSentence(idx) {
    const wb = (window.HSK_WORKBOOKS || {})[currentLessonKey];
    if (!wb || !wb.practice) return;
    const item = wb.practice.writingPart2[idx];
    if (!item) return;
    const userSentence = document.getElementById(`wb-w2-input-${idx}`).value;
    const btnEl = document.getElementById(`wb-w2-btn-${idx}`);
    callGeminiGradeSentence(item.word, item.py, `${item.meaning} — Ngữ cảnh tranh: ${item.contextHint}`, userSentence, `wb-w2-fb-${idx}`, btnEl);
}
window.HSK_WORKSHEETS = window.HSK_WORKSHEETS || {};

const GOOGLE_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbysWYva3wEOT2ePJiYYJxfGbUAHb0HQGKceNWOx8B8V_voKdb94kC9KhvIsqVYcHOF4jw/exec";

function renderWorksheetTab() {
    const container = document.getElementById('worksheet-container');
    if (!container) return;

    const wsData = window.HSK_WORKSHEETS[currentLessonKey] || (currentLesson && currentLesson.worksheet);

    if (!wsData) {
        container.innerHTML = `
            <div class="bg-white p-6 rounded-2xl border border-slate-200 text-sm text-slate-500">
                Chưa có Phiếu bài tập cho bài học này.
            </div>`;
        return;
    }

    let html = `
        <div class="bg-white p-6 sm:p-8 rounded-2xl border border-slate-200 shadow-xs flex flex-col sm:flex-row sm:items-center justify-between gap-4">
            <div>
                <span class="inline-block text-xs font-semibold bg-rose-50 border border-rose-200 text-rose-800 px-3 py-1 rounded-full">
                    Phiếu bài tập thực hành
                </span>
                <h2 class="text-xl sm:text-2xl font-bold text-slate-900 mt-1.5">${wsData.title || 'Phiếu bài tập'}</h2>
                ${wsData.subtitle ? `<p class="text-xs sm:text-sm text-slate-500 mt-1">${wsData.subtitle}</p>` : ''}
            </div>
            <div class="w-full sm:w-64">
                <label class="block text-xs font-semibold text-slate-700 mb-1">Họ tên học viên <span class="text-rose-600">*</span>:</label>
                <input id="ws-student-name" type="text" placeholder="Nhập họ tên bắt buộc..." class="w-full px-3.5 py-2 text-sm bg-slate-50 border border-slate-300 rounded-xl focus:outline-none focus:border-rose-700">
            </div>
        </div>
    `;

    (wsData.parts || []).forEach((part, pIdx) => {
        html += `
            <div class="bg-white p-6 sm:p-8 rounded-2xl border border-slate-200 shadow-xs space-y-5">
                <div>
                    <h3 class="text-lg font-bold text-slate-900">${part.partTitle}</h3>
                    ${part.wordBank && part.wordBank.length ? `
                        <div class="flex flex-wrap gap-2 mt-3 p-3 rounded-xl bg-amber-50/70 border border-amber-200/80">
                            ${part.wordBank.map(w => `<span class="zh-font text-xs sm:text-sm font-semibold text-amber-950 bg-white px-3 py-1 rounded-lg border border-amber-200">${w}</span>`).join('')}
                        </div>
                    ` : ''}
                </div>
                <div class="space-y-4">
        `;

        (part.questions || []).forEach((qItem, qIdx) => {
            const uid = `ws-${pIdx}-${qIdx}`;
            if (qItem.type === 'mc') {
                html += `
                    <div class="p-4 rounded-xl bg-slate-50 border border-slate-200 space-y-2.5">
                        <p class="zh-font text-sm sm:text-base font-medium text-slate-900">${qItem.q}</p>
                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-2">
                            ${(qItem.options || []).map(opt => {
                                const letter = opt.trim().charAt(0);
                                return `
                                    <label class="flex items-center gap-2 p-2.5 rounded-lg bg-white border border-slate-200 hover:border-rose-700 cursor-pointer text-xs sm:text-sm zh-font">
                                        <input type="radio" name="${uid}" value="${letter}" class="accent-rose-800">
                                        <span>${opt}</span>
                                    </label>`;
                            }).join('')}
                        </div>
                        <div id="fb-${uid}" class="hidden text-xs p-2.5 rounded-lg"></div>
                    </div>`;
            } else if (qItem.type === 'ai') {
                html += `
                    <div class="p-4 rounded-xl bg-slate-50 border border-slate-200 space-y-2.5">
                        <div class="flex items-center justify-between gap-2">
                            <p class="zh-font text-sm sm:text-base font-medium text-slate-900">${qItem.q}</p>
                            <span class="shrink-0 text-[11px] font-semibold px-2.5 py-0.5 rounded-full bg-indigo-50 text-indigo-700 border border-indigo-200">✨ AI Chấm</span>
                        </div>
                        <textarea id="input-${uid}" rows="2" placeholder="Nhập câu tiếng Trung của bạn để AI chấm điểm và sửa lỗi..." class="w-full px-3.5 py-2 text-sm bg-white border border-slate-300 rounded-xl focus:outline-none focus:border-indigo-600 zh-font"></textarea>
                        <div id="fb-${uid}" class="hidden text-xs p-3 rounded-lg"></div>
                    </div>`;
            } else {
                html += `
                    <div class="p-4 rounded-xl bg-slate-50 border border-slate-200 space-y-2.5">
                        <p class="zh-font text-sm sm:text-base font-medium text-slate-900">${qItem.q}</p>
                        <input id="input-${uid}" type="text" placeholder="Nhập đáp án tiếng Trung..." class="w-full px-3.5 py-2 text-sm bg-white border border-slate-300 rounded-xl focus:outline-none focus:border-rose-700 zh-font">
                        <div id="fb-${uid}" class="hidden text-xs p-2.5 rounded-lg"></div>
                    </div>`;
            }
        });

        html += `</div></div>`;
    });

    html += `
        <div class="bg-white p-5 rounded-2xl border border-slate-200 flex flex-wrap items-center justify-between gap-4">
            <div class="space-y-1">
                <div id="ws-score-result" class="text-sm font-bold text-rose-800"></div>
                <div id="ws-sync-status" class="text-xs font-medium text-slate-500"></div>
            </div>
            <button id="btn-submit-ws" onclick="submitWorksheet()" class="px-6 py-2.5 rounded-xl bg-rose-800 hover:bg-rose-900 text-white font-semibold text-sm shadow-xs transition-all">
                Nộp Phiếu bài tập & Chấm AI
            </button>
        </div>
    `;

    container.innerHTML = html;
}

function submitWorksheet() {
    const wsData = window.HSK_WORKSHEETS[currentLessonKey] || (currentLesson && currentLesson.worksheet);
    if (!wsData) return;

    const studentNameInput = document.getElementById('ws-student-name');
    const studentName = studentNameInput ? studentNameInput.value.trim() : "";

    if (!studentName) {
        alert("Vui lòng nhập họ tên học viên trước khi nộp bài!");
        studentNameInput?.focus();
        return;
    }

    let autoTotal = 0;
    let autoCorrect = 0;
    let detailLines = [];
    let aiQuestionsPayload = [];
    const clean = s => String(s || '').trim().replace(/[\s，。！？、,.!?]/g, '');

    (wsData.parts || []).forEach((part, pIdx) => {
        (part.questions || []).forEach((qItem, qIdx) => {
            const uid = `ws-${pIdx}-${qIdx}`;
            const fb = document.getElementById(`fb-${uid}`);
            if (fb) fb.classList.remove('hidden');

            if (qItem.type === 'mc') {
                autoTotal++;
                const selected = document.querySelector(`input[name="${uid}"]:checked`);
                const userAns = selected ? selected.value : "(Bỏ trống)";
                const isRight = selected && selected.value === qItem.answer;

                if (isRight) {
                    autoCorrect++;
                    if (fb) {
                        fb.innerHTML = `✅ <strong>Chính xác!</strong> ${qItem.explain || ''}`;
                        fb.className = "text-xs p-2.5 rounded-lg bg-emerald-50 text-emerald-800 border border-emerald-200";
                    }
                } else {
                    if (fb) {
                        fb.innerHTML = `❌ <strong>Chưa đúng.</strong> Đáp án: <strong>${qItem.answer}</strong>. ${qItem.explain || ''}`;
                        fb.className = "text-xs p-2.5 rounded-lg bg-rose-50 text-rose-800 border border-rose-200";
                    }
                }
                detailLines.push(`[TN] ${qItem.q} -> Chọn ${userAns} (${isRight ? 'Đúng' : 'Sai'})`);
            } else if (qItem.type === 'ai') {
                const inputEl = document.getElementById(`input-${uid}`);
                const userAns = inputEl ? inputEl.value.trim() : "";

                if (!userAns) {
                    if (fb) {
                        fb.innerHTML = `⚠️ Bạn đã bỏ trống câu này. Gợi ý mẫu: <strong class="zh-font">${qItem.sampleAnswer || ''}</strong>`;
                        fb.className = "text-xs p-3 rounded-lg bg-amber-50 text-amber-800 border border-amber-200";
                    }
                    detailLines.push(`[AI] ${qItem.q} -> (Bỏ trống)`);
                } else {
                    if (fb) {
                        fb.innerHTML = `⏳ <em>AI đang đọc và chấm câu trả lời của bạn...</em>`;
                        fb.className = "text-xs p-3 rounded-lg bg-indigo-50 text-indigo-800 border border-indigo-200";
                    }
                    aiQuestionsPayload.push({
                        id: uid,
                        question: qItem.q,
                        referenceAnswer: qItem.sampleAnswer || "",
                        studentAnswer: userAns
                    });
                    detailLines.push(`[AI] ${qItem.q} -> Bài làm: "${userAns}"`);
                }
            } else {
                autoTotal++;
                const inputEl = document.getElementById(`input-${uid}`);
                const userAns = inputEl ? inputEl.value.trim() : "";
                const acceptedAnswers = Array.isArray(qItem.answer) ? qItem.answer : [qItem.answer];
                const isRight = inputEl && acceptedAnswers.some(ans => clean(userAns) === clean(ans));

                if (isRight) {
                    autoCorrect++;
                    if (fb) {
                        fb.innerHTML = `✅ <strong>Chính xác!</strong> ${qItem.explain || ''}`;
                        fb.className = "text-xs p-2.5 rounded-lg bg-emerald-50 text-emerald-800 border border-emerald-200";
                    }
                } else {
                    if (fb) {
                        fb.innerHTML = `❌ <strong>Chưa đúng.</strong> Đáp án chuẩn: <strong class="zh-font">${acceptedAnswers[0]}</strong>. ${qItem.explain || ''}`;
                        fb.className = "text-xs p-2.5 rounded-lg bg-rose-50 text-rose-800 border border-rose-200";
                    }
                }
                detailLines.push(`[Điền từ] ${qItem.q} -> "${userAns || 'Bỏ trống'}" (${isRight ? 'Đúng' : 'Sai'})`);
            }
        });
    });

    const scoreText = autoTotal > 0 ? `${autoCorrect}/${autoTotal} (Tự động)` : "Chấm AI";
    document.getElementById('ws-score-result').textContent = autoTotal > 0
        ? `Học viên ${studentName} — Phần trắc nghiệm/điền từ: Đúng ${autoCorrect}/${autoTotal} câu.`
        : `Học viên ${studentName} — Đang xử lý chấm điểm AI...`;

    const syncStatusEl = document.getElementById('ws-sync-status');
    const submitBtn = document.getElementById('btn-submit-ws');

    syncStatusEl.textContent = aiQuestionsPayload.length > 0
        ? "⏳ Đang gửi bài cho AI chấm điểm và lưu về Google Sheets..."
        : "⏳ Đang gửi bài làm cho giáo viên...";
    syncStatusEl.className = "text-xs font-medium text-slate-500";
    submitBtn.disabled = true;
    submitBtn.classList.add("opacity-60");

    // Sử dụng text/plain để tránh lỗi CORS preflight khi nhận phản hồi JSON từ Google Apps Script
    fetch(GOOGLE_SCRIPT_URL, {
        method: "POST",
        headers: { "Content-Type": "text/plain;charset=utf-8" },
        body: JSON.stringify({
            studentName: studentName,
            lessonKey: currentLessonKey,
            worksheetTitle: wsData.title || "Phiếu bài tập",
            score: scoreText,
            details: detailLines.join("\n"),
            aiQuestions: aiQuestionsPayload
        })
    })
    .then(res => res.json())
    .then(data => {
        if (data.aiResults && data.aiResults.length > 0) {
            data.aiResults.forEach(item => {
                const fb = document.getElementById(`fb-${item.id}`);
                if (fb) {
                    const icon = item.isCorrect ? "✅" : "💡";
                    const colorClass = item.isCorrect
                        ? "bg-emerald-50 text-emerald-900 border-emerald-200"
                        : "bg-indigo-50 text-indigo-950 border-indigo-200";
                    fb.innerHTML = `${icon} <strong>AI chấm (${item.score}):</strong> ${item.feedback}`;
                    fb.className = `text-xs p-3 rounded-lg border leading-relaxed ${colorClass}`;
                }
            });
        }
        syncStatusEl.textContent = "✅ Đã chấm điểm xong và gửi kết quả cho giáo viên!";
        syncStatusEl.className = "text-xs font-bold text-emerald-700";
    })
    .catch(() => {
        syncStatusEl.textContent = "⚠️ Đã gửi dữ liệu nhưng không nhận được phản hồi từ AI (kiểm tra lại API Key trong Apps Script).";
        syncStatusEl.className = "text-xs font-bold text-amber-700";
    })
    .finally(() => {
        submitBtn.disabled = false;
        submitBtn.classList.remove("opacity-60");
    });
}
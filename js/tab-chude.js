window.HSK_TOPICS = window.HSK_TOPICS || {};

function renderTopicTab() {
    const container = document.getElementById('topic-container');
    if (!container) return;

    const topicData = window.HSK_TOPICS[currentLessonKey] || (currentLesson && currentLesson.topic);

    if (!topicData) {
        container.innerHTML = `
            <div class="bg-white p-6 rounded-2xl border border-slate-200 text-sm text-slate-500">
                Chưa có nội dung luyện tập theo chủ đề cho bài học này.
            </div>`;
        return;
    }

    let html = `
        <div class="bg-white p-6 sm:p-8 rounded-2xl border border-slate-200 shadow-xs space-y-4">
            <div class="flex flex-wrap items-center justify-between gap-2">
                <span class="inline-block text-xs font-semibold bg-amber-50 border border-amber-200 text-amber-800 px-3 py-1 rounded-full">
                    Luyện tập theo chủ đề
                </span>
            </div>
            <h2 class="text-xl sm:text-2xl font-bold text-slate-900">${topicData.title || 'Luyện tập theo chủ đề'}</h2>
            ${topicData.description ? `<p class="text-sm text-slate-600 leading-relaxed">${topicData.description}</p>` : ''}
            
            ${topicData.keyPhrases && topicData.keyPhrases.length ? `
                <div class="pt-2">
                    <p class="text-xs font-bold uppercase tracking-wider text-slate-400 mb-2">Mẫu câu gợi ý theo chủ đề:</p>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-2.5">
                        ${topicData.keyPhrases.map(kp => `
                            <div class="p-3 rounded-xl bg-amber-50/50 border border-amber-200/70 flex items-center justify-between gap-2">
                                <div>
                                    <p class="zh-font text-sm font-bold text-slate-900">${kp.zh}</p>
                                    <p class="text-xs text-rose-800">${kp.py}</p>
                                    <p class="text-xs text-slate-500">${kp.vi}</p>
                                </div>
                                <button onclick="speakText('${escapeJsSingleQuote(kp.zh)}')" class="w-8 h-8 rounded-lg bg-white border border-amber-200 text-rose-700 flex items-center justify-center shrink-0">🔊</button>
                            </div>
                        `).join('')}
                    </div>
                </div>
            ` : ''}
        </div>
    `;

    (topicData.sections || []).forEach((sec, sIdx) => {
        html += `
            <div class="bg-white p-6 sm:p-8 rounded-2xl border border-slate-200 shadow-xs space-y-5">
                <div>
                    <h3 class="text-lg font-bold text-slate-900">${sec.heading}</h3>
                    ${sec.instruction ? `<p class="text-xs sm:text-sm text-slate-500 mt-1">${sec.instruction}</p>` : ''}
                </div>
                <div class="space-y-4">
        `;

        (sec.items || []).forEach((item, iIdx) => {
            const uid = `topic-${sIdx}-${iIdx}`;
            if (item.type === 'mc') {
                html += `
                    <div class="p-4 rounded-xl bg-slate-50 border border-slate-200 space-y-2.5">
                        <p class="zh-font text-sm sm:text-base font-medium text-slate-900">${item.q}</p>
                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-2">
                            ${(item.options || []).map(opt => {
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
            } else {
                html += `
                    <div class="p-4 rounded-xl bg-slate-50 border border-slate-200 space-y-2.5">
                        <p class="zh-font text-sm sm:text-base font-medium text-slate-900">${item.q}</p>
                        <textarea id="input-${uid}" rows="2" placeholder="Nhập câu trả lời bằng tiếng Trung của bạn..." class="w-full px-3.5 py-2 text-sm bg-white border border-slate-300 rounded-xl focus:outline-none focus:border-rose-700 zh-font"></textarea>
                        <div id="fb-${uid}" class="hidden text-xs p-3 rounded-lg bg-amber-50/80 text-amber-950 border border-amber-200 space-y-1">
                            <div><strong>Đáp án tham khảo:</strong> <span class="zh-font font-bold text-rose-900">${item.sampleZh || ''}</span></div>
                            ${item.samplePy ? `<div class="text-rose-800">${item.samplePy}</div>` : ''}
                            ${item.sampleVi ? `<div class="text-slate-600"><em>(${item.sampleVi})</em></div>` : ''}
                        </div>
                    </div>`;
            }
        });

        html += `</div></div>`;
    });

    html += `
        <div class="bg-white p-5 rounded-2xl border border-slate-200 flex flex-wrap items-center justify-between gap-4">
            <span id="topic-score-result" class="text-sm font-bold text-rose-800"></span>
            <button onclick="submitTopicExercises()" class="px-6 py-2.5 rounded-xl bg-rose-800 hover:bg-rose-900 text-white font-semibold text-sm shadow-xs">
                Nộp bài & Xem gợi ý
            </button>
        </div>
    `;

    container.innerHTML = html;
}

function submitTopicExercises() {
    const topicData = window.HSK_TOPICS[currentLessonKey] || (currentLesson && currentLesson.topic);
    if (!topicData) return;

    let mcTotal = 0;
    let mcCorrect = 0;

    (topicData.sections || []).forEach((sec, sIdx) => {
        (sec.items || []).forEach((item, iIdx) => {
            const uid = `topic-${sIdx}-${iIdx}`;
            const fb = document.getElementById(`fb-${uid}`);
            if (!fb) return;
            fb.classList.remove('hidden');

            if (item.type === 'mc') {
                mcTotal++;
                const selected = document.querySelector(`input[name="${uid}"]:checked`);
                if (selected && selected.value === item.answer) {
                    mcCorrect++;
                    fb.innerHTML = `✅ <strong>Chính xác!</strong> ${item.explain || ''}`;
                    fb.className = "text-xs p-2.5 rounded-lg bg-emerald-50 text-emerald-800 border border-emerald-200";
                } else {
                    fb.innerHTML = `❌ <strong>Chưa đúng.</strong> Đáp án: <strong>${item.answer}</strong>. ${item.explain || ''}`;
                    fb.className = "text-xs p-2.5 rounded-lg bg-rose-50 text-rose-800 border border-rose-200";
                }
            }
        });
    });

    const resultEl = document.getElementById('topic-score-result');
    if (resultEl) {
        resultEl.textContent = mcTotal > 0
            ? `Trắc nghiệm: Đúng ${mcCorrect}/${mcTotal} câu (Đã hiển thị gợi ý phần tự luận).`
            : `Đã hiển thị gợi ý cho tất cả tình huống.`;
    }
}

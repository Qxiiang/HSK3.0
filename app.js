// ============================================================================
// ENGINE XỬ LÝ GIAO DIỆN CHUNG - GIÁO TRÌNH HSK 3.0
// ============================================================================

const booksMeta = [
    { code: "1", name: "Quyển 1" },
    { code: "2", name: "Quyển 2" },
    { code: "3", name: "Quyển 3" },
    { code: "4A", name: "Quyển 4A" },
    { code: "4B", name: "Quyển 4B" },
    { code: "5A", name: "Quyển 5A" },
    { code: "5B", name: "Quyển 5B" },
    { code: "6A", name: "Quyển 6A" },
    { code: "6B", name: "Quyển 6B" }
];

let selectedBookCode = "3";
let currentLessonKey = "3_1";
let currentLesson = null;
let sidebarSearchQuery = "";

let activeVocabFilter = 'all';
let activeVocabView = 'fc';
let currentFcIndex = 0;
let filteredVocabList = [];
let currentFcWord = null;

let activeTextFilter = 'all';
let showPinyinSetting = true;
let showViSetting = true;
let activeGrammarFilter = 'all';

let currentStrokeWord = null;
let strokeWriterInstances = [];
let currentActiveGrammarId = 1;
let currentActiveTextNum = 1;

function escapeJsSingleQuote(str) {
    if (!str) return "";
    return String(str)
        .replace(/\\/g, "\\\\")
        .replace(/'/g, "\\'")
        .replace(/"/g, "&quot;")
        .replace(/\r?\n/g, " ");
}

function initApp() {
    renderBooksGrid();
    updateAiKeyBadge();
    if (typeof updateExcelStatusBadge === 'function') {
        updateExcelStatusBadge();
    }
}

window.addEventListener('DOMContentLoaded', () => {
    initApp();
});

window.addEventListener('hskDataLoaded', () => {
    renderBooksGrid();
});

function getLessonsByBook(bookCode) {
    const allLessons = Object.entries(window.HSK_LESSONS || {});
    return allLessons
        .filter(([_, data]) => data && data.bookCode === bookCode)
        .sort((a, b) => (a[1].lessonNum || 0) - (b[1].lessonNum || 0));
}

function renderBooksGrid() {
    const grid = document.getElementById('books-grid');
    if (!grid) return;
    grid.innerHTML = booksMeta.map(book => {
        const lessons = getLessonsByBook(book.code);
        const hasData = lessons.length > 0;
        const isSelected = book.code === selectedBookCode;
        const statusText = hasData ? `${lessons.length} bài đã nạp` : "Chưa có bài";
        const badgeClass = hasData
            ? "border-amber-500/80 text-amber-800 bg-amber-50/40"
            : "border-slate-300 text-slate-400 bg-slate-50/50";
        const progress = hasData ? Math.min(100, Math.round((lessons.length / 18) * 100)) : 0;

        return `
            <div onclick="handleBookClick('${book.code}')" class="book-card ${isSelected ? 'selected' : ''} rounded-2xl p-5 sm:p-6 cursor-pointer flex flex-col justify-between space-y-4">
                <div class="space-y-1">
                    <div class="text-2xl sm:text-3xl font-bold text-[#a32222] tracking-tight">${book.code}</div>
                    <div class="flex items-center justify-between gap-2 pt-0.5">
                        <span class="text-base font-bold text-slate-900">${book.name}</span>
                        <span class="px-3 py-0.5 rounded-full border text-xs font-medium ${badgeClass}">
                            ${statusText}
                        </span>
                    </div>
                </div>
                <div class="w-full h-1.5 bg-slate-200/80 rounded-full overflow-hidden">
                    <div class="h-full bg-[#15803d] rounded-full transition-all duration-300" style="width: ${progress}%"></div>
                </div>
            </div>
        `;
    }).join('');
}

function handleBookClick(code) {
    selectedBookCode = code;
    renderBooksGrid();
    const lessons = getLessonsByBook(code);
    if (lessons.length > 0) {
        openBookLesson(code);
    } else {
        const book = booksMeta.find(b => b.code === code);
        document.getElementById('empty-book-title').textContent = `${book ? book.name : code} — Chưa có bài`;
        toggleModal('empty-book-modal', true);
    }
}

function openBookLesson(code) {
    selectedBookCode = code;
    const lessons = getLessonsByBook(code);
    if (!lessons.length) return;

    sidebarSearchQuery = "";
    const searchInput = document.getElementById('sidebar-lesson-search');
    if (searchInput) searchInput.value = "";

    populateSidebarBookSelect(code);
    renderLessonSidebar(lessons);
    switchLessonByKey(lessons[0][0]);

    document.getElementById('view-dashboard').classList.add('hidden');
    document.getElementById('view-lesson').classList.remove('hidden');
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

// --- XỬ LÝ CỘT TRÁI CHỌN BÀI HỌC ---
function toggleMobileSidebar(forceState) {
    const sidebar = document.getElementById('lesson-sidebar');
    const backdrop = document.getElementById('sidebar-backdrop');
    if (!sidebar || !backdrop) return;

    const isCurrentlyClosed = sidebar.classList.contains('-translate-x-full');
    const shouldOpen = typeof forceState === 'boolean' ? forceState : isCurrentlyClosed;

    if (shouldOpen) {
        sidebar.classList.remove('-translate-x-full');
        backdrop.classList.remove('hidden');
    } else {
        sidebar.classList.add('-translate-x-full');
        backdrop.classList.add('hidden');
    }
}

function populateSidebarBookSelect(activeCode) {
    const select = document.getElementById('sidebar-book-select');
    if (!select) return;
    select.innerHTML = booksMeta.map(b => {
        const count = getLessonsByBook(b.code).length;
        const disabledAttr = count === 0 ? 'disabled' : '';
        const label = count > 0 ? `Giáo trình HSK 3.0 — ${b.name} (${count} bài)` : `${b.name} (Chưa có dữ liệu)`;
        return `<option value="${b.code}" ${b.code === activeCode ? 'selected' : ''} ${disabledAttr}>${label}</option>`;
    }).join('');
}

function handleSidebarBookChange(newBookCode) {
    const lessons = getLessonsByBook(newBookCode);
    if (!lessons.length) return;
    selectedBookCode = newBookCode;
    sidebarSearchQuery = "";
    const searchInput = document.getElementById('sidebar-lesson-search');
    if (searchInput) searchInput.value = "";
    switchLessonByKey(lessons[0][0]);
}

function filterSidebarLessons(query) {
    sidebarSearchQuery = query.trim().toLowerCase();
    if (currentLesson) {
        const lessons = getLessonsByBook(currentLesson.bookCode);
        renderLessonSidebar(lessons);
    }
}

function renderLessonSidebar(lessons) {
    const listEl = document.getElementById('lesson-sidebar-list');
    const countEl = document.getElementById('sidebar-lesson-count');
    const titleEl = document.getElementById('sidebar-book-title');
    if (!listEl) return;

    const bookMeta = booksMeta.find(b => b.code === selectedBookCode);
    if (titleEl && bookMeta) {
        titleEl.textContent = `Danh sách bài • ${bookMeta.name}`;
    }

    const filtered = lessons.filter(([_, data]) => {
        if (!sidebarSearchQuery) return true;
        const numStr = `bài ${data.lessonNum}`;
        const zh = (data.titleZh || '').toLowerCase();
        const vi = (data.titleVi || '').toLowerCase();
        const py = (data.titlePy || '').toLowerCase();
        return numStr.includes(sidebarSearchQuery) ||
               String(data.lessonNum) === sidebarSearchQuery ||
               zh.includes(sidebarSearchQuery) ||
               vi.includes(sidebarSearchQuery) ||
               py.includes(sidebarSearchQuery);
    });

    if (countEl) {
        countEl.textContent = `Hiển thị ${filtered.length} / ${lessons.length} bài`;
    }

    if (filtered.length === 0) {
        listEl.innerHTML = `<div class="p-4 text-center text-xs text-slate-400">Không tìm thấy bài học phù hợp.</div>`;
        return;
    }

    listEl.innerHTML = filtered.map(([key, data]) => {
        const isActive = key === currentLessonKey;
        const hasWb = Boolean((window.HSK_WORKBOOKS || {})[key]);
        return `
            <button onclick="switchLessonByKey('${key}'); toggleMobileSidebar(false);"
                    id="sidebar-item-${key}"
                    class="lesson-sidebar-item ${isActive ? 'active' : 'bg-white border-slate-200/80 text-slate-800'} w-full text-left p-3 rounded-xl border flex items-start gap-2.5">
                <span class="w-7 h-7 rounded-lg text-xs font-bold flex items-center justify-center shrink-0 mt-0.5 ${isActive ? 'bg-white text-rose-900' : 'bg-rose-50 text-rose-800 border border-rose-200/70'}">
                    ${data.lessonNum}
                </span>
                <div class="min-w-0 flex-1">
                    <div class="flex items-center justify-between gap-1">
                        <span class="zh-font text-sm font-bold truncate ${isActive ? 'text-white' : 'text-slate-900'}">${data.titleZh || ''}</span>
                        ${hasWb ? `<span title="Có Sách bài tập" class="text-[10px] px-1.5 py-0.5 rounded font-semibold shrink-0 ${isActive ? 'bg-white/20 text-amber-200' : 'bg-amber-50 text-amber-800 border border-amber-200/80'}">BT</span>` : ''}
                    </div>
                    <p class="text-[11px] truncate mt-0.5 ${isActive ? 'text-amber-100' : 'text-slate-500'}">${data.titleVi || data.titlePy || ''}</p>
                </div>
            </button>
        `;
    }).join('');
}

function switchLessonByKey(key) {
    const lesson = (window.HSK_LESSONS || {})[key];
    if (!lesson) return;
    currentLessonKey = key;
    currentLesson = lesson;
    selectedBookCode = lesson.bookCode;

    populateSidebarBookSelect(lesson.bookCode);
    const lessons = getLessonsByBook(lesson.bookCode);
    renderLessonSidebar(lessons);

    setTimeout(() => {
        const activeItem = document.getElementById(`sidebar-item-${key}`);
        if (activeItem) {
            activeItem.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
        }
    }, 50);

    document.getElementById('lesson-badge-title').textContent = lesson.badgeTitle || '';
    document.getElementById('lesson-title-zh').textContent = `Bài ${lesson.lessonNum}: ${lesson.titleZh || ''}`;
    document.getElementById('lesson-title-py').textContent = lesson.titlePy || '';
    document.getElementById('lesson-title-vi').textContent = lesson.titleVi || '';

    document.getElementById('goal-modal-list').innerHTML = (lesson.goals || []).map((g, i) => `
        <div class="p-3.5 rounded-xl ${i === 0 ? 'bg-rose-50 border border-rose-100' : 'bg-slate-50 border border-slate-200'} flex gap-3">
            <span class="font-bold text-rose-800">${i + 1}.</span>
            <p>${g}</p>
        </div>
    `).join('');

    activeVocabFilter = 'all';
    activeTextFilter = 'all';
    activeGrammarFilter = 'all';
    document.getElementById('vocab-search').value = '';

    buildFilterBars();
    applyVocabFilterAndSearch('');
    renderTexts();
    renderGrammar();
    renderPracticeSection();
    renderWorksheetSection();
    renderTopicSection();
    if (typeof renderWorkbookSection === 'function') {
        renderWorkbookSection();
    }
}

function buildFilterBars() {
    const vocab = currentLesson.vocab || [];
    const texts = currentLesson.texts || [];
    const grammar = currentLesson.grammar || [];

    document.getElementById('vocab-total-count').textContent = vocab.length;
    document.getElementById('texts-total-count').textContent = texts.length;
    document.getElementById('grammar-total-count').textContent = grammar.length;

    const textNums = [...new Set(vocab.map(v => v.text))].sort((a, b) => a - b);
    document.getElementById('vocab-filter-bar').innerHTML =
        `<button onclick="setVocabFilter('all', this)" class="pill-filter active px-4 py-1.5 rounded-full text-xs sm:text-sm font-medium">Tất cả (${vocab.length})</button>` +
        textNums.map(num => {
            const count = vocab.filter(v => v.text === num).length;
            return `<button onclick="setVocabFilter(${num}, this)" class="pill-filter px-4 py-1.5 rounded-full text-xs sm:text-sm font-medium">Bài ${num} (${count})</button>`;
        }).join('');

    document.getElementById('texts-filter-bar').innerHTML =
        `<button onclick="filterTexts('all', this)" class="pill-filter active px-4 py-1.5 rounded-full text-xs font-medium">Tất cả bài khóa</button>` +
        texts.map(t => `<button onclick="filterTexts(${t.textNum}, this)" class="pill-filter px-4 py-1.5 rounded-full text-xs font-medium">Bài khóa ${t.textNum}</button>`).join('');

    const grammarTextNums = [...new Set(grammar.map(g => g.textNum))].sort((a, b) => a - b);
    document.getElementById('grammar-filter-bar').innerHTML =
        `<button onclick="filterGrammar('all', this)" class="pill-filter active px-4 py-1.5 rounded-full text-xs font-medium">Tất cả ngữ pháp (${grammar.length})</button>` +
        grammarTextNums.map(num => {
            const count = grammar.filter(g => g.textNum === num).length;
            const label = count > 1 ? `Bài khóa ${num} (${count})` : `Bài khóa ${num}`;
            return `<button onclick="filterGrammar(${num}, this)" class="pill-filter px-4 py-1.5 rounded-full text-xs font-medium">${label}</button>`;
        }).join('');
}

function navigateToDashboard() {
    toggleMobileSidebar(false);
    document.getElementById('view-lesson').classList.add('hidden');
    document.getElementById('view-dashboard').classList.remove('hidden');
    renderBooksGrid();
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

function switchMainTab(tabId, btn) {
    document.querySelectorAll('.nav-tab').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    document.querySelectorAll('main > section').forEach(s => s.classList.add('hidden'));
    document.getElementById(`tab-${tabId}`).classList.remove('hidden');
}

function toggleModal(modalId, show) {
    document.getElementById(modalId).classList.toggle('hidden', !show);
}

// --- TAB 1: TỪ VỰNG ---
function setVocabFilter(filterVal, btn) {
    activeVocabFilter = filterVal;
    document.querySelectorAll('#vocab-filter-bar button').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    applyVocabFilterAndSearch(document.getElementById('vocab-search').value);
}

function handleVocabSearch(query) {
    applyVocabFilterAndSearch(query);
}

function applyVocabFilterAndSearch(searchQuery = '') {
    const vocab = currentLesson ? (currentLesson.vocab || []) : [];
    const q = searchQuery.trim().toLowerCase();
    filteredVocabList = vocab.filter(v => {
        const matchFilter = activeVocabFilter === 'all' || v.text === activeVocabFilter;
        const matchCollo = (v.collocations || []).some(c => c.toLowerCase().includes(q));
        const matchQuery = !q || v.hz.includes(q) || v.py.toLowerCase().includes(q) || v.vi.toLowerCase().includes(q) || matchCollo;
        return matchFilter && matchQuery;
    });
    currentFcIndex = 0;
    renderVocab();
}

function switchVocabView(viewMode) {
    activeVocabView = viewMode;
    document.getElementById('btn-mode-fc').classList.toggle('active', viewMode === 'fc');
    document.getElementById('btn-mode-grid').classList.toggle('active', viewMode === 'grid');
    document.getElementById('vocab-view-fc').classList.toggle('hidden', viewMode !== 'fc');
    document.getElementById('vocab-view-grid').classList.toggle('hidden', viewMode !== 'grid');
    if (viewMode === 'grid') renderVocabGrid();
}

function renderVocab() {
    if (filteredVocabList.length > 0) {
        currentFcWord = filteredVocabList[currentFcIndex];
        document.getElementById('fc-counter').textContent = `Thẻ ${currentFcIndex + 1} / ${filteredVocabList.length}`;
        document.getElementById('fc-text-num').textContent = `Bài khóa ${currentFcWord.text}`;
        document.getElementById('fc-hz').textContent = currentFcWord.hz;
        document.getElementById('fc-py').textContent = currentFcWord.py;
        document.getElementById('fc-vi').textContent = currentFcWord.vi;
        document.getElementById('fc-memo').textContent = currentFcWord.memo || 'Ghi nhớ theo ngữ cảnh bài học.';

        const mwEl = document.getElementById('fc-mw');
        const mwWrap = document.getElementById('fc-mw-wrapper');
        if (currentFcWord.mw && currentFcWord.mw.length > 0) {
            mwEl.textContent = currentFcWord.mw.join(', ');
            mwWrap.classList.remove('hidden');
        } else {
            mwWrap.classList.add('hidden');
        }

        const synEl = document.getElementById('fc-syn');
        const synWrap = document.getElementById('fc-syn-wrapper');
        if (currentFcWord.syn && currentFcWord.syn.length > 0) {
            synEl.textContent = currentFcWord.syn.join(', ');
            synWrap.classList.remove('hidden');
        } else {
            synWrap.classList.add('hidden');
        }

        const antEl = document.getElementById('fc-ant');
        const antWrap = document.getElementById('fc-ant-wrapper');
        if (currentFcWord.ant && currentFcWord.ant.length > 0) {
            antEl.textContent = currentFcWord.ant.join(', ');
            antWrap.classList.remove('hidden');
        } else {
            antWrap.classList.add('hidden');
        }

        document.getElementById('fc-collo').innerHTML = (currentFcWord.collocations || [])
            .map(c => `<span onclick="event.stopPropagation(); speakText('${escapeJsSingleQuote(c)}')" class="text-[11px] bg-white/25 hover:bg-white/40 px-2.5 py-0.5 rounded-full cursor-pointer transition-colors">🔊 ${c}</span>`)
            .join('');
    } else {
        currentFcWord = null;
        document.getElementById('fc-counter').textContent = `Không tìm thấy từ vựng`;
        document.getElementById('fc-hz').textContent = '—';
        document.getElementById('fc-py').textContent = '';
        document.getElementById('fc-vi').textContent = 'Không có kết quả';
        document.getElementById('fc-memo').textContent = '';
        document.getElementById('fc-collo').innerHTML = '';
    }
    if (activeVocabView === 'grid') renderVocabGrid();
}

function moveFc(step) {
    if (!filteredVocabList.length) return;
    currentFcIndex = (currentFcIndex + step + filteredVocabList.length) % filteredVocabList.length;
    const cardInner = document.querySelector('#vocab-view-fc .preserve-3d');
    if (cardInner && cardInner.classList.contains('rotate-y-180')) {
        cardInner.classList.remove('rotate-y-180');
    }
    renderVocab();
}

function shuffleVocab() {
    filteredVocabList.sort(() => Math.random() - 0.5);
    currentFcIndex = 0;
    renderVocab();
}

function toggleCardFlip(cardEl) {
    cardEl.querySelector('.preserve-3d').classList.toggle('rotate-y-180');
}

function renderVocabGrid() {
    const gridContainer = document.getElementById('vocab-view-grid');
    gridContainer.innerHTML = filteredVocabList.map(v => `
        <div onclick="openStrokeModal(${v.id})" class="vocab-card p-5 rounded-2xl flex flex-col justify-between cursor-pointer group">
            <div>
                <div class="flex justify-between items-start mb-2">
                    <div>
                        <span class="zh-font text-3xl font-bold text-slate-900 group-hover:text-rose-800 transition-colors">${v.hz}</span>
                        <span class="ml-2 text-sm text-rose-800 font-semibold">${v.py}</span>
                    </div>
                    <div class="flex items-center gap-1.5">
                        <button onclick="event.stopPropagation(); openStrokeModal(${v.id})" class="px-2.5 h-8 rounded-lg bg-slate-100 hover:bg-amber-50 text-slate-700 hover:text-amber-800 flex items-center justify-center text-xs font-semibold gap-1">
                            <span>✍️</span><span class="hidden sm:inline">Viết</span>
                        </button>
                        <button onclick="event.stopPropagation(); speakText('${escapeJsSingleQuote(v.hz)}')" class="w-8 h-8 rounded-lg bg-slate-100 hover:bg-rose-50 text-rose-700 flex items-center justify-center text-sm">🔊</button>
                    </div>
                </div>
                <div class="flex items-center gap-2 mb-2">
                    <span class="text-xs bg-slate-100 text-slate-600 px-2 py-0.5 rounded font-medium">${v.pos}</span>
                    <span class="text-xs bg-amber-50 text-amber-800 px-2 py-0.5 rounded font-medium">Bài khóa ${v.text}</span>
                </div>
                <p class="text-base font-bold text-slate-800">${v.vi}</p>
                ${v.memo ? `<p class="text-xs bg-slate-50 text-slate-600 p-2 rounded-xl mt-2 border border-slate-100">💡 ${v.memo}</p>` : ''}
            </div>
            <div class="mt-3 space-y-1.5 text-xs text-slate-600">
                ${v.mw && v.mw.length ? `<div><strong class="text-slate-500">Lượng từ:</strong> <span class="font-medium text-slate-800">${v.mw.join(', ')}</span></div>` : ''}
                ${v.syn && v.syn.length ? `<div><strong class="text-slate-500">Đồng nghĩa:</strong> <span class="font-medium text-rose-800">${v.syn.join(', ')}</span></div>` : ''}
                ${v.ant && v.ant.length ? `<div><strong class="text-slate-500">Trái nghĩa:</strong> <span class="font-medium text-slate-800">${v.ant.join(', ')}</span></div>` : ''}
            </div>
            ${v.collocations && v.collocations.length ? `
            <div class="mt-3 pt-3 border-t border-slate-100">
                <p class="text-[11px] font-semibold text-slate-400 uppercase tracking-wider mb-1.5">Cụm từ thường gặp:</p>
                <div class="flex flex-wrap gap-1.5">
                    ${v.collocations.map(c => `<span onclick="event.stopPropagation(); speakText('${escapeJsSingleQuote(c)}')" title="Bấm để nghe" class="zh-font text-xs bg-rose-50/70 hover:bg-rose-100 text-rose-900 border border-rose-200/70 px-2.5 py-0.5 rounded-lg transition-colors">${c}</span>`).join('')}
                </div>
            </div>` : ''}
        </div>
    `).join('');
}

// --- HANZI WRITER ---
function openStrokeModal(wordId) {
    const vocab = currentLesson ? (currentLesson.vocab || []) : [];
    const word = vocab.find(v => v.id === wordId);
    if (!word) return;
    currentStrokeWord = word;

    document.getElementById('stroke-word-hz').textContent = word.hz;
    document.getElementById('stroke-word-py').textContent = word.py;
    document.getElementById('stroke-word-vi').textContent = `${word.pos} — ${word.vi}`;
    document.getElementById('stroke-memo-tip').innerHTML = word.memo
        ? `💡 Ghi nhớ: <strong>${word.memo}</strong>`
        : `💡 Bấm <strong>Xem nét</strong> để xem thứ tự nét hoặc <strong>Tập viết</strong> để tự tô theo nét.`;

    const container = document.getElementById('stroke-characters-container');
    const chars = Array.from(word.hz);

    container.className = chars.length === 1
        ? "grid grid-cols-1 gap-6 justify-items-center"
        : chars.length === 2
            ? "grid grid-cols-1 sm:grid-cols-2 gap-6 justify-items-center"
            : "grid grid-cols-1 sm:grid-cols-3 gap-5 justify-items-center";

    container.innerHTML = chars.map((ch, idx) => `
        <div class="bg-slate-50 border border-slate-200 rounded-2xl p-4 flex flex-col items-center space-y-3 w-full max-w-[230px]">
            <div class="flex items-center justify-between w-full text-xs text-slate-500">
                <span class="font-bold text-slate-700">Chữ ${idx + 1}: <span class="zh-font text-base text-rose-800">${ch}</span></span>
                <span id="stroke-status-${idx}" class="text-[11px] font-medium text-slate-400">Thứ tự nét</span>
            </div>
            <div id="hanzi-target-${idx}" class="hanzi-grid-bg w-[170px] h-[170px] rounded-xl border-2 border-slate-300 shadow-2xs flex items-center justify-center overflow-hidden"></div>
            <div class="flex gap-2 w-full">
                <button onclick="animateSingleWriter(${idx})" class="flex-1 py-1.5 rounded-lg bg-white border border-slate-200 hover:bg-rose-50 hover:text-rose-800 text-xs font-semibold text-slate-700">▶ Xem nét</button>
                <button onclick="quizSingleWriter(${idx})" class="flex-1 py-1.5 rounded-lg bg-amber-50 border border-amber-200 hover:bg-amber-100 text-xs font-semibold text-amber-900">✍️ Tập viết</button>
            </div>
        </div>
    `).join('');

    toggleModal('stroke-modal', true);

    strokeWriterInstances = [];
    chars.forEach((ch, idx) => {
        if (typeof HanziWriter !== 'undefined') {
            const writer = HanziWriter.create(`hanzi-target-${idx}`, ch, {
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
            setTimeout(() => writer.animateCharacter(), 200 + idx * 350);
        }
    });
}

function animateSingleWriter(idx) {
    const writer = strokeWriterInstances[idx];
    if (!writer) return;
    document.getElementById(`stroke-status-${idx}`).textContent = "Đang viết mẫu...";
    writer.cancelQuiz();
    writer.showOutline();
    writer.animateCharacter({
        onComplete: () => {
            document.getElementById(`stroke-status-${idx}`).textContent = "Hoàn thành";
        }
    });
}

function quizSingleWriter(idx) {
    const writer = strokeWriterInstances[idx];
    if (!writer) return;
    const statusEl = document.getElementById(`stroke-status-${idx}`);
    statusEl.textContent = "Tô theo khung...";
    statusEl.className = "text-[11px] font-semibold text-amber-700";
    writer.quiz({
        onMistake: function() {
            statusEl.textContent = "Sai nét, thử lại!";
            statusEl.className = "text-[11px] font-semibold text-rose-600";
        },
        onCorrectStroke: function(strokeData) {
            statusEl.textContent = `Đúng nét ${strokeData.strokeNum + 1}`;
            statusEl.className = "text-[11px] font-semibold text-emerald-700";
        },
        onComplete: function() {
            statusEl.textContent = "🎉 Viết xong!";
            statusEl.className = "text-[11px] font-bold text-emerald-700";
        }
    });
}

function animateAllStrokeWriters() {
    strokeWriterInstances.forEach((writer, idx) => {
        setTimeout(() => animateSingleWriter(idx), idx * 450);
    });
}

function speakText(text) {
    if (!('speechSynthesis' in window) || !text) return;
    window.speechSynthesis.cancel();
    const cleanZh = String(text).replace(/男[:：]|女[:：]/g, ' ');
    const utt = new SpeechSynthesisUtterance(cleanZh);
    utt.lang = 'zh-CN';
    utt.rate = 0.92;
    window.speechSynthesis.speak(utt);
}

// --- TAB 2: BÀI KHÓA ---
function filterTexts(filterNum, btn) {
    activeTextFilter = filterNum;
    document.querySelectorAll('#texts-filter-bar button').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    renderTexts();
}

function toggleSetting(type) {
    if (type === 'pinyin') {
        showPinyinSetting = !showPinyinSetting;
        document.getElementById('btn-toggle-py').classList.toggle('active', showPinyinSetting);
    } else if (type === 'vi') {
        showViSetting = !showViSetting;
        document.getElementById('btn-toggle-vi').classList.toggle('active', showViSetting);
    }
    renderTexts();
}

function renderTexts() {
    const container = document.getElementById('texts-container');
    const texts = currentLesson ? (currentLesson.texts || []) : [];
    const list = activeTextFilter === 'all' ? texts : texts.filter(t => t.textNum === activeTextFilter);

    container.innerHTML = list.map(t => `
        <div class="bg-white p-6 sm:p-8 rounded-2xl border border-slate-200 shadow-xs space-y-5">
            <div class="flex flex-wrap items-center justify-between gap-3 border-b border-slate-100 pb-4">
                <div>
                    <span class="text-xs font-bold uppercase tracking-wider text-rose-800">Bài khóa ${t.textNum}</span>
                    <h3 class="text-xl font-bold text-slate-900 mt-0.5">${t.title}</h3>
                    <p class="text-xs text-slate-500 mt-0.5">${t.context}</p>
                </div>
                <div class="flex items-center gap-2 shrink-0">
                    <button onclick="openTextExercise(${t.textNum})" class="px-3.5 py-2 rounded-xl bg-rose-800 hover:bg-rose-900 text-white text-xs font-semibold flex items-center gap-1.5 shadow-2xs transition-colors">
                        <span>✏️</span> <span>Luyện tập</span>
                    </button>
                    <button onclick="playTextParagraph(${t.textNum})" class="pill-filter px-3.5 py-2 rounded-xl text-xs font-semibold flex items-center gap-1.5 shadow-2xs">
                        <span>▶</span> <span>Phát đoạn này</span>
                    </button>
                </div>
            </div>
            <div class="space-y-4">
                ${t.lines ? t.lines.map(l => `
                    <div class="space-y-1">
                        <p class="zh-font text-lg text-slate-900">
                            <strong class="text-slate-600 font-semibold">${l.speaker}:</strong> ${l.text}
                            <button onclick="speakText('${escapeJsSingleQuote(l.text)}')" class="ml-2 text-rose-700 text-xs">🔊</button>
                        </p>
                        <p class="text-sm text-rose-800 font-medium ${showPinyinSetting ? '' : 'hidden'}">${l.pinyin}</p>
                        <p class="text-sm text-slate-500 ${showViSetting ? '' : 'hidden'}">${l.vi}</p>
                    </div>
                `).join('') : (t.paragraphs || []).map(p => `
                    <div class="space-y-1">
                        <p class="zh-font text-lg text-slate-900 leading-relaxed">
                            ${p.text}
                            <button onclick="speakText('${escapeJsSingleQuote(p.text)}')" class="ml-2 text-rose-700 text-xs">🔊</button>
                        </p>
                        <p class="text-sm text-rose-800 font-medium ${showPinyinSetting ? '' : 'hidden'}">${p.pinyin}</p>
                        <p class="text-sm text-slate-500 ${showViSetting ? '' : 'hidden'}">${p.vi}</p>
                    </div>
                `).join('')}
            </div>
        </div>
    `).join('');
}

function openTextExercise(textNum) {
    currentActiveTextNum = textNum;
    const texts = currentLesson ? (currentLesson.texts || []) : [];
    const item = texts.find(t => t.textNum === textNum);
    if (!item) return;

    document.getElementById('text-ex-modal-badge').textContent = `Bài tập luyện tập • Bài khóa ${textNum}`;
    document.getElementById('text-ex-modal-title').textContent = item.title || `Bài khóa ${textNum}`;
    document.getElementById('text-exercise-score-text').textContent = "";

    const bodyContainer = document.getElementById('text-ex-modal-body');
    const exData = item.exercises;

    if (!exData || ((!exData.mc || !exData.mc.length) && (!exData.qa || !exData.qa.length))) {
        bodyContainer.innerHTML = `<div class="p-4 rounded-xl bg-slate-50 border border-slate-200 text-slate-500 text-center">Chưa có dữ liệu bài tập cho bài khóa này.</div>`;
        toggleModal('text-exercise-modal', true);
        return;
    }

    let html = '';
    if (exData.mc && exData.mc.length > 0) {
        html += `
            <div class="space-y-3">
                <div class="flex items-center justify-between flex-wrap gap-2">
                    <h4 class="font-bold text-rose-900 text-sm flex items-center gap-1.5">
                        <span>🎧</span> <span>Phần 1: Nghe/Đọc hội thoại và chọn đáp án đúng</span>
                    </h4>
                    <button onclick="playTextParagraph(${textNum})" class="text-xs text-rose-700 hover:underline font-semibold flex items-center gap-1">
                        <span>🔊</span> Nghe lại bài khóa
                    </button>
                </div>
                <div class="space-y-3">
                    ${exData.mc.map((qItem, idx) => `
                        <div class="p-4 rounded-xl bg-slate-50 border border-slate-200 space-y-2.5">
                            <p class="zh-font font-bold text-slate-900 text-sm">${qItem.q}</p>
                            <div class="grid grid-cols-1 sm:grid-cols-3 gap-2">
                                ${qItem.options.map(opt => {
                                    const letter = opt.trim().charAt(0);
                                    return `
                                        <label class="flex items-center gap-2 p-2.5 rounded-lg bg-white border border-slate-200 hover:border-rose-700 cursor-pointer text-xs font-medium zh-font transition-colors">
                                            <input type="radio" name="text-mc-${idx}" value="${letter}" class="accent-rose-800">
                                            <span>${opt}</span>
                                        </label>
                                    `;
                                }).join('')}
                            </div>
                            <div id="text-mc-fb-${idx}" class="hidden text-xs p-2.5 rounded-lg font-medium"></div>
                        </div>
                    `).join('')}
                </div>
            </div>
        `;
    }

    if (exData.qa && exData.qa.length > 0) {
        html += `
            <div class="space-y-3 pt-2">
                <h4 class="font-bold text-rose-900 text-sm flex items-center gap-1.5">
                    <span>💬</span> <span>Phần 2: Đọc bài khóa và trả lời câu hỏi</span>
                </h4>
                <div class="space-y-3">
                    ${exData.qa.map((qaItem, idx) => `
                        <div class="p-4 rounded-xl bg-slate-50 border border-slate-200 space-y-2.5">
                            <p class="zh-font font-bold text-slate-900 text-sm">${qaItem.q}</p>
                            <input type="text" id="text-qa-input-${idx}" placeholder="Nhập câu trả lời bằng tiếng Trung..." class="w-full px-3.5 py-2 text-sm bg-white border border-slate-300 rounded-xl focus:outline-none focus:border-rose-700 zh-font">
                            <div id="text-qa-fb-${idx}" class="hidden text-xs p-2.5 rounded-lg bg-amber-50/80 text-amber-950 border border-amber-200 space-y-1">
                                <div><strong>Đáp án gợi ý:</strong> <span class="zh-font font-bold text-rose-900">${qaItem.answerZh}</span></div>
                                ${qaItem.answerVi ? `<div class="text-slate-600"><em>(${qaItem.answerVi})</em></div>` : ''}
                            </div>
                        </div>
                    `).join('')}
                </div>
            </div>
        `;
    }

    bodyContainer.innerHTML = html;
    toggleModal('text-exercise-modal', true);
}

function submitTextExercises() {
    const texts = currentLesson ? (currentLesson.texts || []) : [];
    const item = texts.find(t => t.textNum === currentActiveTextNum);
    if (!item || !item.exercises) return;

    const mcList = item.exercises.mc || [];
    const qaList = item.exercises.qa || [];
    let mcCorrect = 0;

    mcList.forEach((qItem, idx) => {
        const selected = document.querySelector(`input[name="text-mc-${idx}"]:checked`);
        const fb = document.getElementById(`text-mc-fb-${idx}`);
        fb.classList.remove('hidden');

        if (selected && selected.value === qItem.answer) {
            mcCorrect++;
            fb.innerHTML = `✅ <strong>Chính xác!</strong> ${qItem.explain || ''}`;
            fb.className = "text-xs p-2.5 rounded-lg bg-emerald-50 text-emerald-800 border border-emerald-200";
        } else {
            fb.innerHTML = `❌ <strong>Chưa đúng.</strong> Đáp án chuẩn là <strong>${qItem.answer}</strong>. ${qItem.explain || ''}`;
            fb.className = "text-xs p-2.5 rounded-lg bg-rose-50 text-rose-800 border border-rose-200";
        }
    });

    qaList.forEach((_, idx) => {
        const fb = document.getElementById(`text-qa-fb-${idx}`);
        if (fb) fb.classList.remove('hidden');
    });

    document.getElementById('text-exercise-score-text').textContent = mcList.length > 0 
        ? `Trắc nghiệm: Đúng ${mcCorrect}/${mcList.length} câu (Đã mở gợi ý tự luận).` 
        : `Đã hiển thị đáp án gợi ý.`;
}

function playTextParagraph(num) {
    const texts = currentLesson ? (currentLesson.texts || []) : [];
    const item = texts.find(t => t.textNum === num);
    if (!item) return;
    const fullText = item.lines
        ? item.lines.map(l => l.text).join(' ')
        : (item.paragraphs || []).map(p => p.text).join(' ');
    speakText(fullText);
}

// --- TAB 3: NGỮ PHÁP ---
function filterGrammar(filterVal, btn) {
    activeGrammarFilter = filterVal;
    document.querySelectorAll('#grammar-filter-bar button').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    renderGrammar();
}

function renderGrammar() {
    const container = document.getElementById('grammar-list-container');
    const grammar = currentLesson ? (currentLesson.grammar || []) : [];
    const list = activeGrammarFilter === 'all' ? grammar : grammar.filter(g => g.textNum === activeGrammarFilter);

    container.innerHTML = list.map(g => `
        <div class="bg-white p-6 sm:p-8 rounded-2xl border border-slate-200 shadow-xs space-y-4">
            <div class="flex items-center justify-between">
                <span class="inline-block text-xs font-semibold bg-rose-50 border border-rose-200 text-rose-800 px-3 py-1 rounded-full">
                    Ngữ pháp Bài khóa ${g.textNum}
                </span>
                <button onclick="openGrammarExercise(${g.id})" class="px-4 py-1.5 rounded-xl bg-rose-800 hover:bg-rose-900 text-white text-xs font-semibold shadow-2xs flex items-center gap-1.5">
                    <span>✏️</span> <span>Luyện tập (10 câu)</span>
                </button>
            </div>
            <h3 class="text-xl font-bold text-slate-900">${g.title}</h3>
            <p class="text-sm text-slate-600 leading-relaxed">${g.explanation}</p>
            <div class="space-y-2 pt-2">
                <p class="text-xs font-bold uppercase tracking-wider text-slate-400">Ví dụ minh họa:</p>
                ${g.examples.map(ex => `
                    <div class="bg-slate-50 p-3.5 rounded-xl border border-slate-200/80 flex items-center justify-between gap-3">
                        <div>
                            <p class="zh-font text-base font-medium text-slate-900">${ex.zh}</p>
                            <p class="text-xs text-slate-500 mt-0.5">${ex.vi}</p>
                        </div>
                        <button onclick="speakText('${escapeJsSingleQuote(ex.zh)}')" class="w-8 h-8 rounded-lg bg-white border border-slate-200 text-rose-700 flex items-center justify-center shrink-0">🔊</button>
                    </div>
                `).join('')}
            </div>
        </div>
    `).join('');
}

function openGrammarExercise(grammarId) {
    currentActiveGrammarId = grammarId;
    document.getElementById('ex-modal-badge').textContent = `Bài tập luyện tập • Điểm ngữ pháp ${grammarId}`;
    document.getElementById('exercise-score-text').textContent = "";
    const statusEl = document.getElementById('grammar-excel-status');
    if (statusEl) statusEl.classList.add('hidden');

    const exMap = currentLesson ? (currentLesson.sentenceExercises || {}) : {};
    const questions = exMap[grammarId] || [];
    const bodyContainer = document.getElementById('ex-modal-body');

    document.getElementById('ex-modal-title').textContent = "Sắp xếp từ thành câu hoàn chỉnh";

    bodyContainer.innerHTML = questions.map((q, idx) => `
        <div class="p-4 rounded-xl bg-slate-50 border border-slate-200 space-y-3">
            <div class="flex items-center justify-between">
                <span class="font-bold text-slate-900 text-xs sm:text-sm zh-font">Câu ${idx + 1}: ${q.shuffled.join(', ')}</span>
            </div>
            <input type="text" id="sentence-input-${idx}" placeholder="Nhập câu tiếng Trung hoàn chỉnh..." class="w-full px-3.5 py-2 text-sm bg-white border border-slate-300 rounded-xl focus:outline-none focus:border-rose-700 zh-font">
            <div id="sentence-feedback-${idx}" class="text-xs font-medium hidden"></div>
        </div>
    `).join('');

    toggleModal('grammar-exercise-modal', true);
}

function submitSentenceExercises() {
    const exMap = currentLesson ? (currentLesson.sentenceExercises || {}) : {};
    const questions = exMap[currentActiveGrammarId] || [];
    let correctCount = 0;
    const detailsArray = [];

    questions.forEach((q, idx) => {
        const inputEl = document.getElementById(`sentence-input-${idx}`);
        const feedbackEl = document.getElementById(`sentence-feedback-${idx}`);
        feedbackEl.classList.remove('hidden');

        const clean = s => s.trim().replace(/[\s，。！？、,.!?]/g, '');
        const isCorrect = clean(inputEl.value) === clean(q.correct);
        if (isCorrect) {
            correctCount++;
            feedbackEl.innerHTML = `🎉 Chính xác! Đáp án: <strong class="zh-font">${q.correct}</strong>`;
            feedbackEl.className = "text-xs font-bold text-emerald-700 bg-emerald-50 p-2.5 rounded-lg border border-emerald-200";
        } else {
            feedbackEl.innerHTML = `❌ Chưa đúng. Đáp án chuẩn: <strong class="zh-font">${q.correct}</strong>`;
            feedbackEl.className = "text-xs font-bold text-rose-700 bg-rose-50 p-2.5 rounded-lg border border-rose-200";
        }

        detailsArray.push({
            question: `Sắp xếp: ${q.shuffled.join(' / ')}`,
            userAnswer: inputEl.value.trim(),
            correctAnswer: q.correct,
            isCorrect: isCorrect
        });
    });

    document.getElementById('exercise-score-text').textContent = `Kết quả: Đúng ${correctCount} / ${questions.length} câu.`;

    if (typeof submitGrammarResultToExcel === 'function' && questions.length > 0) {
        submitGrammarResultToExcel(currentActiveGrammarId, correctCount, questions.length, detailsArray);
    }
}

// --- QUẢN LÝ GEMINI API KEY & CHẤM BÀI AI ---
function updateAiKeyBadge() {
    const key = localStorage.getItem('gemini_api_key') || '';
    const label = document.getElementById('ai-status-label');
    const input = document.getElementById('gemini-api-key-input');
    if (input) input.value = key;
    if (label) {
        label.textContent = key ? 'AI Chấm bài: Đã bật' : 'Cài đặt AI Chấm bài';
    }
}

function saveGeminiApiKey() {
    const val = document.getElementById('gemini-api-key-input').value.trim();
    if (!val) {
        alert('Vui lòng nhập API Key hợp lệ!');
        return;
    }
    localStorage.setItem('gemini_api_key', val);
    updateAiKeyBadge();
    toggleModal('ai-key-modal', false);
}

function clearGeminiApiKey() {
    localStorage.removeItem('gemini_api_key');
    updateAiKeyBadge();
}

async function callGeminiGradeSentence(targetWord, pinyin, meaning, userSentence, feedbackElId, btnEl) {
    const apiKey = localStorage.getItem('gemini_api_key');
    if (!apiKey) {
        toggleModal('ai-key-modal', true);
        return;
    }

    const fbEl = document.getElementById(feedbackElId);
    if (!userSentence.trim()) {
        fbEl.classList.remove('hidden');
        fbEl.className = "text-xs p-3 rounded-xl bg-amber-50 text-amber-800 border border-amber-200 font-medium";
        fbEl.innerHTML = "⚠️ Bạn chưa nhập câu tiếng Trung nào để AI chấm.";
        return;
    }

    const origBtnHtml = btnEl.innerHTML;
    btnEl.disabled = true;
    btnEl.innerHTML = `<span>⏳</span> <span>AI đang chấm...</span>`;
    fbEl.classList.remove('hidden');
    fbEl.className = "text-xs p-3.5 rounded-xl bg-slate-100 text-slate-600 border border-slate-200 animate-pulse";
    fbEl.innerHTML = "🤖 Giáo viên AI đang kiểm tra ngữ pháp, cách dùng từ và độ tự nhiên...";

    const prompt = `Bạn là giáo viên tiếng Trung HSK bản xứ giàu kinh nghiệm. Hãy chấm và sửa câu đặt của học viên Việt Nam.
Từ mới yêu cầu sử dụng: "${targetWord}" (${pinyin} - nghĩa: ${meaning}).
Câu học viên đặt: "${userSentence}"

Hãy trả lời ngắn gọn, rõ ràng bằng tiếng Việt theo đúng 4 gạch đầu dòng sau (không dùng markdown phức tạp):
- Đánh giá: [Đúng hoàn toàn / Khá tốt, cần chỉnh nhẹ / Sai ngữ pháp hoặc dùng sai từ]
- Nhận xét & Sửa lỗi: [Giải thích ngắn gọn lỗi sai về ngữ pháp, từ loại, lượng từ, trật tự từ hoặc dấu câu. Nếu đã đúng, khen ngợi ngắn gọn.]
- Câu sửa chuẩn & tự nhiên: [Viết lại câu tiếng Trung hoàn chỉnh, chuẩn xác nhất]
- Pinyin & Dịch nghĩa: [Pinyin của câu chuẩn] — [Nghĩa tiếng Việt]`;

    try {
        const res = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=${encodeURIComponent(apiKey)}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                contents: [{ parts: [{ text: prompt }] }],
                generationConfig: { temperature: 0.3 }
            })
        });

        const data = await res.json();
        if (!res.ok) {
            throw new Error(data.error ? data.error.message : 'Lỗi kết nối API');
        }

        const replyText = data.candidates?.[0]?.content?.parts?.[0]?.text || 'Không nhận được phản hồi từ AI.';
        const isGood = replyText.includes('Đúng hoàn toàn');
        fbEl.className = isGood
            ? "text-xs p-3.5 rounded-xl bg-emerald-50/90 text-emerald-950 border border-emerald-200 space-y-1.5 leading-relaxed whitespace-pre-line"
            : "text-xs p-3.5 rounded-xl bg-amber-50/90 text-slate-800 border border-amber-200 space-y-1.5 leading-relaxed whitespace-pre-line";
        fbEl.innerHTML = `<div class="font-bold text-rose-900 mb-1 flex items-center gap-1.5"><span>✨</span> <span>Nhận xét của Giáo viên AI:</span></div>` + replyText.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
    } catch (err) {
        fbEl.className = "text-xs p-3 rounded-xl bg-rose-50 text-rose-800 border border-rose-200";
        fbEl.innerHTML = `❌ <strong>Lỗi chấm AI:</strong> ${err.message}. Vui lòng kiểm tra lại API Key.`;
    } finally {
        btnEl.disabled = false;
        btnEl.innerHTML = origBtnHtml;
    }
}

function gradeVocabSentenceById(idx) {
    const vocab = currentLesson ? (currentLesson.vocab || []) : [];
    const word = vocab[idx];
    if (!word) return;
    const inputVal = document.getElementById(`ws-input-${idx}`).value;
    const btnEl = document.getElementById(`ws-btn-${idx}`);
    callGeminiGradeSentence(word.hz, word.py, word.vi, inputVal, `ws-fb-${idx}`, btnEl);
}

// --- TAB 4: BÀI TẬP TỔNG HỢP ---
function renderPracticeSection() {
    const container = document.getElementById('practice-container');
    const groups = currentLesson ? (currentLesson.comprehensivePractice || []) : [];

    if (groups.length === 0) {
        container.innerHTML = `<div class="bg-white p-6 rounded-2xl border border-slate-200 text-sm text-slate-500">Chưa có bài tập tổng hợp cho bài này.</div>`;
        return;
    }

    container.innerHTML = groups.map((grp, gIdx) => `
        <div class="bg-white p-6 sm:p-8 rounded-2xl border border-slate-200 shadow-xs space-y-5">
            <div>
                <h3 class="text-lg sm:text-xl font-bold text-slate-900">${grp.groupTitle}</h3>
                <div class="flex flex-wrap gap-2 mt-3 p-3 rounded-xl bg-amber-50/70 border border-amber-200/80">
                    ${grp.options.map(opt => `<span class="zh-font text-xs sm:text-sm font-semibold text-amber-950 bg-white px-3 py-1 rounded-lg border border-amber-200">${opt}</span>`).join('')}
                </div>
            </div>
            <div class="space-y-4">
                ${grp.questions.map((item, qIdx) => {
                    const uid = `comp-${gIdx}-${qIdx}`;
                    return `
                        <div class="p-4 rounded-xl bg-slate-50 border border-slate-200 space-y-2.5">
                            <p class="zh-font text-sm sm:text-base font-medium text-slate-900">${item.q}</p>
                            <div class="flex flex-wrap items-center gap-2">
                                ${['A', 'B', 'C', 'D', 'E'].slice(0, grp.options.length).map(letter => `
                                    <label class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-white border border-slate-200 hover:border-rose-700 cursor-pointer text-xs font-bold">
                                        <input type="radio" name="${uid}" value="${letter}" onchange="checkCompAnswer('${uid}', '${item.answer}', '${escapeJsSingleQuote(item.explain)}')">
                                        <span>${letter}</span>
                                    </label>
                                `).join('')}
                            </div>
                            <div id="fb-${uid}" class="hidden text-xs p-2.5 rounded-lg"></div>
                        </div>
                    `;
                }).join('')}
            </div>
        </div>
    `).join('');
}

// --- TAB 5: PHIẾU BÀI TẬP ---
function renderWorksheetSection() {
    const aiContainer = document.getElementById('worksheet-ai-container');
    const customContainer = document.getElementById('worksheet-container');
    const vocab = currentLesson ? (currentLesson.vocab || []) : [];

    if (aiContainer) {
        if (vocab.length > 0) {
            aiContainer.innerHTML = `
                <div class="bg-white p-6 sm:p-8 rounded-2xl border border-slate-200 shadow-xs space-y-5">
                    <div class="flex flex-wrap items-center justify-between gap-3 border-b border-slate-100 pb-4">
                        <div>
                            <span class="text-xs font-bold uppercase tracking-wider text-rose-800 bg-rose-50 px-3 py-1 rounded-full border border-rose-200">✨ Phiếu bài tập • AI Chấm trực tiếp</span>
                            <h3 class="text-lg sm:text-xl font-bold text-slate-900 mt-2">Đặt câu với từ mới</h3>
                            <p class="text-xs text-slate-500 mt-0.5">Viết câu tiếng Trung sử dụng từ mới cho sẵn, sau đó bấm <strong>AI Sửa câu</strong> để được chấm ngữ pháp và gợi ý diễn đạt chuẩn xác.</p>
                        </div>
                        <button onclick="toggleModal('ai-key-modal', true)" class="px-3.5 py-2 rounded-xl bg-amber-50 hover:bg-amber-100 text-amber-900 border border-amber-200 text-xs font-semibold flex items-center gap-1.5">
                            <span>🔑</span> <span>Cấu hình API Key</span>
                        </button>
                    </div>

                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                        ${vocab.map((w, idx) => `
                            <div class="p-4 rounded-xl bg-slate-50 border border-slate-200 space-y-3 flex flex-col justify-between">
                                <div class="space-y-2">
                                    <div class="flex items-center justify-between gap-2">
                                        <div>
                                            <span class="text-xs font-bold text-slate-400 mr-1.5">Câu ${idx + 1}.</span>
                                            <span class="zh-font text-lg font-bold text-rose-900">${w.hz}</span>
                                            <span class="text-xs font-semibold text-rose-700 ml-1.5">${w.py}</span>
                                        </div>
                                        <span class="text-[11px] bg-white border border-slate-200 text-slate-600 px-2 py-0.5 rounded font-medium">${w.pos}</span>
                                    </div>
                                    <p class="text-xs text-slate-600 font-medium">Nghĩa: ${w.vi}</p>
                                    <textarea id="ws-input-${idx}" rows="2" placeholder="Đặt 1 câu tiếng Trung có chứa từ「${w.hz}」..." class="w-full p-2.5 text-sm bg-white border border-slate-300 rounded-xl focus:outline-none focus:border-rose-700 zh-font"></textarea>
                                </div>
                                <div class="space-y-2.5">
                                    <div class="flex items-center justify-end gap-2">
                                        <button onclick="speakText(document.getElementById('ws-input-${idx}').value)" class="px-3 py-1.5 rounded-lg bg-white border border-slate-200 hover:bg-slate-100 text-slate-700 text-xs font-semibold">🔊 Nghe câu</button>
                                        <button id="ws-btn-${idx}" onclick="gradeVocabSentenceById(${idx})" class="px-4 py-1.5 rounded-lg bg-rose-800 hover:bg-rose-900 text-white text-xs font-semibold flex items-center gap-1.5 shadow-2xs transition-colors">
                                            <span>✨</span> <span>AI Sửa câu</span>
                                        </button>
                                    </div>
                                    <div id="ws-fb-${idx}" class="hidden"></div>
                                </div>
                            </div>
                        `).join('')}
                    </div>
                </div>
            `;
        } else {
            aiContainer.innerHTML = '';
        }
    }

    if (typeof renderWorksheetTab === 'function') {
        renderWorksheetTab();
    } else if (!vocab.length && customContainer) {
        customContainer.innerHTML = `<div class="bg-white p-6 rounded-2xl border border-slate-200 text-sm text-slate-500">Chưa có phiếu bài tập cho bài này.</div>`;
    }

    const wsTab = document.getElementById('tab-worksheet');
    if (wsTab) {
        let submitBar = document.getElementById('worksheet-submit-bar');
        if (!submitBar) {
            submitBar = document.createElement('div');
            submitBar.id = 'worksheet-submit-bar';
            wsTab.appendChild(submitBar);
        }
        submitBar.className = "bg-white p-5 sm:p-6 rounded-2xl border border-slate-200 shadow-xs space-y-3";
        submitBar.innerHTML = `
            <div class="flex flex-wrap items-center justify-between gap-3">
                <div>
                    <h4 class="text-sm sm:text-base font-bold text-slate-900">📤 Nộp kết quả Phiếu bài tập cho giáo viên</h4>
                    <p class="text-xs text-slate-500 mt-0.5">Toàn bộ câu đặt từ mới (kèm nhận xét AI nếu đã chấm) và bài làm phiếu mở rộng sẽ được gửi thẳng về bảng Excel.</p>
                </div>
                <div class="flex flex-wrap items-center gap-2.5">
                    <button onclick="submitWorksheetToExcel()" class="px-5 py-2.5 rounded-xl bg-rose-800 hover:bg-rose-900 text-white text-xs font-semibold flex items-center gap-1.5 shadow-2xs transition-colors">
                        <span>📊</span> <span>Nộp Phiếu bài tập về Excel</span>
                    </button>
                    <button onclick="downloadWorksheetExcel()" class="px-4 py-2.5 rounded-xl bg-emerald-700 hover:bg-emerald-800 text-white text-xs font-semibold flex items-center gap-1.5 shadow-2xs transition-colors">
                        <span>📥</span> <span>Tải file Excel (.xlsx)</span>
                    </button>
                </div>
            </div>
            <div id="worksheet-excel-status" class="hidden"></div>
        `;
    }
}

function checkCompAnswer(uid, correctLetter, explain) {
    const selected = document.querySelector(`input[name="${uid}"]:checked`);
    const fb = document.getElementById(`fb-${uid}`);
    if (!selected || !fb) return;

    fb.classList.remove('hidden');
    if (selected.value === correctLetter) {
        fb.innerHTML = `✅ <strong>Chính xác!</strong> ${explain}`;
        fb.className = "text-xs p-2.5 rounded-lg bg-emerald-50 text-emerald-800 border border-emerald-200";
    } else {
        fb.innerHTML = `❌ <strong>Chưa đúng.</strong> Đáp án đúng là <strong>${correctLetter}</strong>. ${explain}`;
        fb.className = "text-xs p-2.5 rounded-lg bg-rose-50 text-rose-800 border border-rose-200";
    }
}

// --- TAB 6: CHỦ ĐỀ & LUYỆN TẬP MỞ RỘNG ---
function renderTopicSection() {
    const container = document.getElementById('topic-container');
    const topicData = currentLesson ? (currentLesson.topicExercises || null) : null;

    if (!topicData) {
        container.innerHTML = `<div class="bg-white p-6 rounded-2xl border border-slate-200 text-xs text-slate-500">Chưa có dữ liệu bài tập chủ đề mở rộng cho bài này.</div>`;
        return;
    }

    let html = `<div class="space-y-10 text-xs">`;

    if (topicData.listeningImages && topicData.listeningImages.length > 0) {
        html += `
            <div class="bg-white p-6 sm:p-8 rounded-2xl border border-slate-200 shadow-xs space-y-6">
                <h3 class="text-sm font-bold text-rose-900 flex items-center gap-2"><span>🎧</span> Bài 1: Nghe hội thoại ngắn và chọn hình ảnh phù hợp</h3>
                <div class="flex justify-center bg-slate-50 p-4 rounded-2xl border border-slate-200">
                    <img src="${topicData.listeningImages[0].imageDesc}" alt="6 hình Bài 1" class="max-h-80 object-contain rounded-xl shadow-2xs">
                </div>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    ${topicData.listeningImages.map((item, idx) => `
                        <div class="p-4 rounded-xl bg-slate-50 border border-slate-200 space-y-3">
                            <div class="flex items-center justify-between">
                                <span class="font-bold text-xs text-slate-900">Câu ${idx + 1} (Chọn đáp án A-F)</span>
                                <input type="text" id="t1-ans-${idx}" placeholder="Nhập đáp án..." class="w-24 px-2.5 py-1 text-xs uppercase bg-white border border-slate-300 rounded-lg text-center font-bold focus:outline-none focus:border-rose-700">
                            </div>
                            <button onclick="playTopic1Audio(${idx})" class="w-full py-2 rounded-lg bg-rose-50 hover:bg-rose-100 text-rose-800 font-semibold flex items-center justify-center gap-1.5 transition-colors">
                                <span>🔊</span> Phát âm thanh câu ${idx + 1}
                            </button>
                            <div id="t1-content-${idx}" class="hidden text-xs bg-white p-2.5 rounded-lg border border-slate-200 space-y-1">
                                <p class="zh-font text-slate-800 font-medium whitespace-pre-line"><strong>Nội dung:</strong> ${item.dialogue}</p>
                                <p class="text-emerald-700 font-bold">Đáp án đúng: ${item.answer}</p>
                            </div>
                        </div>
                    `).join('')}
                </div>
                <div>
                    <button onclick="checkTopic1(${topicData.listeningImages.length})" class="px-5 py-2.5 rounded-xl bg-rose-800 hover:bg-rose-900 text-white text-xs font-semibold shadow-2xs">Kiểm tra Bài 1</button>
                </div>
            </div>
        `;
    }

    if (topicData.trueFalse && topicData.trueFalse.length > 0) {
        html += `
            <div class="bg-white p-6 sm:p-8 rounded-2xl border border-slate-200 shadow-xs space-y-6">
                <h3 class="text-sm font-bold text-rose-900 flex items-center gap-2"><span>✔️</span> Bài 2: Nghe hội thoại và điền Đúng / Sai</h3>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    ${topicData.trueFalse.map((tf, idx) => `
                        <div class="p-4 rounded-xl bg-slate-50 border border-slate-200 space-y-3">
                            <span class="font-bold text-xs text-slate-900 block">Câu ${idx + 6}. Phát biểu: <span class="text-rose-800">${tf.statement}</span></span>
                            <button onclick="playTopic2Audio(${idx})" class="w-full py-2 rounded-lg bg-rose-50 hover:bg-rose-100 text-rose-800 font-semibold flex items-center justify-center gap-1.5 transition-colors">
                                <span>🔊</span> Phát âm thanh câu ${idx + 6}
                            </button>
                            <div class="flex items-center gap-4 pt-1">
                                <label class="text-xs font-bold cursor-pointer"><input type="radio" name="tf-choice-${idx}" value="true" class="accent-rose-800"> Đúng (✓)</label>
                                <label class="text-xs font-bold cursor-pointer"><input type="radio" name="tf-choice-${idx}" value="false" class="accent-rose-800"> Sai (✕)</label>
                            </div>
                            <div id="t2-content-${idx}" class="hidden text-xs bg-white p-3 rounded-lg border border-slate-200 space-y-1.5">
                                <p class="zh-font text-slate-800 whitespace-pre-line"><strong>Hội thoại:</strong> ${tf.dialogue}</p>
                                <p id="t2-fb-${idx}" class="font-bold"></p>
                            </div>
                        </div>
                    `).join('')}
                </div>
                <div>
                    <button onclick="checkTopic2(${topicData.trueFalse.length})" class="px-5 py-2.5 rounded-xl bg-rose-800 hover:bg-rose-900 text-white text-xs font-semibold shadow-2xs">Kiểm tra Bài 2</button>
                </div>
            </div>
        `;
    }

    if (topicData.sentenceOrdering && topicData.sentenceOrdering.length > 0) {
        html += `
            <div class="bg-white p-6 sm:p-8 rounded-2xl border border-slate-200 shadow-xs space-y-6">
                <h3 class="text-sm font-bold text-rose-900 flex items-center gap-2"><span>🔤</span> Bài 3: Sắp xếp các câu thành đoạn văn hoàn chỉnh</h3>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    ${topicData.sentenceOrdering.map((ord, idx) => `
                        <div class="p-4 rounded-xl bg-slate-50 border border-slate-200 space-y-3">
                            <h4 class="font-bold text-xs text-slate-900">${ord.title}</h4>
                            <div class="space-y-1.5 text-xs zh-font text-slate-700">
                                ${ord.sentences.map(s => `<div class="p-2 bg-white rounded-lg border border-slate-200">${s}</div>`).join('')}
                            </div>
                            <input type="text" id="ord-input-${idx}" placeholder="Nhập thứ tự (Ví dụ: B-A-D-E-C)..." class="w-full px-3 py-2 text-xs bg-white border border-slate-300 rounded-lg focus:outline-none focus:border-rose-700 uppercase font-bold">
                            <button onclick="checkOrdering(${idx}, '${ord.correctOrder}')" class="px-4 py-1.5 rounded-lg bg-rose-800 text-white text-xs font-semibold">Kiểm tra</button>
                            <div id="ord-fb-${idx}" class="hidden text-xs p-2 rounded-lg font-medium"></div>
                        </div>
                    `).join('')}
                </div>
            </div>
        `;
    }

    if (topicData.imageDescriptions && topicData.imageDescriptions.length > 0) {
        html += `
            <div class="bg-white p-6 sm:p-8 rounded-2xl border border-slate-200 shadow-xs space-y-6">
                <h3 class="text-sm font-bold text-rose-900 flex items-center gap-2"><span>🖼️</span> Bài 4: Mô tả hình ảnh bằng tiếng Trung</h3>
                <div class="flex justify-center bg-slate-50 p-4 rounded-2xl border border-slate-200">
                    <img src="${topicData.imageDescriptions[0].imageFile}" alt="6 hình Bài 4" class="max-h-80 object-contain rounded-xl shadow-2xs">
                </div>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    ${topicData.imageDescriptions.map((img, idx) => `
                        <div class="p-4 rounded-xl bg-slate-50 border border-slate-200 space-y-2.5">
                            <p class="text-xs font-bold text-rose-800">Hình ${idx + 1}</p>
                            <textarea id="t4-input-${idx}" rows="2" placeholder="Nhập câu mô tả tiếng Trung của bạn..." class="w-full p-2.5 text-xs bg-white border border-slate-300 rounded-lg focus:outline-none focus:border-rose-700 zh-font"></textarea>
                            <div id="t4-content-${idx}" class="hidden text-xs bg-white p-2.5 rounded-lg border border-emerald-200 text-emerald-900 space-y-1">
                                <p><strong>Câu mẫu tiếng Trung:</strong> <span class="zh-font font-bold text-rose-900">${img.descZh}</span></p>
                            </div>
                        </div>
                    `).join('')}
                </div>
                <div>
                    <button onclick="checkTopic4(${topicData.imageDescriptions.length})" class="px-5 py-2.5 rounded-xl bg-rose-800 hover:bg-rose-900 text-white text-xs font-semibold shadow-2xs">Hiện tất cả câu mẫu</button>
                </div>
            </div>
        `;
    }

    html += `</div>`;
    container.innerHTML = html;
}

function playTopic1Audio(idx) {
    const list = currentLesson && currentLesson.topicExercises ? currentLesson.topicExercises.listeningImages : [];
    if (list[idx]) speakText(list[idx].dialogue);
}

function playTopic2Audio(idx) {
    const list = currentLesson && currentLesson.topicExercises ? currentLesson.topicExercises.trueFalse : [];
    if (list[idx]) speakText(list[idx].dialogue);
}

function checkTopic1(total) {
    const topicData = currentLesson.topicExercises.listeningImages;
    for (let i = 0; i < total; i++) {
        const userVal = document.getElementById(`t1-ans-${i}`).value.trim().toUpperCase();
        const contentDiv = document.getElementById(`t1-content-${i}`);
        contentDiv.classList.remove('hidden');
        if (userVal === topicData[i].answer) {
            contentDiv.style.borderColor = "#10b981";
        } else {
            contentDiv.style.borderColor = "#f43f5e";
        }
    }
}

function checkTopic2(total) {
    const topicData = currentLesson.topicExercises.trueFalse;
    for (let i = 0; i < total; i++) {
        const selected = document.querySelector(`input[name="tf-choice-${i}"]:checked`);
        const contentDiv = document.getElementById(`t2-content-${i}`);
        const fb = document.getElementById(`t2-fb-${i}`);
        contentDiv.classList.remove('hidden');

        if (selected) {
            const userBool = selected.value === 'true';
            if (userBool === topicData[i].answer) {
                fb.innerHTML = `✅ Chính xác!`;
                fb.className = "font-bold text-emerald-700";
            } else {
                fb.innerHTML = `❌ Chưa đúng. Đáp án chuẩn: <strong>${topicData[i].answer ? 'Đúng' : 'Sai'}</strong>`;
                fb.className = "font-bold text-rose-700";
            }
        } else {
            fb.innerHTML = `⚠️ Bạn chưa chọn. Đáp án chuẩn: <strong>${topicData[i].answer ? 'Đúng' : 'Sai'}</strong>`;
            fb.className = "font-bold text-amber-700";
        }
    }
}

function checkOrdering(idx, correctOrder) {
    const inputVal = document.getElementById(`ord-input-${idx}`).value.trim().replace(/\s+/g, '').toUpperCase();
    const cleanCorrect = correctOrder.replace(/\s+/g, '').toUpperCase();
    const fb = document.getElementById(`ord-fb-${idx}`);
    fb.classList.remove('hidden');

    if (inputVal === cleanCorrect) {
        fb.innerHTML = `🎉 Chính xác hoàn toàn! Thứ tự đúng là: <strong>${correctOrder}</strong>`;
        fb.className = "text-xs p-2 rounded-lg bg-emerald-50 text-emerald-800 border border-emerald-200 font-bold";
    } else {
        fb.innerHTML = `❌ Chưa đúng. Thứ tự chuẩn là: <strong>${correctOrder}</strong>`;
        fb.className = "text-xs p-2 rounded-lg bg-rose-50 text-rose-800 border border-rose-200 font-bold";
    }
}

function checkTopic4(total) {
    for (let i = 0; i < total; i++) {
        const contentDiv = document.getElementById(`t4-content-${i}`);
        contentDiv.classList.remove('hidden');
    }
}

// ============================================================================
// MODULE LIÊN KẾT EXCEL / GOOGLE SHEETS NHẬN KẾT QUẢ HỌC VIÊN (excel-sync.js)
// ============================================================================

// 👉 GIÁO VIÊN DÁN LINK WEB APP GOOGLE APPS SCRIPT VÀO DẤU NGOẶC KÉP BÊN DƯỚI:
// Khi dán link vào đây và đẩy lên GitHub, mọi học viên làm bài sẽ tự động gửi kết quả về bảng tính của bạn.
const TEACHER_EXCEL_WEBHOOK_URL = "https://script.google.com/macros/s/AKfycby_IevfSRNLv3MXXm5lzjGKm-dyrtTnoee4L3YmKaswIm6TcVhhcBYOLzM9rvYfH24/exec";

const EXCEL_STORAGE_KEYS = {
    WEBHOOK_URL: "hsk_excel_webhook_url",
    STUDENT_NAME: "hsk_student_name",
    STUDENT_CLASS: "hsk_student_class",
    SUBMISSIONS: "hsk_student_submissions"
};

function getExcelWebhookUrl() {
    if (TEACHER_EXCEL_WEBHOOK_URL && TEACHER_EXCEL_WEBHOOK_URL.trim() !== "") {
        return TEACHER_EXCEL_WEBHOOK_URL.trim();
    }
    return (localStorage.getItem(EXCEL_STORAGE_KEYS.WEBHOOK_URL) || "").trim();
}

function getStudentInfo() {
    return {
        name: (localStorage.getItem(EXCEL_STORAGE_KEYS.STUDENT_NAME) || "").trim(),
        className: (localStorage.getItem(EXCEL_STORAGE_KEYS.STUDENT_CLASS) || "").trim()
    };
}

function updateExcelStatusBadge() {
    const url = getExcelWebhookUrl();
    const student = getStudentInfo();
    const label = document.getElementById("excel-status-label");
    const urlInput = document.getElementById("excel-webhook-input");
    const nameInput = document.getElementById("student-name-input");
    const classInput = document.getElementById("student-class-input");

    if (urlInput && !TEACHER_EXCEL_WEBHOOK_URL) {
        urlInput.value = url;
    } else if (urlInput && TEACHER_EXCEL_WEBHOOK_URL) {
        urlInput.value = "Đã cấu hình sẵn bởi giáo viên";
        urlInput.disabled = true;
    }
    if (nameInput) nameInput.value = student.name;
    if (classInput) classInput.value = student.className;

    if (label) {
        if (url && student.name) {
            label.textContent = `Excel: ${student.name}`;
        } else if (url) {
            label.textContent = "Excel: Đã kết nối";
        } else {
            label.textContent = "Kết nối Excel";
        }
    }
}

function saveExcelConfig() {
    const nameVal = (document.getElementById("student-name-input")?.value || "").trim();
    const classVal = (document.getElementById("student-class-input")?.value || "").trim();
    const urlInput = document.getElementById("excel-webhook-input");

    if (!nameVal) {
        alert("Vui lòng nhập Họ và tên học viên!");
        return;
    }

    localStorage.setItem(EXCEL_STORAGE_KEYS.STUDENT_NAME, nameVal);
    localStorage.setItem(EXCEL_STORAGE_KEYS.STUDENT_CLASS, classVal);

    if (urlInput && !urlInput.disabled) {
        const urlVal = urlInput.value.trim();
        localStorage.setItem(EXCEL_STORAGE_KEYS.WEBHOOK_URL, urlVal);
    }

    updateExcelStatusBadge();
    toggleModal("excel-config-modal", false);

    if (typeof window._pendingExcelSubmit === "function") {
        const fn = window._pendingExcelSubmit;
        window._pendingExcelSubmit = null;
        fn();
    }
}

function ensureStudentIdentity(callback) {
    const student = getStudentInfo();
    if (student.name) {
        callback(student);
        return;
    }
    window._pendingExcelSubmit = () => {
        const updated = getStudentInfo();
        if (updated.name) callback(updated);
    };
    updateExcelStatusBadge();
    toggleModal("excel-config-modal", true);
}

function saveSubmissionLocally(record) {
    try {
        const list = JSON.parse(localStorage.getItem(EXCEL_STORAGE_KEYS.SUBMISSIONS) || "[]");
        list.unshift(record);
        if (list.length > 100) list.length = 100;
        localStorage.setItem(EXCEL_STORAGE_KEYS.SUBMISSIONS, JSON.stringify(list));
    } catch (e) {
        console.warn("Không thể lưu lịch sử cục bộ:", e);
    }
}

async function sendPayloadToExcelWebhook(payload, statusEl) {
    const webhookUrl = getExcelWebhookUrl();
    saveSubmissionLocally(payload);

    if (!webhookUrl) {
        if (statusEl) {
            statusEl.classList.remove("hidden");
            statusEl.className = "text-xs p-3 rounded-xl bg-amber-50 text-amber-900 border border-amber-200 font-medium";
            statusEl.innerHTML = `⚠️ <strong>Chưa gắn link Google Sheets/Excel.</strong> Kết quả đã được lưu tạm trên máy — bạn có thể bấm <strong>Tải file Excel (.xlsx)</strong> hoặc bấm <strong>Kết nối Excel</strong> ở góc trên để dán link nhận bài tự động.`;
        }
        return false;
    }

    if (statusEl) {
        statusEl.classList.remove("hidden");
        statusEl.className = "text-xs p-3 rounded-xl bg-slate-100 text-slate-700 border border-slate-200 animate-pulse font-medium";
        statusEl.innerHTML = `⏳ Đang gửi kết quả của <strong>${payload.studentName}</strong> về bảng Excel của giáo viên...`;
    }

    try {
        await fetch(webhookUrl, {
            method: "POST",
            mode: "no-cors",
            headers: {
                "Content-Type": "text/plain;charset=utf-8"
            },
            body: JSON.stringify(payload)
        });

        if (statusEl) {
            statusEl.className = "text-xs p-3 rounded-xl bg-emerald-50 text-emerald-900 border border-emerald-200 font-medium";
            statusEl.innerHTML = `✅ <strong>Đã gửi kết quả thành công!</strong> Học viên: <strong>${payload.studentName}</strong> (${payload.studentClass || "Không ghi lớp"}) • Điểm/Trạng thái: <strong>${payload.scoreSummary}</strong>.`;
        }
        return true;
    } catch (err) {
        if (statusEl) {
            statusEl.className = "text-xs p-3 rounded-xl bg-rose-50 text-rose-800 border border-rose-200 font-medium";
            statusEl.innerHTML = `❌ <strong>Lỗi gửi dữ liệu:</strong> ${err.message}. Bạn vẫn có thể tải file Excel (.xlsx) về máy để nộp.`;
        }
        return false;
    }
}

// ============================================================================
// 1. GỬI KẾT QUẢ BÀI TẬP NGỮ PHÁP
// ============================================================================
function submitGrammarResultToExcel(grammarId, correctCount, totalCount, detailsArray) {
    ensureStudentIdentity((student) => {
        const lesson = typeof currentLesson !== "undefined" ? currentLesson : null;
        const grammarObj = (lesson?.grammar || []).find(g => g.id === grammarId);
        const grammarTitle = grammarObj ? grammarObj.title : `Điểm ngữ pháp ${grammarId}`;

        const payload = {
            timestamp: new Date().toLocaleString("vi-VN"),
            studentName: student.name,
            studentClass: student.className,
            bookCode: lesson ? `Quyển ${lesson.bookCode}` : "",
            lessonTitle: lesson ? `Bài ${lesson.lessonNum}: ${lesson.titleZh || ""}` : "",
            sectionType: "Bài tập Ngữ pháp",
            exerciseName: grammarTitle,
            scoreSummary: `${correctCount}/${totalCount} câu đúng`,
            detailsText: detailsArray.map((d, i) =>
                `Câu ${i + 1}: Học viên viết "${d.userAnswer || "(bỏ trống)"}" | Đáp án: "${d.correctAnswer}" => ${d.isCorrect ? "Đúng" : "Sai"}`
            ).join("\n"),
            items: detailsArray
        };

        const statusEl = document.getElementById("grammar-excel-status");
        window._lastGrammarPayload = payload;
        sendPayloadToExcelWebhook(payload, statusEl);
    });
}

function downloadLastGrammarExcel() {
    if (!window._lastGrammarPayload) {
        alert("Bạn hãy bấm 'Nộp bài & Gửi Excel' trước để tạo bảng điểm!");
        return;
    }
    exportPayloadToXlsx(window._lastGrammarPayload, "KetQua_NguPhap");
}

// ============================================================================
// 2. THU THẬP & GỬI KẾT QUẢ PHIẾU BÀI TẬP (ĐẶT CÂU AI + PHIẾU MỞ RỘNG)
// ============================================================================
function collectWorksheetData() {
    const lesson = typeof currentLesson !== "undefined" ? currentLesson : null;
    const vocab = lesson?.vocab || [];
    const items = [];
    let answeredCount = 0;

    // A. Thu thập phần đặt câu với từ mới (#worksheet-ai-container)
    vocab.forEach((w, idx) => {
        const inputEl = document.getElementById(`ws-input-${idx}`);
        const fbEl = document.getElementById(`ws-fb-${idx}`);
        if (!inputEl) return;

        const ans = inputEl.value.trim();
        if (ans) answeredCount++;

        let aiNote = "";
        if (fbEl && !fbEl.classList.contains("hidden")) {
            aiNote = fbEl.innerText.replace(/Nhận xét của Giáo viên AI:\s*/i, "").trim();
        }

        items.push({
            question: `[Đặt câu từ mới] ${w.hz} (${w.py} - ${w.vi})`,
            userAnswer: ans || "(Chưa làm)",
            correctAnswer: aiNote || "(Chưa bấm AI chấm)",
            isCorrect: aiNote.includes("Đúng hoàn toàn") ? "Đạt" : (ans ? "Đã nộp" : "Chưa làm")
        });
    });

    // B. Thu thập thêm mọi câu hỏi trong #worksheet-container (từ tab-phieubaitap.js nếu có)
    const customContainer = document.getElementById("worksheet-container");
    if (customContainer) {
        const inputs = customContainer.querySelectorAll("input[type='text'], textarea, select");
        inputs.forEach((el, i) => {
            const val = (el.value || "").trim();
            if (val) answeredCount++;
            const card = el.closest("div");
            const labelText = card ? (card.querySelector("p, h4, label")?.innerText || `Câu mở rộng ${i + 1}`) : `Câu mở rộng ${i + 1}`;
            items.push({
                question: `[Phiếu mở rộng] ${labelText.slice(0, 100)}`,
                userAnswer: val || "(Chưa làm)",
                correctAnswer: "",
                isCorrect: val ? "Đã nộp" : "Chưa làm"
            });
        });

        const radioNames = new Set();
        customContainer.querySelectorAll("input[type='radio']").forEach(r => {
            if (r.name) radioNames.add(r.name);
        });
        radioNames.forEach((rName, idx) => {
            const checked = customContainer.querySelector(`input[name="${rName}"]:checked`);
            const val = checked ? checked.value : "";
            if (val) answeredCount++;
            items.push({
                question: `[Trắc nghiệm phiếu] Câu ${idx + 1} (${rName})`,
                userAnswer: val || "(Chưa chọn)",
                correctAnswer: "",
                isCorrect: val ? "Đã chọn" : "Chưa làm"
            });
        });
    }

    return {
        items,
        answeredCount,
        totalCount: items.length
    };
}

function submitWorksheetToExcel() {
    const collected = collectWorksheetData();
    if (collected.totalCount === 0) {
        alert("Không tìm thấy nội dung phiếu bài tập để nộp.");
        return;
    }
    if (collected.answeredCount === 0) {
        alert("Bạn chưa điền câu trả lời nào trong Phiếu bài tập!");
        return;
    }

    ensureStudentIdentity((student) => {
        const lesson = typeof currentLesson !== "undefined" ? currentLesson : null;
        const payload = {
            timestamp: new Date().toLocaleString("vi-VN"),
            studentName: student.name,
            studentClass: student.className,
            bookCode: lesson ? `Quyển ${lesson.bookCode}` : "",
            lessonTitle: lesson ? `Bài ${lesson.lessonNum}: ${lesson.titleZh || ""}` : "",
            sectionType: "Phiếu bài tập",
            exerciseName: "Đặt câu từ mới & Luyện tập phiếu",
            scoreSummary: `Hoàn thành ${collected.answeredCount}/${collected.totalCount} câu`,
            detailsText: collected.items.map((it, i) =>
                `${i + 1}. ${it.question}\n   -> Bài làm: ${it.userAnswer}${it.correctAnswer ? `\n   -> Nhận xét/Gợi ý: ${it.correctAnswer}` : ""}`
            ).join("\n"),
            items: collected.items
        };

        const statusEl = document.getElementById("worksheet-excel-status");
        sendPayloadToExcelWebhook(payload, statusEl);
    });
}

function downloadWorksheetExcel() {
    const collected = collectWorksheetData();
    const student = getStudentInfo();
    const lesson = typeof currentLesson !== "undefined" ? currentLesson : null;

    const payload = {
        timestamp: new Date().toLocaleString("vi-VN"),
        studentName: student.name || "HocVien",
        studentClass: student.className || "",
        bookCode: lesson ? `Quyển ${lesson.bookCode}` : "",
        lessonTitle: lesson ? `Bài ${lesson.lessonNum}: ${lesson.titleZh || ""}` : "",
        sectionType: "Phiếu bài tập",
        exerciseName: "Đặt câu từ mới & Luyện tập phiếu",
        scoreSummary: `Hoàn thành ${collected.answeredCount}/${collected.totalCount} câu`,
        items: collected.items
    };

    exportPayloadToXlsx(payload, "PhieuBaiTap");
}

// ============================================================================
// 3. XUẤT FILE EXCEL (.XLSX) TRỰC TIẾP TRÊN TRÌNH DUYỆT
// ============================================================================
function exportPayloadToXlsx(payload, filePrefix) {
    const rows = [
        ["Thời gian nộp", "Họ tên học viên", "Lớp", "Giáo trình", "Bài học", "Phần bài", "Câu hỏi / Từ vựng", "Bài làm của học viên", "Đáp án / Nhận xét AI", "Kết quả"]
    ];

    (payload.items || []).forEach((it, idx) => {
        rows.push([
            payload.timestamp,
            payload.studentName,
            payload.studentClass,
            payload.bookCode,
            payload.lessonTitle,
            `${payload.sectionType} - ${payload.exerciseName}`,
            it.question || `Câu ${idx + 1}`,
            it.userAnswer || "",
            it.correctAnswer || "",
            typeof it.isCorrect === "boolean" ? (it.isCorrect ? "Đúng" : "Sai") : (it.isCorrect || "")
        ]);
    });

    const safeName = (payload.studentName || "HocVien").replace(/[^a-zA-Z0-9\u00C0-\u1EF9_-]/g, "_");
    const fileName = `${filePrefix}_${safeName}_${new Date().toISOString().slice(0, 10)}.xlsx`;

    if (typeof XLSX !== "undefined") {
        const wb = XLSX.utils.book_new();
        const ws = XLSX.utils.aoa_to_sheet(rows);
        ws["!cols"] = [
            { wch: 20 }, { wch: 22 }, { wch: 12 }, { wch: 12 }, { wch: 22 },
            { wch: 26 }, { wch: 34 }, { wch: 36 }, { wch: 42 }, { wch: 12 }
        ];
        XLSX.utils.book_append_sheet(wb, ws, "KetQuaHocVien");
        XLSX.writeFile(wb, fileName);
    } else {
        const csv = "\uFEFF" + rows.map(r => r.map(c => `"${String(c).replace(/"/g, '""')}"`).join(",")).join("\n");
        const blob = new Blob([csv], { type: "text/csv;charset=utf-8;" });
        const link = document.createElement("a");
        link.href = URL.createObjectURL(blob);
        link.download = fileName.replace(".xlsx", ".csv");
        link.click();
    }
}

function copyAppsScriptCode() {
    const code = `function doPost(e) {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  if (sheet.getLastRow() === 0) {
    sheet.appendRow([
      "Thời gian nộp", "Họ tên học viên", "Lớp", "Giáo trình",
      "Bài học", "Loại bài tập", "Tên bài", "Điểm / Tổng kết", "Chi tiết bài làm"
    ]);
    sheet.getRange(1, 1, 1, 9).setFontWeight("bold").setBackground("#991b1b").setFontColor("#ffffff");
  }
  var data = JSON.parse(e.postData.contents);
  sheet.appendRow([
    data.timestamp || new Date().toLocaleString("vi-VN"),
    data.studentName || "",
    data.studentClass || "",
    data.bookCode || "",
    data.lessonTitle || "",
    data.sectionType || "",
    data.exerciseName || "",
    data.scoreSummary || "",
    data.detailsText || ""
  ]);
  return ContentService.createTextOutput(JSON.stringify({ status: "success" }))
    .setMimeType(ContentService.MimeType.JSON);
}`;
    navigator.clipboard.writeText(code).then(() => {
        const btn = document.getElementById("btn-copy-gas");
        if (btn) {
            const orig = btn.innerHTML;
            btn.innerHTML = "✅ Đã copy mã Apps Script!";
            setTimeout(() => btn.innerHTML = orig, 2500);
        }
    });
}

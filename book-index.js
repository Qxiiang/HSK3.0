// ============================================================================
// DANH MỤC NẠP DỮ LIỆU GIÁO TRÌNH & SÁCH BÀI TẬP HSK 3.0 (book-index.js)
// Khi thêm bài học mới vào thư mục data/, chỉ cần khai báo tên file tại đây.
// ============================================================================

window.HSK_LESSONS = window.HSK_LESSONS || {};
window.HSK_WORKBOOKS = window.HSK_WORKBOOKS || {};
window.HSK_WORKSHEETS = window.HSK_WORKSHEETS || {};

(function loadAllBookData() {
    const lessonCounts = [
        { prefix: "hsk1_bai", count: 15 },
        { prefix: "hsk2_bai", count: 15 },
        { prefix: "hsk3_bai", count: 18 },
        { prefix: "hsk4a_bai", count: 10 },
        { prefix: "hsk4b_bai", count: 10 }
    ];

    const files = [];

    // 1. Tự động sinh danh sách file bài học (hskX_baiY.js)
    lessonCounts.forEach(({ prefix, count }) => {
        for (let i = 1; i <= count; i++) {
            files.push(`data/${prefix}${i}.js`);
        }
    });

    // 2. Tự động sinh danh sách file sách bài tập (hskX_baiY_bt.js)
    lessonCounts.forEach(({ prefix, count }) => {
        for (let i = 1; i <= count; i++) {
            files.push(`data/${prefix}${i}_bt.js`);
        }
    });

    // 3. Các file chủ đề & phiếu bài tập mở rộng
    const extraFiles = [
        "data/hsk3_bai4_chude.js",
        "data/hsk3_bai1_pbt.js"
    ];

    const allScripts = [...files, ...extraFiles];
    let loadedCount = 0;

    function onScriptFinish() {
        loadedCount++;
        if (loadedCount === allScripts.length) {
            window.HSK_DATA_READY = true;
            window.dispatchEvent(new Event("hskDataLoaded"));
        }
    }

    allScripts.forEach(src => {
        const script = document.createElement("script");
        script.src = src;
        script.async = false; // Đảm bảo thực thi đúng thứ tự
        script.onload = onScriptFinish;
        script.onerror = onScriptFinish; // Bỏ qua nếu file chưa tồn tại mà không làm treo trang
        document.body.appendChild(script);
    });
})();

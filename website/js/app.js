// js/app.js

/**
 * 指定したMarkdownファイルを読み込み、HTMLに変換して表示する
 * @param {string} url - Markdownファイルのパス
 * @param {string} elementId - 描画先の要素ID
 */
async function loadMarkdown(url, elementId) {
    const element = document.getElementById(elementId);
    if (!element) return;

    try {
        element.innerHTML = '<div class="text-center py-10"><div class="animate-spin rounded-full h-8 w-8 border-b-2 border-slate-800 mx-auto"></div><p class="mt-2 text-slate-500">Loading...</p></div>';
        
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const text = await response.text();
        
        // markedが読み込まれているか確認
        if (typeof marked === 'undefined') {
            throw new Error("marked.js is not loaded.");
        }

        // MarkdownをHTMLに変換
        const html = marked.parse(text);
        
        // 描画 (Tailwind Typographyのクラスである `prose` を適用済みの要素に入れる想定)
        element.innerHTML = html;

    } catch (error) {
        console.error("Failed to load markdown:", error);
        element.innerHTML = `<div class="bg-red-50 text-red-500 p-4 rounded-lg">
            <h3 class="font-bold">コンテンツの読み込みに失敗しました</h3>
            <p class="text-sm">ファイルが存在しないか、ネットワークエラーです。</p>
            <p class="text-xs mt-2 font-mono">${url}</p>
        </div>`;
    }
}

/**
 * URLなどのクエリパラメータから現在の週（week）を取得
 */
function getCurrentWeek() {
    const params = new URLSearchParams(window.location.search);
    return params.get('week') || '34system/week01'; // デフォルトは Week01
}

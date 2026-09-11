// --- 1. Animacje przewijania ---
document.addEventListener("DOMContentLoaded", function () {
    const items = document.querySelectorAll('.timeline-item');
    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = 1;
                entry.target.style.transform = 'translateY(0)';
            }
        });
    });
    items.forEach(item => {
        item.style.opacity = 0;
        item.style.transform = 'translateY(30px)';
        item.style.transition = 'all 0.6s ease-out';
        observer.observe(item);
    });
});

// --- 2. Dynamiczne pobieranie algorytmów z plików .py ---
async function openEditor(algorithm) {
    const modal = document.getElementById('editorModal');
    const codeArea = document.getElementById('pythonCode');
    const outputArea = document.getElementById('pythonOutput');

    modal.style.display = 'block';
    outputArea.innerHTML = 'Kliknij "Run", aby zobaczyć wynik...';
    codeArea.value = '# Wczytywanie pliku Python...';

    try {
        const response = await fetch(`algorithms/${algorithm}.py`);
        if (!response.ok) {
            throw new Error(`Nie udało się wczytać pliku algorithms/${algorithm}.py`);
        }
        const codeText = await response.text();
        codeArea.value = codeText;
    } catch (err) {
        codeArea.value = `# Błąd ładowania pliku:\n# ${err.message}\n\n# Upewnij się, że uruchamiasz stronę przez serwer (np. Live Server w VS Code).`;
    }
}

function closeEditor() {
    document.getElementById('editorModal').style.display = 'none';
}

// --- 3. Silnik Pythona w przeglądarce (Skulpt) ---
function outf(text) {
    var mypre = document.getElementById("pythonOutput");
    mypre.innerHTML = mypre.innerHTML + text;
}

function builtinRead(x) {
    if (Sk.builtinFiles === undefined || Sk.builtinFiles["files"][x] === undefined)
        throw "File not found: '" + x + "'";
    return Sk.builtinFiles["files"][x];
}

function runPython() {
    var prog = document.getElementById("pythonCode").value;
    var mypre = document.getElementById("pythonOutput");
    mypre.innerHTML = '';

    Sk.pre = "pythonOutput";
    Sk.configure({ output: outf, read: builtinRead });

    var myPromise = Sk.misceval.asyncToPromise(function () {
        return Sk.importMainWithBody("<stdin>", false, prog, true);
    });

    myPromise.catch(function (err) {
        mypre.innerHTML = "<span style='color:red; font-weight:bold;'>" + err.toString() + "</span>";
    });
}
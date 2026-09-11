document.addEventListener("DOMContentLoaded", function () {
    // Animacja Timeline Items
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

    // animation stuck
    const canvas = document.getElementById("confetti");
    if (canvas) {
        const ctx = canvas.getContext("2d");

        const COLORS = [
            [238, 96, 169],
            [68, 213, 217],
            [245, 187, 152],
            [144, 148, 188],
            [235, 234, 77]
        ];

        let W = window.innerWidth;
        let H = window.innerHeight;
        canvas.width = W;
        canvas.height = H;

        window.addEventListener('resize', function() {
            W = window.innerWidth;
            H = window.innerHeight;
            canvas.width = W;
            canvas.height = H;
        });

        const mp = 80;
        const particles = [];

        for (let i = 0; i < mp; i++) {
            particles.push({
                x: Math.random() * W,
                y: Math.random() * H,
                fontSize: Math.floor(Math.random() * 10 + 12),
                speed: Math.random() * 2 + 1,         
                digit: Math.floor(Math.random() * 10).toString(), 
                color: COLORS[Math.floor(Math.random() * COLORS.length)]
            });
        }

        function drawDigits() {
            ctx.clearRect(0, 0, W, H);

            for (let i = 0; i < mp; i++) {
                const p = particles[i];

                ctx.fillStyle = "rgba(" + p.color.join(",") + ", 0.8)";
                ctx.font = `${p.fontSize}px 'Montserrat', monospace`;
                ctx.fillText(p.digit, p.x, p.y);
            }

            update();
        }

        function update() {
            for (let i = 0; i < mp; i++) {
                const p = particles[i];
                
                p.y += p.speed;

                if (p.y > H + 20) {
                    particles[i] = {
                        x: Math.random() * W,
                        y: -10,
                        fontSize: Math.floor(Math.random() * 10 + 12),
                        speed: Math.random() * 2 + 1,
                        digit: Math.floor(Math.random() * 10).toString(),
                        color: COLORS[Math.floor(Math.random() * COLORS.length)]
                    };
                }
            }
        }

        setInterval(drawDigits, 33);
    }
});

//Skulpt
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
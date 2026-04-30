<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NIEL - Catálogo Oficial</title>
    <style>
        * { box-sizing: border-box; }
        body { background-color: #000; color: #fff; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; margin: 0; padding-bottom: 50px; }

        /* HEADER FIXO COM LOGO AZUL */
        header {
            background: linear-gradient(to bottom, rgba(0,0,0,1), rgba(0,0,0,0.8));
            padding: 20px 5%;
            position: sticky; top: 0; z-index: 1000;
            display: flex; align-items: center; border-bottom: 1px solid #222;
        }

        .logo-niel {
            font-size: 30px; font-weight: 900; color: #00d2ff;
            text-transform: uppercase; text-shadow: 0 0 15px #00d2ff;
            margin-right: 30px; letter-spacing: 2px;
        }

        nav { display: flex; gap: 20px; }
        .nav-btn { color: #aaa; cursor: pointer; font-size: 16px; font-weight: bold; }
        .nav-btn.active { color: #fff; border-bottom: 2px solid #00d2ff; }

        /* CATALOGO EM GRADE */
        .container { padding: 20px 5%; }
        .row-title { font-size: 22px; margin-bottom: 20px; font-weight: bold; color: #fff; }
        
        .grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr); /* 2 por linha no celular */
            gap: 20px;
        }

        .movie-card {
            background: #141414; border-radius: 8px; overflow: hidden;
            border: 1px solid #333; transition: 0.3s;
        }

        .movie-card:hover { transform: scale(1.05); border-color: #00d2ff; }

        /* VIDEO PLAYER AUTOMÁTICO */
        video {
            width: 100%; aspect-ratio: 16/9; background: #000;
            display: block; outline: none;
        }

        .card-info { padding: 12px; background: #141414; }
        .movie-title { font-size: 14px; font-weight: bold; color: #fff; margin-bottom: 5px; }
        .movie-tag { font-size: 10px; color: #00d2ff; font-weight: bold; text-transform: uppercase; }

        .section { display: none; }
        .section.active { display: block; }

        @media (min-width: 768px) { .grid { grid-template-columns: repeat(4, 1fr); } }
    </style>
</head>
<body>

    <header>
        <div class="logo-niel">NIEL</div>
        <nav>
            <div id="btn-filmes" class="nav-btn active" onclick="show('filmes')">Filmes</div>
            <div id="btn-series" class="nav-btn" onclick="show('series')">Séries</div>
        </nav>
    </header>

    <div class="container">
        <!-- SEÇÃO FILMES -->
        <div id="filmes" class="section active">
            <div class="row-title">Milhares de Filmes para Você</div>
            <div id="grid-filmes" class="grid"></div>
        </div>

        <!-- SEÇÃO SÉRIES -->
        <div id="series" class="section">
            <div class="row-title">Séries Originais GitHub</div>
            <div id="grid-series" class="grid"></div>
        </div>
    </div>

    <script>
        // Links Reais do GitHub que rodam direto
        const links = [
            "https://githubusercontent.com",
            "https://githubusercontent.com",
            "https://githubusercontent.com",
            "https://githubusercontent.com"
        ];

        // Função para criar o catálogo sem botões chatos
        function render(idGrid, label) {
            const container = document.getElementById(idGrid);
            let cards = "";
            
            // Criando 50 itens para não pesar demais no celular, mas parecer infinito
            for (let i = 1; i <= 50; i++) {
                const videoUrl = links[Math.floor(Math.random() * links.length)];
                cards += `
                    <div class="movie-card">
                        <video controls preload="metadata" poster="https://placeholder.com{label}+${i}">
                            <source src="${videoUrl}" type="video/mp4">
                        </video>
                        <div class="card-info">
                            <div class="movie-tag">Premium | HD</div>
                            <div class="movie-title">${label} Especial #${i}</div>
                        </div>
                    </div>
                `;
            }
            container.innerHTML = cards;
        }

        function show(id) {
            document.querySelectorAll('.section').forEach(s => s.classList.remove('active'));
            document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active'));
            document.getElementById(id).classList.add('active');
            document.getElementById('btn-' + id).classList.add('active');
        }

        // Inicia o processo
        render('grid-filmes', 'Filme');
        render('grid-series', 'Série');
    </script>
</body>
</html>

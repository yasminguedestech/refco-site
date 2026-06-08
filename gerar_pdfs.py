from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
from reportlab.lib.units import mm

W, H = A4

# ── Cores RefCo ───────────────────────────────────────────────
ROXO       = HexColor("#5B2D8E")
ROXO_DARK  = HexColor("#3D1580")
LILAS      = HexColor("#EDE7F6")
LILAS_MED  = HexColor("#D8CFF0")
ROXO_LIGHT = HexColor("#7B3FC4")
BRANCO     = HexColor("#FFFFFF")
CINZA_T    = HexColor("#888888")
VERDE_OK   = HexColor("#2E9E5B")

# ── Helpers ───────────────────────────────────────────────────
def fundo(c, cor=LILAS):
    c.setFillColor(cor)
    c.rect(0, 0, W, H, fill=1, stroke=0)

def barra_topo(c, cor=ROXO, h=14*mm):
    c.setFillColor(cor)
    c.rect(0, H - h, W, h, fill=1, stroke=0)

def barra_rodape(c, texto="refcotech.com · @refcotech", cor=ROXO):
    c.setFillColor(cor)
    c.rect(0, 0, W, 10*mm, fill=1, stroke=0)
    c.setFillColor(BRANCO)
    c.setFont("Helvetica", 7.5)
    c.drawCentredString(W/2, 3.2*mm, texto)

def logo_texto(c, x, y, tamanho=18, cor=BRANCO):
    c.setFillColor(cor)
    c.setFont("Helvetica-Bold", tamanho)
    c.drawString(x, y, "RefCo")

def titulo_secao(c, texto, y, cor=ROXO_DARK):
    c.setFillColor(cor)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(25*mm, y, texto)
    c.setStrokeColor(ROXO_LIGHT)
    c.setLineWidth(1.5)
    c.line(25*mm, y - 3*mm, 180*mm, y - 3*mm)

def caixa_cor(c, x, y, w, h, hex_cor, nome, hex_txt):
    cor = HexColor(hex_cor)
    c.setFillColor(cor)
    c.roundRect(x, y, w, h, 4*mm, fill=1, stroke=0)
    # nome da cor
    c.setFillColor(BRANCO if _luminancia(hex_cor) < 0.4 else ROXO_DARK)
    c.setFont("Helvetica-Bold", 8.5)
    c.drawCentredString(x + w/2, y + h - 7*mm, nome)
    c.setFont("Helvetica", 7.5)
    c.drawCentredString(x + w/2, y + 3.5*mm, hex_txt)

def _luminancia(hex_cor):
    r, g, b = int(hex_cor[1:3],16)/255, int(hex_cor[3:5],16)/255, int(hex_cor[5:7],16)/255
    return 0.299*r + 0.587*g + 0.114*b

def checkbox(c, x, y, marcado=False):
    c.setStrokeColor(ROXO)
    c.setLineWidth(1.2)
    c.roundRect(x, y, 4.5*mm, 4.5*mm, 0.8*mm, fill=0, stroke=1)
    if marcado:
        c.setStrokeColor(VERDE_OK)
        c.setLineWidth(1.5)
        c.line(x+1*mm, y+2.2*mm, x+1.8*mm, y+1*mm)
        c.line(x+1.8*mm, y+1*mm, x+3.5*mm, y+3.5*mm)

def item_check(c, x, y, texto, sub="", marcado=False):
    checkbox(c, x, y)
    c.setFillColor(ROXO_DARK)
    c.setFont("Helvetica-Bold", 9.5)
    c.drawString(x + 6.5*mm, y + 1.2*mm, texto)
    if sub:
        c.setFillColor(CINZA_T)
        c.setFont("Helvetica", 8)
        c.drawString(x + 6.5*mm, y - 3.5*mm, sub)

# ══════════════════════════════════════════════════════════════
#   KIT DE REFERENCIAS DIGITAL
# ══════════════════════════════════════════════════════════════
def criar_kit():
    c = canvas.Canvas(
        "C:/Users/Yasmin Guedes/OneDrive/Documentos/project/refco-site/kit-referencias-refco.pdf",
        pagesize=A4
    )

    # ── CAPA ─────────────────────────────────────────────────
    fundo(c, ROXO_DARK)

    # Forma decorativa
    c.setFillColor(HexColor("#4A2380"))
    c.circle(W + 30*mm, H - 40*mm, 80*mm, fill=1, stroke=0)
    c.setFillColor(HexColor("#6B35A0"))
    c.circle(-20*mm, 30*mm, 60*mm, fill=1, stroke=0)

    # Badge
    c.setFillColor(ROXO_LIGHT)
    c.roundRect(25*mm, H - 52*mm, 45*mm, 8*mm, 4*mm, fill=1, stroke=0)
    c.setFillColor(BRANCO)
    c.setFont("Helvetica-Bold", 7)
    c.drawString(29*mm, H - 47*mm, "GRATUITO  .  REFCO")

    logo_texto(c, 25*mm, H - 72*mm, 28, BRANCO)

    c.setFillColor(BRANCO)
    c.setFont("Helvetica-Bold", 32)
    c.drawString(25*mm, H - 100*mm, "Kit de")
    c.drawString(25*mm, H - 122*mm, "Referencias")
    c.drawString(25*mm, H - 144*mm, "Digital")

    c.setFillColor(LILAS_MED)
    c.setFont("Helvetica", 11)
    c.drawString(25*mm, H - 162*mm, "Paletas de cor . Tipografias . Inspiracoes de layout")

    # divisor
    c.setStrokeColor(ROXO_LIGHT)
    c.setLineWidth(1)
    c.line(25*mm, H - 172*mm, 120*mm, H - 172*mm)

    c.setFillColor(LILAS_MED)
    c.setFont("Helvetica", 10)
    c.drawString(25*mm, H - 185*mm, "Tudo que voce precisa para comecar a criar")
    c.drawString(25*mm, H - 197*mm, "sua presenca digital com identidade propria.")

    barra_rodape(c)
    c.showPage()

    # ── PAG 2: PALETAS ─────────────────────────────────────────
    fundo(c, LILAS)
    barra_topo(c)
    barra_rodape(c)

    c.setFillColor(BRANCO)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(25*mm, H - 8*mm, "KIT DE REFERENCIAS DIGITAL  .  REFCO")

    titulo_secao(c, "Paletas de Cor", H - 28*mm)

    c.setFillColor(ROXO_DARK)
    c.setFont("Helvetica", 9)
    c.drawString(25*mm, H - 38*mm, "Combinacoes de cor profissionais para o seu projeto digital.")

    paletas = [
        ("Violeta Moderno",  ["#5B2D8E","#7B3FC4","#EDE7F6","#FFFFFF","#1A1A2E"]),
        ("Terra Criativa",   ["#C97B3B","#E8B98A","#F5ECD7","#4A3728","#2C1810"]),
        ("Digital Fresco",   ["#0EA5E9","#38BDF8","#E0F2FE","#0C4A6E","#FFFFFF"]),
        ("Minimalista Dark", ["#18181B","#3F3F46","#71717A","#D4D4D8","#FAFAFA"]),
        ("Verde Confianca",  ["#16A34A","#4ADE80","#DCFCE7","#14532D","#FFFFFF"]),
    ]

    y_base = H - 48*mm
    col_w  = 30*mm
    gap    = 6*mm
    for pi, (nome_pal, cores) in enumerate(paletas):
        y = y_base - pi * 30*mm
        c.setFillColor(ROXO_DARK)
        c.setFont("Helvetica-Bold", 9)
        c.drawString(25*mm, y, nome_pal)
        for ci, cor_hex in enumerate(cores):
            caixa_cor(c, 25*mm + ci*(col_w + gap), y - 20*mm, col_w, 17*mm, cor_hex, "", cor_hex)

    c.showPage()

    # ── PAG 3: TIPOGRAFIA ──────────────────────────────────────
    fundo(c, LILAS)
    barra_topo(c)
    barra_rodape(c)

    c.setFillColor(BRANCO)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(25*mm, H - 8*mm, "KIT DE REFERENCIAS DIGITAL  .  REFCO")

    titulo_secao(c, "Tipografias Profissionais", H - 28*mm)

    c.setFillColor(ROXO_DARK)
    c.setFont("Helvetica", 9)
    c.drawString(25*mm, H - 38*mm, "Duplas de fontes do Google Fonts — gratuitas e prontas para usar.")

    fontes = [
        ("Syne + Plus Jakarta Sans",    "Moderna e tecnica. Otima para portfolios criativos e sites de tecnologia.",   "fonts.google.com  .  Uso: titulos em Syne 800, corpo em Plus Jakarta 400"),
        ("Playfair Display + Lato",     "Elegante e editorial. Ideal para marcas pessoais e profissionais criativos.", "fonts.google.com  .  Uso: titulos em Playfair italic 700, corpo em Lato 400"),
        ("Space Grotesk + Inter",       "Limpa e contemporanea. Perfeita para devs, dados e tech.",                    "fonts.google.com  .  Uso: titulos em Space Grotesk 700, corpo em Inter 400"),
        ("Fraunces + DM Sans",          "Com personalidade. Para marcas autorais e diferenciais.",                     "fonts.google.com  .  Uso: titulos em Fraunces italic, corpo em DM Sans 400"),
        ("Montserrat + Source Sans Pro","Classica e versatil. Funciona para qualquer segmento.",                       "fonts.google.com  .  Uso: titulos em Montserrat 700, corpo em Source Sans 400"),
    ]

    y = H - 48*mm
    for nome_f, desc, uso in fontes:
        c.setFillColor(BRANCO)
        c.roundRect(25*mm, y - 18*mm, W - 50*mm, 20*mm, 3*mm, fill=1, stroke=0)
        c.setFillColor(ROXO)
        c.setFont("Helvetica-Bold", 10)
        c.drawString(29*mm, y - 5*mm, nome_f)
        c.setFillColor(ROXO_DARK)
        c.setFont("Helvetica", 8)
        c.drawString(29*mm, y - 10.5*mm, desc)
        c.setFillColor(CINZA_T)
        c.setFont("Helvetica", 7.5)
        c.drawString(29*mm, y - 15.5*mm, uso)
        y -= 24*mm

    c.showPage()

    # ── PAG 4: LAYOUT ──────────────────────────────────────────
    fundo(c, LILAS)
    barra_topo(c)
    barra_rodape(c)

    c.setFillColor(BRANCO)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(25*mm, H - 8*mm, "KIT DE REFERENCIAS DIGITAL  .  REFCO")

    titulo_secao(c, "Inspiracoes de Layout", H - 28*mm)

    c.setFillColor(ROXO_DARK)
    c.setFont("Helvetica", 9)
    c.drawString(25*mm, H - 38*mm, "Padroes que funcionam — e por que funcionam.")

    dicas = [
        ("Hero com foco no nome",
         "Primeira dobra: seu nome em destaque, subtitulo com o que voce faz e CTA claro.",
         "Ex: 'Ana Lima — Designer de Produto'  +  'Transformo ideias em interfaces que convertem'"),
        ("Grade de projetos 3x2",
         "Mostre no maximo 6 projetos. Qualidade > quantidade. Thumbnail impactante.",
         "Dica: use imagens horizontais 16:9 com hover mostrando titulo e categoria."),
        ("Sobre com foto e numeros",
         "Uma foto profissional ou de perfil + 3 numeros de impacto (anos, projetos, clientes).",
         "Ex: '4 anos de experiencia  .  23 projetos entregues  .  100% de satisfacao'"),
        ("Secao de habilidades visual",
         "Evite listas simples. Use tags, icones ou barras de progresso com moderacao.",
         "Dica: agrupe por area (Design, Codigo, Ferramentas) e limite a 12 itens."),
        ("Contato direto e visivel",
         "Nao esconda o contato. Coloque email clicavel e link do LinkedIn no topo e rodape.",
         "Dica: adicione 'Aberto a oportunidades' se estiver buscando trabalho."),
        ("Tipografia com hierarquia clara",
         "3 tamanhos: grande (titulo), medio (subtitulo), pequeno (corpo). Nunca mais que isso.",
         "Regra: se o leitor nao sabe o que ler primeiro, o layout precisa de ajuste."),
    ]

    y = H - 48*mm
    col = 0
    for titulo_d, desc_d, dica_d in dicas:
        x = 25*mm if col == 0 else 110*mm
        c.setFillColor(BRANCO)
        c.roundRect(x, y - 32*mm, 80*mm, 35*mm, 3*mm, fill=1, stroke=0)
        c.setFillColor(ROXO)
        c.setFont("Helvetica-Bold", 8.5)
        _draw_wrapped(c, titulo_d, x+4*mm, y - 8*mm, 72*mm, 8.5)
        c.setFillColor(ROXO_DARK)
        c.setFont("Helvetica", 7.5)
        _draw_wrapped(c, desc_d, x+4*mm, y - 17*mm, 72*mm, 7.5)
        c.setFillColor(CINZA_T)
        c.setFont("Helvetica-Oblique", 7)
        _draw_wrapped(c, dica_d, x+4*mm, y - 27*mm, 72*mm, 7)
        col += 1
        if col == 2:
            col = 0
            y -= 40*mm

    c.showPage()

    # ── PAG 5: ENCERRAMENTO ────────────────────────────────────
    fundo(c, ROXO_DARK)
    c.setFillColor(HexColor("#4A2380"))
    c.circle(W + 20*mm, H/2, 70*mm, fill=1, stroke=0)

    logo_texto(c, 25*mm, H - 50*mm, 24, BRANCO)

    c.setFillColor(BRANCO)
    c.setFont("Helvetica-Bold", 22)
    c.drawString(25*mm, H - 78*mm, "Pronto para criar")
    c.drawString(25*mm, H - 97*mm, "algo incrivel?")

    c.setFillColor(LILAS_MED)
    c.setFont("Helvetica", 11)
    c.drawString(25*mm, H - 116*mm, "Use este kit como ponto de partida, nao como")
    c.drawString(25*mm, H - 128*mm, "regra. Sua identidade e o que vai diferenciar")
    c.drawString(25*mm, H - 140*mm, "o seu projeto de todos os outros.")

    c.setStrokeColor(ROXO_LIGHT)
    c.setLineWidth(1)
    c.line(25*mm, H - 154*mm, 80*mm, H - 154*mm)

    c.setFillColor(BRANCO)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(25*mm, H - 167*mm, "Quer ajuda para colocar em pratica?")
    c.setFillColor(LILAS_MED)
    c.setFont("Helvetica", 9.5)
    c.drawString(25*mm, H - 178*mm, "instagram.com/refcotech")
    c.drawString(25*mm, H - 190*mm, "refcotech.com")

    barra_rodape(c, "Kit de Referencias Digital  .  RefCo  .  @refcotech")
    c.showPage()
    c.save()
    print("kit-referencias-refco.pdf criado!")


# ══════════════════════════════════════════════════════════════
#   CHECKLIST DO PORTFOLIO PERFEITO
# ══════════════════════════════════════════════════════════════
def criar_checklist():
    c = canvas.Canvas(
        "C:/Users/Yasmin Guedes/OneDrive/Documentos/project/refco-site/checklist-portfolio-refco.pdf",
        pagesize=A4
    )

    # ── CAPA ─────────────────────────────────────────────────
    fundo(c, LILAS)

    c.setFillColor(ROXO_DARK)
    c.rect(0, H - 90*mm, W, 90*mm, fill=1, stroke=0)
    c.setFillColor(HexColor("#4A2380"))
    c.circle(W - 10*mm, H - 45*mm, 55*mm, fill=1, stroke=0)

    c.setFillColor(LILAS_MED)
    c.setFont("Helvetica-Bold", 8)
    c.drawString(25*mm, H - 16*mm, "CHECKLIST GRATUITO  .  REFCO")

    logo_texto(c, 25*mm, H - 32*mm, 22, BRANCO)

    c.setFillColor(BRANCO)
    c.setFont("Helvetica-Bold", 30)
    c.drawString(25*mm, H - 60*mm, "Checklist do")
    c.drawString(25*mm, H - 80*mm, "Portfolio Perfeito")

    # Secoes badge
    secoes = ["Estrutura","Conteudo","Design","SEO","Publicacao"]
    x_b = 25*mm
    c.setFillColor(ROXO)
    c.roundRect(x_b - 2*mm, H - 108*mm, 155*mm, 10*mm, 5*mm, fill=1, stroke=0)
    c.setFillColor(BRANCO)
    c.setFont("Helvetica", 8)
    for s in secoes:
        c.drawString(x_b, H - 102*mm, s)
        x_b += 31*mm

    c.setFillColor(ROXO_DARK)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(25*mm, H - 128*mm, "Tudo que o seu portfolio precisa ter")
    c.setFont("Helvetica", 11)
    c.drawString(25*mm, H - 142*mm, "para abrir portas, gerar oportunidades")
    c.drawString(25*mm, H - 155*mm, "e representar quem voce e de verdade.")

    # Numero de itens
    c.setFillColor(ROXO)
    c.circle(25*mm + 12*mm, H - 195*mm, 12*mm, fill=1, stroke=0)
    c.setFillColor(BRANCO)
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(25*mm + 12*mm, H - 198*mm, "32")
    c.setFillColor(ROXO_DARK)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(25*mm + 28*mm, H - 193*mm, "itens para verificar")
    c.setFont("Helvetica", 9)
    c.drawString(25*mm + 28*mm, H - 201*mm, "marque cada um conforme completa")

    barra_rodape(c)
    c.showPage()

    # ── PAG 2: ESTRUTURA + CONTEUDO ────────────────────────────
    fundo(c, LILAS)
    barra_topo(c)
    barra_rodape(c)
    c.setFillColor(BRANCO)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(25*mm, H - 8*mm, "CHECKLIST DO PORTFOLIO PERFEITO  .  REFCO")

    titulo_secao(c, "1. Estrutura", H - 28*mm)

    estrutura = [
        ("Pagina inicial (home) clara",     "Deixa obvio quem voce e e o que faz nos primeiros 3 segundos"),
        ("Pagina de projetos",               "Galeria ou grade com seus melhores trabalhos"),
        ("Pagina Sobre",                     "Sua historia, trajetoria e o que te diferencia"),
        ("Pagina de Contato",                "Formulario ou e-mail clicavel + redes sociais"),
        ("Menu de navegacao visivel",        "Links claros, presentes em todas as paginas"),
        ("Dominio proprio",                  "Ex: seunome.com ou seunome.dev — evite subdominos gratuitos"),
        ("HTTPS ativo",                      "Certificado SSL instalado — obrigatorio para credibilidade"),
    ]

    y = H - 38*mm
    for txt, sub in estrutura:
        item_check(c, 25*mm, y, txt, sub)
        y -= 11.5*mm

    titulo_secao(c, "2. Conteudo", y - 5*mm)
    y -= 16*mm

    conteudo = [
        ("Titulo/headline impactante",      "Nao so o cargo — o que voce faz de diferente"),
        ("Descricao profissional (bio)",    "2-3 frases: quem voce e, o que faz e para quem"),
        ("Minimo 3 projetos completos",     "Com contexto: problema, solucao e resultado"),
        ("Foto profissional",               "Rosto visivel, iluminacao boa, fundo neutro"),
        ("Depoimentos ou resultados",       "Provas sociais aumentam muito a confianca"),
        ("Links para redes relevantes",     "LinkedIn, GitHub, Behance — conforme sua area"),
        ("CTA (chamada para acao) clara",  "Botao de contato visivel acima da dobra"),
    ]

    for txt, sub in conteudo:
        item_check(c, 25*mm, y, txt, sub)
        y -= 11.5*mm

    c.showPage()

    # ── PAG 3: DESIGN + SEO + PUBLICACAO ──────────────────────
    fundo(c, LILAS)
    barra_topo(c)
    barra_rodape(c)
    c.setFillColor(BRANCO)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(25*mm, H - 8*mm, "CHECKLIST DO PORTFOLIO PERFEITO  .  REFCO")

    titulo_secao(c, "3. Design Visual", H - 28*mm)

    design = [
        ("Paleta de ate 3 cores",           "Primaria, secundaria e neutra — coerencia visual"),
        ("Maximo 2 fontes",                 "Uma para titulos, outra para corpo de texto"),
        ("Espacamento e respiro generoso",  "Nao lotea a pagina — o branco tambem comunica"),
        ("Imagens de alta qualidade",       "Nada pixelado ou esticado"),
        ("Responsivo no celular",           "+60% dos acessos vem de mobile — teste sempre"),
        ("Carregamento rapido",             "Imagens otimizadas, menos plugins, codigo limpo"),
    ]

    y = H - 38*mm
    for txt, sub in design:
        item_check(c, 25*mm, y, txt, sub)
        y -= 11.5*mm

    titulo_secao(c, "4. SEO Basico", y - 5*mm)
    y -= 16*mm

    seo = [
        ("Title tag com seu nome + cargo",  "Ex: 'Ana Lima | Designer de UX'"),
        ("Meta description preenchida",     "Resumo de 150 caracteres sobre voce e seu trabalho"),
        ("URLs amigaveis",                  "Ex: /projetos/app-financas  nao  /page?id=3"),
        ("Texto alternativo nas imagens",   "Descreva cada imagem — ajuda no SEO e acessibilidade"),
        ("Google Search Console configurado","Permite acompanhar indexacao e cliques organicos"),
    ]

    for txt, sub in seo:
        item_check(c, 25*mm, y, txt, sub)
        y -= 11.5*mm

    titulo_secao(c, "5. Publicacao e Lancamento", y - 5*mm)
    y -= 16*mm

    publicacao = [
        ("Testado em Chrome, Safari e Firefox","Compatibilidade entre navegadores"),
        ("Testado no celular (iOS e Android)", "Layout e interacoes funcionando"),
        ("Sem links quebrados",               "Clique em todos os links antes de publicar"),
        ("Formulario de contato funcionando", "Envie uma mensagem de teste"),
        ("Analytics instalado",               "Google Analytics ou Plausible para acompanhar visitas"),
        ("Compartilhado no LinkedIn",         "Anuncie o lancamento — visibilidade inicial e essencial"),
        ("URL na bio de todas as redes",      "Instagram, LinkedIn, GitHub, etc."),
    ]

    for txt, sub in publicacao:
        item_check(c, 25*mm, y, txt, sub)
        y -= 11.5*mm

    c.showPage()

    # ── PAG 4: ENCERRAMENTO ────────────────────────────────────
    fundo(c, ROXO_DARK)
    c.setFillColor(HexColor("#4A2380"))
    c.circle(-15*mm, H - 60*mm, 65*mm, fill=1, stroke=0)

    logo_texto(c, 25*mm, H - 48*mm, 24, BRANCO)

    c.setFillColor(BRANCO)
    c.setFont("Helvetica-Bold", 22)
    c.drawString(25*mm, H - 76*mm, "Seu portfolio esta")
    c.drawString(25*mm, H - 95*mm, "pronto. E agora?")

    proximos = [
        ("Compartilhe", "Poste no LinkedIn, mande para recrutadores e clientes em potencial."),
        ("Atualize sempre", "Adicione novos projetos a cada 2-3 meses. Portfolio parado passa imagem errada."),
        ("Peca feedback", "Mostre para alguem da area e pergunte: ficou claro o que eu faco?"),
        ("Monitore os acessos", "Use o Google Analytics para ver de onde vem seu trafego."),
    ]

    y = H - 116*mm
    for titulo_p, desc_p in proximos:
        c.setFillColor(ROXO_LIGHT)
        c.circle(27*mm, y + 1.5*mm, 1.8*mm, fill=1, stroke=0)
        c.setFillColor(BRANCO)
        c.setFont("Helvetica-Bold", 10)
        c.drawString(32*mm, y, titulo_p)
        c.setFillColor(LILAS_MED)
        c.setFont("Helvetica", 8.5)
        c.drawString(32*mm, y - 7*mm, desc_p[:70])
        if len(desc_p) > 70:
            c.drawString(32*mm, y - 14*mm, desc_p[70:])
        y -= 26*mm

    c.setStrokeColor(ROXO_LIGHT)
    c.setLineWidth(1)
    c.line(25*mm, y, 80*mm, y)
    y -= 12*mm

    c.setFillColor(BRANCO)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(25*mm, y, "Precisa de ajuda para montar o seu portfolio?")
    c.setFillColor(LILAS_MED)
    c.setFont("Helvetica", 9.5)
    c.drawString(25*mm, y - 11*mm, "instagram.com/refcotech")

    barra_rodape(c, "Checklist do Portfolio Perfeito  .  RefCo  .  @refcotech")
    c.showPage()
    c.save()
    print("checklist-portfolio-refco.pdf criado!")


# ── Helper: texto com quebra de linha ─────────────────────────
def _draw_wrapped(c, texto, x, y, max_w, font_size, interline=4):
    words = texto.split()
    line = ""
    yi = y
    for w in words:
        test = (line + " " + w).strip()
        if c.stringWidth(test, c._fontname, font_size) <= max_w:
            line = test
        else:
            c.drawString(x, yi, line)
            yi -= (font_size + interline) * 0.352778  # pt -> mm -> unidades
            line = w
    if line:
        c.drawString(x, yi, line)


if __name__ == "__main__":
    criar_kit()
    criar_checklist()
    print("Ambos os PDFs gerados com sucesso!")

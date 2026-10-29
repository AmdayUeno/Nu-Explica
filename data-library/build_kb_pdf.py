import sys
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, KeepTogether
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

OUT = sys.argv[1]

pdfmetrics.registerFont(TTFont("Arial", r"C:\Windows\Fonts\arial.ttf"))
pdfmetrics.registerFont(TTFont("Arial-Bold", r"C:\Windows\Fonts\arialbd.ttf"))
pdfmetrics.registerFont(TTFont("Arial-Italic", r"C:\Windows\Fonts\ariali.ttf"))
pdfmetrics.registerFontFamily("Arial", normal="Arial", bold="Arial-Bold", italic="Arial-Italic")

ROXO = colors.HexColor("#820AD1")
CINZA = colors.HexColor("#555555")

title = ParagraphStyle("t", fontName="Arial-Bold", fontSize=22, leading=28, textColor=ROXO, spaceAfter=6)
subtitle = ParagraphStyle("st", fontName="Arial", fontSize=11, leading=15, textColor=CINZA, spaceAfter=14)
h1 = ParagraphStyle("h1", fontName="Arial-Bold", fontSize=15, leading=20, textColor=ROXO, spaceBefore=14, spaceAfter=6)
h2 = ParagraphStyle("h2", fontName="Arial-Bold", fontSize=11.5, leading=15, spaceBefore=8, spaceAfter=3)
body = ParagraphStyle("b", fontName="Arial", fontSize=10.5, leading=15, spaceAfter=6)
note = ParagraphStyle("n", parent=body, fontName="Arial-Italic", textColor=CINZA)
bullet = ParagraphStyle("bl", parent=body, leftIndent=14, bulletIndent=4, spaceAfter=3)

# Each section is written to stand alone, because the Data Library splits the
# document into chunks and the agent may retrieve one chunk without the others.
SECTIONS = [
    ("Sobre este documento", [
        ("p", "Esta é a base de conhecimento do Nu Explica, assistente educativo do Nubank (protótipo de demonstração). O conteúdo explica conceitos básicos de investimentos para quem nunca investiu."),
        ("p", "Todo o conteúdo é educativo e não é recomendação de investimento. Este documento não traz taxas, rendimentos, preços ou regras atuais do Nubank ou do mercado. Para dados atualizados, a pessoa deve procurar os canais oficiais dentro do app do Nubank."),
        ("p", "Todos os números que aparecem aqui são exemplos fictícios, usados só para ilustrar um conceito."),
    ]),
    ("Etapa 1 de 7: Objetivo e prazo", [
        ("h", "Por onde começo a investir?"),
        ("p", "O primeiro passo é saber para que o dinheiro vai servir e quando ele vai ser necessário. O objetivo e o prazo ajudam a entender quais características de investimento fazem sentido para cada pessoa."),
        ("h", "Tipos de prazo"),
        ("b", "Curto prazo: dinheiro que pode ser necessário em até 1 ano. Exemplo: uma viagem no próximo verão."),
        ("b", "Médio prazo: dinheiro para daqui a 1 a 5 anos. Exemplo: a entrada de um carro."),
        ("b", "Longo prazo: dinheiro para daqui a mais de 5 anos. Exemplo: a aposentadoria."),
        ("p", "Quanto mais curto o prazo, mais importa conseguir resgatar o dinheiro na hora certa, sem surpresas."),
        ("n", "Exemplo fictício: Ana quer juntar 3.000 reais para uma viagem daqui a 10 meses. O objetivo dela é de curto prazo, então ela precisa de um investimento que permita resgatar o dinheiro antes da viagem."),
    ]),
    ("Etapa 2 de 7: Reserva de emergência", [
        ("h", "O que é reserva de emergência?"),
        ("p", "Reserva de emergência é um dinheiro guardado para imprevistos, como perder o emprego, uma conta médica ou o conserto do carro. Ela serve para a pessoa não precisar se endividar quando algo inesperado acontece."),
        ("h", "Por que a reserva vem antes dos outros investimentos?"),
        ("p", "Sem reserva, qualquer imprevisto pode obrigar a pessoa a resgatar um investimento na pior hora ou a usar crédito caro, como o rotativo do cartão. Por isso, montar a reserva costuma ser o primeiro passo antes de investir para outros objetivos."),
        ("h", "Quanto guardar na reserva?"),
        ("p", "Uma referência comum é juntar o equivalente a alguns meses de gastos essenciais (moradia, comida, transporte, contas). O número de meses varia: quem tem renda instável costuma precisar de uma reserva maior. A pessoa decide o valor de acordo com a própria realidade."),
        ("p", "O dinheiro da reserva precisa poder ser resgatado rápido, em qualquer dia, e não deve oscilar muito."),
        ("n", "Exemplo fictício: Bruno gasta 2.000 reais por mês com o essencial. Se ele decidir ter 6 meses de reserva, a meta dele é 12.000 reais."),
        ("h", "E se a pessoa tiver dívidas?"),
        ("p", "Quem tem dívidas com juros altos costuma ganhar mais organizando e quitando essas dívidas antes de investir, porque os juros da dívida geralmente são maiores que o retorno de um investimento. Nesse caso, vale buscar atendimento humano nos canais oficiais dentro do app do Nubank para organizar as contas."),
    ]),
    ("Etapa 3 de 7: Liquidez", [
        ("h", "O que é liquidez?"),
        ("p", "Liquidez é a rapidez com que um investimento pode virar dinheiro disponível na conta. É como a diferença entre tirar dinheiro de um cofrinho, que é na hora, e vender um carro, que pode levar semanas."),
        ("h", "Tipos de liquidez"),
        ("b", "Liquidez diária: o dinheiro pode ser resgatado em qualquer dia útil."),
        ("b", "Liquidez no vencimento: o dinheiro só fica disponível na data combinada no início. Exemplo: daqui a 2 anos."),
        ("b", "Carência: um período inicial em que não é possível resgatar."),
        ("p", "Antes de investir, é importante saber quando o dinheiro vai estar disponível e se resgatar antes do prazo muda o valor recebido."),
        ("h", "Liquidez e objetivo andam juntos"),
        ("p", "Para a reserva de emergência, liquidez diária costuma fazer mais sentido. Para um objetivo com data marcada, um investimento que vence perto dessa data pode fazer sentido. A escolha depende do objetivo e do prazo de cada pessoa."),
        ("n", "Exemplo fictício: Carla aplicou 1.000 reais em um investimento que só libera o dinheiro em 2028. Se ela precisar do valor antes disso, pode não conseguir resgatar."),
    ]),
    ("Etapa 4 de 7: Risco e retorno", [
        ("h", "Por que ganho alto costuma vir com risco alto?"),
        ("p", "Retorno é quanto o investimento pode render. Risco é a chance de o resultado ser diferente do esperado, incluindo perder dinheiro. Em geral, investimentos que podem render mais também podem oscilar mais ou ter mais chance de perda. Quem promete ganho alto e garantido ao mesmo tempo está prometendo algo que o mercado não costuma entregar."),
        ("h", "Tipos de risco"),
        ("b", "Risco de mercado: o valor do investimento sobe e desce com o tempo."),
        ("b", "Risco de crédito: quem recebeu o dinheiro (um banco ou uma empresa) pode não conseguir devolver."),
        ("b", "Risco de liquidez: não conseguir resgatar quando precisar."),
        ("h", "Rentabilidade passada garante o futuro?"),
        ("p", "Não. Um investimento que rendeu bem no passado pode render menos ou perder valor no futuro. Rentabilidade passada não garante resultado futuro."),
        ("h", "Diversificação"),
        ("p", "Diversificar é não colocar todo o dinheiro em um lugar só. Se um investimento for mal, os outros podem compensar parte da perda."),
        ("h", "Investimentos de risco maior: criptomoedas, ações, day trade, alavancagem e derivativos"),
        ("p", "Ações são pequenas partes de empresas, e o preço delas sobe e desce todos os dias. Criptomoedas são moedas digitais que podem ter variações muito fortes em pouco tempo. Day trade é comprar e vender no mesmo dia tentando lucrar com pequenas variações. Alavancagem é investir com dinheiro emprestado, o que pode multiplicar tanto o ganho quanto a perda. Derivativos são contratos cujo valor depende de outro ativo."),
        ("p", "Todos eles envolvem risco maior e exigem estudo. Este conteúdo explica só os conceitos e não opina sobre nenhum ativo específico."),
    ]),
    ("Etapa 5 de 7: Renda fixa básica", [
        ("h", "O que é renda fixa?"),
        ("p", "Renda fixa é um tipo de investimento em que a pessoa empresta dinheiro para um banco, uma empresa ou o governo e recebe juros por isso. As regras de rendimento são definidas no momento da aplicação. Renda fixa não quer dizer que não existe risco."),
        ("h", "O que é CDB?"),
        ("p", "CDB (Certificado de Depósito Bancário) é um título em que a pessoa empresta dinheiro para um banco. Em troca, o banco devolve o valor com juros depois de um prazo combinado. Cada CDB tem suas próprias regras de prazo, liquidez e rendimento."),
        ("h", "O que é CDI?"),
        ("p", "CDI é uma taxa de referência usada pelos bancos quando emprestam dinheiro entre si. Ela costuma andar perto da Selic, a taxa básica de juros do país. Muitos investimentos usam o CDI como régua: um investimento que rende 100% do CDI acompanha essa taxa."),
        ("n", "Exemplo fictício: se o CDI de um ano fosse 10%, um investimento de 100% do CDI renderia cerca de 10% no ano, antes dos impostos. Esses números não representam taxas reais."),
        ("h", "Prefixado e pós-fixado"),
        ("b", "Prefixado: a taxa é definida no início. A pessoa já sabe quanto vai receber se ficar até o vencimento, mas não se beneficia se os juros do país subirem."),
        ("b", "Pós-fixado: o rendimento acompanha um indicador, como o CDI. A pessoa só sabe o valor final no resgate."),
        ("b", "Atrelado à inflação: rende uma taxa fixa mais a inflação do período."),
        ("p", "Nenhum desses tipos é melhor para todo mundo. A escolha depende do objetivo, do prazo e de como a pessoa lida com a incerteza."),
    ]),
    ("Etapa 6 de 7: Custos e proteções", [
        ("h", "Imposto de renda regressivo"),
        ("p", "Em muitos investimentos de renda fixa, como o CDB, o imposto de renda é cobrado só sobre o rendimento, e não sobre o valor aplicado. A tabela é regressiva: quanto mais tempo o dinheiro fica investido, menor é o percentual de imposto. As faixas vigentes são definidas pela legislação e podem mudar, então devem ser conferidas em fontes oficiais."),
        ("p", "Alguns investimentos também podem ter cobrança de IOF quando o resgate acontece nos primeiros dias após a aplicação. Isso também deve ser conferido nas regras de cada produto."),
        ("n", "Exemplo fictício: Diego aplicou 1.000 reais e o investimento rendeu 100 reais. O imposto incide sobre os 100 reais de rendimento, não sobre os 1.000 reais aplicados."),
        ("h", "O que é o FGC?"),
        ("p", "O FGC (Fundo Garantidor de Créditos) é um fundo garantidor, com limite. Se uma instituição financeira associada quebrar, ele pode devolver o dinheiro de alguns investimentos até um limite de cobertura por pessoa e por instituição."),
        ("p", "Pontos importantes: existe um limite de cobertura por pessoa e por instituição; nem todo produto é coberto pelo FGC; as regras e os limites vigentes estão no site oficial do FGC."),
        ("h", "Outros custos"),
        ("p", "Alguns investimentos podem ter taxas, como taxa de administração ou de custódia. Antes de investir, vale ler as condições do produto para saber se existe algum custo."),
    ]),
    ("Etapa 7 de 7: Próximos passos de aprendizado", [
        ("h", "O que estudar depois do básico?"),
        ("p", "Depois de entender objetivo, reserva, liquidez, risco e renda fixa, a pessoa pode aprofundar os estudos em temas como:"),
        ("b", "Tesouro Direto: títulos públicos, em que o dinheiro é emprestado para o governo."),
        ("b", "LCI e LCA: títulos de renda fixa ligados aos setores imobiliário e do agronegócio, com regras de imposto próprias."),
        ("b", "Fundos de investimento: o dinheiro de várias pessoas é reunido e administrado por um gestor."),
        ("b", "Inflação e juro real: quanto o dinheiro realmente cresce depois de descontar a alta dos preços."),
        ("b", "Juros compostos: como o rendimento sobre o rendimento faz o dinheiro crescer com o tempo."),
        ("p", "Uma boa prática é estudar um tema por vez, ler as condições de cada produto antes de investir e sempre conferir as informações nas fontes oficiais."),
    ]),
    ("Golpes: sinais de alerta", [
        ("h", "Como reconhecer uma oferta suspeita?"),
        ("b", "Promessa de ganho alto e garantido, como uma porcentagem alta por mês."),
        ("b", "Pressa para decidir: \"só hoje\", \"últimas vagas\"."),
        ("b", "Contato por mensagem, rede social ou ligação que a pessoa não pediu."),
        ("b", "Pedido de transferência para conta de pessoa física ou de desconhecidos."),
        ("b", "Links recebidos por mensagem pedindo dados ou senha."),
        ("p", "Diante desses sinais, o recomendado é não transferir dinheiro, não clicar em links recebidos por mensagem e procurar os canais oficiais dentro do app do Nubank."),
        ("p", "Em caso de roubo do celular ou perda de acesso ao app, é urgente usar outro aparelho para procurar os canais oficiais do Nubank, digitando o endereço oficial ou baixando o app na loja oficial, e registrar boletim de ocorrência se houve roubo."),
    ]),
    ("Glossário", [
        ("g", "Ativo", "Qualquer coisa em que se pode investir, como um título, uma ação ou um imóvel."),
        ("g", "Aplicação", "O ato de colocar dinheiro em um investimento."),
        ("g", "Carência", "Período inicial em que não é possível resgatar o investimento."),
        ("g", "CDB", "Título em que a pessoa empresta dinheiro para um banco e recebe juros."),
        ("g", "CDI", "Taxa de referência usada pelos bancos e por muitos investimentos de renda fixa."),
        ("g", "Diversificação", "Distribuir o dinheiro entre diferentes investimentos."),
        ("g", "FGC", "Fundo garantidor, com limite por pessoa e por instituição, que cobre alguns produtos."),
        ("g", "Inflação", "Aumento geral dos preços ao longo do tempo."),
        ("g", "IOF", "Imposto que pode ser cobrado em resgates feitos nos primeiros dias após a aplicação."),
        ("g", "Liquidez", "Rapidez com que um investimento pode virar dinheiro disponível."),
        ("g", "Pós-fixado", "Investimento cujo rendimento acompanha um indicador, como o CDI."),
        ("g", "Prefixado", "Investimento com taxa definida no momento da aplicação."),
        ("g", "Rentabilidade", "Quanto um investimento rendeu em um período."),
        ("g", "Reserva de emergência", "Dinheiro guardado para imprevistos, com resgate rápido."),
        ("g", "Resgate", "Tirar o dinheiro de um investimento."),
        ("g", "Selic", "Taxa básica de juros do país, definida pelo Banco Central."),
        ("g", "Vencimento", "Data em que o investimento termina e o dinheiro é devolvido."),
    ]),
    ("Perguntas frequentes", [
        ("h", "Qual investimento eu devo escolher?"),
        ("p", "O Nu Explica não indica produtos. A decisão é da pessoa e pode ser feita olhando três critérios: o prazo do objetivo, a liquidez de que ela precisa e o quanto de oscilação ela aceita."),
        ("h", "Quanto está rendendo hoje?"),
        ("p", "O Nu Explica não tem acesso a dados em tempo real. Taxas e rendimentos atualizados estão nos canais oficiais dentro do app do Nubank."),
        ("h", "Com quanto dinheiro dá para começar?"),
        ("p", "Muitos investimentos de renda fixa aceitam valores pequenos. O valor mínimo depende de cada produto. O mais importante no começo é criar o hábito e entender o que está sendo feito."),
        ("h", "Posso perder dinheiro na renda fixa?"),
        ("p", "Pode. A renda fixa também tem riscos: a instituição pode não pagar (risco de crédito), o resgate antes do prazo pode render menos e alguns títulos variam de preço até o vencimento."),
        ("h", "O Nu Explica pode aplicar, resgatar ou ver meu saldo?"),
        ("p", "Não. O Nu Explica é educativo e não executa operações nem consulta contas. Nunca compartilhe CPF, senha, número de conta ou de cartão em uma conversa."),
    ]),
]


def render():
    story = [
        Paragraph("Nu Explica", title),
        Paragraph("Base de conhecimento sobre investimentos para iniciantes. Protótipo de demonstração. Conteúdo educativo, não é recomendação de investimento.", subtitle),
    ]
    for i, (heading, items) in enumerate(SECTIONS):
        block = [Paragraph(heading, h1)]
        for item in items:
            kind = item[0]
            if kind == "h":
                block.append(Paragraph(item[1], h2))
            elif kind == "p":
                block.append(Paragraph(item[1], body))
            elif kind == "n":
                block.append(Paragraph(item[1], note))
            elif kind == "b":
                block.append(Paragraph(item[1], bullet, bulletText="•"))
            elif kind == "g":
                block.append(Paragraph(f"<b>{item[1]}:</b> {item[2]}", bullet))
        story.append(KeepTogether(block[:3]))
        story.extend(block[3:])
        story.append(Spacer(1, 4))

    def footer(canvas, doc):
        canvas.saveState()
        canvas.setFont("Arial", 8)
        canvas.setFillColor(CINZA)
        canvas.drawString(2 * cm, 1.2 * cm, "Nu Explica: conteúdo educativo, não é recomendação de investimento. Exemplos numéricos são fictícios.")
        canvas.drawRightString(A4[0] - 2 * cm, 1.2 * cm, f"Página {doc.page}")
        canvas.restoreState()

    doc = SimpleDocTemplate(OUT, pagesize=A4, leftMargin=2 * cm, rightMargin=2 * cm, topMargin=2 * cm, bottomMargin=2 * cm,
                            title="Nu Explica - Base de Conhecimento", author="Nu Explica (protótipo)", subject="Educação financeira básica sobre investimentos")
    doc.build(story, onFirstPage=footer, onLaterPages=footer)


render()

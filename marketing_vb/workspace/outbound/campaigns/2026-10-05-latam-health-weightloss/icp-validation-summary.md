---
campaign: 2026-10-05-latam-health-weightloss
product: fitxpress
profile: katya
step: 4-validate
date: 2026-10-05
status: v2, QC fixes applied (QC 13/20, workspace/_quality/outbound/2026-10-05-icp-validator-latam-health-weightloss.md); checkpoint waived by Vadim 2026-10-05 («продовжуй без апруву»), this file is the record
version: 2 (v1 kept as people-validated-v1-2026-10-05.csv)
inputs: card-validate.md (hypothesis 93e9f647105e4857), people-compact.csv (176 rows, Sales Navigator)
---

# ICP Validation Summary — 2026-10-05-latam-health-weightloss

Профіль `katya` (Kateryna), South America, перша кампанія профілю на цьому ринку. Продукт: fitxpress. Прогін без чекпоинтів; Opus QC після кроку лишається. Реєстр: 176 clear, виключень 0.

**Правило для one-line профілів (`empty-profile`), застосоване до кожного такого рядка:** PASS лише тоді, коли рядок несе функційний титул, специфічний для акаунта чи його бізнесу, headline, прізвищевий зв'язок із підтвердженою людиною або дефолт картки, що називає саме цю людину з роллю; загальний власницький чи ранговий титул (Proprietário, Empresária, Sócio, Executivo, Chefe, Diretor, Gerente geral), сама лише сторінка компанії або перегрупований рядок без сторінки дають WEAK, а тір картки лишається в `decisions.md`.

## Що змінилося у v2 (QC 13/20)

- Правило вище замінило v1, де результат залежав від того, чи картка назвала людину для перевірки. 12 PASS стали WEAK: 10 зі списку QC (Milena Espinha, lisete espindola, Mônica Melli, Sandra Baldassari, Cristiane Aguilar, Elaine Tadiello, Meire Satelite, Alejandro Gorissen, Silvia Lima, Carlos Coelho), Fabrícia Dias (перевірена за правилом: перегрупований рядок N2B без сторінки, лише «head de expansão») і Regiane Viana de Oliveira. QC залишав Regiane в PASS, але «Gerente geral» — ранговий титул: Geovana Dorys і Elaine Tadiello з тим самим титулом WEAK, тому вона теж WEAK. Жоден WEAK не став PASS.
- Причини в `decisions.md` тепер кажуть лише те, що показує рядок або картка. Прибрано «власниця юніта Lipocenter», «генеральна менеджерка юніта Siluets», «проводить безкоштовну оцінку», «Аракажу» та подібні висновки.
- Adrielle Dalul позначена як можлива людина рівня франчайзора (lane картки без змін).
- Додано frontmatter.

## Stats

**176 рядків** = 158 людей із send-списку картки (163 мінус 5 людей чотирьох клінік, утриманих до валідації: Jacques Maciel, Indira Cruz, Ulysses Maciel з Clínica da Obesidade, Valentina Sanabria з Perfect clinic, Javier Rhea з Ihealthy) + 11 company-named рядків (дванадцятий, Clínica Lev Vida, утримано разом із клініками) + 3 дублікати + 4 колізії імен, що збіглися з ключем IN-групи.

| | Людей |
|---|---|
| **PASS (SEND)** | **128** |
| · P1 | 15 |
| · P2 | 17 |
| · P3 | 32 |
| · P4 | 64 |
| **WEAK (REVIEW)** | **41** (company-named 11, правило one-line 12, перевірки ідентичності з картки 14, радники 3, гілка картки 1) |
| **FAIL** | **7** (4 колізії імен, 3 дублікати) |
| Виключено реєстром | 0 |

**Angle (PASS):** referral 64 · product 20 · technical-integration 16 · partnership 15 · operations 10 · clinical 3.

**Tier × lane (PASS):** P1: product 12, operations 2, clinical 1 · P2: product 8, operations 7, clinical 2 · P3: technical-integration 16, partnership 15, operations 1 · P4: referral 64.

**Кеп `cap_per_group: 50`:** найбільша група Vidalink, 16. Ніхто не впирається. Відправляють 38 груп із 39; у Grupo Endos є лише company-named рядок.

| Група | PASS | P1 | P2 | P3 | P4 | WEAK | FAIL | Кеп |
|---|---|---|---|---|---|---|---|---|
| Vidalink | 16 | 4 | 1 | 4 | 7 | 2 |  | 50 |
| Nilo Saúde | 10 | 2 | 1 | 5 | 2 | 3 | 1 | 50 |
| Magrass | 8 |  |  |  | 8 | 6 | 1 | 50 |
| Liti | 7 | 1 |  | 3 | 3 | 1 | 1 | 50 |
| OrienteMe | 7 | 3 |  | 1 | 3 |  |  | 50 |
| RWE Telemedicina | 5 |  |  | 4 | 1 | 1 | 1 | 50 |
| Telecárdio | 5 |  |  | 3 | 2 |  |  | 50 |
| GESmed | 4 | 1 | 3 |  |  |  |  | 50 |
| L2D Saúde Digital | 4 |  | 2 | 1 | 1 |  |  | 50 |
| Llamando al Doctor | 4 |  | 2 | 1 | 1 |  |  | 50 |
| Saluta | 4 |  |  | 2 | 2 |  |  | 50 |
| Siluets | 4 |  |  |  | 4 | 8 |  | 50 |
| Atrys Brasil | 3 | 1 |  |  | 2 | 3 |  | 50 |
| Grupo Wellness Latina | 3 |  |  | 1 | 2 |  |  | 50 |
| Pró-Corpo | 3 |  | 2 |  | 1 | 7 | 1 | 50 |
| Reliv | 3 |  | 2 | 1 |  |  |  | 50 |
| Salvia Saúde Corporativa | 3 | 1 |  |  | 2 |  |  | 50 |
| Sensorial | 3 |  |  | 1 | 2 |  |  | 50 |
| TELUS Health Brazil | 3 |  |  | 1 | 2 | 1 |  | 50 |
| Wellbe | 3 | 1 |  | 1 | 1 |  |  | 50 |
| Amparo Saúde | 2 |  |  |  | 2 | 1 |  | 50 |
| Céntriqo | 2 |  | 1 |  | 1 |  |  | 50 |
| Emagrecentro | 2 |  |  |  | 2 |  |  | 50 |
| GnTech | 2 |  |  | 1 | 1 |  |  | 50 |
| Grupo 5S | 2 |  | 1 |  | 1 |  | 1 | 50 |
| MedTrue | 2 | 1 |  |  | 1 |  |  | 50 |
| Zínea | 2 |  |  | 1 | 1 |  |  | 50 |
| holadr. IPS | 2 |  | 1 |  | 1 |  |  | 50 |
| Abertta Saúde | 1 |  |  |  | 1 |  |  | 50 |
| Face Doctor | 1 |  |  |  | 1 |  |  | 50 |
| Inc Beauty | 1 |  |  |  | 1 |  |  | 50 |
| Instituto GL | 1 |  |  |  | 1 |  |  | 50 |
| Instituto Lumiere | 1 |  | 1 |  |  |  |  | 50 |
| Lipocenter | 1 |  |  |  | 1 | 6 |  | 50 |
| N2B Brasil | 1 |  |  | 1 |  | 1 |  | 50 |
| SPDM | 1 |  |  |  | 1 |  |  | 50 |
| Terapia Online | 1 |  |  |  | 1 |  | 1 | 50 |
| iMND | 1 |  |  |  | 1 |  |  | 50 |
| Grupo Endos | 0 |  |  |  |  | 1 |  | 50 |

**Звірка з карткою.** P1 15 з 15. P2 17 = 20 мінус Jacques Maciel і Javier Rhea (утримані з клініками) мінус Patricia Coutinho (WEAK). P3 32 = 33 мінус Fabrícia Dias (WEAK за правилом). P4 64 = 95 мінус 3 утримані з клініками (Indira Cruz, Ulysses Maciel, Valentina Sanabria) мінус 28 WEAK.

**One-line профілі, що лишилися в PASS (9), і їхня підстава:**
- Daniele Araujo (Abertta Saúde): титул health plan «Gerente de Regulação e Relacionamento».
- Wesley Denardin (Emagrecentro): дефолт гілки картки.
- Viviane Lins (Emagrecentro): дефолт гілки картки.
- Abilio Costa (Instituto Lumiere): картка називає його власником.
- Janiel José Zioti (L2D Saúde Digital): титул і картка: group executive director.
- aline caio (Lipocenter): дефолт гілки картки.
- Simone Fatima Amaral martins (Pró-Corpo): headline називає Pró-Corpo.
- Adrielle Dalul (Siluets): прізвищевий зв'язок із Flaminio Dalul (Rio Preto).
- Susana Augusto de Camargo Silva (Vidalink): функційний титул «Lider de CS».

**Гілки картки, як розв'язані:**
- **Gabriela Biazus** — WEAK. «Sócia-fundadora at Magrass» без юніта і без сторінки; рядок не показує ні ролі у франчайзора, ні юніта. Картка: «if neither can be shown, hold».
- **Flaminio Dalul** — PASS referral P4: headline «Siluets rio preto», ролі у франчайзора на рядку немає.
- **aline caio** — PASS referral P4: «Diretor» на сторінці LIPOCENTER FRANQUIA, без юніта і без ролі у франчайзора.
- **Emagrecentro** (Viviane Lins, Wesley Denardin) — PASS referral P4: роль у франчайзора не показана. «Diretora Geral» у Viviane Lins може означати HQ.
- **Clínica da Obesidade і Perfect clinic** — утримані до валідації, у файлі їх немає.
- **Pró-Corpo** — Patricia Coutinho WEAK («CEO» суперечить її єдиній іншій ролі «Atendente at Pró-Corpo»; засновниця — Marisa Peraro); п'ять власницьких one-line рядків WEAK. PASS: Marisa Peraro, Simone Fatima Amaral Martins (headline), Andreza Zatorre Pereira.
- **Радники** — Graziela Heusser Azeredo PASS (місце в раді Zínea — поточний титул рядка). Ana Claudia Pinto, Fabio Katayama, Rafael L. Ribeiro — WEAK: поточний рядок належить іншій компанії, роль у Liti чи Nilo є лише серед інших ролей.
- **Перевірки ідентичності** — garga Mel, Renan Schonton (Vidalink), Geovana Dorys (Nilo), Fabricio Pires і one-line профілі Magrass (Regina Alves Ribeiro, Roberta Mascarenhas, Tami Bianca, Renata Assuncao) — WEAK: на рядку лише загальний титул.
- **Martin Samaniego** — PASS P2 у Céntriqo; Reliv для нього минула роль. Копі тільки від Céntriqo, ніколи від Reliv.
- **Дублікати** — FAIL на `sandra-panza`, `paulo-almança-5215083b2`, `luana-barreto-139b8638b`; залишені рядки мають PASS.

## Proposed to SEND (128)

| Група | Людина | Title | P | Angle |
|---|---|---|---|---|
| Vidalink | Edson Ferreira Augusto Corrêa | Senior Product Manager · AI & Intelligent Systems | 1 | product |
| Vidalink | Eliane Simeão | Diretora de Operações | 1 | operations |
| Vidalink | Jorge Sousa | COO | 1 | operations |
| Vidalink | Luis Gonzalez | CEO and co-founder | 1 | product |
| Vidalink | Karen Ribeiro | Gerente operacional | 2 | operations |
| Vidalink | Bruno Menendes | Senior Data Engineer | 3 | technical-integration |
| Vidalink | Daniela Junqueira | Tech Lead de Engenharia de Dados e Analytics | 3 | technical-integration |
| Vidalink | Lucas Mateus Silva de Souza | Senior Data Analyst | 3 | technical-integration |
| Vidalink | Tiago Soares | Tech Lead | 3 | technical-integration |
| Vidalink | Abi Nogueira | Gerente de Revenue Operations (RevOps) | 4 | referral |
| Vidalink | Alessandro Dourado da Silva | Senior Manager Sales Business Development | 4 | referral |
| Vidalink | Aline Dos Santos | Líder de Negociações de contratos | 4 | referral |
| Vidalink | Daniel Oliveira | Consultor Comercial Sênior | 4 | referral |
| Vidalink | Nadia Panow | Gerente Administrativo Financeiro -  controladoria Contábil e Fiscal | 4 | referral |
| Vidalink | Paulo Gonçalves | Head de Controladoria e Finanças | 4 | referral |
| Vidalink | Susana Augusto de Camargo Silva | Lider de CS | 4 | referral |
| Nilo Saúde | Rafael Alves Martins | Head of Product | 1 | product |
| Nilo Saúde | Victor Marcondes | Founder | 1 | product |
| Nilo Saúde | Carolina Beltramini | Head de Experiência do Cliente | 2 | operations |
| Nilo Saúde | Cesar Nobre | Chief Technology Officer | 3 | technical-integration |
| Nilo Saúde | Diego Freire | Senior Software Engineer | 3 | technical-integration |
| Nilo Saúde | Filipe Firmino | Coordenador de experiencia do cliente | 3 | operations |
| Nilo Saúde | Iasmini Gomes | Senior Software Engineer (L5) – Backend Python | 3 | technical-integration |
| Nilo Saúde | Rodolfo Stangherlin | Staff Software Engineer | 3 | technical-integration |
| Nilo Saúde | Steffany C. | Business Development Representative Enterprise Sênior | 4 | referral |
| Nilo Saúde | Vitor Honda | Head de Business Analytics | 4 | referral |
| Magrass | Janaina Possebon | Sócia administradora | 4 | referral |
| Magrass | Luiz dos Santos Nunes Filho | Sócio proprietário | 4 | referral |
| Magrass | Marcio Jorge Pinho Deriggi | Sócio proprietário | 4 | referral |
| Magrass | MARINA MICHAELSEN DERIGGI | Sócia proprietária da Magrass Montenegro | 4 | referral |
| Magrass | Rafaela Klein | Nutricionista clínico | 4 | referral |
| Magrass | Rhúã Robson D´Cézares Rodrigues de Oliveira das Chagas Netto | Gerente geral | 4 | referral |
| Magrass | Rodrigo Baroni | Proprietário | 4 | referral |
| Magrass | Sandra Geres Alves Panza | Diretora | 4 | referral |
| Liti | Fernando Vilela | Co-Founder | 1 | product |
| Liti | Bruno Silva | CTO | 3 | technical-integration |
| Liti | Maycon Soligo | Full Stack Engineer | 3 | technical-integration |
| Liti | William Weckl | Staff Software Engineer | 3 | technical-integration |
| Liti | Ana Paula Moraes | Nutricionista | 4 | referral |
| Liti | Gabriela Teixeira | Nutricionista clínico | 4 | referral |
| Liti | Rodrigo Casale Abe | CFO | 4 | referral |
| OrienteMe | Bruno Haidar | CoFounder & CEO | 1 | product |
| OrienteMe | Fernanda Maluf | Co-Founder | 1 | product |
| OrienteMe | Fernanda Mondin | Head of Nutrition | 1 | clinical |
| OrienteMe | Alessi Soncini | CTO at orienteme | 3 | technical-integration |
| OrienteMe | Jessica, Rayane | Senior Account Analyst | 4 | referral |
| OrienteMe | Maurício Lima | Head Comercial | 4 | referral |
| OrienteMe | Renata Tavolaro | Head de Psicologia | 4 | referral |
| RWE Telemedicina | Eduarda Cuerci | Diretora operacional | 3 | partnership |
| RWE Telemedicina | Emerson Goulart | Diretor | 3 | partnership |
| RWE Telemedicina | Luana Barreto | Diretora | 3 | partnership |
| RWE Telemedicina | Vinicius Cuerci de Souza | Diretor operacional | 3 | partnership |
| RWE Telemedicina | Paulo Castilho | Gerente geral | 4 | referral |
| Telecárdio | ALEXANDRE Pimentel | Diretor | 3 | partnership |
| Telecárdio | Marcelo Lapa Espiga | Co-CEO | 3 | partnership |
| Telecárdio | Roberto Stryjer | Sócio Fundador | 3 | partnership |
| Telecárdio | Amanda Micaela Alves | Executiva Comercial Sênior / Executiva de Contas Sênior, | 4 | referral |
| Telecárdio | Flavio Svaiter | Diretor Financeiro | 4 | referral |
| GESmed | Fernando Marques | Sócio Fundador e CEO | 1 | product |
| GESmed | Lucas Lau | Líder de Processo e Tecnologia de Gestão | 2 | operations |
| GESmed | Marcela Ferreira Lima Guimarães | Líder de Gestão de Saúde | 2 | clinical |
| GESmed | Thiara Amanda Corrêa de Almeida | Líder de Tecnologia e Processo de Saúde | 2 | operations |
| L2D Saúde Digital | Janiel José Zioti | Diretor executivo do grupo | 2 | product |
| L2D Saúde Digital | LUCAS SCHNEIDER | Diretor - L2D Telemedicina | 2 | operations |
| L2D Saúde Digital | Fernando P. | Head de Tecnologia e Processos | 3 | technical-integration |
| L2D Saúde Digital | Juliana Faure | Medical Doctor (Telemedicina) | 4 | referral |
| Llamando al Doctor | Guillermo Gonzalez | Chief Executive Officer | 2 | product |
| Llamando al Doctor | Ricardo Gordillo | Chief Operating Officer | 2 | operations |
| Llamando al Doctor | Martín Lucas Golini | Chief Technology Officer | 3 | technical-integration |
| Llamando al Doctor | Viviana Salazar | CFO_Director de Administración, Finanzas y RRHH | 4 | referral |
| Saluta | Luis Hincapié | Director de operaciones | 3 | partnership |
| Saluta | María Alejandra Silva Castro | Directora | 3 | partnership |
| Saluta | Gabriela Galvis | Líder de Venta Digital | 4 | referral |
| Saluta | Ricardo Perales Aravena | Director Comercial | 4 | referral |
| Siluets | Adrielle Dalul | Diretor executivo de vendas | 4 | referral |
| Siluets | Flaminio Dalul | Sócio proprietário | 4 | referral |
| Siluets | Jackeline Lopes | Gerente Geral | 4 | referral |
| Siluets | Lívia Sales | Diretora Presidente | 4 | referral |
| Atrys Brasil | Tiago Vieira | Diretor Executivo | 1 | product |
| Atrys Brasil | Luciana Ito | Gerente de relacionamento com o cliente | 4 | referral |
| Atrys Brasil | Matheus Rodrigues | Analista contabil e fiscal Sênior | 4 | referral |
| Grupo Wellness Latina | Andrea Lardani | Director and Co-founder | 3 | partnership |
| Grupo Wellness Latina | Jimena Maldonado de Chazal | Nutrition Counselor | 4 | referral |
| Grupo Wellness Latina | Ángeles Dubini | Senior Account Manager | 4 | referral |
| Pró-Corpo | Marisa Peraro | Founder | 2 | product |
| Pró-Corpo | Simone Fatima Amaral martins | gestora geral | 2 | operations |
| Pró-Corpo | Andreza Zatorre Pereira | Consultora de Estética PL | 4 | referral |
| Reliv | Paola Almeida | Cofundadora & COO | 2 | product |
| Reliv | Sebastián Guarderas-Castro | Chief Medical Officer | 2 | clinical |
| Reliv | Mauricio Padilla | Tech Lead | 3 | technical-integration |
| Salvia Saúde Corporativa | Mirian Maria Marques Pinheiro | CEO | 1 | product |
| Salvia Saúde Corporativa | Bárbara Carvalho | Diretora comercial | 4 | referral |
| Salvia Saúde Corporativa | Renise M. | Head Comercial | 4 | referral |
| Sensorial | Milton Ávila | CEO & Founder | 3 | partnership |
| Sensorial | Kevin Lucas | BACKEND SOFTWARE ENGINEER | 4 | referral |
| Sensorial | Victor Cavallari | Sócio-Fundador | 4 | referral |
| TELUS Health Brazil | ligia antunes pinto ferreira | Director of Operation TELUS Health Brazil | 3 | partnership |
| TELUS Health Brazil | Carlos Prestes | International Account Manager | 4 | referral |
| TELUS Health Brazil | Sonia Maria Figueiredo | Consultora e Palestrante | 4 | referral |
| Wellbe | Lucas Vieira Werner | Co-founder & CTO | 1 | product |
| Wellbe | William Bin Falinski | Tech Lead | 3 | technical-integration |
| Wellbe | Sidnei Salmaso ∴ | Consultor de negócios sênior | 4 | referral |
| Amparo Saúde | Marcus Nunes | Agente de recepção | 4 | referral |
| Amparo Saúde | Paty Marques | Gerente de vendas | 4 | referral |
| Céntriqo | Martin Samaniego | CEO Céntriqo | 2 | product |
| Céntriqo | Natalia Dezerega Molina | Chief of Staff | 4 | referral |
| Emagrecentro | Viviane Lins | Diretora Geral | 4 | referral |
| Emagrecentro | Wesley Denardin | Diretor | 4 | referral |
| GnTech | Paula Pedrassani Boabaid May | Vice Presidente e Diretora Comercial | 3 | partnership |
| GnTech | Adriano Oliveira | Technical Lead | 4 | referral |
| Grupo 5S | Dra Edivana Poltronieri | Diretora | 2 | product |
| Grupo 5S | Paulo Almança | Head de Finanças | 4 | referral |
| MedTrue | Lucas Quintella | CEO | 1 | product |
| MedTrue | Ramon Guedes | Head of Revenue | 4 | referral |
| Zínea | Anderson Baldissera | Co-Founder & CTO | 3 | partnership |
| Zínea | Graziela Heusser Azeredo | Membro do conselho consultivo | 4 | referral |
| holadr. IPS | Paola Cristina Giraldo Osorio | Chief Executive Officer | 2 | product |
| holadr. IPS | Ana Maria Restrepo Gomez | Líder de Comunicaciones | 4 | referral |
| Abertta Saúde | Daniele Araujo | Gerente de Regulação e Relacionamento | 4 | referral |
| Face Doctor | Monique Diana Martins | Sócia Proprietária na Face Doctor Perdizes | 4 | referral |
| Inc Beauty | Paula Tecchio | Head Comercial | 4 | referral |
| Instituto GL | Arthur Silva Da Ros | CFO | 4 | referral |
| Instituto Lumiere | Abilio Costa | Proprietário da empresa | 2 | product |
| Lipocenter | aline caio | Diretor | 4 | referral |
| N2B Brasil | João Murackami | Senior Analytics Engineer | 3 | partnership |
| SPDM | Adriana Bottoni | Diretora Técnica | 4 | referral |
| Terapia Online | Rodrigo Alvarez Diaz | Supervisor Area Pacientes | 4 | referral |
| iMND | Isabelle Ferraz | Chief Financial Officer | 4 | referral |

## WEAK — потрібне рішення Вадима (41)

`people-validated.csv` не записує пріоритет для WEAK. Тір і lane з картки стоять у `decisions.md`, і команди promote нижче передають їх явно.

| Людина | Title | Група | Тір / lane картки | Підстава | Чому на межі |
|---|---|---|---|---|---|
| Fabricio Pires | Empreendedor | Magrass | P4 referral | Перевірка ідентичності з картки | Card identity check: one-line profile, owner title "Empreendedor" only. |
| Regina Alves Ribeiro | Sócio | Magrass | P4 referral | Перевірка ідентичності з картки | Card identity check on one-line Magrass profiles: owner title "Sócio" only. |
| Renata Assuncao | Vice-diretora | Magrass | P4 referral | Перевірка ідентичності з картки | Card identity check on one-line Magrass profiles: re-grouped row with no company page, "Vice-diretora" only. |
| Roberta Mascarenhas | Sócia Gerente | Magrass | P4 referral | Перевірка ідентичності з картки | Card identity check on one-line Magrass profiles: owner title "Sócia Gerente" only. |
| Tami Bianca | Empresario | Magrass | P4 referral | Перевірка ідентичності з картки | Card identity check on one-line Magrass profiles: owner title "Empresario" only. |
| Geovana Dorys | Gerente geral | Nilo Saúde | P4 referral | Перевірка ідентичності з картки | Card identity check: one-line profile, rank title "Gerente geral" only, nothing else on the row. |
| Clovis Clodovil | Empreendedor | Pró-Corpo | P4 referral | Перевірка ідентичності з картки | Card identity check: one-line profile, owner title at a chain whose units the company owns. |
| Josemar Silva | Proprietário | Pró-Corpo | P4 referral | Перевірка ідентичності з картки | Card identity check: one-line profile, owner title at a chain whose units the company owns. |
| Michelly Carneiro de araujo | Pequeno empresário | Pró-Corpo | P4 referral | Перевірка ідентичності з картки | Card identity check: one-line profile, "Pequeno empresário" at a chain whose units the company owns. |
| Patricia Coutinho | CEO | Pró-Corpo | P2 product | Перевірка ідентичності з картки | Card identity check: "CEO" against her only other role, Atendente at Pró-Corpo; the founder is Marisa Peraro. |
| Rita Santos | Empreendedor | Pró-Corpo | P4 referral | Перевірка ідентичності з картки | Card identity check: one-line profile, owner title at a chain whose units the company owns. |
| Solange Bader | Empressaria | Pró-Corpo | P4 referral | Перевірка ідентичності з картки | Card identity check: one-line profile, owner title at a chain whose units the company owns. |
| garga Mel | Diretor | Vidalink | P4 referral | Перевірка ідентичності з картки | Card identity check: one-line profile, rank title "Diretor" only; "garga Mel" does not read as a full personal name. |
| Renan Schonton | Chefe | Vidalink | P4 referral | Перевірка ідентичності з картки | Card identity check: one-line profile, rank title "Chefe" only, nothing else on the row. |
| Gabriela Biazus | Sócia-fundadora | Magrass | P4 referral | Гілка картки | Branch unresolved: "Sócia-fundadora at Magrass" names no unit and has no page; the row shows neither a franchisor role nor a unit. |
| Alejandro Gorissen | CFO | Atrys Brasil | P4 referral | Правило one-line (v2) | One-line profile on a re-grouped AxisMed row with no company page (brand sold to Atrys in 2020): CFO title only. |
| Silvia Lima | Psychologist | Atrys Brasil | P4 referral | Правило one-line (v2) | One-line profile on a re-grouped AxisMed row with no company page (brand sold to Atrys in 2020): Psychologist title only. |
| Cristiane Aguilar | Proprietário | Lipocenter | P4 referral | Правило one-line (v2) | One-line profile, owner title "Proprietário" only on the Lipocenter row. |
| lisete espindola | proprietaria | Lipocenter | P4 referral | Правило one-line (v2) | One-line profile on a re-grouped Lipocenter row with no company page, "proprietaria" only. |
| Milena Espinha | proprietária | Lipocenter | P4 referral | Правило one-line (v2) | One-line profile on a re-grouped Lipocenter row with no company page, "proprietária" only. |
| Mônica Melli | Diretora Administrativa | Lipocenter | P4 referral | Правило one-line (v2) | One-line profile on a re-grouped Lipocenter row with no company page, "Diretora Administrativa" only. |
| Sandra Baldassari | Empresária | Lipocenter | P4 referral | Правило one-line (v2) | One-line profile, owner title "Empresária" only on the Lipocenter row. |
| Fabrícia Dias | head de expansão | N2B Brasil | P3 partnership | Правило one-line (v2) | One-line profile on a re-grouped N2B Brasil row with no company page, "head de expansão" only. |
| Carlos Coelho | Executivo | RWE Telemedicina | P4 referral | Правило one-line (v2) | One-line profile, rank title "Executivo" only on the RWE row. |
| Elaine Tadiello | Gerente Geral | Siluets | P4 referral | Правило one-line (v2) | One-line profile on a re-grouped Siluets row with no company page, "Gerente Geral" only. |
| Meire Satelite | Empresaria | Siluets | P4 referral | Правило one-line (v2) | One-line profile, owner title "Empresaria" only on the Siluets row. |
| Regiane Viana de Oliveira | Gerente geral | Siluets | P4 referral | Правило one-line (v2) | One-line profile, rank title "Gerente geral" only on the Siluets row. |
| Ana Claudia Pinto, MD, PhD, MBA | CEO da Find.AI | Liti | P4 referral | Радник | Advisor held: current row is CEO of Find.AI, the Liti board seat appears only among other roles. |
| Fabio Katayama | Partner | Nilo Saúde | P4 referral | Радник | Advisor held: current row is Partner at MGL Consultoria, the Nilo advisory seat appears only among other roles. |
| Rafael L. Ribeiro | Director · Digital Ventures (CDO) | Nilo Saúde | P4 referral | Радник | Advisor held: current row is CDO at Aché Laboratórios, the Nilo strategic-advisor role appears only among other roles. |
| Amparo Agência de cuidados | Gerente geral | Amparo Saúde | P4 referral | Company-named | company-named row, no person |
| AxisMed Telefónica | Proprietário da empresa | Atrys Brasil | P4 referral | Company-named | company-named row, no person |
| GRUPO ENDOS - Unidades ENDOSSP - ENDOSBH - ENDOSES | DIREÇÃO ADMINISTRATIVA - MÉDICAC | Grupo Endos | P2 product | Company-named | company-named row, no person |
| Lipocenter Emagrecimento E Estética | diretor | Lipocenter | P4 referral | Company-named | company-named row, no person |
| Clínica Ferraz Ferraz | Proprietário | Pró-Corpo | P4 referral | Company-named | company-named row, no person |
| Clínica Siluets Vila Nova | CEO | Siluets | P4 referral | Company-named | company-named row, no person |
| Dermish Clínica médica e estética | Proprietário | Siluets | P4 referral | Company-named | company-named row, no person |
| Siluets Casa Verde | Proprietário da empresa | Siluets | P4 referral | Company-named | company-named row, no person |
| Siluets Estética Unidade Brooklin | Sócio Proprietário | Siluets | P4 referral | Company-named | company-named row, no person |
| Siluets Estética Unidade Santo André | Sócio proprietário | Siluets | P4 referral | Company-named | company-named row, no person |
| Eap Brasil | Director EAP | TELUS Health Brazil | P4 referral | Company-named | company-named row, no person |

## Кого залишили за бортом: пули

`skipped`: 48 людей не йдуть у розсилку (41 WEAK і 7 FAIL), із них 9 старших. Пулу людей поза персоною немає: картка дала lane кожній функції в IN-компаніях, тож за бортом лишилися тільки утримані перевірками рядки і FAIL.

| Пул | Людей | Хто (3-5 імен) | Пропонований angle | Що змінити в гіпотезі, щоб їх узяти |
|---|---|---|---|---|
| One-line профілі за правилом v2 | 12 | Alejandro Gorissen (Atrys Brasil, CFO), Fabrícia Dias (N2B, head de expansão), Mônica Melli (Lipocenter, Diretora Administrativa), Carlos Coelho (RWE), Meire Satelite (Siluets) | referral P4; Fabrícia: partnership P3 | Вважати сторінку компанії або назву компанії в клітинці достатнім підтвердженням для one-line профілю |
| Радники без підтвердженої поточної ролі | 3 | Ana Claudia Pinto (Liti; на рядку CEO Find.AI), Fabio Katayama (Nilo; на рядку Partner MGL Consultoria), Rafael L. Ribeiro (Nilo; на рядку CDO Aché Laboratórios) | referral P4 | Брати радника без підтвердження, що роль поточна (зараз у картці: «held, not failed») |
| Перевірки ідентичності з картки | 14 | Patricia Coutinho (Pró-Corpo, «CEO»), garga Mel і Renan Schonton (Vidalink), Geovana Dorys (Nilo), Fabricio Pires (Magrass) і ще 9 | Patricia: product P2; решта: referral P4 | Те саме, що для пулу one-line: сторінка компанії як достатнє підтвердження |
| Company-named профілі | 11 | Eap Brasil (TELUS Health Brazil, «Director EAP»), Clínica Siluets Vila Nova («CEO»), GRUPO ENDOS, AxisMed Telefónica, Amparo Agência de cuidados | referral P4 (Grupo Endos: product P2) | Назвати людину за профілем; без імені привітання неможливе, тому promote не пропоную |

Додати за іменами (без нового раунду; спершу `--dry-run`; `--force` потрібен для рядків із прапорцем `empty-profile` або `other-company-page`):

```bash
# one-line профілі за правилом v2 (без Fabrícia Dias)
python3 scripts/outbound_pack.py promote --campaign 2026-10-05-latam-health-weightloss \
    --names "milena-espinha-60225065; lisete-espindola-b2385427; mônica-melli-68b8aa67; sandra-baldassari-08636a298; cristiane-aguilar-77b620275; elaine-tadiello-621405154; meire-satelite-a08125111; regiane-viana-de-oliveira-2bb003155; alejandro-gorissen-20821b; silvia-lima-45a228a; carlos-coelho-83859a360" \
    --angle referral --priority 4 --pool one-line --force
python3 scripts/outbound_pack.py promote --campaign 2026-10-05-latam-health-weightloss \
    --names "fabrícia-dias-81b46736b" --angle partnership --priority 3 --pool one-line --force
# радники
python3 scripts/outbound_pack.py promote --campaign 2026-10-05-latam-health-weightloss \
    --names "ana-claudia-pinto-md-phd-mba; fabiokatayama; rafael-l-ribeiro-31aa3549" \
    --angle referral --priority 4 --pool advisors --force
# перевірки ідентичності з картки
python3 scripts/outbound_pack.py promote --campaign 2026-10-05-latam-health-weightloss \
    --names "patricia-coutinho-4a14b0189" --angle product --priority 2 --pool identity
python3 scripts/outbound_pack.py promote --campaign 2026-10-05-latam-health-weightloss \
    --names "garga-mel-46943135b; renan-schonton-b66b36363; geovana-dorys-316053338; fabricio-pires-83347736b; regina-alves-ribeiro-30210317b; roberta-mascarenhas-a6167a212; tami-bianca-7b4023354; renata-assuncao-160796176; solange-bader-955613107; clovis-clodovil-2840bb251; josemar-silva-56008b254; michelly-carneiro-de-araujo-3a94731b7; rita-santos-04aa54396" \
    --angle referral --priority 4 --pool identity --force
# Gabriela Biazus: referral P4, якщо це юніт; product P1, якщо Вадим знає, що вона в HQ
python3 scripts/outbound_pack.py promote --campaign 2026-10-05-latam-health-weightloss \
    --names "gabriela-biazus-808294166" --angle referral --priority 4 --pool franchise
```

## FAIL (7)

| Людина | Група | Причина |
|---|---|---|
| Marta Larti | Liti | name collision, liti Argentina |
| Sandra Panza | Magrass | duplicate of sandra-geres-alves-panza |
| Claudia Posada | Nilo Saúde | name collision, Nilo Colombia |
| Cristina Nanin | Terapia Online | name collision, Terapia Online Brazil |
| Silbia Díaz | Pró-Corpo | name collision, Uruguay |
| Luana Barreto | RWE Telemedicina | duplicate of luana-barreto-43819922b |
| PAULO ALMANÇA | Grupo 5S | duplicate of paulo-almança-4bb7026a |

## Top concerns

- **У франчайзингових мережах немає покупця.** 16 PASS (Magrass 8, Siluets 4, Emagrecentro 2, Lipocenter 1, Face Doctor 1), усі referral до HQ; підтвердженого керівника франчайзора у виписці немає. Прогалину закриває відкрите питання 3 (top-up pull).
- **Можливі люди рівня франчайзора серед referral.** Adrielle Dalul («Diretor executivo de vendas», Siluets) може бути продажами франчайзора, а не юніта; Viviane Lins («Diretora Geral», Emagrecentro) може бути HQ. У Lívia Sales титул «Diretora Presidente», але headline «Micropigmentadora» і перегрупований рядок без сторінки вказують радше на юніт. Lane картки не змінено; referral-копі має нормально читатися і для людини з HQ, а перед відправкою їх варто перевірити.
- **Lipocenter майже випав.** Усі 6 рядків з людьми були one-line профілями; за правилом лишилася тільки aline caio (дефолт гілки картки). Статус франчайзора не підтверджено: сайт не резолвиться, преси немає. Siluets так само: сайт не резолвиться, остання преса 2017-2018. Сторінка Emagrecentro має HQ у Curitiba і 20 людей, хоча мережу заснували в São Bernardo do Campo.
- **Виписка за компанією, а не за title.** Через це в Pró-Corpo 8 з 11 рядків не йдуть: власницькі титули в мережі власних юнітів, колізія з Уругваю, company-named рядок. Той самий механізм дав 11 company-named профілів.
- **Перевірки, яких з рядка не зробити.** Картка просить повторити displacement check перед імпортом і пройти job-change check по всіх. Валідатор читає лише картку й compact-список, тож обидві перевірки лишаються на крок перед імпортом.
- **Lucas Quintella (MedTrue, P1).** Headline і попередня роль: executive director у Go Laser; MedTrue заснована 2025 року і має 14 людей. Job-change check тут особливо потрібен.
- **Lane за карткою, хоч і сумнівний.** Victor Cavallari (Sensorial, co-founder і COO) іде як referral, хоча сам є власником партнерського рішення; Adriano Oliveira (GnTech, technical lead) теж referral. Lane картки не змінено.
- **Grupo 5S.** Ризик CFN: копі ніколи не згадує метод 5S і не схвалює його.
- **Martin Samaniego.** Тільки копі від Céntriqo, ніколи від Reliv; Natalia Dezerega Molina (ex-Reliv) так само.
- **Hook-таблиці в картці немає.** Секцію «Message angle» у `card-validate.md` не перенесли, тому тір і lane взято зі списків P1-P4; hook sequencer бере зі своєї картки.

## Відкриті питання гіпотези (Open questions for Vadim) і прийняті дефолти

1. **Мова: англійська (дефолт), бразильська португальська чи іспанська для іспаномовних акаунтів?** Копі португальською чи іспанською потребувало б перекладених банів, затверджених формулювань і гейта, що читає ці мови, а Каті довелося б відповідати на відповіді цими мовами. Дефолт: англійська.
2. **Compliance- і регуляторні формулювання для Латинської Америки.** За замовчуванням жодного рядка в жодній послідовності. Чи має legal підготувати відповіді щодо LGPD, інших національних законів про захист даних і міжнародної передачі (і сказати, чи потрібне щось для ANVISA чи інших регуляторів) до того, як підуть відповіді? Дефолт: у копі нічого; відповіді йдуть на legal@3dlook.me.
3. **Top-up pull для HQ франчайзорів** (блок `titles` через Sales Navigator або Apollo) у Magrass, Emagrecentro, Siluets, Lipocenter і Face Doctor, а також для відсутніх медичних і продуктових лідів у Liti, Vidalink, Salvia і MedTrue? Директора з експансії Magrass називала преса 2023 року. Дефолт: pull не робимо; люди з франшиз ідуть як referral.
4. **Use-case файл для естетичних клінік** (`use-cases/fx-plastic-surgery.md`, у `INDEX.md` позначений як відсутній). Ця кампанія замість нього переказує в картці `icp-detail.md` §9. Створити файл до наступної естетичної кампанії? Дефолт: лише переказ.
5. **LinkedIn-профіль Каті** досі позиціонований на Ізраїль? Провести аудит перед відправкою чи прийняти ризик, як із `nick` (2026-09-29)? Дефолт: прийняти як є.
6. **163 інвайти одним файлом:** лишити постійне правило одного файлу й дати Closely самій розподілити темп чи спершу відправити core-акаунти? Дефолт: один файл, як вирішено 2026-09-29. Після валідації в цьому файлі 128.

## Рішення Вадима 2026-10-05 (прогін без чекпоинтів): прийняті дефолти

1. **Мова:** холодне копі англійською.
2. **Compliance:** жодного compliance-рядка в жодній послідовності і жодної заяви про LGPD чи інший місцевий закон.
3. **Top-up pull:** для керівників HQ франчайзорів не робимо. Власники юнітів ідуть referral до HQ, як записано.
4. **Естетичні клініки:** використовують §9 з icp-detail у переказі цієї картки; окремого use-case файлу немає.
5. **Позиціонування LinkedIn-профілю Каті:** ризик прийнято, будь-яку зміну профілю вирішує Вадим.
6. **Один файл імпорту** на всіх IN-людей, без хвиль.
Гіпотезу переобрали за скоупом після її QC (15/20; 21 правку застосовано в тому самому проході). Цілком повторно її не QC-или: нові lanes покривають QC на кроках validate і messages.

## Vadim — please confirm

1. Список SEND (128 людей)?
2. WEAK: кого беремо? 30 утримано перевірками (команди promote вище) і 11 company-named (без імені не відправляються).
3. Пули: one-line за правилом v2 (12), радників (3) і перевірки ідентичності (14) беремо? Додаються через promote, без нового раунду.
4. Кеп: ніхто не впирається (максимум Vidalink, 16 з 50), питання знято.
5. Відкрите питання 3 (top-up pull для HQ франчайзорів) тепер важить більше: усі 16 франчайзингові PASS — referral, покупця в цьому сегменті у списку немає.

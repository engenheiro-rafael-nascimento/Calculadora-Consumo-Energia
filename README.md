**--- Calculadora de Consumo de Energia Elétrica ---**

Uma aplicação desktop desenvolvida em Python para cálculo, gerenciamento e exportação de relatórios de consumo elétrico de equipamentos.

![Python](https://img.shields.io/badge/Python-306998?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-blue?style=for-the-badge)

---

**Sobre o Projeto**

O objetivo principal desta aplicação é permitir que o usuário cadastre equipamentos elétricos, informe suas potências, tempo médio de uso diário e a tarifa de energia (kW/h), calculando automaticamente a estimativa de consumo mensal em reais (R$).

Além do cálculo individual, o sistema permite consolidar a lista de equipamentos cadastrados e exportá-la diretamente para um relatório em **Excel (`.xlsx`)**, além de permitir a leitura e exibição de relatórios existentes no terminal.

---

**Funcionalidades**

- **Interface Gráfica Amigável:** Desenvolvida com `Tkinter`.
- **Validação de Dados:** Tratamento de entradas inválidas ou campos vazios com alertas (`messagebox`).
- **Flexibilidade de Formatação:** Suporte automático para valores numéricos digitados com vírgula (ex: `1,5`) ou ponto (ex: `1.5`).
- **Cálculo de Consumo Mensal**
- **Exportação para Excel:** Geração automatizada de planilhas `.xlsx` utilizando a biblioteca `Pandas`.
- **Manipulação de Arquivos:** Integração com o seletor de arquivos do sistema (`filedialog`).

---

**Tecnologias Utilizadas**

- **[Python](https://www.python.org/):** Linguagem principal.
- **[Tkinter](https://docs.python.org/3/library/tkinter.html):** Construção da interface gráfica (GUI).
- **[Pandas](https://pandas.pydata.org/):** Manipulação, tratamento de dados e geração de planilhas Excel.
- **[OpenPyXL](https://openpyxl.readthedocs.io/):** Engine para suporte de escrita/leitura de arquivos `.xlsx` no Pandas.

---

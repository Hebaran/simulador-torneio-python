# ⚔️ Simulador de Torneio de Batalha em Python

![Status](https://img.shields.io/badge/status-conclu%C3%ADdo-brightgreen)
![Python](https://img.shields.io/badge/python-3.12%2B-blue)

Um simulador de torneio de batalha "mata-mata" totalmente funcional, construído em Python puro, com foco nos princípios da Programação Orientada a Objetos (POO).

---

### 🎬 Demonstração em Ação

(Aqui você vai colocar o GIF do seu programa rodando!)

---

### ✨ Funcionalidades

* **Geração Procedural de Personagens:** Seis combatentes são criados no início de cada torneio com nomes, vida e ataque distribuídos aleatoriamente.
* **Sistema de Torneio "Mata-Mata":** Os lutadores batalham em pares aleatórios a cada rodada, e apenas o vencedor avança.
* **Combate em Turnos:** As batalhas individuais são simuladas turno a turno, com cada personagem atacando alternadamente.
* **Design Orientado a Objetos:** O código é estruturado usando uma classe `Personagem` que encapsula todos os dados e comportamentos dos lutadores, como `atacar()`, `receber_dano()` e `status_vida()`.
* **Lógica de Recuperação:** O vencedor de cada batalha recupera sua vida totalmente para a próxima rodada, seguindo uma regra de torneio clássica.

---

### 🛠️ Tecnologias Utilizadas

* **Python 3:** Linguagem principal do projeto.
* **Bibliotecas Nativas:**
  * `random`: Para a aleatoriedade na criação de personagens e seleção de oponentes.
  * `time`: Para pausas dramáticas (`sleep`) durante a simulação da batalha.
  * `os`: Para limpar o console (`system("clear")`) e melhorar a legibilidade a cada turno.

---

### 🚀 Como Rodar o Projeto

Você precisa ter o Python 3 instalado na sua máquina.

1. **Clone este repositório:**

    ```bash
    git clone [https://github.com/hebaran/seu-repositorio.git](https://github.com/hebaran/seu-repositorio.git)
    ```

2. **Navegue até a pasta do projeto:**

    ```bash
    cd seu-repositorio
    ```

3. **Execute o script principal:**

    ```bash
    python main.py
    ```

    E o torneio começará no seu terminal!

---

### 📂 Estrutura de Arquivos

O projeto é modularizado em dois arquivos principais:

* `char_class.py`: Contém a classe `Personagem`, que é o "molde" para todos os lutadores.
* `main.py`: É o arquivo principal que importa a classe `Personagem`, cria os lutadores e executa a lógica do torneio.

---

### 👨‍💻 Autor

* **Heitor Rangel**
* **LinkedIn:** [https://www.linkedin.com/in/heitor-rangel/](https://www.linkedin.com/in/heitor-rangel/)
* **GitHub:** [https://github.com/hebaran/](https://github.com/hebaran/)

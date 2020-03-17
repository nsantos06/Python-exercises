#Cria extensão de quatro tipos de arquivos diferentes, .txt .py .html .css

k = int(input("1txt, 2 python, 3 html, 4 css :"))
if k == 1:
    def txt():
        nome = str(input("nome do file :"))
        file = open(nome + '.txt', 'w')
        print(file)
        file.close()
    txt()
elif k == 2:
    def py():
        nome2 = str(input("nome do file:"))
        python = open(nome2 + '.py', 'w')
        print(python)
        python.close()
    py()

elif k == 3:
    def html():
        nome3 = str(input("nome do file:"))
        html = open(nome3 + '.html', 'w')
        print(html)
        html.close()
    html()

elif k == 4:
    def css():
        nome4 = str(input("nome do file:"))
        css = open(nome4 + '.css', 'w')
        print(css)
        css.close()
    css()

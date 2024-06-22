#завдання 1
rd = input("Введіть рядок: ")
dr = rd[::-1]
if rd == dr:
   print("rd - паліндром")

#завдання 2

tx = input("введіть текст: ")
wd = input("введіть слова: ")
print(tx.rfind(wd,0,10000))
fn = str(wd.upper())
print(tx.replace(wd,fn))

#завдання 3

txt = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
n = txt.count(".",0,10000))
m = txt.count("!",0,10000))
g = txt.count("?",0,10000))
w = n + m + g
print(f"кількість речень - {w}")

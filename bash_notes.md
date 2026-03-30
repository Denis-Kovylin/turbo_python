# Bash notes

## Навигация
pwd — показать текущую директорию  
ls — список файлов  
ls -la — список с подробностями (включая скрытые)  
cd — перейти в домашнюю папку  
cd folder — перейти в папку  
cd .. — выйти на уровень выше  

---

## Работа с файлами
touch file.py — создать файл  
rm file.py — удалить файл  
mv file.py folder/ — переместить файл  
mv old.py new.py — переименовать файл  
cp file.py copy.py — копировать файл  

---

## Работа с папками
mkdir folder — создать папку  
rm -r folder — удалить папку с содержимым  

---

## Чтение файлов
cat file.txt — вывести содержимое файла  
less file.txt — открыть файл постранично (выход: q)  

---

## Запись в файл
echo "text" > file.txt — перезаписать файл  
echo "text" >> file.txt — добавить в конец  

---

## Многострочная запись (EOF)
cat > file.txt << EOF — начать запись  
(пишешь текст)  
EOF — завершить  

cat >> file.txt << EOF — добавить несколько строк  

cat > file.txt << 'EOF' — безопасный режим (без обработки символов)  

---

## Подсчет
wc -l file.txt — количество строк  
wc file.txt — строки, слова, байты  

---

## Поиск и полезные команды
which python — показать путь к программе  
where python — аналог в Windows  
history — история команд  
clear — очистить терминал  

---

## Запуск Python
python file.py — запуск скрипта  
python3 file.py — альтернативный вариант  

Важно:  
файл сам по себе не запускается — нужно указать интерпретатор  

❌ file.py  
✔ python file.py  

---

## Virtual environment (venv)
python -m venv .venv — создать окружение  
source .venv/Scripts/activate — активировать (Git Bash)  
deactivate — выйти  
pip list — список пакетов  
pip install requests — установить пакет  

---

## Git
git status — состояние репозитория
git status -s — состояние репозитория (сокращенное) 
git branch — список веток  
git checkout <branch> — переключиться на существующую ветку
git checkout -b name — создать и перейти в ветку  
git add file — добавить файл  
git add . — добавить всё ( в текущем каталоге)
git add -A — добавить ВСЕ изменения во всём проекте (работает независимо от текущей директории)
git commit -m "msg" — создать коммит  
git restore --staged file — убрать файл из индекса (отменить git add)
## Работа с удалённым репозиторием
git remote add origin <url> — добавить удалённый репозиторий (связать локальный проект с GitHub)
git remote -v — посмотреть список подключённых удалённых репозиториев (origin = основной)
git remote set-url origin <url> — изменить ссылку на удалённый репозиторий (например, SSH → HTTPS)
git push -u origin <branch> — отправить ветку в удалённый репозиторий И связать её с origin
(после этого можно просто писать git push / git pull)


---

## Частые ошибки
command not found — команда не найдена  
python: command not found — bash не видит python  
wc: invalid option -- '1' — использована цифра 1 вместо буквы l  

---

## Минимум для запоминания
pwd  
ls  
cd  
touch  
rm  
mv  
cat  
echo  
python  
git status  
git add  
git commit  

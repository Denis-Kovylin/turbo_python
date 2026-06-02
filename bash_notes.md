# Bash notes

## Навигация
pwd — показать текущую директорию  
ls — список файлов  
ls -la — список с подробностями (включая скрытые)  
cd — перейти в домашнюю папку  
cd folder — перейти в папку  
cd .. — выйти на уровень выше  
cd ../.. — выйти на два уровня выше  
cd - — вернуться в предыдущую директорию  

---

## Работа с файлами
touch file.py — создать файл  
touch file1.py file2.py — создать несколько файлов сразу  
rm file.py — удалить файл  
mv file.py folder/ — переместить файл  
mv old.py new.py — переименовать файл  
cp file.py copy.py — копировать файл  
cp file.py folder/ — копировать файл в папку  

---

## Работа с папками
mkdir folder — создать папку  
mkdir -p folder/subfolder — создать папку с подпапкой сразу  
rm -r folder — удалить папку с содержимым  

---

## Чтение файлов
cat file.txt — вывести содержимое файла  
less file.txt — открыть файл постранично (выход: q)  
head file.txt — первые 10 строк файла  
tail file.txt — последние 10 строк файла  

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

cat > file.txt << EOF — безопасный режим (без обработки символов)  

---

## Подсчет
wc -l file.txt — количество строк  
wc file.txt — строки, слова, байты  

---

## Поиск
which python — показать путь к программе  
where python — аналог в Windows  
find . -name "*.py" — найти все .py файлы в текущей папке и подпапках  
grep "text" file.txt — найти строку с текстом в файле  
grep -r "text" folder/ — поиск текста рекурсивно по всей папке  

---

## Полезные команды
history — история команд  
clear — очистить терминал  
echo "text" — вывести текст в терминал  
open . — открыть текущую папку в проводнике (Git Bash)  
explorer . — открыть текущую папку в проводнике (Windows)  

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
pip freeze > requirements.txt — сохранить список пакетов в файл  
pip install -r requirements.txt — установить пакеты из файла  

---

## Git — основное
git status — состояние репозитория  
git status -s — состояние репозитория (сокращённое)  
git log — история коммитов  
git log --oneline — история коммитов (коротко)  
git diff — посмотреть незакоммиченные изменения  

## Git — ветки
git branch — список веток  
git branch -a — список всех веток включая удалённые  
git checkout <branch> — переключиться на существующую ветку  
git checkout -b name — создать и перейти в ветку  
git merge <branch> — влить ветку в текущую  
git branch -d <branch> — удалить ветку (после merge)  

## Git — индекс и коммиты
git add file — добавить файл  
git add . — добавить всё в текущем каталоге  
git add -A — добавить ВСЕ изменения во всём проекте  
git commit -m "msg" — создать коммит  
git restore --staged file — убрать файл из индекса (отменить git add)  
git restore file — отменить изменения в файле (вернуть как было в последнем коммите)  

## Git — удалённый репозиторий
git remote add origin <url> — связать локальный проект с GitHub  
git remote -v — список подключённых удалённых репозиториев  
git remote set-url origin <url> — изменить ссылку на удалённый репозиторий  
git push -u origin <branch> — отправить ветку и связать с origin  
git push — отправить изменения (после связки)  
git pull — получить изменения с GitHub  
git clone <url> — клонировать репозиторий  

## SSH для GitHub
ssh-keygen -t ed25519 -C "email" — сгенерировать ключ
cat ~/.ssh/id_ed25519.pub — показать публичный ключ (копируешь на GitHub)
git remote set-url origin git@github.com:USERNAME/REPO.git — переключить на SSH

---

## Частые ошибки
command not found — команда не найдена  
python: command not found — bash не видит python  
wc: invalid option -- 1 — использована цифра 1 вместо буквы l  

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
git push  
git pull

# Условие задачи

В файле https://stepik.org/media/attachments/lesson/258944/New-York.html  есть несколько таблиц, у которых атрибут `class` равен `wikitable collapsible collapsed`.

Вам необходимо найти вторую (при нумерации с единицы) такую таблицу и просто напечатать тег из `BeautifiulSoup` для этой таблицы (должен выводить html-код, начинающийся с тега `<table>` и заканчивающийся `</table>`). Этот текст необходимо сдать в качестве ответа.

Для решения этой задачи полезно использовать аргумент attrs в методе `find_all` или другом аналогичном методе. В качестве параметра `attrs` принимает словарь, где ключом является название атрибута, а значением - значение атрибута.
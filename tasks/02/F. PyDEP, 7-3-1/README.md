# Условие задачи

Мы сохранили статью с википедии, она доступна по ссылке https://stepik.org/media/attachments/lesson/258939/webpage.html

Вам необходимо обработать ее с помощью `BeautifulSoup` и вывести все ссылки, которые есть на этой странице, в том порядке как они встречались по одной в строке.

Под ссылкой понимается содержимое аттрибута `href` тега `a`.

Вам могут быть полезны методы `find_all` для супа (он позволяет найти все теги на странице), метод `has_attr` для тега (проверяет есть ли такой атрибут у тега) и доступ к атрибуту тега по аналогии со словарем.


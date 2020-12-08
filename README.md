# admin
username: artem
password: 9898

# run jupyter notebook
python manage.py shell_plus --notebook"


# Ограничения
- Система не учитывает комплексные вакцины (от нескольких болезней за раз)
- Не учитывает возраст и пол людей
- Не учитывает возможные противопоказания в зависимости от болезней человека
- Не учитывает многошаговые вакцины (ставящиеся в несколько приемов)
- Не учитывает совместимость вакцин между собой
- Responsive design нет почти нигде (изначально был на collection_list.html, но потом я и там сломал пока делал анимацию нажатия на карточку)

# Дальнейшие улучшения (помимо указанных выше)
- Можно добавить отдельно группу домашних животных: собак и кошек
- Можно монетизировать приложение через добавление клиник и указания их цен - то есть можно добавить карту с точками на ней
- Можно добавить подробное описание к каждой болезни с картинками (где встречается, как влияет на человека, кто возбудитель)

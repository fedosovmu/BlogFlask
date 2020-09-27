INSERT INTO post (title, short_description, img_url, publication_date)
VALUES ('Google не узнает, что вы делали прошлым летом (ну почти)',
'Google (или его родительский  холдинг Alphabet) на данный  владеет самым популярным одноименным поисковым сервисом, самым популярным видеохостингом YouTube, самым популярным сервисом электронной почты с Gmail, самой популярной мобильной операционной системой Android и целым рядом популярных облачных приложений для работы с документами Google Docs. По крайней мере восемь продуктов корпорации имеют более миллиарда пользователей. Бородатая шутка из середины нулевых о том, что скоро мы все будем ездить на работу в Гугле на Гугле, чтобы заработать немного Гугла, сегодня оказалась близка к реальности как никогда.',
'http://placehold.it/750x300',
'2020-09-27T16:04:19.511530'
);

INSERT INTO post (title, short_description, img_url, publication_date)
VALUES ('Четыре способа получить аудио вк или «это не баг, а фича»',
'Всем привет! Сегодня я расскажу вам о моем опыте с ВК, найденных багах, об отношении к пользователям и, собственно, как получить аудиозаписи вк, пользуясь "не багами а фичами", как меня заверяли сотрудники данной корпорации. Итак, приступим!',
'http://placehold.it/750x300',
'2020-09-27T16:04:19.511530'
);

INSERT INTO post (title, short_description, img_url, publication_date)
VALUES ('Новые лампы Remez с солнечным спектром',
'В начале этого года российский бренд Remez выпустил первые в мире серийные светодиодные лампы с солнечным спектром, использующие светодиоды Sunlike. Теперь к ним добавились пять новых моделей в двух цветовых температурах.',
'http://placehold.it/750x300',
'2020-09-27T16:04:19.511530'
);

INSERT INTO comment (post_id, text)
WITH post_ids AS (
	SELECT
		(SELECT post_id FROM post WHERE title LIKE '%Google%' LIMIT 1) AS "first_post_id",
		(SELECT post_id FROM post WHERE title LIKE '%Четыре способа получить аудио вк%' LIMIT 1) AS "second_post_id",
		(SELECT post_id FROM post WHERE title LIKE '%Новые лампы Remez%' LIMIT 1) AS "third_post_id"
)
	SELECT
		(SELECT first_post_id FROM post_ids),
		'А если применить контроллер в маленьком корпусе, например tiny-AVR, то можно сделать устройство на плате не больше CR2032'
UNION ALL
	SELECT
		(SELECT first_post_id FROM post_ids),
		'Отличное хобби! Прямо завидую.'
UNION ALL
	SELECT
		(SELECT first_post_id FROM post_ids),
		'Учитывая, что Artemis 3 планирует посадку на местах посадки Apollo, у любителей конспирологии остается мало времени, чтобы успеть разведать это все самим.'
UNION ALL
	SELECT
		(SELECT second_post_id FROM post_ids),
		'Интересно. а гибкие e-ink, небольшого формата, где-нибудь продаются?'
UNION ALL
	SELECT
		(SELECT second_post_id FROM post_ids),
		'Какое среднее потребление при опросе раз в минуту (для обновления часов и экрана)? А то между 8 мА пикового потребления и 2мкА потребления в спящем режиме — пропасть.'
UNION ALL
	SELECT
		(SELECT second_post_id FROM post_ids),
		'На фотографиях последних версий у Вас присутствует атмосферное давление. Само по себе текущее значение давления малоинформативно, гораздо полезнее знать скорость его изменения. Это может быть сделано либо в виде миниграфика, либо в виде отображения приращения за какой-то фиксированный интервал времени, например час.'
UNION ALL
	SELECT
		(SELECT third_post_id FROM post_ids),
		'Делал как раз на основе этого модуля термометр с передачей цифр в БД через домашнюю точку доступа. Печатаный корпус, внутри эта платка, 4 магнита, мини-АКБ и датчик температуры/влажности — висит на холодильнике, цифры хорошо видно и в базе всегда актуальные данные. Заряжать нужно ~1 раз в год.'
UNION ALL
	SELECT
		(SELECT third_post_id FROM post_ids),
		'А какая живность в аквариуме?'
UNION ALL
	SELECT
		(SELECT third_post_id FROM post_ids),
		'А почему вдруг не подойдут RGB диоды?';








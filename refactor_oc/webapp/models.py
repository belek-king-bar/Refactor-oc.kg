from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from webauth.managers import UserManager
from django.utils.translation import ugettext_lazy as _


class OCUser(AbstractUser):
    login = models.CharField(max_length=32, unique=True, verbose_name=_('login'))
    password = models.CharField(max_length=255, verbose_name=_('password'))
    email = models.CharField(max_length=255, unique=True)
    ip = models.TextField()
    balans = models.DecimalField(max_digits=9, decimal_places=2, default=1.00)
    user_group = models.SmallIntegerField(default=0)
    view_activity = models.IntegerField(null=True)
    play_activity = models.IntegerField(null=True)
    register_date = models.DateTimeField(auto_now_add=True)
    mode = models.IntegerField(default=1, null=True)
    ipfw_rule = models.IntegerField(default=0, null=True)
    enabled = models.SmallIntegerField(default=1, null=True)
    preferences = models.TextField(default=None, null=True)
    status = models.CharField(max_length=2048, default=None, null=True)
    username = models.CharField(max_length=200, null=True, blank=True)

    USERNAME_FIELD = 'login'

    objects = UserManager()

    def __str__(self):
        return "Пользователь"

    class Meta:
        db_table = 'users'
        verbose_name = _('ocuser')
        verbose_name_plural = _('ocusers')


class Check(models.Model):
    user_id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=70)
    date = models.DateField()

    def __str__(self):
        return "Проверка"

    class Meta:
        db_table = 'check'
        verbose_name = _('check')
        verbose_name_plural = _('checks')


class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(OCUser, on_delete=models.PROTECT, related_name='comments')
    to_user = models.OneToOneField(OCUser, on_delete=models.PROTECT, related_name='comment', null=True, blank=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    ip = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return "Комментарий"

    class Meta:
        db_table = 'comments'
        verbose_name = _('comment')
        verbose_name_plural = _('comments')


class CommentsRating(models.Model):
    comment = models.OneToOneField(Comment, on_delete=models.CASCADE, related_name='comments_ratings', primary_key=True)
    vote = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'comments_rating'


class CommentsVote(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='comments_votes', primary_key=True)
    user = models.ForeignKey(OCUser, on_delete=models.PROTECT, related_name='comments_votes')
    votes = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'comments_votes'


class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return "Страна"

    class Meta:
        db_table = 'countries'
        verbose_name = _('country')
        verbose_name_plural = _('countries')


class File(models.Model):
    file_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    path = models.CharField(max_length=255)
    is_dir = models.IntegerField()
    size = models.FloatField()
    md5_hash = models.CharField(max_length=32)
    metainfo = models.TextField(blank=True, null=True)
    translation = models.CharField(max_length=255)
    quality = models.CharField(max_length=100)
    frames = models.TextField(blank=True, null=True)
    tth_hash = models.CharField(max_length=40)
    tries = models.IntegerField()
    active = models.IntegerField()
    seconds = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return "Файл"

    class Meta:
        db_table = 'files'
        verbose_name = _('file')
        verbose_name_plural = _('files')


class FilesLost(models.Model):
    file_id = models.IntegerField(primary_key=True)
    path = models.CharField(max_length=255)

    def __str__(self):
        return "Потерянные файлы"

    class Meta:
        db_table = 'files_lost'
        verbose_name = _('filelost')
        verbose_name_plural = _('fileslost')


class FilesTask(models.Model):
    file_task_id = models.AutoField(primary_key=True)
    from_field = models.CharField(db_column='from', max_length=255)
    to = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    tries = models.IntegerField()

    def __str__(self):
        return "FilesTask"

    class Meta:
        db_table = 'files_tasks'
        verbose_name = _('files_task')
        verbose_name_plural = _('files_tasks')


class Filesstat(models.Model):
    fileid = models.PositiveIntegerField()
    lastaccess = models.DateTimeField()

    def __str__(self):
        return "Filesstat"

    class Meta:
        db_table = 'files_stat'
        verbose_name = _('files_stat')
        verbose_name_plural = _('files_stats')


class Genre(models.Model):
    genre_id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return "Жанр"

    class Meta:
        db_table = 'genres'
        verbose_name = _('genre')
        verbose_name_plural = _('genres')


class Incoming(models.Model):
    incoming_id = models.AutoField(primary_key=True)
    path = models.CharField(unique=True, max_length=255)
    level = models.IntegerField()
    is_dir = models.IntegerField()
    size = models.FloatField(blank=True, null=True)
    expanded = models.IntegerField()
    name = models.CharField(max_length=255)
    files = models.TextField(blank=True, null=True)
    quality = models.TextField(blank=True, null=True)
    translation = models.TextField(blank=True, null=True)
    last_query = models.CharField(max_length=255, blank=True, null=True)
    search_results = models.TextField(blank=True, null=True)
    parsing_url = models.CharField(max_length=255, blank=True, null=True)
    parsed_info = models.TextField(blank=True, null=True)
    info = models.TextField(blank=True, null=True)
    active = models.IntegerField()
    hidden = models.IntegerField()
    sort = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return "Incoming"

    class Meta:
        db_table = 'incoming'
        verbose_name = _('incoming')
        verbose_name_plural = _('incomings')


class LanguagesProto(models.Model):
    lang = models.CharField(primary_key=True, max_length=2)
    combination = models.CharField(max_length=4)
    freq = models.FloatField()

    def __str__(self):
        return "LanguagesProto"

    class Meta:
        db_table = 'languages_proto'
        verbose_name = _('languages_proto')
        verbose_name_plural = _('languages_protos')


class Log(models.Model):
    log_id = models.AutoField(primary_key=True)
    pid = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=64)
    status = models.IntegerField()
    started_at = models.DateTimeField()
    ended_at = models.DateTimeField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    report = models.TextField(blank=True, null=True)

    def __str__(self):
        return "Log"

    class Meta:
        db_table = 'logs'
        verbose_name = _('log')
        verbose_name_plural = _('logs')


class Selection(models.Model):
    selection_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, blank=True, null=True)
    genres = models.ManyToManyField(Genre, related_name='selections')
    image = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return "Подборка"

    class Meta:
        db_table = 'selections'
        verbose_name = _('selection')
        verbose_name_plural = _('selections')


class Movie(models.Model):
    movie_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    international_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    wishuser = models.CharField(max_length=128, blank=True, null=True)
    year = models.CharField(max_length=18)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    translation = models.CharField(max_length=255)
    quality = models.CharField(max_length=100)
    mpaa = models.CharField(max_length=255, blank=True, null=True)
    covers = models.TextField()
    trailer = models.TextField(blank=True, null=True)
    hidden = models.IntegerField()
    hit = models.IntegerField()
    type_of_movie = models.CharField(max_length=255)
    created_by = models.IntegerField(blank=True, null=True)
    present_by = models.CharField(max_length=255)
    group = models.CharField(max_length=255)
    rank = models.FloatField()
    comments = models.ManyToManyField(Comment, related_name='movies')
    genres = models.ManyToManyField(Genre, related_name='movies')
    selections = models.ManyToManyField(Selection, related_name='movies')
    files = models.ManyToManyField(File, related_name='movies')
    countries = models.ManyToManyField(Country, related_name='movies')

    def __str__(self):
        return 'Фильм'

    class Meta:
        db_table = 'movies'
        verbose_name = _('movie')
        verbose_name_plural = _('movies')


class Bestseller(models.Model):
    category_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    movies = models.TextField()
    rank = models.IntegerField()

    def __str__(self):
        return 'Бестселлер'

    class Meta:
        db_table = 'bestsellers'
        verbose_name = _('bestseller')
        verbose_name_plural = _('bestsellers')


class Bookmark(models.Model):
    bookmark_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(OCUser, on_delete=models.PROTECT, related_name='bookmarks')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='bookmarks')

    def __str__(self):
        return 'Закладка'

    class Meta:
        db_table = 'bookmarks'
        verbose_name = _('bookmark')
        verbose_name_plural = _('bookmarks')


class Hit(models.Model):
    hit_id = models.AutoField(primary_key=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='hits')
    user = models.ForeignKey(OCUser, on_delete=models.CASCADE, related_name='hits')
    ip = models.CharField(max_length=15, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'hits'
        verbose_name = _('hit')
        verbose_name_plural = _('hits')


class MovieUserRating(models.Model):
    movie_user_rating_id = models.AutoField(primary_key=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='user_ratings')
    user = models.ForeignKey(OCUser, on_delete=models.CASCADE, related_name='user_ratings')
    rating = models.SmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'movies_users_ratings'


class Person(models.Model):
    person_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    international_name = models.CharField(max_length=100)
    info = models.TextField(blank=True, null=True)
    photos = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True)
    rank = models.FloatField()
    updated_at = models.DateTimeField()
    tries = models.IntegerField()

    def __str__(self):
        return 'Персона'

    class Meta:
        db_table = 'persones'
        verbose_name = _('person')
        verbose_name_plural = _('persons')


class Rating(models.Model):
    rating_id = models.AutoField(primary_key=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='ratings')
    system = models.CharField(max_length=9)
    system_uid = models.IntegerField(blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    details = models.CharField(max_length=255, blank=True, null=True)
    updated_at = models.DateTimeField()

    def __str__(self):
        return 'Рейтинг'

    class Meta:
        db_table = 'ratings'
        verbose_name = _('rating')
        verbose_name_plural = _('ratings')


class Registry(models.Model):
    key = models.CharField(max_length=255, primary_key=True)
    value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'registry'
        verbose_name = _('registry')
        verbose_name_plural = _('registries')


class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    name_hyphenated = models.CharField(max_length=100, blank=True, null=True)
    sort = models.IntegerField()

    def __str__(self):
        return 'Роль'

    class Meta:
        db_table = 'roles'
        verbose_name = _('role')
        verbose_name_plural = _('roles')


class Participant(models.Model):
    participant_id = models.AutoField(primary_key=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='participants')
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='participants')
    character = models.CharField(max_length=100, blank=True, null=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='participants')

    def __str__(self):
        return 'Участник'

    class Meta:
        db_table = 'participants'
        verbose_name = _('participant')
        verbose_name_plural = _('participants')


class SearchTrigram(models.Model):
    id = models.IntegerField(primary_key=True)
    trigram = models.CharField(max_length=3)
    type = models.CharField(max_length=6)

    class Meta:
        db_table = 'search_trigrams'
        verbose_name = _('search_trigram')
        verbose_name_plural = _('search_trigrams')


class Suggestion(models.Model):
    suggestion_id = models.AutoField(primary_key=True)
    word = models.CharField(max_length=255)
    type = models.CharField(max_length=6)

    class Meta:
        db_table = 'suggestions'
        verbose_name = _('suggestion')
        verbose_name_plural = _('suggestions')


class SuggestionCache(models.Model):
    query = models.CharField(max_length=255, primary_key=True)
    result = models.TextField()

    class Meta:
        db_table = 'suggestion_cache'
        verbose_name = _('suggestion_cache')
        verbose_name_plural = _('suggestion_cache')

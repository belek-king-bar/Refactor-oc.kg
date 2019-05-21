from django.contrib import admin
from webapp.models import *

models = OCUser, Movie, Bestseller, Bookmark, Check, Comment, CommentsVote, CommentsRating, Incoming, Country, File, Filesstat, FilesLost, FilesTask, Genre, Hit, Log, Participant, Person, Rating, Registry, Role, SearchTrigram, Selection, Suggestion, SuggestionCache


admin.site.register(models)


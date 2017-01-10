from django.core.management import BaseCommand
from cesar_app.models import Word


class Command(BaseCommand):
    """Command generate database from
       text file
    """

    help = 'My generate command'

    def handle(self, *args, **options):
        cnt = 0  # counter words added to the database
        with open('./fix.txt')as f:  # opening file with words
            self.stdout.write('Start script')  # get info-text
            for word in f:
                if (type(word) is str) and (word != ' '):
                    word = word.strip().lower()  # word without spaces
                    self.stdout.write('Word: {0}, trying save to DB '.format(word))  # get info-text starting
                    to_db = Word(
                        name=word
                        )
                    try:
                        to_db.save()  # trying save into database
                    except Exception as err:
                        self.stdout.write('Not saved! Error: {0}'.format(str(err)))  # get info-text error
                    else:
                        self.stdout.write(' {0} saved to DB'.format(word))  # get info-text saving
                        cnt += 1
            self.stdout.write('Done. Add {0} items to DB. Script ended'.format(str(cnt)))  # get info-text ending

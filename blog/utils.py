import random
import re
import string
import unicodedata

from MySQLdb import STRING

ALPHANUMERIC_CHARS = string.ascii_lowercase + string.digits
STRING_LENGHT = 16

def generate_random_string(chars=ALPHANUMERIC_CHARS, length=STRING_LENGHT):
    return "".join(random.choice(chars) for _ in range(length))

def slugify(value):
    value = str(value)
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s]', '', value).strip().lower()
    return re.sub(r'[-\s]+', '-', value )

def title_slugifier(value):
    return slugify(value) + "-" + generate_random_string()
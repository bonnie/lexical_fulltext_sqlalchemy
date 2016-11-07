"""code to create a row whose data is indexed

references: 

https://blog.garage-coding.com/2015/12/18/postgres-fulltext-search.html
http://docs.sqlalchemy.org/en/latest/dialects/postgresql.html#full-text-search

"""


# necessary import from sqlalchemy to create tsvector data for column
from sqlalchemy import func

# create a title and a body for the poem
title = 'a meditation on cows'
body = 'how now brown cow'

# create the poem, with the tsv column being a tsvector of the title and body
p = Poem(title=title, poem_url='', body=body, tsv=func.to_tsvector(' '.join([title, body])))

# add and commit
db.session.add(p)
db.session.commit()

# how to search using the tsvector column
# not entirely sure the postgresql_reconfig='english' is necessary
matching_poems = Poem.query.filter_by(tsv.match('cow', postgresql_reconfig='english')).all()


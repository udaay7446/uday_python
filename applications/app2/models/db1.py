# -*- coding: utf-8 -*-

db.define_table('blog_post',
                Field('title',requires=IS_NOT_EMPTY()),
                Field('image','upload'),
                Field('body','text',requires=IS_NOT_EMPTY()),
                auth.signature)
db.define_table('blog_comment',
                Field('blog_post','reference blog_post'),
                Field('comm','text',required=IS_NOT_EMPTY()),
                auth.signature)

# Cache

It stores information at temperory bases(caching) of web documents like web pages, images and other types of Web Multimedia, and reduces server lag.

Caching is one of those methods which a website implements to became faster.
It is cost efficient and saves CPU processing time.

Django comes with it's own system for cache. You can cache the output of specific views, you can cache only the pieces that are difficult to produce, or you can cache your entire site.

## Types of caching in Django

-> Database Caching
-> File System Caching
-> Local Memory Caching 

## How Cache Works ?

Scenario1: Suppose there is a website which are already in cache then in this case when this website will send request cache will say yes I have this web page and it will send response to web page and load the webpage.

Scenario2: Suppose there is a website which is not in cache so in this case when website sends the request cache will say I don't have this web page then page will generated and then stored in cache in this scenario website will get response from it's generated page

## How to setup django for caching ?

## How to implement Cache ?
1. Per-site cache : cache entire site
2. Per-view cache : cache the output of individual views.
3. Template fragment caching : This gives you more control what to cache (in templates(HTML) we can put specific code in caching)
(where to store cache databse, local system, file memory)

### Per-site cache
Once the cache is set up, the simplest way to use caching is to cache your entire site.

MIDDLEWARE = [
    # do this in this order only
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware', # already in django
    'django.middleware.cache.FetchFromCacheMiddleware',
]

CACHE_MIDDLEWARE_ALIAS - The cache alias to use for storage.
CACHE_MIDDLEWARE_SECONDS - The number of seconds each page should be cached.
CACHE_MIDDLEWARE_KEY_PREFIX

### Database Caching
Django can store it's cached data in your database. This works best if you've got a fast, well-indexed database server.

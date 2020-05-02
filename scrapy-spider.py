import scrapy


class MovieReleases(scrapy.Spider):
    name = 'movie_releases_spider'
    start_urls = ['https://www.imdb.com/calendar?region=CA']

    def parse(self, response):
        for date in response.css('#main > h4'):
            movies_on_date = date.xpath('following-sibling::ul[1]')
            current_date_results = []

            for movie_on_date in movies_on_date.css(' a'):
                current_date_results.append(
                    movie_on_date.css('::text').get())

            yield {'date': date.css('::text').get(),
                   'movies': current_date_results}

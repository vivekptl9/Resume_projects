next_page = response.css("li.next a::attr(href)").get()
        # if next_page is not None:
        #     next_page_url = "https: // books.toscrape.com" + next_page
        #     yield response.follow(next_page_url,callback = self.parse)
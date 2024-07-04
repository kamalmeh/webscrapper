from django.core.management import BaseCommand
from scrapper.utils import scrape_all_links

class Command(BaseCommand):
    help020= "Scrape the configured websites"
    
    def handle(self, *args, **kwargs):
        links = scrape_all_links()
        self.stdout.write(self.style.SUCCESS(links))
        for link in links:
                self.stdout.write(self.style.SUCCESS(f'{link.name}: {link.text}'))
       
from django.core.management.base import BaseCommand
from django.conf import settings
from builder.models import Idea
import json
import yaml
import markdown

try:
    import tomli as tomllib
except ImportError:
    import tomllib

class Command(BaseCommand):
    help = 'Load ideas from data files into database'

    def handle(self, *args, **options):
        data_dir = settings.DATA_DIR
        loaded_count = 0
        skipped_count = 0

        for file_path in data_dir.glob('ideas.json'):
            loaded, skipped = self.process_json_file(file_path)
            loaded_count += loaded
            skipped_count += skipped

        for file_path in data_dir.glob('ideas.yaml'):
            loaded, skipped = self.process_yaml_file(file_path)
            loaded_count += loaded
            skipped_count += skipped

        for file_path in data_dir.glob('ideas.yml'):
            loaded, skipped = self.process_yaml_file(file_path)
            loaded_count += loaded
            skipped_count += skipped

        self.stdout.write(self.style.SUCCESS(f'Loaded {loaded_count} ideas'))
        if skipped_count > 0:
            self.stdout.write(self.style.WARNING(f'Skipped {skipped_count} existing ideas'))

    def process_json_file(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                ideas_array = json.load(f)

            if not isinstance(ideas_array, list):
                self.stdout.write(self.style.ERROR(f'{file_path.name} must contain an array'))
                return 0, 0

            return self.process_ideas(ideas_array, file_path.name)

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error processing {file_path.name}: {str(e)}'))
            return 0, 0

    def process_yaml_file(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                ideas_array = yaml.safe_load(f)

            if not isinstance(ideas_array, list):
                self.stdout.write(self.style.ERROR(f'{file_path.name} must contain an array'))
                return 0, 0

            return self.process_ideas(ideas_array, file_path.name)

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error processing {file_path.name}: {str(e)}'))
            return 0, 0

    def process_ideas(self, ideas_array, filename):
        loaded_count = 0
        skipped_count = 0

        for idea_data in ideas_array:
            slug = idea_data.get('slug')
            if not slug:
                self.stdout.write(self.style.ERROR(f'Idea missing slug in {filename}'))
                continue

            if Idea.objects.filter(slug=slug).exists():
                skipped_count += 1
                continue

            content = idea_data.get('content', '')
            if content:
                content = markdown.markdown(content)

            try:
                Idea.objects.create(
                    slug=slug,
                    title=idea_data.get('title', ''),
                    category=idea_data.get('category', ''),
                    description=idea_data.get('description', ''),
                    content=content
                )
                self.stdout.write(self.style.SUCCESS(f'Loaded idea: {idea_data.get("title")}'))
                loaded_count += 1
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error creating idea {slug}: {str(e)}'))

        return loaded_count, skipped_count

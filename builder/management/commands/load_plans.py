from django.core.management.base import BaseCommand
from django.conf import settings
from builder.models import Plan
import json
import yaml
import markdown

try:
    import tomli as tomllib
except ImportError:
    import tomllib

class Command(BaseCommand):
    help = 'Load plans from data files into database'

    def handle(self, *args, **options):
        data_dir = settings.DATA_DIR
        loaded_count = 0
        skipped_count = 0

        for file_path in data_dir.glob('plans.json'):
            loaded, skipped = self.process_json_file(file_path)
            loaded_count += loaded
            skipped_count += skipped

        for file_path in data_dir.glob('plans.yaml'):
            loaded, skipped = self.process_yaml_file(file_path)
            loaded_count += loaded
            skipped_count += skipped

        for file_path in data_dir.glob('plans.yml'):
            loaded, skipped = self.process_yaml_file(file_path)
            loaded_count += loaded
            skipped_count += skipped

        self.stdout.write(self.style.SUCCESS(f'Loaded {loaded_count} plans'))
        if skipped_count > 0:
            self.stdout.write(self.style.WARNING(f'Skipped {skipped_count} existing plans'))

    def process_json_file(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                plans_array = json.load(f)

            if not isinstance(plans_array, list):
                self.stdout.write(self.style.ERROR(f'{file_path.name} must contain an array'))
                return 0, 0

            return self.process_plans(plans_array, file_path.name)

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error processing {file_path.name}: {str(e)}'))
            return 0, 0

    def process_yaml_file(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                plans_array = yaml.safe_load(f)

            if not isinstance(plans_array, list):
                self.stdout.write(self.style.ERROR(f'{file_path.name} must contain an array'))
                return 0, 0

            return self.process_plans(plans_array, file_path.name)

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error processing {file_path.name}: {str(e)}'))
            return 0, 0

    def process_plans(self, plans_array, filename):
        loaded_count = 0
        skipped_count = 0

        for plan_data in plans_array:
            slug = plan_data.get('slug')
            if not slug:
                self.stdout.write(self.style.ERROR(f'Plan missing slug in {filename}'))
                continue

            if Plan.objects.filter(slug=slug).exists():
                skipped_count += 1
                continue

            content = plan_data.get('content', '')
            if content:
                content = markdown.markdown(content)

            try:
                Plan.objects.create(
                    slug=slug,
                    title=plan_data.get('title', ''),
                    category=plan_data.get('category', ''),
                    description=plan_data.get('description', ''),
                    content=content
                )
                self.stdout.write(self.style.SUCCESS(f'Loaded plan: {plan_data.get("title")}'))
                loaded_count += 1
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error creating plan {slug}: {str(e)}'))

        return loaded_count, skipped_count

from django.test import TestCase, Client
from django.urls import reverse
from .models import Idea, Plan

class ViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.idea = Idea.objects.create(
            slug='test-idea',
            title='Test Idea',
            category='Technology',
            description='Test description',
            content='<h1>Test Content</h1><h2>Subtitle</h2>'
        )
        self.plan = Plan.objects.create(
            slug='test-plan',
            title='Test Plan',
            category='Business',
            description='Test plan description',
            content='<h1>Plan Content</h1>'
        )

    def test_home_page(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Brain')

    def test_idea_list_page(self):
        response = self.client.get(reverse('idea_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Ideas')
        self.assertContains(response, 'Test Idea')

    def test_plan_list_page(self):
        response = self.client.get(reverse('plan_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Plans')
        self.assertContains(response, 'Test Plan')

    def test_idea_detail_with_valid_slug(self):
        response = self.client.get(reverse('idea_detail', kwargs={'slug': 'test-idea'}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Idea')
        self.assertContains(response, 'Technology')

    def test_plan_detail_with_valid_slug(self):
        response = self.client.get(reverse('plan_detail', kwargs={'slug': 'test-plan'}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Plan')
        self.assertContains(response, 'Business')

    def test_idea_detail_with_invalid_slug(self):
        response = self.client.get(reverse('idea_detail', kwargs={'slug': 'nonexistent'}))
        self.assertEqual(response.status_code, 404)

    def test_plan_detail_with_invalid_slug(self):
        response = self.client.get(reverse('plan_detail', kwargs={'slug': 'nonexistent'}))
        self.assertEqual(response.status_code, 404)

    def test_markdown_rendering(self):
        response = self.client.get(reverse('idea_detail', kwargs={'slug': 'test-idea'}))
        self.assertContains(response, '<h1>')
        self.assertContains(response, '<h2>')

    def test_idea_model_str(self):
        self.assertEqual(str(self.idea), 'Test Idea')

    def test_plan_model_str(self):
        self.assertEqual(str(self.plan), 'Test Plan')

from django.test import TestCase


class HomePageTests(TestCase):
    def test_home_page_loads(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'myapp/spark_admin/index.html')
        self.assertContains(response, 'Faith Cheptooh')
        self.assertContains(response, 'faithcheptoo38@gmail.com')
        self.assertContains(
            response,
            '/static/myapp/spark-admin/assets/libs/bootstrap/css/bootstrap.min.css',
        )
        self.assertContains(
            response,
            '/static/myapp/spark-admin/assets/images/profile.jpg',
        )
        self.assertNotContains(response, 'Administrator')

    def test_dashboard_pages_load(self):
        pages = (
            '/tables-basic/',
            '/ui-forms/',
            '/ui-buttons/',
            '/page-blank/',
            '/page-login/',
            '/page-404/',
        )

        for page in pages:
            with self.subTest(page=page):
                self.assertEqual(self.client.get(page).status_code, 200)

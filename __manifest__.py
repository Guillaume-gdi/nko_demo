{
    'name': "nko demo",
    'summary': """""",
    'description':
        """

        """,
    'author': "Guillaume (gdi)",
    'maintainer': "Guillaume (gdi)",
    'category': "Custom Development",
    'version': "1.0",
    'license': "OPL-1",
    'depends': ['sale_subscription'],
    'data': [
        # Views
        'views/portal_views.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'nko_demo/static/src/js/sub.js',
        ],
    },
    'application': True,
}

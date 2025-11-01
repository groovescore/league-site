# SPDX-License-Identifier: AGPL-3.0-or-later
# SPDX-FileCopyrightText: 2025 Jani Nikula <jani@nikula.org>
#
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import pathlib

from jinja2 import Environment, FileSystemLoader

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Snooker League'
copyright = '2025, Jani'
author = 'Jani'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

# Redirects
ROOT = pathlib.Path(__file__).parent.parent.resolve()

TEMPLATE_PATH = (ROOT / 'templates').resolve()
REDIRECT_PATH = (ROOT / 'redirects').resolve()
os.makedirs(REDIRECT_PATH, exist_ok=True)

html_extra_path = [str(REDIRECT_PATH)]

redirects = {
    # format: 'subdir': (target_url, template, javascript)
    'info': (
        'https://docs.google.com/spreadsheets/d/e/2PACX-1vQobmxLXbaetuf0twsuBLLeAvDZXfJj1Bsoj3ZRWOLjymOiSdjTmomZwWY9puUz8lwmbGf1igXjzBIt/pubhtml?gid=1727048767&single=true',
        'redirect.html',
        False
    ),
    'signup': (
        'https://forms.gle/UCxCSi99qRCxfHHd8',
        'redirect.html',
        False
    ),
    'sheet': (
        'https://docs.google.com/spreadsheets/d/1R2E2bx-0bj33z7jurkFAQED-24mgDQzYYmnm68lk5bY/view',
        'redirect.html',
        True
    ),
}

def generate_redirects(app):
    env = Environment(loader=FileSystemLoader(TEMPLATE_PATH))

    for name, (target, template, javascript) in redirects.items():
        template = env.get_template(template)
        out_path = REDIRECT_PATH / name
        os.makedirs(out_path, exist_ok=True)
        with open(out_path / 'index.html', 'w', encoding='utf-8') as f:
            f.write(template.render(target=target, javascript=javascript))

def setup(app):
    app.connect('builder-inited', generate_redirects)

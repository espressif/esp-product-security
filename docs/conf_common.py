# The content below is copied from the esp-dl repo and modified acc to the esp-hdg repo

from esp_docs.conf_docs import *  # noqa: F403,F401

languages = ['en']
extensions += ['sphinx_copybutton',
               # Note: order is important here, events must
               # be registered by one extension before they can be
               # connected to another extension
               'linuxdoc.rstFlatTable',
               'esp_docs.esp_extensions.dummy_build_system',
               ]

# Disable format_esp_target
extensions.remove('esp_docs.esp_extensions.format_esp_target')

# link roles config
project_homepage = 'https://github.com/espressif/esp-product-security'
github_repo = 'espressif/esp-product-security'

# context used by sphinx_idf_theme
html_context['github_user'] = 'espressif'
html_context['github_repo'] = 'esp-product-security'

html_static_path = ['../_static']
html_css_files = ['js/chatbot_widget.css']

# Extra options required by sphinx_idf_theme
project_slug = 'esp-product-security'

# Contains info used for constructing target and version selector
# Can also be hosted externally, see esp-idf for example
versions_url = './_static/docs_version.js'

# Final PDF filename will contains target and version
pdf_file_prefix = u'esp-product-security'

# disable the check for link anchors
linkcheck_anchors = False

linkcheck_exclude_documents = ['index',  # several false positives due to the way we link to different sections
                               ]

# Measurement ID for Google Analytics
# google_analytics_id = 'G-RP8SCKE54N'

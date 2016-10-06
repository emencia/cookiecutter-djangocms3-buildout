# -*- coding: utf-8 -*-
TEMPLATES[0]['OPTIONS']['context_processors'] = add_to_tuple(
    TEMPLATES[0]['OPTIONS']['context_processors'],
    'project.utils.context_processors.site_metas',
    'project.utils.context_processors.marketingtags_metas',
)

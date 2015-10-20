from web.template import CompiledTemplate, ForLoop, TemplateResult

import site, admin
_dummy = CompiledTemplate(lambda: None, 'dummy')
join_ = _dummy._join
escape_ = _dummy._escape


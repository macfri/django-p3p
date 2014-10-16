from django.views.generic import TemplateView

class _XmlMixin(TemplateView):
    def render_to_response(self, context, **response_kwargs):
        response_kwargs.update({ 'content_type': 'text/xml' })
        return super(_XmlMixin, self).render_to_response(context, **response_kwargs)    


class XmlView(_XmlMixin):
    template_name = 'p3p/p3p.xml'

class P3PView(_XmlMixin):
    template_name = 'p3p/policy.p3p'

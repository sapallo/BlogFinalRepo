from django.views.generic import TemplateView
from apps.post.models import Post, Category
from django.shortcuts import render

class IndexView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['random_posts'] = Post.objects.order_by('?')[:3]  # Selecciona 3 posts aleatorios
        context['categories'] = Category.objects.all()
        return context

class AboutView(TemplateView):
    template_name = 'about.html'

# Es importante que el argumento exception esté presente
# para que Django lo pueda identificar como un manejador de errores
def not_found_view(request, exception):
    return render(request, 'errors/error_not_found.html', status=404)

def internal_error_view(request):
    return render(request, 'errors/error_internal.html', status=500)

def forbidden_view(request, exception):
    return render(request, 'errors/error_forbidden.html', status=403)
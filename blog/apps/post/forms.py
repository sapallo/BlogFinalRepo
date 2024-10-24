from django import forms
from apps.post.models import Comment
from apps.post.models import Post, PostImage, Category


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

        label = {
            'content': 'Comentario'
        }

        widgets = {
            'content': forms.Textarea(attrs={'rows':3, 'placeholder': 'Escribe tu'
'comentario...', 'class': 'p-2'})
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'allow_comments', 'category')
        categories = forms.ModelMultipleChoiceField(  # Este es el nuevo campo
        queryset=Category.objects.all(),  # Obtiene todas las categorías disponibles
        widget=forms.CheckboxSelectMultiple,  # Puedes usar otro widget si prefieres
        required=False
    )

    class Meta:
        model = Post
        fields = ('title', 'content', 'allow_comments', 'category')  # Incluye 'categories'

class NewPostForm(PostForm):
    image = forms.ImageField(required=False)

    def save(self, commit = True):
        post = super().save(commit=False)
        image = self.cleaned_data['image']

        if commit:
            post.save()
            
            if image:
                PostImage.objects.create(post=post, image=image)
        return post
    
class UpdatePostForm(PostForm):
    image = forms.ImageField(required=False)

    def __init__(self, *args, **kwargs):
    # Obtenemos las imágenes activas del post que se quiere actualizar
        self.active_images = kwargs.pop('active_images', None)
        super(UpdatePostForm, self).__init__(*args, **kwargs)

        if self.active_images:
            for image in self.active_images:
                field_name = f"keep_image_{image.id}"
                self.fields[field_name] = forms.BooleanField(
                    required=False, initial=True, label=f"Mantener {image}"
            )
    def save(self, commit=True):
        post = super().save(commit=False)
        if commit:
            post.save()
            if self.cleaned_data['image']:         # Si el usuario sube una nueva imagen
                PostImage.objects.create(
                    post=post, image=self.cleaned_data['image'])
        if self.active_images: # Si hay imágenes activas y se quiere mantener alguna
            for image in self.active_images:
                if not self.cleaned_data.get(f"keep_image_{image.id}", True):
                    image.delete() # Eliminar la imagen si el usuario no la quiere mantener, checkboxes desmarcados
        return post
    
class PostFilterForm(forms.Form):
    search_query = forms.CharField(
        required = False,
        widget=forms.TextInput(attrs={'placeholder': 'Buscar...', 'class': 'w-fullp-2'})
    )
    order_by = forms.ChoiceField(
        required = False,
        choices=(
            ('-creation_date', 'Más reciente'),
            ('creation_date', 'Más antiguo'),
            ('-comments_count', 'Más comentado'),
            ('-title', 'Ascendente'),
            ('title', 'Descendente'),
            # agregar orden alfabetico title 
        ),
        widget=forms.Select(attrs={'class': 'w-full p-2'})
    )
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from bancadaweb.models import AnaliseDesgaste
from bancadaweb.forms import AnaliseDesgasteForm

class Home(TemplateView):
    template_name = "home.html"

class Graph(TemplateView):
    template_name = "graph.html"

class AnaliseDesgasteList(ListView):

    template_name = 'list.html'
    context_object_name = 'analises'
    model = AnaliseDesgaste
    fields = '__all__'

    success_url = reverse_lazy('list_analise')

class AnaliseDesgasteDetail(DetailView):
    
    template_name = 'detail.html'
    context_object_name = 'analise'
    model = AnaliseDesgaste
    fields = '__all__'

    success_url = reverse_lazy('list_analise')

class AnaliseDesgasteCreate(CreateView):
    template_name = 'form.html'
    form_class = AnaliseDesgasteForm
    success_url = reverse_lazy('list_analise')

    def form_valid(self, form):
        form.instance.criado_por = self.request.user
        return super(AnaliseDesgasteCreate, self).form_valid(form)

    def get_initial(self):
        return { 'criado_por': self.request.user.id }

class AnaliseDesgasteUpdate(UpdateView):
    template_name = 'form.html'
    form_class = AnaliseDesgasteForm
    model = AnaliseDesgaste

    success_url = reverse_lazy('detail_analise')

class AnaliseDesgasteDelete(DeleteView):
    template_name = 'delete.html'
    model = AnaliseDesgaste
    success_url = reverse_lazy('list_analise')
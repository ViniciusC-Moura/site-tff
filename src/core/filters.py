import django_filters
from django import forms
from .models import Jogo

class JogoFilter(django_filters.FilterSet):
    competicao = django_filters.ChoiceFilter(
        choices=Jogo.COMPETICAO_CHOICES,
        empty_label="Todas",
        widget=forms.Select(attrs={'class': 'filtro-select'}),
    )
    edicao = django_filters.ChoiceFilter(
        empty_label="Todas",
        widget=forms.Select(attrs={'class': 'filtro-select'}),
    )
    fase_competicao = django_filters.ChoiceFilter(
        empty_label="Todas",
        widget=forms.Select(attrs={'class': 'filtro-select'}),
    )
    modalidade = django_filters.ChoiceFilter(
        empty_label="Todas",
        widget=forms.Select(attrs={'class': 'filtro-select'}),
    )

    class Meta:
        model = Jogo
        fields = ['competicao', 'edicao', 'fase_competicao', 'modalidade']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Gera as opções dos selects dinamicamente a partir dos valores
        # distintos já cadastrados no banco (em vez de choices fixos)
        for campo in ['edicao', 'fase_competicao', 'modalidade']:
            valores = (
                Jogo.objects
                .order_by(campo)
                .values_list(campo, flat=True)
                .distinct()
            )
            self.filters[campo].extra['choices'] = [
                (v, v) for v in valores if v
            ]
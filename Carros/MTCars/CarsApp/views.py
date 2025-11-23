from django.shortcuts import render
from CarsApp.models import MTCars, RankingItem

# =======================
# View existente para pesquisa de carros
# =======================
def searchf(request):
    if request.method == 'GET':
        return render(request, 'CarsApp/home.html')
    else:
        search_query = request.POST.get('search')
        # Aqui você pode adicionar a lógica para filtrar os carros com base na pesquisa
        carros = MTCars.objects.filter(name__icontains=search_query)
        # contexto é uma variável do tipo dicionário 
        # que armazena os dados a serem enviados para o template.
        # No template, você pode acessar esses dados usando as chaves do dicionário.
        contexto = {
            'search_query': search_query,   # o texto pesquisado
            'carros': carros                # os resultados da pesquisa
        }
        return render(request, 'CarsApp/home.html', contexto)


# =======================
# Nova view para exibir o ranking
# =======================
def ranking_view(request):
    # Pega todos os itens do ranking do banco de dados
    ranking_items = RankingItem.objects.all()
    
    # Renderiza no template passando a lista de itens
    return render(request, 'CarsApp/ranking.html', {'ranking_items': ranking_items})
